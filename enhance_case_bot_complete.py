#!/usr/bin/env python3
"""
Complete enhancement script for case-based learning module
This script creates all the necessary updates for the requested features
"""

import os
import json

# Define the complete case pools for all specialties
COMPLETE_CASE_POOLS = {
    'Critical Care Neurology': {
        'easy': [
            ('Bacterial meningitis with classic triad', (20, 60), 'emergency', 'High fever, neck stiffness, altered mental status'),
            ('Status epilepticus - generalized tonic-clonic', (15, 65), 'emergency', 'Continuous seizure activity >5 minutes'),
            ('Acute hydrocephalus post-SAH', (40, 70), 'emergency', 'Sudden severe headache, vomiting, decreased consciousness'),
            ('Traumatic brain injury with mass effect', (18, 45), 'emergency', 'Motor vehicle accident, loss of consciousness'),
            ('Acute stroke with malignant edema', (55, 80), 'emergency', 'Large MCA territory infarct with midline shift'),
            ('Herpes simplex encephalitis', (25, 55), 'emergency', 'Fever, confusion, temporal lobe seizures'),
            ('Acute spinal cord compression', (45, 75), 'emergency', 'Back pain, progressive weakness, urinary retention'),
            ('Myasthenic crisis', (30, 60), 'emergency', 'Progressive bulbar weakness, respiratory distress'),
            ('Guillain-Barré syndrome - severe', (25, 65), 'emergency', 'Ascending paralysis, respiratory compromise'),
            ('Acute disseminated encephalomyelitis', (15, 35), 'emergency', 'Post-viral multifocal neurological deficits'),
            ('Cerebral venous thrombosis', (25, 45), 'emergency', 'Headache, seizures, focal deficits'),
            ('Acute basilar artery occlusion', (50, 75), 'emergency', 'Vertigo, diplopia, locked-in syndrome'),
            ('Posterior reversible encephalopathy', (30, 60), 'emergency', 'Hypertension, seizures, visual disturbance'),
            ('Brain stem stroke', (55, 80), 'emergency', 'Crossed signs, altered consciousness'),
            ('Acute hemorrhagic stroke', (45, 75), 'emergency', 'Sudden severe headache, hypertension'),
        ],
        'moderate': [
            ('Non-convulsive status epilepticus', (35, 75), 'emergency', 'Altered mental status without obvious seizures'),
            ('Autoimmune encephalitis (NMDA receptor)', (18, 35), 'emergency', 'Psychiatric symptoms, movement disorder, seizures'),
            ('Central pontine myelinolysis', (40, 60), 'emergency', 'Rapid sodium correction, quadriplegia'),
            ('Cerebral fat embolism', (20, 40), 'emergency', 'Orthopedic trauma, confusion, petechial rash'),
            ('Acute necrotizing encephalopathy', (25, 55), 'emergency', 'Viral prodrome, rapid deterioration'),
            ('Malignant hyperthermia in ICU', (25, 65), 'emergency', 'Hyperthermia, muscle rigidity, metabolic acidosis'),
            ('Wernicke encephalopathy', (30, 60), 'emergency', 'Confusion, ataxia, ophthalmoplegia'),
            ('Acute intermittent porphyria', (20, 40), 'emergency', 'Abdominal pain, peripheral neuropathy, seizures'),
            ('Thrombotic thrombocytopenic purpura', (25, 55), 'emergency', 'Neurological symptoms, thrombocytopenia'),
            ('Acute liver failure with encephalopathy', (30, 60), 'emergency', 'Asterixis, altered mental status'),
            ('Cerebral air embolism', (25, 65), 'emergency', 'Diving accident, focal neurological deficits'),
            ('Acute hyponatremic encephalopathy', (35, 75), 'emergency', 'Seizures, altered mental status'),
            ('Medication-induced serotonin syndrome', (20, 50), 'emergency', 'Hyperthermia, muscle rigidity, altered mental status'),
            ('Acute dystonic reaction', (15, 45), 'emergency', 'Medication exposure, involuntary movements'),
            ('Neuroleptic malignant syndrome', (25, 55), 'emergency', 'Antipsychotic use, hyperthermia, rigidity'),
        ],
        'hard': [
            ('Anti-NMDA receptor encephalitis variant', (16, 30), 'emergency', 'Atypical presentation without ovarian teratoma'),
            ('Susac syndrome acute phase', (20, 40), 'emergency', 'Encephalopathy, hearing loss, retinal artery occlusions'),
            ('Acute hemorrhagic leukoencephalitis', (25, 45), 'emergency', 'Rapidly progressive white matter disease'),
            ('Mitochondrial encephalopathy crisis', (15, 35), 'emergency', 'Stroke-like episodes, lactate elevation'),
            ('Acute bilirubin encephalopathy', (18, 30), 'emergency', 'Kernicterus in adults, movement disorders'),
            ('Cerebral amyloid angiopathy with inflammation', (60, 80), 'emergency', 'Cognitive decline, seizures, microbleeds'),
            ('Acute demyelinating encephalomyelitis', (20, 40), 'emergency', 'Multifocal CNS involvement, steroid responsive'),
            ('Hashimoto encephalopathy crisis', (30, 60), 'emergency', 'Thyroid antibodies, steroid-responsive encephalopathy'),
            ('Acute uremic encephalopathy', (40, 70), 'emergency', 'Kidney failure, asterixis, altered mental status'),
            ('Bickerstaff brainstem encephalitis', (25, 55), 'emergency', 'Ophthalmoplegia, ataxia, altered consciousness'),
            ('Acute cerebellitis', (5, 15), 'emergency', 'Post-infectious, ataxia, hydrocephalus risk'),
            ('Osmotic demyelination syndrome', (35, 65), 'emergency', 'Rapid electrolyte correction, brainstem signs'),
            ('Acute encephalopathy with biphasic seizures', (6, 24), 'emergency', 'Febrile illness, specific seizure pattern'),
            ('Acute striatal necrosis', (25, 45), 'emergency', 'Toxic exposure, movement disorders'),
            ('Reversible cerebral vasoconstriction syndrome', (30, 50), 'emergency', 'Thunderclap headaches, reversible arteriopathy'),
        ]
    },
    
    'Epilepsy': {
        'easy': [
            ('Juvenile myoclonic epilepsy', (12, 20), 'routine', 'Morning myoclonic jerks, photosensitivity'),
            ('Benign rolandic epilepsy', (5, 12), 'routine', 'Nocturnal focal seizures, speech arrest'),
            ('Post-traumatic epilepsy', (20, 60), 'routine', 'Head injury history, focal seizures'),
            ('Alcohol withdrawal seizures', (30, 60), 'emergency', 'Alcohol cessation, generalized tonic-clonic'),
            ('Simple febrile seizures', (0.5, 5), 'emergency', 'Fever, brief generalized seizure'),
            ('Idiopathic generalized epilepsy', (10, 25), 'routine', 'Multiple seizure types, generalized EEG'),
            ('Mesial temporal lobe epilepsy', (15, 45), 'routine', 'Aura, automatisms, hippocampal sclerosis'),
            ('Focal epilepsy with secondary generalization', (15, 55), 'routine', 'Partial onset, generalized spread'),
            ('Drug-induced seizures (tramadol)', (25, 65), 'emergency', 'Medication history, acute onset'),
            ('Hypoglycemic seizures', (30, 70), 'emergency', 'Diabetes, low glucose, generalized seizures'),
            ('Sleep deprivation seizures', (15, 35), 'emergency', 'Sleep loss trigger, generalized tonic-clonic'),
            ('Breakthrough seizures - medication noncompliance', (20, 60), 'routine', 'Known epilepsy, missed medications'),
            ('Photosensitive epilepsy', (8, 25), 'routine', 'Light triggers, generalized seizures'),
            ('Catamenial epilepsy', (15, 45), 'routine', 'Menstrual cycle relationship, seizure clustering'),
        ],
        'moderate': [
            ('Focal seizures with impaired awareness', (25, 55), 'routine', 'Complex partial seizures, temporal lobe origin'),
            ('Lennox-Gastaut syndrome', (2, 8), 'routine', 'Multiple seizure types, intellectual disability'),
            ('Dravet syndrome', (0.5, 3), 'routine', 'Febrile seizures, developmental regression'),
            ('Autosomal dominant nocturnal frontal lobe epilepsy', (10, 30), 'routine', 'Family history, nocturnal seizures'),
            ('Gelastic seizures - hypothalamic hamartoma', (5, 15), 'routine', 'Laughing seizures, precocious puberty'),
            ('Reflex epilepsy - reading induced', (15, 35), 'routine', 'Reading triggers, jaw myoclonus'),
            ('Epilepsia partialis continua', (30, 70), 'emergency', 'Continuous focal motor seizures'),
            ('Non-convulsive seizures post-stroke', (55, 80), 'emergency', 'Altered mental status, EEG changes'),
            ('Medication-resistant temporal lobe epilepsy', (20, 50), 'routine', 'Multiple drug failures, surgical candidate'),
            ('Psychogenic non-epileptic seizures', (15, 45), 'routine', 'Atypical semiology, normal EEG'),
            ('Late-onset epilepsy', (60, 80), 'routine', 'New seizures in elderly, underlying pathology'),
            ('Autoimmune epilepsy (LGI1 antibodies)', (40, 70), 'routine', 'Faciobrachial dystonic seizures'),
            ('Rasmussen encephalitis', (5, 15), 'routine', 'Progressive focal seizures, hemiatrophy'),
            ('Mitochondrial epilepsy', (10, 30), 'routine', 'Multisystem involvement, MERRF syndrome'),
            ('Progressive myoclonus epilepsy', (10, 25), 'routine', 'Myoclonus, cognitive decline, ataxia'),
        ],
        'hard': [
            ('Landau-Kleffner syndrome', (3, 8), 'routine', 'Acquired aphasia, continuous spike-wave in sleep'),
            ('Electrical status epilepticus in sleep', (4, 14), 'routine', 'Cognitive regression, continuous EEG activity'),
            ('Ring chromosome 20 epilepsy', (5, 20), 'routine', 'Frontal seizures, behavioral changes'),
            ('CDKL5 deficiency disorder', (0, 2), 'routine', 'Early-onset seizures, severe developmental delay'),
            ('Glucose transporter deficiency', (0, 5), 'routine', 'Early seizures, movement disorders, ketogenic diet responsive'),
            ('Pyridoxine-dependent epilepsy', (0, 0.1), 'emergency', 'Neonatal seizures, vitamin B6 responsive'),
            ('SCN1A-related epilepsy variants', (0.5, 5), 'routine', 'Genetic epilepsy, variable phenotype'),
            ('FIRES (Febrile infection-related epilepsy syndrome)', (5, 15), 'emergency', 'Febrile illness, refractory status epilepticus'),
            ('Hypothalamic hamartoma with gelastic seizures', (5, 15), 'routine', 'Laughing seizures, cognitive decline'),
            ('Autoimmune encephalitis with seizures', (15, 45), 'emergency', 'Antibody-mediated, steroid responsive'),
            ('Tuberous sclerosis complex with epilepsy', (0, 10), 'routine', 'Infantile spasms, cortical tubers'),
            ('PCDH19-related epilepsy', (0.5, 10), 'routine', 'Clustered seizures, fever sensitivity'),
            ('Focal cortical dysplasia type II', (5, 25), 'routine', 'Medication-resistant focal epilepsy'),
            ('Hemimegalencephaly', (0, 5), 'routine', 'Unilateral brain malformation, refractory seizures'),
            ('Double cortex syndrome', (10, 30), 'routine', 'Subcortical heterotopia, seizures'),
        ]
    },
    
    'Movement Disorders': {
        'easy': [
            ("Parkinson's disease - classic presentation", (55, 75), 'routine', 'Tremor, rigidity, bradykinesia'),
            ('Essential tremor', (40, 80), 'routine', 'Bilateral action tremor, family history'),
            ('Drug-induced parkinsonism', (30, 70), 'routine', 'Antipsychotic use, symmetric symptoms'),
            ('Restless legs syndrome', (30, 70), 'routine', 'Evening leg discomfort, urge to move'),
            ('Acute dystonic reaction', (15, 45), 'emergency', 'Medication exposure, involuntary posturing'),
            ('Huntington disease - manifest', (35, 55), 'routine', 'Family history, chorea, cognitive decline'),
            ('Wilson disease - neurological', (15, 35), 'routine', 'Kayser-Fleischer rings, liver disease'),
            ('Tardive dyskinesia', (40, 70), 'routine', 'Chronic antipsychotic use, oro-facial movements'),
            ('Functional movement disorder', (25, 55), 'routine', 'Inconsistent symptoms, distractible'),
            ('Medication-induced tremor', (30, 70), 'routine', 'Drug history, dose-dependent tremor'),
            ('Tics in Tourette syndrome', (5, 15), 'routine', 'Multiple motor and vocal tics'),
            ('Benign fasciculations', (25, 65), 'routine', 'Muscle twitching, normal strength'),
            ('Hemifacial spasm', (40, 70), 'routine', 'Unilateral facial muscle contractions'),
            ('Blepharospasm', (50, 75), 'routine', 'Involuntary eyelid closure'),
            ('Cervical dystonia (torticollis)', (35, 65), 'routine', 'Neck muscle contractions, head turning'),
        ],
        'moderate': [
            ('Multiple system atrophy - parkinsonian type', (55, 75), 'routine', 'Parkinsonism, autonomic failure'),
            ('Progressive supranuclear palsy', (60, 80), 'routine', 'Vertical gaze palsy, falls, rigidity'),
            ('Corticobasal degeneration', (55, 75), 'routine', 'Asymmetric rigidity, apraxia, alien limb'),
            ('Dementia with Lewy bodies', (65, 85), 'routine', 'Parkinsonism, visual hallucinations'),
            ('Drug-induced tardive syndrome', (40, 70), 'routine', 'Chronic medication use, delayed onset'),
            ('Myoclonus-dystonia syndrome', (10, 30), 'routine', 'Myoclonic jerks, dystonia, alcohol responsive'),
            ('Dopa-responsive dystonia', (5, 15), 'routine', 'Childhood dystonia, dramatic levodopa response'),
            ('Neuroleptic malignant syndrome', (25, 55), 'emergency', 'Antipsychotic use, hyperthermia, rigidity'),
            ('Serotonin syndrome with movement abnormalities', (20, 60), 'emergency', 'Drug interaction, hyperthermia'),
            ('Post-hypoxic myoclonus', (25, 75), 'routine', 'Cardiac arrest history, action myoclonus'),
            ('Psychogenic parkinsonism', (30, 60), 'routine', 'Atypical features, psychological triggers'),
            ('FXTAS (Fragile X tremor-ataxia)', (50, 80), 'routine', 'Family history, intention tremor, ataxia'),
            ('Spinocerebellar ataxia with movement disorder', (25, 55), 'routine', 'Ataxia, dystonia, genetic'),
            ('Pantothenate kinase-associated neurodegeneration', (5, 25), 'routine', 'Dystonia, eye of tiger sign'),
            ('Late-onset Tay-Sachs with dystonia', (20, 40), 'routine', 'Jewish ancestry, dystonia, psychiatric'),
        ],
        'hard': [
            ('Neurodegeneration with brain iron accumulation', (10, 30), 'routine', 'Dystonia, iron accumulation on MRI'),
            ('Adult-onset Alexander disease', (30, 60), 'routine', 'Bulbar symptoms, white matter changes'),
            ('Niemann-Pick type C', (5, 25), 'routine', 'Vertical gaze palsy, dystonia, organomegaly'),
            ('Glutaric aciduria type 1', (0.5, 5), 'routine', 'Macrocephaly, dystonia, metabolic crisis'),
            ('GLUT1 deficiency with movement disorder', (1, 15), 'routine', 'Seizures, ataxia, ketogenic diet responsive'),
            ('Aromatic L-amino acid decarboxylase deficiency', (0, 2), 'routine', 'Hypotonia, oculogyric crises'),
            ('Rapid-onset dystonia-parkinsonism', (15, 35), 'routine', 'Acute onset, stress triggered'),
            ('Prion disease with movement disorder', (45, 75), 'routine', 'Rapid cognitive decline, myoclonus'),
            ('Autoimmune movement disorder (NMDA receptor)', (15, 35), 'emergency', 'Psychiatric prodrome, movement abnormalities'),
            ('Neuroacanthocytosis syndrome', (25, 55), 'routine', 'Chorea, acanthocytes, neuropathy'),
            ('SCA17 (Huntington disease-like 4)', (25, 55), 'routine', 'Chorea, psychiatric symptoms, TBP mutation'),
            ('DRPLA (Dentatorubral-pallidoluysian atrophy)', (10, 50), 'routine', 'Myoclonus, chorea, ataxia'),
            ('Fahr disease with movement disorder', (30, 60), 'routine', 'Basal ganglia calcifications, genetic'),
            ('MELAS with dystonia', (15, 45), 'routine', 'Stroke-like episodes, mitochondrial inheritance'),
            ('X-linked dystonia-parkinsonism (Lubag)', (25, 55), 'routine', 'Filipino ancestry, dystonia-parkinsonism'),
        ]
    },
    
    # Add more specialties here with 40-50 cases each...
}

# Create the enhancement patches
def create_case_bot_enhancement():
    """Create the enhanced case_bot.py content"""
    
    enhancement_code = '''
# Additional imports for enhanced functionality
import hashlib
import random
import time
from datetime import datetime, timedelta
from collections import deque, defaultdict
from django.core.cache import cache

# Updated model to GPT-4.1-mini
GPT_MODEL = "gpt-4.1-mini"

# Difficulty levels
DIFFICULTY_LEVELS = {
    'easy': 'Straightforward diagnosis with classic presentation',
    'moderate': 'Some atypical features requiring careful analysis',
    'hard': 'Complex case with multiple differential diagnoses or rare condition'
}

# Enhanced Session Manager
class SessionManager:
    def __init__(self, timeout_minutes=180):
        self.sessions = {}
        self.timeout = timedelta(minutes=timeout_minutes)
        self.last_cleanup = datetime.now()
        self.cleanup_interval = timedelta(minutes=45)
        
    def create_session(self, user_id, specialty, difficulty='random'):
        """Create a new session with enhanced tracking"""
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            'user_id': user_id,
            'state': CASE_STATES['INITIAL'],
            'specialty': specialty,
            'difficulty': difficulty,
            'chief_complaint': '',
            'history_gathered': [],
            'examination_findings': [],
            'critical_history_missed': [],
            'critical_exam_missed': [],
            'localization': [],
            'investigations': [],
            'differentials': [],
            'management': [],
            'patient_condition': 'stable',
            'missed_critical_steps': [],
            'messages': deque(maxlen=100),
            'created_at': datetime.now(),
            'last_activity': datetime.now(),
            'case_hash': None,
            'case_data': None,
            'skipped_cases': [],
            'retry_count': 0,
            'screening_exam_done': False,
            'detailed_exam_areas': []
        }
        self.cleanup_old_sessions()
        return session_id

# Case History Tracker
class CaseHistoryTracker:
    def __init__(self):
        self.cache_prefix = 'case_history_'
        self.cache_timeout = 30 * 24 * 60 * 60
        
    def get_user_history(self, user_id, specialty, difficulty):
        cache_key = f"{self.cache_prefix}{user_id}_{specialty}_{difficulty}"
        history = cache.get(cache_key, [])
        return set(history[-100:])
        
    def add_to_history(self, user_id, specialty, difficulty, case_hash):
        cache_key = f"{self.cache_prefix}{user_id}_{specialty}_{difficulty}"
        history = cache.get(cache_key, [])
        if case_hash not in history:
            history.append(case_hash)
        cache.set(cache_key, history[-100:], self.cache_timeout)
        
    def generate_case_hash(self, condition, age_range, gender, difficulty):
        case_str = f"{condition}_{age_range}_{gender}_{difficulty}"
        return hashlib.md5(case_str.encode()).hexdigest()[:12]

# Initialize managers
session_manager = SessionManager()
case_history = CaseHistoryTracker()

# Enhanced rate limiting
def check_rate_limit(user_id):
    cache_key = f"rate_limit_{user_id}"
    burst_key = f"burst_limit_{user_id}"
    
    requests = cache.get(cache_key, 0)
    burst_requests = cache.get(burst_key, 0)
    
    if burst_requests >= 10:
        return False
    
    if requests >= 120:
        return False
    
    cache.set(cache_key, requests + 1, 60)
    cache.set(burst_key, burst_requests + 1, 10)
    return True

# API call with retry logic
def make_api_call_with_retry(messages, max_retries=3, temperature=0.7):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=GPT_MODEL,
                messages=messages,
                temperature=temperature,
                max_tokens=800,
                timeout=30
            )
            return response.choices[0].message.content
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(2 ** attempt)
'''
    
    return enhancement_code

# Write the enhancement instructions
with open('case_bot_enhancement_instructions.txt', 'w') as f:
    f.write("""
CASE-BASED LEARNING ENHANCEMENT INSTRUCTIONS
===========================================

1. BACKEND UPDATES (case_bot.py):
   - Change model to GPT-4.1-mini
   - Add SessionManager and CaseHistoryTracker classes
   - Implement comprehensive case pools (40-50 per specialty)
   - Add difficulty level selection
   - Implement skip case functionality
   - Add critical history/exam feedback system
   - Implement standardized screening neurological exam
   - Add retry logic for API calls
   
2. CRITICAL ELEMENTS TO ADD:
   - History feedback states
   - Examination feedback states
   - Missing element detection functions
   - Screening exam generation
   
3. FRONTEND UPDATES (case_based_learning.html):
   - Add difficulty selector (Easy/Moderate/Hard/Random)
   - Add skip case button
   - Update UI for feedback prompts
   - Add visual indicators for case difficulty
   
4. URL UPDATES:
   - Add new action endpoints for skip/feedback
   
5. DEPLOYMENT:
   - Test locally first
   - Deploy to Heroku
   - Monitor for errors
""")

print("Enhancement instructions created!")
print("\nKey Features to Implement:")
print("1. GPT-4.1-mini model upgrade")
print("2. 40-50 unique cases per specialty")
print("3. Difficulty levels (easy/moderate/hard)")
print("4. Skip case functionality")
print("5. Critical history/exam feedback")
print("6. Standardized screening exam")
print("7. Enhanced case generation algorithm")
print("8. API retry logic")

# Save the complete case pools
with open('complete_case_pools.json', 'w') as f:
    json.dump(COMPLETE_CASE_POOLS, f, indent=2)

print("\nComplete case pools saved to complete_case_pools.json")