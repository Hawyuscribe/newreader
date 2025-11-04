#!/usr/bin/env python3
"""
Implement session persistence for case-based learning using Django's database
"""

def create_session_model():
    """Create a Django model to persist sessions"""
    
    model_code = '''# Add this to django_neurology_mcq/mcq/models.py

class CaseLearningSession(models.Model):
    """Persistent storage for case-based learning sessions"""
    session_id = models.CharField(max_length=100, unique=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_sessions')
    
    # Session state
    state = models.IntegerField(default=0)
    specialty = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    
    # Case data
    case_data = models.JSONField(default=dict)
    chief_complaint = models.TextField(blank=True)
    
    # Progress tracking
    history_gathered = models.JSONField(default=list)
    examination_findings = models.JSONField(default=list)
    localization = models.JSONField(default=list)
    investigations = models.JSONField(default=list)
    differentials = models.JSONField(default=list)
    management = models.JSONField(default=list)
    
    # Critical elements tracking
    critical_history_missed = models.JSONField(default=list)
    critical_exam_missed = models.JSONField(default=list)
    missed_critical_steps = models.JSONField(default=list)
    
    # Conversation history
    messages = models.JSONField(default=list)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    
    # Additional state
    screening_exam_done = models.BooleanField(default=False)
    detailed_exam_areas = models.JSONField(default=list)
    patient_condition = models.CharField(max_length=50, default='stable')
    
    class Meta:
        ordering = ['-last_activity']
        indexes = [
            models.Index(fields=['user', '-last_activity']),
            models.Index(fields=['session_id']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.specialty} - {self.created_at}"
'''
    
    print("Model code to add:")
    print(model_code)
    return model_code

def create_persistent_session_manager():
    """Create an enhanced session manager that uses database persistence"""
    
    manager_code = '''# Replace the SessionManager class in case_bot.py with this:

class PersistentSessionManager:
    """Session manager with database persistence"""
    
    def __init__(self, timeout_minutes=180):
        self.timeout = timedelta(minutes=timeout_minutes)
        self.memory_cache = {}  # Keep in-memory cache for performance
        
    def create_session(self, user_id, specialty, difficulty='random'):
        """Create a new session with database persistence"""
        from .models import CaseLearningSession
        
        session_id = str(uuid.uuid4())
        
        # Create database record
        db_session = CaseLearningSession.objects.create(
            session_id=session_id,
            user_id=user_id,
            state=CASE_STATES['INITIAL'],
            specialty=specialty,
            difficulty=difficulty,
            case_data={},
            messages=[],
            history_gathered=[],
            examination_findings=[],
            critical_history_missed=[],
            critical_exam_missed=[],
            localization=[],
            investigations=[],
            differentials=[],
            management=[],
            missed_critical_steps=[],
            detailed_exam_areas=[]
        )
        
        # Also cache in memory
        self.memory_cache[session_id] = {
            'db_id': db_session.id,
            'user_id': user_id,
            'last_access': datetime.now()
        }
        
        return session_id
    
    def get_session(self, session_id):
        """Get session from database or memory cache"""
        from .models import CaseLearningSession
        
        # Check memory cache first
        if session_id in self.memory_cache:
            # Update last access time
            self.memory_cache[session_id]['last_access'] = datetime.now()
        
        try:
            # Get from database
            db_session = CaseLearningSession.objects.get(session_id=session_id)
            
            # Check if session is expired
            if datetime.now() - db_session.last_activity > self.timeout:
                return None
            
            # Update last activity
            db_session.last_activity = datetime.now()
            db_session.save(update_fields=['last_activity'])
            
            # Convert to dictionary format expected by the rest of the code
            session_dict = {
                'user_id': db_session.user_id,
                'state': db_session.state,
                'specialty': db_session.specialty,
                'difficulty': db_session.difficulty,
                'chief_complaint': db_session.chief_complaint,
                'history_gathered': db_session.history_gathered,
                'examination_findings': db_session.examination_findings,
                'critical_history_missed': db_session.critical_history_missed,
                'critical_exam_missed': db_session.critical_exam_missed,
                'localization': db_session.localization,
                'investigations': db_session.investigations,
                'differentials': db_session.differentials,
                'management': db_session.management,
                'patient_condition': db_session.patient_condition,
                'missed_critical_steps': db_session.missed_critical_steps,
                'messages': deque(db_session.messages, maxlen=100),
                'created_at': db_session.created_at,
                'last_activity': db_session.last_activity,
                'case_data': db_session.case_data,
                'screening_exam_done': db_session.screening_exam_done,
                'detailed_exam_areas': db_session.detailed_exam_areas,
                'session_id': session_id,
                'db_session': db_session  # Keep reference for updates
            }
            
            return session_dict
            
        except CaseLearningSession.DoesNotExist:
            return None
    
    def update_session(self, session_id, updates):
        """Update session in database"""
        from .models import CaseLearningSession
        
        try:
            db_session = CaseLearningSession.objects.get(session_id=session_id)
            
            # Update fields
            for key, value in updates.items():
                if hasattr(db_session, key):
                    # Convert deque to list for JSON storage
                    if isinstance(value, deque):
                        value = list(value)
                    setattr(db_session, key, value)
            
            db_session.save()
            return True
            
        except CaseLearningSession.DoesNotExist:
            return False
    
    def get_user_sessions(self, user_id, limit=10):
        """Get recent sessions for a user"""
        from .models import CaseLearningSession
        
        return CaseLearningSession.objects.filter(
            user_id=user_id,
            completed=False,
            last_activity__gte=datetime.now() - self.timeout
        ).order_by('-last_activity')[:limit]
    
    def cleanup_old_sessions(self):
        """Remove expired sessions from database"""
        from .models import CaseLearningSession
        
        cutoff_time = datetime.now() - self.timeout
        CaseLearningSession.objects.filter(
            last_activity__lt=cutoff_time
        ).delete()

# Replace the initialization
session_manager = PersistentSessionManager()
'''
    
    print("\nSession manager code to replace:")
    print(manager_code)
    return manager_code

def create_resume_view():
    """Create a view to show and resume previous sessions"""
    
    view_code = '''# Add this to the case_bot.py views:

@login_required
def list_sessions(request):
    """List user's recent case sessions"""
    sessions = session_manager.get_user_sessions(request.user.id)
    
    session_list = []
    for session in sessions:
        session_list.append({
            'session_id': session.session_id,
            'specialty': session.specialty,
            'difficulty': session.difficulty,
            'state': list(CASE_STATES.keys())[session.state],
            'created': session.created_at.strftime('%Y-%m-%d %H:%M'),
            'last_activity': session.last_activity.strftime('%Y-%m-%d %H:%M'),
            'chief_complaint': session.chief_complaint[:100] + '...' if session.chief_complaint else 'Not started'
        })
    
    return JsonResponse({'sessions': session_list})

# Update the main chat handler to save after each interaction:
# Add this after processing each message:

# Save session state to database
if session.get('db_session'):
    session_manager.update_session(session_id, {
        'state': session['state'],
        'messages': list(session['messages']),
        'history_gathered': session['history_gathered'],
        'examination_findings': session['examination_findings'],
        'localization': session.get('localization', []),
        'investigations': session.get('investigations', []),
        'differentials': session.get('differentials', []),
        'management': session.get('management', []),
        'chief_complaint': session.get('chief_complaint', ''),
        'case_data': session.get('case_data', {}),
        'screening_exam_done': session.get('screening_exam_done', False),
        'detailed_exam_areas': session.get('detailed_exam_areas', [])
    })
'''
    
    print("\nView code to add:")
    print(view_code)
    return view_code

def create_frontend_resume():
    """Create frontend UI for resuming sessions"""
    
    frontend_code = '''<!-- Add this to case_based_learning_enhanced.html -->

<!-- Resume Session Modal -->
<div class="modal fade" id="resumeSessionModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Resume Previous Case</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <div id="previousSessions">
                    <p class="text-muted">Loading previous sessions...</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Add Resume Button -->
<button type="button" class="btn btn-info" onclick="showPreviousSessions()">
    <i class="fas fa-history"></i> Resume Previous Case
</button>

<script>
function showPreviousSessions() {
    fetch('/case-learning/sessions/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('previousSessions');
            
            if (data.sessions.length === 0) {
                container.innerHTML = '<p class="text-muted">No previous sessions found.</p>';
                return;
            }
            
            let html = '<div class="list-group">';
            data.sessions.forEach(session => {
                html += `
                    <div class="list-group-item">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <h6 class="mb-1">${session.specialty} - ${session.difficulty}</h6>
                                <p class="mb-1 text-muted">${session.chief_complaint}</p>
                                <small>State: ${session.state} | Last active: ${session.last_activity}</small>
                            </div>
                            <button class="btn btn-primary btn-sm" onclick="resumeSession('${session.session_id}')">
                                Resume
                            </button>
                        </div>
                    </div>
                `;
            });
            html += '</div>';
            
            container.innerHTML = html;
        });
    
    $('#resumeSessionModal').modal('show');
}

function resumeSession(sessionId) {
    // Set the session ID
    window.sessionId = sessionId;
    
    // Close modal
    $('#resumeSessionModal').modal('hide');
    
    // Send a message to resume
    sendMessage("Resume session");
    
    // Update UI to show resumed state
    addMessage('system', 'Resuming your previous case session...');
}
</script>
'''
    
    print("\nFrontend code to add:")
    print(frontend_code)
    return frontend_code

def create_migration():
    """Create Django migration"""
    
    migration_steps = '''
# Steps to implement session persistence:

1. First, add the model to django_neurology_mcq/mcq/models.py

2. Create the migration:
   python django_neurology_mcq/manage.py makemigrations

3. Apply the migration locally:
   python django_neurology_mcq/manage.py migrate

4. Deploy to Heroku:
   git add -A
   git commit -m "Add session persistence for case-based learning"
   git push heroku stable_version:main

5. Run migration on Heroku:
   heroku run python django_neurology_mcq/manage.py migrate

Benefits:
- Sessions persist across server restarts
- Users can resume cases even after closing browser
- Multiple devices can access same session
- Full case history preserved
- No data loss on timeout
'''
    
    print("\nImplementation steps:")
    print(migration_steps)

if __name__ == "__main__":
    print("=== Session Persistence Implementation Plan ===\n")
    
    create_session_model()
    print("\n" + "="*50 + "\n")
    
    create_persistent_session_manager()
    print("\n" + "="*50 + "\n")
    
    create_resume_view()
    print("\n" + "="*50 + "\n")
    
    create_frontend_resume()
    print("\n" + "="*50 + "\n")
    
    create_migration()