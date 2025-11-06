"""
Create a temporary test endpoint for MCQ conversion testing
This can be added to urls.py temporarily for testing
"""

# Add this to django_neurology_mcq/mcq/urls.py temporarily:

TEST_ENDPOINT_CODE = """
# Temporary test endpoint (REMOVE AFTER TESTING)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["GET", "POST"])
def test_mcq_conversion(request, mcq_id=None):
    '''Temporary endpoint for testing MCQ conversion without login'''
    from .models import MCQ, User
    from .mcq_case_converter import convert_mcq_to_case, clear_mcq_cache
    import json
    
    try:
        # Use provided MCQ ID or default to the problematic one
        if not mcq_id:
            mcq_id = request.GET.get('mcq_id', 100420848)
        
        # Get MCQ
        mcq = MCQ.objects.get(id=mcq_id)
        
        # Clear cache if requested
        if request.GET.get('clear_cache') == 'true':
            clear_mcq_cache(mcq.id)
        
        # Get or create test user
        test_user, _ = User.objects.get_or_create(
            username='test_conversion_user',
            defaults={'email': 'test@example.com'}
        )
        
        # Convert MCQ to case
        case_data = convert_mcq_to_case(mcq)
        
        # Extract key information
        result = {
            'success': True,
            'mcq_id': mcq.id,
            'subspecialty': mcq.subspecialty,
            'question_preview': mcq.question_text[:100],
            'case_summary': {
                'patient': case_data.get('patient_demographics'),
                'specialty': case_data.get('specialty'),
                'core_concept': case_data.get('core_concept_type'),
                'clinical_presentation': case_data.get('clinical_presentation', '')[:200],
            },
            'validation': None
        }
        
        # Check validation if available
        if '_extended_data' in case_data and 'validation_metadata' in case_data['_extended_data']:
            result['validation'] = case_data['_extended_data']['validation_metadata']
        
        # Check if case matches MCQ topic
        case_text = json.dumps(case_data).lower()
        if mcq_id == 100420848:  # The Parkinson's MCQ
            result['content_check'] = {
                'has_parkinsons': 'parkinson' in case_text,
                'has_peripheral_neuropathy': 'peripheral neuropathy' in case_text,
                'correct': 'parkinson' in case_text and 'peripheral neuropathy' not in case_text
            }
        
        return JsonResponse(result)
        
    except MCQ.DoesNotExist:
        return JsonResponse({'success': False, 'error': f'MCQ {mcq_id} not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

# Add to urlpatterns:
# path('test-conversion/<int:mcq_id>/', test_mcq_conversion, name='test_mcq_conversion'),
# path('test-conversion/', test_mcq_conversion, name='test_mcq_conversion_default'),
"""

print("To add a test endpoint, add the following to your urls.py:")
print("=" * 80)
print(TEST_ENDPOINT_CODE)
print("=" * 80)
print("\nThen you can test with:")
print("curl https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/test-conversion/100420848/")
print("curl https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/test-conversion/?clear_cache=true")