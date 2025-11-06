#!/usr/bin/env python3
"""
Script to test the enhanced case-based learning locally
"""

import os
import sys
import json

def test_case_pools():
    """Test that case pools are properly populated"""
    print("Testing case pools...")
    
    # Import the case pools
    sys.path.insert(0, 'django_neurology_mcq/mcq')
    try:
        from case_bot_enhanced import get_comprehensive_case_pools
        
        pools = get_comprehensive_case_pools()
        
        print(f"\nSpecialties found: {len(pools)}")
        
        for specialty, cases in pools.items():
            total_cases = 0
            print(f"\n{specialty}:")
            for difficulty, case_list in cases.items():
                print(f"  {difficulty}: {len(case_list)} cases")
                total_cases += len(case_list)
            print(f"  Total: {total_cases} cases")
            
            if total_cases < 40:
                print(f"  ⚠️  Warning: {specialty} has less than 40 cases!")
    
    except ImportError as e:
        print(f"Error importing case_bot_enhanced: {e}")
        return False
    
    return True

def test_critical_elements():
    """Test that critical elements are defined"""
    print("\n\nTesting critical elements...")
    
    try:
        from case_bot_enhanced import CRITICAL_ELEMENTS
        
        print(f"History elements for {len(CRITICAL_ELEMENTS['history'])} specialties")
        print(f"Examination elements for {len(CRITICAL_ELEMENTS['examination'])} specialties")
        
        # Check a sample
        if 'Epilepsy' in CRITICAL_ELEMENTS['history']:
            print(f"\nSample - Epilepsy history elements:")
            for elem in CRITICAL_ELEMENTS['history']['Epilepsy'][:3]:
                print(f"  - {elem}")
    
    except ImportError as e:
        print(f"Error: {e}")
        return False
    
    return True

def check_dependencies():
    """Check if all required dependencies are available"""
    print("\n\nChecking dependencies...")
    
    dependencies = [
        ('OpenAI', 'openai'),
        ('Django', 'django'),
        ('Hashlib', 'hashlib'),
        ('JSON', 'json'),
        ('UUID', 'uuid'),
        ('Datetime', 'datetime'),
        ('Collections', 'collections'),
    ]
    
    all_good = True
    for name, module in dependencies:
        try:
            __import__(module)
            print(f"✓ {name} is available")
        except ImportError:
            print(f"✗ {name} is NOT available")
            all_good = False
    
    return all_good

def main():
    print("Enhanced Case-Based Learning Test Script")
    print("=" * 50)
    
    # Check if files exist
    files_to_check = [
        'django_neurology_mcq/mcq/case_bot_enhanced.py',
        'django_neurology_mcq/templates/mcq/case_based_learning_enhanced.html',
        'django_neurology_mcq/mcq/urls_enhanced.py'
    ]
    
    print("\nChecking files...")
    all_files_exist = True
    for file in files_to_check:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} NOT FOUND")
            all_files_exist = False
    
    if not all_files_exist:
        print("\n⚠️  Some files are missing!")
        return
    
    # Run tests
    if test_case_pools() and test_critical_elements() and check_dependencies():
        print("\n✅ All tests passed!")
        print("\nNext steps:")
        print("1. Update django_neurology_mcq/mcq/urls.py to use urls_enhanced.py")
        print("2. Run: python manage.py runserver")
        print("3. Visit: http://localhost:8000/case-based-learning-enhanced/")
        print("\nOr deploy directly to Heroku using deploy_enhanced_case_learning.sh")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()