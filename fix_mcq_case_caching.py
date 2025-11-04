"""
Fix MCQ Case Converter Caching Issue

This script provides a solution to prevent repeated generation of the same case
when converting MCQs to case-based learning sessions.
"""

import json
import hashlib
from datetime import datetime, timedelta

from mcq.openai_integration import (
    client as openai_client,
    chat_completion,
    DEFAULT_MODEL,
)

# Solution 1: Add caching to mcq_case_converter.py
MCQ_CASE_CONVERTER_CACHE_FIX = '''
# Add this import at the top of mcq_case_converter.py
from django.core.cache import cache

# Add this function to generate a cache key for MCQ conversions
def get_mcq_cache_key(mcq_id):
    """Generate cache key for MCQ conversion"""
    return f"mcq_case_conversion_{mcq_id}_v2"

# Modify the convert_mcq_to_case function to use caching
def convert_mcq_to_case(mcq):
    """Convert MCQ to interactive case data using validated AI analysis with caching"""
    
    # Check cache first
    cache_key = get_mcq_cache_key(mcq.id)
    cached_case = cache.get(cache_key)
    
    if cached_case:
        print(f"✅ Using cached case conversion for MCQ #{mcq.id}")
        # Add a timestamp to track cache usage
        cached_case['cache_used'] = True
        cached_case['cache_timestamp'] = str(datetime.now())
        return cached_case
    
    if not client:
        raise Exception("OpenAI client not available")
    
    # Rest of the existing function...
    # [existing code continues]
    
    # Before returning case_data, cache it
    # Cache for 7 days (604800 seconds)
    cache.set(cache_key, case_data, 604800)
    print(f"💾 Cached case conversion for MCQ #{mcq.id}")
    
    return case_data
'''

# Solution 2: Add variation to the generation
MCQ_CASE_CONVERTER_VARIATION_FIX = '''
# Modify the generate_validated_case function to add slight variation
def generate_validated_case(mcq, key_terms, mcq_category, attempt):
    """Generate case with domain-specific constraints and slight variation"""
    
    # Create stricter prompt based on attempt number
    strictness_level = min(attempt + 1, 3)  # 1, 2, or 3
    
    # Add slight variation based on current timestamp
    import random
    random.seed(int(datetime.now().timestamp()))
    
    # Vary patient demographics slightly
    age_variation = random.randint(-2, 2)
    
    prompt = create_domain_specific_prompt(mcq, key_terms, mcq_category, strictness_level, age_variation)
    
    response = chat_completion(
        openai_client,
        DEFAULT_MODEL,
        messages=[
            {
                "role": "system", 
                "content": f"""You are a medical education expert converting MCQs to interactive cases.

ABSOLUTE RULES:
1. NEVER change the medical condition (if MCQ is about post-CABG, case MUST be about post-CABG)
2. NEVER change patient age by more than 10 years
3. NEVER switch medical domains (cardiac surgery stays cardiac surgery, epilepsy stays epilepsy)
4. PRESERVE all clinical signs, symptoms, and context exactly
5. If you generate a different medical condition, you have FAILED
6. Add slight variations in presentation details while maintaining clinical accuracy

Strictness level: {strictness_level}/3 - Be {"extremely" if strictness_level == 3 else "very" if strictness_level == 2 else ""} strict about preservation.
Variation seed: {int(datetime.now().timestamp())}"""
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=2500,
        temperature=0.3  # Increase slightly from 0.1 to 0.3 for more variation
    )
    
    # Rest of the function remains the same...
'''

# Solution 3: Track MCQ conversions in the database
MCQ_CONVERSION_MODEL = '''
# Add this to models.py

class MCQCaseConversion(models.Model):
    """Cache MCQ to case conversions"""
    mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE, related_name='case_conversions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Conversion data
    case_data = models.JSONField()
    conversion_version = models.CharField(max_length=10, default='v1')
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)
    use_count = models.IntegerField(default=1)
    
    # Expiration
    expires_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['mcq', '-created_at']),
            models.Index(fields=['expires_at']),
        ]
    
    def save(self, *args, **kwargs):
        # Set expiration to 30 days from now
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=30)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Case conversion for MCQ #{self.mcq.id}"
'''

# Solution 4: Update views.py to check for existing conversions
VIEWS_UPDATE = '''
# Update the mcq_to_case_learning function in views.py

@login_required
def mcq_to_case_learning(request, mcq_id):
    """Convert MCQ to interactive case-based learning session with caching"""
    mcq = get_object_or_404(MCQ, id=mcq_id)
    
    try:
        # Check for existing conversion first
        from .models import MCQCaseConversion
        
        # Try to get recent conversion (within last 7 days)
        recent_conversion = MCQCaseConversion.objects.filter(
            mcq=mcq,
            expires_at__gt=timezone.now()
        ).order_by('-created_at').first()
        
        if recent_conversion:
            # Use existing conversion
            case_data = recent_conversion.case_data
            recent_conversion.use_count += 1
            recent_conversion.save()
            print(f"✅ Using existing case conversion for MCQ #{mcq_id}")
        else:
            # Import the conversion function
            from .mcq_case_converter import convert_mcq_to_case
            
            # Convert MCQ to case
            case_data = convert_mcq_to_case(mcq)
            
            # Save conversion for future use
            MCQCaseConversion.objects.create(
                mcq=mcq,
                user=request.user,
                case_data=case_data
            )
            print(f"💾 Created new case conversion for MCQ #{mcq_id}")
        
        # Create session ID for the case
        import uuid
        session_id = str(uuid.uuid4())
        case_data['session_id'] = session_id
        
        # Store case session data in session for state management
        request.session[f'case_session_{session_id}'] = {
            'case_data': case_data,
            'mcq_id': mcq_id,
            'state': 'INITIAL',
            'created_at': str(timezone.now()),
            'source': 'mcq_conversion'
        }
        
        return JsonResponse({
            'success': True,
            'session_id': session_id,
            'case_data': case_data,
            'message': 'MCQ successfully converted to case-based learning'
        })
        
    except Exception as e:
        print(f'Error converting MCQ {mcq_id} to case: {e}')
        return JsonResponse({
            'success': False,
            'error': f'Failed to convert MCQ to case: {str(e)}'
        }, status=500)
'''

# Solution 5: Management command to clear stale conversions
CLEANUP_COMMAND = '''
# Create management/commands/cleanup_mcq_conversions.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from mcq.models import MCQCaseConversion

class Command(BaseCommand):
    help = 'Clean up expired MCQ case conversions'
    
    def handle(self, *args, **options):
        # Delete expired conversions
        expired = MCQCaseConversion.objects.filter(
            expires_at__lt=timezone.now()
        )
        count = expired.count()
        expired.delete()
        
        self.stdout.write(
            self.style.SUCCESS(f'Deleted {count} expired MCQ case conversions')
        )
        
        # Clear cache entries
        from django.core.cache import cache
        # Note: This requires knowing all MCQ IDs or using a cache backend that supports pattern deletion
        self.stdout.write('Cache entries should expire automatically based on TTL')
'''

if __name__ == "__main__":
    print("MCQ Case Converter Caching Fix")
    print("=" * 50)
    print("\nThis fix addresses the issue of repeated generation of the same case")
    print("when converting MCQs to case-based learning sessions.")
    print("\nSolutions provided:")
    print("1. Add caching to mcq_case_converter.py")
    print("2. Add slight variation to case generation")
    print("3. Create MCQCaseConversion model for database storage")
    print("4. Update views.py to use cached conversions")
    print("5. Add management command for cleanup")
    print("\nImplementation steps:")
    print("1. Add the caching code to mcq_case_converter.py")
    print("2. Create and run migration for MCQCaseConversion model")
    print("3. Update views.py with the caching logic")
    print("4. Deploy the changes")
