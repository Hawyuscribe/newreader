from mcq.models import MCQ
from django.db import transaction
import json
import sys
import os

# Load JSON file
json_file = '/tmp/import_data.json'
print(f"Loading MCQs from {json_file}...")

try:
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Check if we have MCQs
    if "mcqs" in data:
        mcqs_data = data["mcqs"]
        print(f"Found {len(mcqs_data)} MCQs in the JSON file")
    else:
        print("No MCQs found in the JSON file")
        sys.exit(1)
    
    # Import MCQs
    success_count = 0
    error_count = 0
    subspecialty = "Headache"
    
    # Count existing MCQs
    existing_count = MCQ.objects.filter(subspecialty=subspecialty).count()
    print(f"Existing MCQs for {subspecialty}: {existing_count}")
    
    # Process MCQs
    with transaction.atomic():
        for mcq_data in mcqs_data:
            try:
                # Build MCQ object
                options = {}
                for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
                    option_key = f"Option {letter}"
                    if option_key in mcq_data and mcq_data[option_key]:
                        options[letter] = mcq_data[option_key].strip()
                
                # Get question text
                question_text = mcq_data.get("Question Text", "").strip()
                if not question_text and "Question" in mcq_data:
                    question_text = mcq_data["Question"].strip()
                
                # Get correct answer
                correct_answer = None
                if "Correct Answer" in mcq_data and mcq_data["Correct Answer"]:
                    correct_answer = mcq_data["Correct Answer"].strip().upper()
                    if correct_answer and len(correct_answer) > 0:
                        correct_answer = correct_answer[0]
                
                # Check if MCQ already exists
                existing = MCQ.objects.filter(
                    question_text=question_text,
                    subspecialty=subspecialty
                ).first()
                
                # Create explanation sections if available
                explanation_sections = {}
                section_fields = [
                    "Conceptual Foundation", "Pathophysiology", "Clinical Correlation",
                    "Diagnostic Approach", "Management Principles", "Classification and Neurology",
                    "Clinical Pearls", "Current Evidence", "Classification & Nosology"
                ]
                
                for field in section_fields:
                    if field in mcq_data and mcq_data[field]:
                        section_key = field.lower().replace(" ", "_").replace("&", "and")
                        explanation_sections[section_key] = mcq_data[field]
                
                # Create or update MCQ
                if existing:
                    # Update existing
                    existing.question_text = question_text
                    existing.options = options
                    existing.correct_answer = correct_answer
                    existing.explanation = mcq_data.get("Option Analysis", "")
                    existing.exam_type = mcq_data.get("Exam Type", "Unknown")
                    existing.exam_year = mcq_data.get("Exam Year", "Unknown")
                    existing.question_number = mcq_data.get("Question Number", "")
                    existing.has_image = mcq_data.get("Has Image", "No").lower() == "yes"
                    existing.image_url = mcq_data.get("Image URL", "")
                    existing.original_id = mcq_data.get("ID", "")
                    
                    if explanation_sections:
                        existing.explanation_sections = explanation_sections
                    
                    existing.save()
                else:
                    # Create new MCQ
                    mcq = MCQ(
                        question_text=question_text,
                        options=options,
                        correct_answer=correct_answer,
                        subspecialty=subspecialty,
                        explanation=mcq_data.get("Option Analysis", ""),
                        exam_type=mcq_data.get("Exam Type", "Unknown"),
                        exam_year=mcq_data.get("Exam Year", "Unknown"),
                        question_number=mcq_data.get("Question Number", ""),
                        has_image=mcq_data.get("Has Image", "No").lower() == "yes",
                        image_url=mcq_data.get("Image URL", ""),
                        original_id=mcq_data.get("ID", "")
                    )
                    
                    if explanation_sections:
                        mcq.explanation_sections = explanation_sections
                    
                    mcq.save()
                
                success_count += 1
            except Exception as e:
                print(f"Error importing MCQ: {str(e)}")
                error_count += 1
    
    # Count MCQs after import
    after_count = MCQ.objects.filter(subspecialty=subspecialty).count()
    print(f"After import: {after_count} MCQs for {subspecialty}")
    print(f"Imported: {success_count} successful, {error_count} failed")
    print(f"Net change: {after_count - existing_count} MCQs added")
    
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)
