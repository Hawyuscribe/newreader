from django.core.management.base import BaseCommand
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
import json
import os
from datetime import datetime
import requests

class Command(BaseCommand):
    help = 'Import all MCQs from a consolidated source'

    def handle(self, *args, **options):
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"MCQ Import - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.stdout.write(f"{'='*60}\n")
        
        # Clear existing data
        with transaction.atomic():
            self.stdout.write("Clearing existing data...")
            Flashcard.objects.all().delete()
            IncorrectAnswer.objects.all().delete()
            Bookmark.objects.all().delete()
            deleted = MCQ.objects.all().delete()[0]
            self.stdout.write(f"Deleted {deleted} existing MCQs\n")
        
        # Try to load from a URL or local file
        mcqs_to_import = []
        
        # Option 1: Try loading from a public URL (if you upload the JSON to a gist or public location)
        # url = "https://gist.githubusercontent.com/your-username/gist-id/raw/all_mcqs.json"
        # try:
        #     response = requests.get(url, timeout=30)
        #     if response.status_code == 200:
        #         data = response.json()
        #         mcqs_to_import = data.get('mcqs', [])
        # except Exception as e:
        #     self.stdout.write(f"Could not load from URL: {e}")
        
        # Option 2: Load a subset of MCQs directly
        if not mcqs_to_import:
            self.stdout.write("Loading sample MCQs...")
            mcqs_to_import = self.get_sample_mcqs()
        
        # Import the MCQs
        total_imported = 0
        batch_size = 50
        
        with transaction.atomic():
            for i in range(0, len(mcqs_to_import), batch_size):
                batch = mcqs_to_import[i:i+batch_size]
                
                for mcq_data in batch:
                    try:
                        # Extract options
                        options = mcq_data.get('options', [])
                        option_a = options[0] if len(options) > 0 else ''
                        option_b = options[1] if len(options) > 1 else ''
                        option_c = options[2] if len(options) > 2 else ''
                        option_d = options[3] if len(options) > 3 else ''
                        option_e = options[4] if len(options) > 4 else ''
                        
                        # Get explanation sections
                        explanation_data = mcq_data.get('explanation', {})
                        explanation_sections = {}
                        
                        if isinstance(explanation_data, dict):
                            for key in ['option_analysis', 'clinical_manifestation', 'diagnostic_approach', 
                                       'management_principles', 'follow_up_guidelines', 'conceptual_foundation',
                                       'pathophysiology', 'clinical_pearls', 'references']:
                                if key in explanation_data:
                                    explanation_sections[key] = explanation_data[key]
                        
                        # Create unified explanation
                        unified_explanation = mcq_data.get('unified_explanation', '')
                        if not unified_explanation and explanation_sections:
                            unified_explanation = '\n\n'.join([
                                f"{k.replace('_', ' ').title()}: {v}"
                                for k, v in explanation_sections.items()
                                if v and 'included within the unified explanation' not in v
                            ])
                        
                        # Create MCQ
                        mcq = MCQ(
                            question=mcq_data['question'],
                            option_a=option_a,
                            option_b=option_b,
                            option_c=option_c,
                            option_d=option_d,
                            option_e=option_e,
                            correct_answer=mcq_data.get('correct_answer', ''),
                            explanation=unified_explanation,
                            explanation_sections=explanation_sections,
                            specialty='Neurology',
                            subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                            exam_name=f"{mcq_data.get('exam_type', '')} {mcq_data.get('exam_year', '')}".strip(),
                            year=mcq_data.get('exam_year'),
                            topic='',
                            difficulty=3,
                            cognitive_level='Recall',
                            references=explanation_sections.get('references', ''),
                            high_yield=False,
                            image_url=''
                        )
                        mcq.save()
                        total_imported += 1
                        
                    except Exception as e:
                        self.stdout.write(f"Error importing MCQ: {str(e)[:100]}")
                        continue
                
                self.stdout.write(f"Imported {total_imported} MCQs...")
        
        # Final report
        total_in_db = MCQ.objects.count()
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(self.style.SUCCESS(f"Import Complete!"))
        self.stdout.write(f"Total MCQs imported: {total_imported}")
        self.stdout.write(f"Total MCQs in database: {total_in_db}")
        
        # Show subspecialty breakdown
        from django.db.models import Count
        subspecialties = MCQ.objects.values('subspecialty').annotate(
            count=Count('id')
        ).order_by('-count')[:15]
        
        self.stdout.write(f"\nSubspecialty breakdown:")
        for spec in subspecialties:
            self.stdout.write(f"  {spec['subspecialty']}: {spec['count']}")
        
        self.stdout.write(f"{'='*60}\n")
    
    def get_sample_mcqs(self):
        """Returns sample MCQs to ensure the system works"""
        return [
            {
                "question": "A 65-year-old man presents with sudden onset of right-sided weakness and difficulty speaking. His symptoms began 2 hours ago. CT scan shows no hemorrhage. What is the most appropriate immediate treatment?",
                "options": ["Aspirin 325 mg", "Intravenous tissue plasminogen activator (tPA)", "Heparin infusion", "Warfarin", "Clopidogrel 300 mg"],
                "correct_answer": "B",
                "subspecialty": "Vascular Neurology/Stroke",
                "exam_year": "2024",
                "exam_type": "Part II",
                "explanation": {
                    "option_analysis": "For acute ischemic stroke within 4.5 hours of symptom onset and no contraindications, IV tPA is the treatment of choice. Option A (Aspirin) is used for secondary prevention. Option C (Heparin) is not routinely used in acute stroke. Option D (Warfarin) is for long-term anticoagulation. Option E (Clopidogrel) is for secondary prevention.",
                    "clinical_manifestation": "Sudden onset focal neurological deficits including hemiparesis, aphasia, and facial droop are classic presentations of acute ischemic stroke.",
                    "management_principles": "Time is brain. IV tPA within 4.5 hours improves outcomes. Exclude hemorrhage with CT. Monitor for hemorrhagic transformation."
                }
            },
            {
                "question": "A patient with Parkinson's disease presents with hallucinations and forgetfulness. What is the most appropriate management option?",
                "options": ["Rivastigmine", "Clozapine", "Levodopa", "Amantadine"],
                "correct_answer": "A",
                "subspecialty": "Movement Disorders",
                "exam_year": "2024",
                "exam_type": "Part I",
                "explanation": {
                    "option_analysis": "In Parkinson's disease dementia with psychosis, rivastigmine (cholinesterase inhibitor) is first-line as it improves cognition and can reduce hallucinations without worsening motor symptoms.",
                    "pathophysiology": "PD dementia involves cholinergic deficits and Lewy body pathology extending to cortical regions.",
                    "management_principles": "Start rivastigmine 1.5 mg BID, titrate slowly. Monitor for GI side effects. Avoid anticholinergics."
                }
            },
            {
                "question": "Which medication is most effective for preventing migraine headaches?",
                "options": ["Sumatriptan", "Propranolol", "Acetaminophen", "Prednisone", "Morphine"],
                "correct_answer": "B",
                "subspecialty": "Headache Medicine",
                "exam_year": "2024",
                "exam_type": "Part I",
                "explanation": {
                    "option_analysis": "Propranolol is a beta-blocker proven effective for migraine prophylaxis. Sumatriptan is for acute treatment, not prevention.",
                    "clinical_manifestation": "Migraines present with unilateral throbbing headache, photophobia, phonophobia, and sometimes aura.",
                    "management_principles": "Prophylaxis indicated for >4 headache days/month. Start propranolol 40 mg BID, titrate to effect."
                }
            },
            {
                "question": "A 28-year-old woman presents with optic neuritis. MRI shows multiple periventricular white matter lesions. What is the most likely diagnosis?",
                "options": ["Multiple sclerosis", "Neuromyelitis optica", "ADEM", "CNS lymphoma", "Sarcoidosis"],
                "correct_answer": "A",
                "subspecialty": "Neuroimmunology",
                "exam_year": "2024",
                "exam_type": "Part II",
                "explanation": {
                    "option_analysis": "Young woman with optic neuritis and periventricular white matter lesions is classic for MS. NMO typically has longitudinally extensive spinal cord lesions.",
                    "diagnostic_approach": "McDonald criteria: dissemination in space and time. CSF oligoclonal bands. Visual evoked potentials.",
                    "management_principles": "Acute: IV methylprednisolone 1g daily x 3-5 days. DMT options include interferons, glatiramer, fingolimod, natalizumab."
                }
            },
            {
                "question": "A patient presents with ptosis and diplopia that worsen with activity. Which test is most diagnostic?",
                "options": ["EMG", "Edrophonium test", "MRI brain", "Acetylcholine receptor antibodies", "Muscle biopsy"],
                "correct_answer": "D",
                "subspecialty": "Neuromuscular",
                "exam_year": "2024",
                "exam_type": "Part I",
                "explanation": {
                    "option_analysis": "Fatigable ptosis and diplopia suggest myasthenia gravis. AChR antibodies are highly specific (>95%) and diagnostic.",
                    "pathophysiology": "Autoimmune destruction of postsynaptic acetylcholine receptors at neuromuscular junction.",
                    "management_principles": "Pyridostigmine for symptomatic relief. Immunosuppression with prednisone, azathioprine. Thymectomy if thymoma."
                }
            }
        ]