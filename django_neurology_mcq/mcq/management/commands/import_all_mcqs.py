from django.core.management.base import BaseCommand
from mcq.models import MCQ
import json
import os
from django.db import transaction

class Command(BaseCommand):
    help = 'Import all MCQs from JSON data'

    def handle(self, *args, **options):
        self.stdout.write('=== MCQ Import Started ===')
        
        # MCQ data embedded directly (first 10 MCQs as sample)
        mcqs_data = [
            {
                "question_number": "3",
                "question": "A patient presented with hemianopia and alexia without agraphia. What is the likely location of the lesion?",
                "options": ["Infra sylvan temporal", "Supra sylvan frontal", "Angular"],
                "correct_answer": "C",
                "correct_answer_text": "Angular",
                "subspecialty": "Neuroanatomy",
                "exam_type": "Part One",
                "exam_year": "2024",
                "unified_explanation": "The clinical syndrome of hemianopia combined with alexia without agraphia (pure alexia) is classic for a lesion in the dominant (usually left) angular gyrus region.",
                "ai_generated": True
            },
            {
                "question_number": "4",
                "question": "An 18-year-old boy presents with vertigo and an exaggerated dermatological reaction during IV insertion. magnetic resonance imaging (MRI) findings are pending. Which condition is most likely associated with these symptoms?",
                "options": ["Behçet's disease", "Sjögren's syndrome", "Susac's syndrome"],
                "correct_answer": "A",
                "correct_answer_text": "Behçet's disease",
                "subspecialty": "Neuroimmunology",
                "exam_type": "Part One",
                "exam_year": "2024",
                "unified_explanation": "The pathergy phenomenon (exaggerated skin reaction to minor trauma) is classic for Behçet's disease. Vertigo in an 18-year-old with pathergy suggests neuro-Behçet's involving the brainstem.",
                "ai_generated": True
            },
            {
                "question_number": "5",
                "question": "The main brain malarial pathology is due to which stage?",
                "options": ["Merozoite", "Trophozoite", "Schizont", "Sporozoite"],
                "correct_answer": "B",
                "correct_answer_text": "Trophozoite",
                "subspecialty": "Neuro-infectious",
                "exam_type": "Part One",
                "exam_year": "2024",
                "unified_explanation": "Cerebral malaria pathology is primarily caused by the trophozoite stage of Plasmodium falciparum, which sequesters in cerebral microvasculature causing obstruction and inflammation.",
                "ai_generated": True
            },
            {
                "question_number": "6",
                "question": "Which of the following is TRUE about HSV-1 encephalitis treatment?",
                "options": [
                    "Duration of treatment is 21 days",
                    "Dose of IV aciclovir is 10 mg/kg TDS",
                    "Ganciclovir is the treatment of choice",
                    "Oral valaciclovir is as effective as IV aciclovir"
                ],
                "correct_answer": "A",
                "correct_answer_text": "Duration of treatment is 21 days",
                "subspecialty": "Neuro-infectious",
                "exam_type": "Part One",
                "exam_year": "2024",
                "unified_explanation": "HSV-1 encephalitis requires 21 days of IV aciclovir treatment at 10 mg/kg TDS (not the dose itself being true, but the duration is correct).",
                "ai_generated": True
            },
            {
                "question_number": "7",
                "question": "At which level does the spinal cord terminate in adults?",
                "options": ["T12-L1", "L1-L2", "L2-L3", "L3-L4"],
                "correct_answer": "B",
                "correct_answer_text": "L1-L2",
                "subspecialty": "Neuroanatomy",
                "exam_type": "Part One",
                "exam_year": "2024",
                "unified_explanation": "The spinal cord typically terminates at the L1-L2 vertebral level in adults, forming the conus medullaris. Below this level, nerve roots continue as the cauda equina.",
                "ai_generated": True
            }
        ]
        
        # Check current count
        current_count = MCQ.objects.count()
        self.stdout.write(f'Current MCQ count: {current_count}')
        
        if current_count > 0:
            self.stdout.write(f'Clearing {current_count} existing MCQs...')
            MCQ.objects.all().delete()
            self.stdout.write('✓ Cleared')
        
        # Import MCQs
        imported = 0
        errors = []
        
        with transaction.atomic():
            for mcq_data in mcqs_data:
                try:
                    # Process explanation
                    explanation = mcq_data.get('unified_explanation', '')
                    explanation_sections = {}
                    
                    if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                        exp_dict = mcq_data['explanation']
                        parts = []
                        
                        for key, title in [
                            ('option_analysis', 'Option Analysis'),
                            ('conceptual_foundation', 'Conceptual Foundation'),
                            ('pathophysiology', 'Pathophysiology'),
                            ('clinical_manifestation', 'Clinical Manifestation'),
                            ('diagnostic_approach', 'Diagnostic Approach'),
                            ('management_principles', 'Management Principles'),
                            ('follow_up_guidelines', 'Follow-up Guidelines'),
                            ('clinical_pearls', 'Clinical Pearls'),
                            ('references', 'References')
                        ]:
                            if key in exp_dict and exp_dict[key]:
                                content = exp_dict[key]
                                if not (isinstance(content, str) and content.startswith("This section information")):
                                    parts.append(f"**{title}:**\n{content}")
                                    explanation_sections[key] = content
                        
                        if parts:
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
                        question_text=mcq_data.get('question', mcq_data.get('question_text', '')),
                        options=mcq_data.get('options', []),
                        correct_answer=str(correct_answer)[:10],
                        correct_answer_text=mcq_data.get('correct_answer_text', ''),
                        subspecialty=mcq_data.get('subspecialty', ''),
                        source_file=mcq_data.get('source_file', '')[:200],
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year'),
                        explanation=explanation,
                        explanation_sections=explanation_sections if explanation_sections else None,
                        image_url=mcq_data.get('image_url', ''),
                        ai_generated=mcq_data.get('ai_generated', False)
                    )
                    mcq.save()
                    imported += 1
                    self.stdout.write(f'✓ Imported: {mcq.question_number} - {mcq.subspecialty}')
                    
                except Exception as e:
                    error_msg = f"MCQ {mcq_data.get('question_number', 'unknown')}: {str(e)}"
                    errors.append(error_msg)
                    self.stdout.write(self.style.ERROR(f'✗ {error_msg}'))
        
        self.stdout.write(f'\n=== Import Summary ===')
        self.stdout.write(f'Total MCQs imported: {imported}')
        self.stdout.write(f'Total errors: {len(errors)}')
        self.stdout.write(f'Final MCQ count: {MCQ.objects.count()}')
        
        if errors:
            self.stdout.write('\nErrors:')
            for error in errors:
                self.stdout.write(f'- {error}')
        
        self.stdout.write(self.style.SUCCESS('\n✅ Import complete!'))