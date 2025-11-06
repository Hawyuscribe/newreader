#!/usr/bin/env python3
"""
Script to fix case pool issues and enhance case tracking logic
"""

# Issues to fix:
print("""
CASE POOL ISSUES IDENTIFIED:
1. Age Range Problems:
   - Acute bilirubin encephalopathy (18-30y) should be neonatal (0-1y) 
   - Acute encephalopathy with biphasic seizures (6-24y) should be (6-24 months = 0.5-2y)

2. Missing Specialties (11 total):
   - Neurogenetics
   - Neuroimmunology  
   - Neuro-infectious
   - Neuro-oncology
   - Neuro-otology
   - Neuroophthalmology
   - Neuropsychiatry
   - Neurotoxicology
   - Pediatric Neurology
   - Sleep Neurology
   - Plus any others mentioned in template but not in code

3. Case Tracking Logic Issues:
   - Currently tracks only last 100 cases, which may cause premature recycling
   - Hash generation uses 'any' for gender instead of actual gender, reducing uniqueness
   - No clear indication to user when all cases have been seen
""")

# Fix 1: Update problematic age ranges
age_range_fixes = {
    "Critical Care Neurology": {
        "hard": [
            # Find and replace these specific cases
            ("Acute bilirubin encephalopathy", "old_range": "(18, 30)", "new_range": "(0, 1)", 
             "new_description": "Neonatal kernicterus with movement disorders"),
            ("Acute encephalopathy with biphasic seizures", "old_range": "(6, 24)", 
             "new_range": "(0.5, 2)", "new_description": "Febrile illness in infant, specific seizure pattern"),
        ]
    }
}

# Fix 2: Add missing specialties with appropriate cases
missing_specialties = {
    'Neurogenetics': {
        'easy': [
            ('Duchenne muscular dystrophy', (3, 10), 'routine', 'Progressive proximal weakness, Gowers sign'),
            ('Neurofibromatosis type 1', (5, 25), 'routine', 'Café-au-lait spots, neurofibromas'),
            ('Tuberous sclerosis complex', (0, 10), 'routine', 'Seizures, ash leaf spots, developmental delay'),
            ('Huntington disease - juvenile', (5, 20), 'routine', 'Family history, chorea, cognitive decline'),
            ('Fragile X syndrome', (2, 15), 'routine', 'Intellectual disability, behavioral issues, dysmorphic features'),
        ],
        'moderate': [
            ('Mitochondrial myopathy', (10, 40), 'routine', 'Exercise intolerance, ptosis, multisystem involvement'),
            ('Spinocerebellar ataxia', (20, 50), 'routine', 'Progressive ataxia, family history'),
            ('Hereditary spastic paraplegia', (10, 40), 'routine', 'Progressive lower limb spasticity'),
            ('Leukodystrophy - adult onset', (20, 50), 'routine', 'White matter changes, cognitive decline'),
            ('Charcot-Marie-Tooth disease', (10, 30), 'routine', 'Distal weakness, pes cavus, family history'),
        ],
        'hard': [
            ('Ataxia telangiectasia', (2, 10), 'routine', 'Ataxia, telangiectasias, immunodeficiency'),
            ('Alexander disease - adult', (20, 50), 'routine', 'Bulbar symptoms, white matter abnormalities'),
            ('Neuronal ceroid lipofuscinosis', (5, 15), 'routine', 'Vision loss, seizures, cognitive decline'),
            ('Niemann-Pick type C', (5, 25), 'routine', 'Vertical gaze palsy, ataxia, cognitive decline'),
            ('Wilson disease - neurological', (10, 30), 'routine', 'Movement disorder, Kayser-Fleischer rings'),
        ]
    },
    'Neuroimmunology': {
        'easy': [
            ('Multiple sclerosis - relapsing-remitting', (20, 40), 'routine', 'Optic neuritis, sensory symptoms'),
            ('Neuromyelitis optica spectrum disorder', (25, 50), 'routine', 'Severe optic neuritis, transverse myelitis'),
            ('Acute disseminated encephalomyelitis', (5, 15), 'emergency', 'Post-viral, multifocal deficits'),
            ('Myasthenia gravis - ocular', (20, 60), 'routine', 'Ptosis, diplopia, fatigability'),
            ('Guillain-Barré syndrome - mild', (20, 60), 'emergency', 'Ascending weakness, areflexia'),
        ],
        'moderate': [
            ('Anti-MOG associated disorder', (5, 45), 'emergency', 'Optic neuritis, ADEM-like presentation'),
            ('Autoimmune encephalitis - LGI1', (50, 70), 'emergency', 'Faciobrachial dystonic seizures'),
            ('Stiff person syndrome', (30, 60), 'routine', 'Axial rigidity, spasms, GAD antibodies'),
            ('CIDP (Chronic inflammatory demyelinating polyneuropathy)', (40, 70), 'routine', 'Progressive weakness, sensory loss'),
            ('Paraneoplastic cerebellar degeneration', (50, 70), 'routine', 'Subacute ataxia, cancer association'),
        ],
        'hard': [
            ('Bickerstaff brainstem encephalitis', (20, 60), 'emergency', 'Ophthalmoplegia, ataxia, consciousness'),
            ('Anti-NMDA receptor encephalitis', (15, 35), 'emergency', 'Psychiatric symptoms, seizures, dyskinesias'),
            ('Progressive encephalomyelitis with rigidity', (40, 70), 'routine', 'Rigidity, myoclonus, brainstem signs'),
            ('Hashimoto encephalopathy', (30, 60), 'emergency', 'Encephalopathy, thyroid antibodies'),
            ('Voltage-gated potassium channel encephalitis', (50, 70), 'emergency', 'Memory loss, seizures, hyponatremia'),
        ]
    },
    # Add more specialties...
}

# Fix 3: Enhanced case tracking logic
enhanced_tracking_logic = """
class EnhancedCaseHistoryTracker:
    def __init__(self):
        self.cache_prefix = 'case_history_v2_'
        self.cache_timeout = 90 * 24 * 60 * 60  # 90 days instead of 30
        
    def get_user_history(self, user_id, specialty, difficulty):
        '''Get complete history without arbitrary limit'''
        cache_key = f"{self.cache_prefix}{user_id}_{specialty}_{difficulty}"
        history = cache.get(cache_key, {})
        return history  # Return dict instead of set for more info
        
    def add_to_history(self, user_id, specialty, difficulty, case_hash):
        '''Add case with timestamp to user's history'''
        cache_key = f"{self.cache_prefix}{user_id}_{specialty}_{difficulty}"
        history = cache.get(cache_key, {})
        history[case_hash] = {
            'timestamp': datetime.now().isoformat(),
            'seen_count': history.get(case_hash, {}).get('seen_count', 0) + 1
        }
        cache.set(cache_key, history, self.cache_timeout)
        
    def generate_case_hash(self, condition, age_range, gender, difficulty):
        '''Generate unique hash including actual gender'''
        case_str = f"{condition}_{age_range}_{gender}_{difficulty}"
        return hashlib.md5(case_str.encode()).hexdigest()[:16]  # Longer hash
        
    def get_completion_stats(self, user_id, specialty, difficulty):
        '''Get statistics on case completion'''
        history = self.get_user_history(user_id, specialty, difficulty)
        case_pools = get_comprehensive_case_pools()
        
        total_cases = len(case_pools.get(specialty, {}).get(difficulty, []))
        seen_cases = len(history)
        
        return {
            'total_cases': total_cases,
            'seen_cases': seen_cases,
            'completion_percentage': (seen_cases / total_cases * 100) if total_cases > 0 else 0,
            'all_seen': seen_cases >= total_cases
        }
"""

# Fix 4: Improved case selection logic
improved_selection_logic = """
def generate_unique_case(specialty, user_id, difficulty='random', skip_list=None):
    '''Generate a unique case with better tracking and user feedback'''
    case_pools = get_comprehensive_case_pools()
    
    # ... existing specialty/difficulty resolution ...
    
    # Get user's complete case history
    history = case_history.get_user_history(user_id, specialty, difficulty)
    skip_set = set(skip_list or [])
    
    # Get completion stats
    stats = case_history.get_completion_stats(user_id, specialty, difficulty)
    
    # Find unseen cases with actual gender consideration
    unseen_cases = []
    seen_once_cases = []  # Cases seen only once
    
    for condition, age_range, urgency, description in available_cases:
        # Generate hashes for both genders
        male_hash = case_history.generate_case_hash(condition, age_range, 'male', difficulty)
        female_hash = case_history.generate_case_hash(condition, age_range, 'female', difficulty)
        
        # Check if either gender variant is unseen
        if male_hash not in history and male_hash not in skip_set:
            unseen_cases.append((condition, age_range, urgency, description, male_hash, 'male'))
        if female_hash not in history and female_hash not in skip_set:
            unseen_cases.append((condition, age_range, urgency, description, female_hash, 'female'))
            
        # Track cases seen only once for better recycling
        for hash_val, gender in [(male_hash, 'male'), (female_hash, 'female')]:
            if hash_val in history and history[hash_val].get('seen_count', 0) == 1:
                seen_once_cases.append((condition, age_range, urgency, description, hash_val, gender))
    
    # Selection priority:
    # 1. Completely unseen cases
    # 2. Cases seen only once (if no unseen)
    # 3. Least recently seen cases (if all seen multiple times)
    
    if unseen_cases:
        selected = random.choice(unseen_cases)
        is_repeat = False
    elif seen_once_cases:
        selected = random.choice(seen_once_cases)
        is_repeat = True
    else:
        # Sort by timestamp and select from oldest 25%
        sorted_cases = sorted(
            [(c, history.get(case_history.generate_case_hash(c[0], c[1], g, difficulty), {}).get('timestamp', ''))
             for c in available_cases for g in ['male', 'female']],
            key=lambda x: x[1]
        )
        oldest_cases = sorted_cases[:max(1, len(sorted_cases) // 4)]
        case_data, _ = random.choice(oldest_cases)
        gender = random.choice(['male', 'female'])
        case_hash = case_history.generate_case_hash(case_data[0], case_data[1], gender, difficulty)
        selected = case_data + (case_hash, gender)
        is_repeat = True
    
    condition, age_range, urgency, description, case_hash, gender = selected[:6]
    
    # Generate age within range
    age = random.randint(age_range[0], age_range[1])
    
    # Add to history
    case_history.add_to_history(user_id, specialty, difficulty, case_hash)
    
    return {
        'condition': condition,
        'age': age,
        'gender': gender,
        'urgency': urgency,
        'description': description,
        'case_hash': case_hash,
        'difficulty': difficulty,
        'is_repeat': is_repeat,
        'completion_stats': stats,
        'critical_history': CRITICAL_ELEMENTS['history'].get(specialty, []),
        'critical_exam': CRITICAL_ELEMENTS['examination'].get(specialty, [])
    }
"""

print("\nPROPOSED FIXES:")
print("1. Correct age ranges for 2 cases in Critical Care Neurology")
print("2. Add missing 11 specialties with 15 cases each (5 per difficulty)")
print("3. Enhance case tracking to avoid premature recycling")
print("4. Improve case selection logic with better gender handling")
print("5. Add completion statistics to inform users of their progress")
print("\nThese changes will ensure:")
print("- Age-appropriate case presentations")
print("- Complete specialty coverage as shown in UI")
print("- True non-repetition until pool exhaustion")
print("- Better user experience with progress tracking")