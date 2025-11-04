#!/usr/bin/env python
"""
Simple view to trigger MCQ import and check database status
Add this to urls.py: path('admin/import-mcqs/', trigger_import_view, name='trigger_import')
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
from mcq.models import MCQ
import json
import os

@staff_member_required
@require_http_methods(["GET", "POST"])
def trigger_import_view(request):
    """View to check MCQ count and optionally trigger import."""
    
    try:
        # Get current count
        current_count = MCQ.objects.count()
        
        if request.method == "GET":
            return JsonResponse({
                "status": "success",
                "current_mcq_count": current_count,
                "action": "status_check"
            })
        
        # POST request - trigger import
        try:
            # Try to find consolidated file
            possible_paths = [
                'consolidated_all_mcqs.json',
                '/app/consolidated_all_mcqs.json',
                '/app/django_neurology_mcq/consolidated_all_mcqs.json'
            ]
            
            json_file_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    json_file_path = path
                    break
            
            if not json_file_path:
                return JsonResponse({
                    "status": "error",
                    "message": "Consolidated MCQ file not found",
                    "current_mcq_count": current_count
                })
            
            # Load and check for missing MCQs
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            all_mcqs = data.get('mcqs', [])
            existing_question_numbers = set(MCQ.objects.values_list('question_number', flat=True))
            
            missing_mcqs = []
            for mcq_data in all_mcqs:
                question_number = mcq_data.get('question_number', '')
                if question_number and question_number not in existing_question_numbers:
                    missing_mcqs.append(mcq_data)
            
            if not missing_mcqs:
                return JsonResponse({
                    "status": "success",
                    "message": "No missing MCQs found",
                    "current_mcq_count": current_count,
                    "total_available": len(all_mcqs)
                })
            
            # Import missing MCQs (limit to 50 for safety)
            created_count = 0
            errors = []
            
            for mcq_data in missing_mcqs[:50]:  # Limit for safety
                try:
                    # Process explanation sections
                    explanation_sections = {}
                    if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                        explanation_sections = mcq_data['explanation']
                    
                    # Create MCQ
                    mcq = MCQ(
                        question_number=mcq_data.get('question_number', ''),
                        question_text=mcq_data.get('question', ''),
                        options=mcq_data.get('options', []),
                        correct_answer=mcq_data.get('correct_answer', ''),
                        correct_answer_text=mcq_data.get('correct_answer_text', ''),
                        subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                        explanation_sections=explanation_sections,
                        source_file=mcq_data.get('source_file', ''),
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year', ''),
                        ai_generated=mcq_data.get('ai_generated', False),
                        unified_explanation=mcq_data.get('unified_explanation', ''),
                        image_url=mcq_data.get('image_url', '')
                    )
                    mcq.save()
                    created_count += 1
                
                except Exception as e:
                    errors.append(f"MCQ {mcq_data.get('question_number', 'Unknown')}: {str(e)}")
            
            final_count = MCQ.objects.count()
            
            return JsonResponse({
                "status": "success",
                "message": f"Import completed successfully",
                "created_count": created_count,
                "initial_count": current_count,
                "final_count": final_count,
                "missing_found": len(missing_mcqs),
                "errors": errors[:5]  # Show first 5 errors only
            })
        
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": f"Import failed: {str(e)}",
                "current_mcq_count": current_count
            })
    
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": f"Database error: {str(e)}"
        })