from django.core.management.base import BaseCommand
from mcq.models import MCQ, Flashcard, IncorrectAnswer, Bookmark
from django.db import transaction
import json
import os
from datetime import datetime

class Command(BaseCommand):
    help = 'Import MCQs using the correct model field names'

    def handle(self, *args, **options):
        self.stdout.write(f"\n{'='*60}")
        self.stdout.write(f"MCQ Import (Correct Format) - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.stdout.write(f"{'='*60}\n")
        
        # Clear existing data
        with transaction.atomic():
            self.stdout.write("Clearing existing data...")
            Flashcard.objects.all().delete()
            IncorrectAnswer.objects.all().delete()
            Bookmark.objects.all().delete()
            deleted = MCQ.objects.all().delete()[0]
            self.stdout.write(f"Deleted {deleted} existing MCQs\n")
        
        # Load sample MCQs with correct field mapping
        mcqs_to_import = self.get_sample_mcqs()
        
        # Import the MCQs
        total_imported = 0
        
        with transaction.atomic():
            for mcq_data in mcqs_to_import:
                try:
                    # Get explanation sections from your JSON structure
                    explanation_data = mcq_data.get('explanation', {})
                    explanation_sections = {}
                    
                    if isinstance(explanation_data, dict):
                        # Map the explanation sections
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
                    
                    # Use the CORRECT field names from your model
                    mcq = MCQ(
                        question_number=mcq_data.get('question_number', ''),
                        question_text=mcq_data['question'],  # question_text not question
                        options=mcq_data.get('options', []),  # options as JSON array
                        correct_answer=mcq_data.get('correct_answer', ''),
                        correct_answer_text=mcq_data.get('correct_answer_text', ''),
                        subspecialty=mcq_data.get('subspecialty', 'General Neurology'),
                        source_file=mcq_data.get('source_file', ''),
                        exam_type=mcq_data.get('exam_type', ''),
                        exam_year=mcq_data.get('exam_year', ''),
                        ai_generated=mcq_data.get('ai_generated', False),
                        unified_explanation=unified_explanation,
                        explanation=unified_explanation,  # Also store in explanation field
                        explanation_sections=explanation_sections,
                        image_url=mcq_data.get('image_url', '')
                    )
                    mcq.save()
                    total_imported += 1
                    
                except Exception as e:
                    self.stdout.write(f"Error importing MCQ: {str(e)}")
                    continue
        
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
        """Returns sample MCQs in the exact format from your JSON files"""
        return [
            {
                "question_number": "1",
                "question": "A 65-year-old man presents with sudden onset of right-sided weakness and difficulty speaking. His symptoms began 2 hours ago. CT scan shows no hemorrhage. What is the most appropriate immediate treatment?",
                "options": [
                    "Aspirin 325 mg",
                    "Intravenous tissue plasminogen activator (tPA)", 
                    "Heparin infusion",
                    "Warfarin",
                    "Clopidogrel 300 mg"
                ],
                "correct_answer": "B",
                "correct_answer_text": "Intravenous tissue plasminogen activator (tPA)",
                "subspecialty": "Vascular Neurology/Stroke",
                "exam_year": "2024",
                "exam_type": "Part II",
                "ai_generated": True,
                "explanation": {
                    "option_analysis": "Option A: Aspirin 325 mg is used for secondary stroke prevention, not acute treatment. Option B: IV tPA is the gold standard for acute ischemic stroke within 4.5 hours of symptom onset in eligible patients. Option C: Heparin is not routinely recommended for acute stroke. Option D: Warfarin is for long-term anticoagulation. Option E: Clopidogrel is for secondary prevention.",
                    "clinical_manifestation": "Acute focal neurological deficits including hemiparesis, aphasia, and facial droop are classic presentations of acute ischemic stroke. Time of onset is critical for treatment decisions.",
                    "management_principles": "Time is brain in acute stroke. IV tPA should be administered within 4.5 hours of symptom onset after excluding hemorrhage with CT and confirming eligibility criteria.",
                    "references": "Powers WJ et al. Stroke. 2019;50:e344-e418. AHA/ASA Guidelines for Acute Ischemic Stroke Treatment."
                },
                "source_file": "vascular_neurology_stroke_mcqs.json"
            },
            {
                "question_number": "2", 
                "question": "A patient with Parkinson's disease presents with hallucinations and forgetfulness. What is the most appropriate management option?",
                "options": [
                    "Rivastigmine",
                    "Clozapine", 
                    "Levodopa",
                    "Amantadine"
                ],
                "correct_answer": "A",
                "correct_answer_text": "Rivastigmine",
                "subspecialty": "Movement Disorders",
                "exam_year": "2024",
                "exam_type": "Part I",
                "ai_generated": True,
                "explanation": {
                    "option_analysis": "Option A: Rivastigmine (cholinesterase inhibitor) is first-line for PD dementia with psychosis as it improves cognition and can reduce hallucinations without worsening motor symptoms. Option B: Clozapine treats refractory psychosis but carries agranulocytosis risk. Option C: Levodopa may worsen hallucinations. Option D: Amantadine is not indicated for cognitive impairment.",
                    "pathophysiology": "PD dementia involves cholinergic deficits and Lewy body pathology extending to cortical regions, leading to cognitive decline and visual hallucinations.",
                    "management_principles": "Start rivastigmine 1.5 mg BID, titrate slowly. Monitor for GI side effects. Avoid anticholinergics which worsen cognition.",
                    "references": "Emre M et al. Lancet Neurol. 2004;3:496-503. Cholinesterase inhibitors in PD dementia."
                },
                "source_file": "movement_disorders_mcqs.json"
            },
            {
                "question_number": "3",
                "question": "Which medication is most effective for preventing migraine headaches?",
                "options": [
                    "Sumatriptan",
                    "Propranolol",
                    "Acetaminophen", 
                    "Prednisone",
                    "Morphine"
                ],
                "correct_answer": "B",
                "correct_answer_text": "Propranolol",
                "subspecialty": "Headache Medicine",
                "exam_year": "2024", 
                "exam_type": "Part I",
                "ai_generated": False,
                "explanation": {
                    "option_analysis": "Option A: Sumatriptan is for acute migraine treatment, not prevention. Option B: Propranolol is a proven first-line migraine prophylactic agent. Option C: Acetaminophen is for acute treatment. Option D: Prednisone is not used for migraine prevention. Option E: Morphine is not appropriate for migraine.",
                    "clinical_manifestation": "Migraines present with unilateral throbbing headache, photophobia, phonophobia, and sometimes visual or sensory aura lasting 4-72 hours.",
                    "management_principles": "Prophylaxis indicated for ≥4 headache days/month or significant disability. Start propranolol 40 mg BID, titrate to 80-240 mg daily divided.",
                    "references": "Silberstein SD et al. Neurology. 2012;78:1337-1345. AAN migraine prevention guidelines."
                },
                "source_file": "headache_mcqs.json"
            },
            {
                "question_number": "4",
                "question": "A 28-year-old woman presents with optic neuritis. MRI shows multiple periventricular white matter lesions. What is the most likely diagnosis?",
                "options": [
                    "Multiple sclerosis",
                    "Neuromyelitis optica",
                    "ADEM", 
                    "CNS lymphoma",
                    "Sarcoidosis"
                ],
                "correct_answer": "A",
                "correct_answer_text": "Multiple sclerosis",
                "subspecialty": "Neuroimmunology",
                "exam_year": "2024",
                "exam_type": "Part II", 
                "ai_generated": True,
                "explanation": {
                    "option_analysis": "Option A: Young woman with optic neuritis and periventricular white matter lesions is classic for MS presentation. Option B: NMO typically has longitudinally extensive spinal cord lesions and AQP4 antibodies. Option C: ADEM is monophasic and more common in children. Option D: CNS lymphoma shows contrast enhancement. Option E: Sarcoidosis has different imaging pattern.",
                    "diagnostic_approach": "McDonald criteria require dissemination in space and time. CSF oligoclonal bands, visual evoked potentials, and MRI monitoring for new lesions help confirm diagnosis.",
                    "management_principles": "Acute: IV methylprednisolone 1g daily x 3-5 days. Disease-modifying therapy options include interferons, glatiramer acetate, fingolimod, natalizumab.",
                    "references": "Thompson AJ et al. Lancet Neurol. 2018;17:162-173. Updated McDonald criteria for MS diagnosis."
                },
                "source_file": "neuroimmunology_mcqs.json"
            },
            {
                "question_number": "5",
                "question": "A patient presents with ptosis and diplopia that worsen with activity. Which test is most diagnostic?",
                "options": [
                    "EMG",
                    "Edrophonium test",
                    "MRI brain",
                    "Acetylcholine receptor antibodies",
                    "Muscle biopsy"
                ],
                "correct_answer": "D", 
                "correct_answer_text": "Acetylcholine receptor antibodies",
                "subspecialty": "Neuromuscular",
                "exam_year": "2024",
                "exam_type": "Part I",
                "ai_generated": False,
                "explanation": {
                    "option_analysis": "Option A: EMG may show decremental response but is not specific. Option B: Edrophonium test is less commonly used due to cardiac risks. Option C: MRI brain does not diagnose myasthenia gravis. Option D: AChR antibodies are highly specific (>95%) and diagnostic for myasthenia gravis. Option E: Muscle biopsy is not indicated.",
                    "pathophysiology": "Autoimmune destruction of postsynaptic acetylcholine receptors at the neuromuscular junction leads to fatigable weakness, particularly affecting extraocular and bulbar muscles.",
                    "management_principles": "Pyridostigmine for symptomatic relief. Immunosuppression with prednisone, azathioprine, or mycophenolate. Thymectomy if thymoma present.",
                    "references": "Gilhus NE et al. Nat Rev Dis Primers. 2019;5:30. Myasthenia gravis pathophysiology and treatment."
                },
                "source_file": "neuromuscular_mcqs.json"
            }
        ]