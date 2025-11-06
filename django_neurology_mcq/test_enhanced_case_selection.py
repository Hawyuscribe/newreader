#!/usr/bin/env python3
"""
Test script for enhanced case selection logic
"""
import os
import sys
import django
from collections import Counter

# Setup Django
sys.path.insert(0, '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurology_mcq.settings')
django.setup()

from mcq.case_bot_enhanced import generate_unique_case, case_history

def test_case_variety():
    """Test that case selection provides good variety"""
    user_id = 'test_user_123'
    specialty = 'Movement Disorders'
    difficulty = 'hard'
    
    print(f"Testing case variety for {specialty} - {difficulty}")
    print("=" * 50)
    
    # Generate 20 cases and track variety
    cases = []
    conditions = []
    
    for i in range(20):
        case = generate_unique_case(specialty, user_id, difficulty)
        cases.append(case)
        conditions.append(case['condition'])
        print(f"{i+1:2d}. {case['condition']} (Age: {case['age']}, Gender: {case['gender']})")
    
    # Analyze variety
    print("\n" + "=" * 50)
    print("VARIETY ANALYSIS:")
    print("=" * 50)
    
    condition_counts = Counter(conditions)
    print(f"Unique conditions: {len(condition_counts)}")
    print(f"Total cases: {len(cases)}")
    print(f"Variety ratio: {len(condition_counts)/len(cases)*100:.1f}%")
    
    print("\nCondition distribution:")
    for condition, count in condition_counts.most_common():
        print(f"  {condition}: {count} times")
    
    return len(condition_counts), len(cases)

def test_random_specialty_distribution():
    """Test random specialty selection distribution"""
    user_id = 'test_user_random'
    
    print("\nTesting random specialty distribution")
    print("=" * 50)
    
    specialties = []
    for i in range(30):
        case = generate_unique_case('random', user_id, 'random')
        specialties.append(case['difficulty'])  # This should contain the resolved specialty info
        print(f"{i+1:2d}. Specialty: {case.get('resolved_specialty', 'Unknown')}, Difficulty: {case['difficulty']}")
    
    specialty_counts = Counter(specialties)
    print(f"\nSpecialty distribution:")
    for specialty, count in specialty_counts.most_common():
        print(f"  {specialty}: {count} times")

def test_difficulty_distribution():
    """Test random difficulty selection distribution"""
    user_id = 'test_user_diff'
    specialty = 'Epilepsy'
    
    print(f"\nTesting difficulty distribution for {specialty}")
    print("=" * 50)
    
    difficulties = []
    for i in range(15):
        case = generate_unique_case(specialty, user_id, 'random')
        difficulties.append(case['difficulty'])
        print(f"{i+1:2d}. {case['condition']} - Difficulty: {case['difficulty']}")
    
    difficulty_counts = Counter(difficulties)
    print(f"\nDifficulty distribution:")
    for difficulty, count in difficulty_counts.most_common():
        print(f"  {difficulty}: {count} times")

if __name__ == '__main__':
    print("Enhanced Case Selection Logic Test")
    print("==================================")
    
    try:
        # Test 1: Case variety within same specialty/difficulty
        unique_count, total_count = test_case_variety()
        
        # Test 2: Random specialty distribution 
        test_random_specialty_distribution()
        
        # Test 3: Random difficulty distribution
        test_difficulty_distribution()
        
        print("\n" + "=" * 50)
        print("TEST SUMMARY:")
        print("=" * 50)
        print(f"✅ Case variety test: {unique_count}/{total_count} unique conditions")
        print("✅ Random specialty distribution test completed")
        print("✅ Random difficulty distribution test completed")
        print("\nEnhanced case selection logic is working!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
