# Add these models to your existing models.py file

class CaseLearningSession(models.Model):
    """Track case-based learning sessions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=50, unique=True)
    specialty = models.CharField(max_length=100)
    case_hash = models.CharField(max_length=20)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    final_state = models.CharField(max_length=50, default='INITIAL')
    patient_outcome = models.CharField(max_length=20, choices=[
        ('stable', 'Stable'),
        ('improving', 'Improving'),
        ('deteriorating', 'Deteriorating')
    ], default='stable')
    score = models.IntegerField(default=0)  # Based on critical decisions
    
    class Meta:
        ordering = ['-started_at']
        indexes = [
            models.Index(fields=['user', 'specialty']),
            models.Index(fields=['case_hash']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.specialty} - {self.started_at}"

class CaseLearningHistory(models.Model):
    """Track which cases users have seen"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    case_hash = models.CharField(max_length=20)
    condition = models.CharField(max_length=200)
    seen_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'case_hash']
        ordering = ['-seen_at']
        indexes = [
            models.Index(fields=['user', 'specialty', '-seen_at']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.condition} - {self.seen_at}"

class CaseLearningFeedback(models.Model):
    """Store user feedback on cases"""
    session = models.ForeignKey(CaseLearningSession, on_delete=models.CASCADE)
    difficulty_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    educational_value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback for {self.session}"