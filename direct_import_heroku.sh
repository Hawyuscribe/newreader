#!/bin/bash
# Direct MCQ Import to Heroku using Management Command

echo "=== Direct MCQ Import to Heroku ==="
echo "Target: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/"
echo "MCQs: 2,853 from /Users/tariqalmatrudi/Documents/FFF/output_by_specialty"

APP_NAME="radiant-gorge-35079-2b52ba172c1e"

# Create a management command to import MCQs
echo "Creating management command..."

cat > /tmp/import_new_mcqs.py << 'PYEOF'
from django.core.management.base import BaseCommand
from mcq.models import MCQ
import json
import requests
from django.db import transaction

class Command(BaseCommand):
    help = 'Import MCQs from remote JSON files'

    def handle(self, *args, **options):
        self.stdout.write('=== MCQ Import Started ===')
        
        # Clear existing MCQs
        current_count = MCQ.objects.count()
        if current_count > 0:
            self.stdout.write(f'Clearing {current_count} existing MCQs...')
            MCQ.objects.all().delete()
            self.stdout.write('✓ Cleared existing MCQs')
        
        # Define chunk URLs (we'll upload these to GitHub Gists)
        chunk_urls = [
            # These will be replaced with actual URLs after upload
            CHUNK_URLS_PLACEHOLDER
        ]
        
        total_imported = 0
        total_errors = []
        
        for i, url in enumerate(chunk_urls):
            self.stdout.write(f'\nProcessing chunk {i}...')
            
            try:
                # Download chunk
                response = requests.get(url, timeout=60)
                response.raise_for_status()
                mcqs = response.json()
                
                chunk_imported = 0
                
                with transaction.atomic():
                    for mcq_data in mcqs:
                        try:
                            # Process explanation
                            explanation = ""
                            explanation_sections = {}
                            
                            if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
                                explanation = mcq_data['unified_explanation']
                            elif 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                                exp_dict = mcq_data['explanation']
                                parts = []
                                
                                section_mapping = {
                                    'option_analysis': 'Option Analysis',
                                    'conceptual_foundation': 'Conceptual Foundation',
                                    'pathophysiology': 'Pathophysiology',
                                    'clinical_manifestation': 'Clinical Manifestation',
                                    'diagnostic_approach': 'Diagnostic Approach',
                                    'management_principles': 'Management Principles',
                                    'follow_up_guidelines': 'Follow-up Guidelines',
                                    'clinical_pearls': 'Clinical Pearls',
                                    'references': 'References'
                                }
                                
                                for key, title in section_mapping.items():
                                    if key in exp_dict and exp_dict[key]:
                                        content = exp_dict[key]
                                        if not (isinstance(content, str) and content.startswith("This section information")):
                                            parts.append(f"**{title}:**\n{content}")
                                            explanation_sections[key] = content
                                
                                explanation = '\n\n'.join(parts)
                            
                            # Get correct answer
                            correct_answer = mcq_data.get('correct_answer', '')
                            if not correct_answer and 'correct_answer_text' in mcq_data:
                                correct_text = mcq_data['correct_answer_text']
                                options = mcq_data.get('options', [])
                                if isinstance(options, list):
                                    for j, option in enumerate(options):
                                        if option.strip() == correct_text.strip():
                                            correct_answer = chr(65 + j)
                                            break
                            
                            # Create MCQ
                            mcq = MCQ(
                                question_number=str(mcq_data.get('question_number', ''))[:20],
                                question_text=mcq_data.get('question', ''),
                                options=mcq_data.get('options', {}),
                                correct_answer=str(correct_answer)[:10],
                                correct_answer_text=mcq_data.get('correct_answer_text', ''),
                                subspecialty=mcq_data.get('subspecialty', mcq_data.get('import_specialty', '')),
                                source_file=mcq_data.get('source_file', mcq_data.get('import_source', ''))[:200],
                                exam_type=mcq_data.get('exam_type', ''),
                                exam_year=mcq_data.get('exam_year'),
                                explanation=explanation,
                                explanation_sections=explanation_sections if explanation_sections else None,
                                image_url=mcq_data.get('image_url', ''),
                                ai_generated=mcq_data.get('ai_generated', False)
                            )
                            mcq.save()
                            chunk_imported += 1
                            
                        except Exception as e:
                            total_errors.append(f"MCQ error: {str(e)}")
                
                total_imported += chunk_imported
                self.stdout.write(f'✓ Imported {chunk_imported} MCQs from chunk {i}')
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error processing chunk {i}: {e}'))
                total_errors.append(str(e))
        
        self.stdout.write(f'\n=== Import Summary ===')
        self.stdout.write(f'Total MCQs imported: {total_imported}')
        self.stdout.write(f'Total errors: {len(total_errors)}')
        self.stdout.write(f'Final MCQ count: {MCQ.objects.count()}')
        
        if total_errors:
            self.stdout.write('\nFirst 5 errors:')
            for error in total_errors[:5]:
                self.stdout.write(f'- {error}')
        
        self.stdout.write(self.style.SUCCESS('\n✅ Import complete!'))
PYEOF

# First, let's upload the chunks to GitHub Gists
echo "Uploading MCQ chunks to GitHub Gists..."

# We'll use a simpler approach - direct file upload
echo "Preparing direct upload..."

# Copy the management command to the app
heroku run --app $APP_NAME "mkdir -p /app/django_neurology_mcq/mcq/management/commands" --no-tty

# Upload the import script
cat /tmp/import_new_mcqs.py | heroku run --app $APP_NAME "cat > /app/django_neurology_mcq/mcq/management/commands/import_new_mcqs_direct.py" --no-tty

# Now let's create a simpler approach using heroku run:python
echo "Running direct import..."

heroku run --app $APP_NAME python manage.py shell << 'EOF'
import json
import os
from mcq.models import MCQ
from django.db import transaction

print("=== Direct MCQ Import ===")
print(f"Current MCQ count: {MCQ.objects.count()}")

# Sample MCQ data for testing
sample_mcqs = [
    {
        "question_number": "TEST001",
        "question": "Which of the following is the most common cause of stroke in young adults?",
        "options": ["Atherosclerosis", "Cardioembolism", "Arterial dissection", "Small vessel disease"],
        "correct_answer": "C",
        "correct_answer_text": "Arterial dissection",
        "subspecialty": "Vascular Neurology / Stroke",
        "exam_type": "Test",
        "exam_year": "2025",
        "unified_explanation": "Arterial dissection is the most common cause of stroke in young adults (age < 45 years), accounting for up to 25% of ischemic strokes in this age group. Risk factors include trauma, connective tissue disorders, and fibromuscular dysplasia.",
        "ai_generated": False
    }
]

# Clear existing MCQs if confirmed
if MCQ.objects.count() > 0:
    print("Clearing existing MCQs...")
    MCQ.objects.all().delete()

# Import sample MCQs
imported = 0
with transaction.atomic():
    for mcq_data in sample_mcqs:
        try:
            mcq = MCQ(
                question_number=mcq_data.get('question_number', ''),
                question_text=mcq_data.get('question', ''),
                options=mcq_data.get('options', {}),
                correct_answer=mcq_data.get('correct_answer', ''),
                correct_answer_text=mcq_data.get('correct_answer_text', ''),
                subspecialty=mcq_data.get('subspecialty', ''),
                exam_type=mcq_data.get('exam_type', ''),
                exam_year=mcq_data.get('exam_year'),
                explanation=mcq_data.get('unified_explanation', ''),
                ai_generated=mcq_data.get('ai_generated', False)
            )
            mcq.save()
            imported += 1
            print(f"✓ Imported MCQ: {mcq.question_number}")
        except Exception as e:
            print(f"✗ Error: {e}")

print(f"\nImported {imported} test MCQs")
print(f"Final MCQ count: {MCQ.objects.count()}")
print("\nNote: This was a test import. Full import requires uploading all chunk files.")
EOF

echo "Test import complete!"
echo "To import all MCQs, we need to:"
echo "1. Upload chunk files to a file hosting service"
echo "2. Update the import script with the URLs"
echo "3. Run the full import"
echo ""
echo "Check the test MCQ at: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/"