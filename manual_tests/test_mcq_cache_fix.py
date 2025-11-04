"""
Test script for MCQ case converter caching fix
"""

import os
import sys
import django

# Set up Django environment
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from mcq.mcq_case_converter import convert_mcq_to_case, clear_mcq_cache, get_mcq_cache_key
from django.core.cache import cache

def test_mcq_caching():
    """Test the MCQ caching functionality"""
    
    # Get a sample MCQ
    mcq = MCQ.objects.first()
    if not mcq:
        print("❌ No MCQs found in database")
        return
    
    print(f"🧪 Testing MCQ caching with MCQ #{mcq.id}")
    print(f"📝 MCQ question: {mcq.question_text[:100]}...")
    
    # Clear any existing cache
    clear_mcq_cache(mcq.id)
    
    # Test first conversion (should generate new)
    print("\n1️⃣ First conversion (should generate new case):")
    start_time = time.time()
    case_data_1 = convert_mcq_to_case(mcq)
    time_1 = time.time() - start_time
    print(f"⏱️ Time taken: {time_1:.2f} seconds")
    print(f"🆔 Case hash: {case_data_1.get('case_hash', 'N/A')}")
    print(f"📊 Cache used: {case_data_1.get('cache_used', False)}")
    
    # Test second conversion (should use cache)
    print("\n2️⃣ Second conversion (should use cache):")
    start_time = time.time()
    case_data_2 = convert_mcq_to_case(mcq)
    time_2 = time.time() - start_time
    print(f"⏱️ Time taken: {time_2:.2f} seconds")
    print(f"🆔 Case hash: {case_data_2.get('case_hash', 'N/A')}")
    print(f"📊 Cache used: {case_data_2.get('cache_used', False)}")
    
    # Compare results
    print("\n📋 Comparison:")
    print(f"Speed improvement: {((time_1 - time_2) / time_1 * 100):.1f}%")
    print(f"Cache working: {'✅' if case_data_2.get('cache_used') else '❌'}")
    
    # Test cache key
    cache_key = get_mcq_cache_key(mcq.id)
    cached_data = cache.get(cache_key)
    print(f"Direct cache check: {'✅ Found' if cached_data else '❌ Not found'}")
    
    # Clear cache and test again
    print("\n3️⃣ After clearing cache (should generate new case):")
    clear_mcq_cache(mcq.id)
    start_time = time.time()
    case_data_3 = convert_mcq_to_case(mcq)
    time_3 = time.time() - start_time
    print(f"⏱️ Time taken: {time_3:.2f} seconds")
    print(f"📊 Cache used: {case_data_3.get('cache_used', False)}")
    
    return {
        'mcq_id': mcq.id,
        'times': [time_1, time_2, time_3],
        'cache_working': case_data_2.get('cache_used', False)
    }

def test_multiple_mcqs():
    """Test caching with multiple MCQs"""
    print("\n🔄 Testing multiple MCQs:")
    
    mcqs = MCQ.objects.all()[:3]  # Test with first 3 MCQs
    
    for i, mcq in enumerate(mcqs, 1):
        print(f"\n📌 MCQ #{i} (ID: {mcq.id}):")
        
        # Clear cache first
        clear_mcq_cache(mcq.id)
        
        # Generate twice
        case_1 = convert_mcq_to_case(mcq)
        case_2 = convert_mcq_to_case(mcq)
        
        print(f"First: Cache used = {case_1.get('cache_used', False)}")
        print(f"Second: Cache used = {case_2.get('cache_used', False)}")

if __name__ == "__main__":
    import time
    
    print("MCQ Case Converter Caching Test")
    print("=" * 50)
    
    try:
        # Test basic caching
        results = test_mcq_caching()
        
        # Test multiple MCQs
        test_multiple_mcqs()
        
        print("\n✅ Testing completed successfully!")
        
        if results and results['cache_working']:
            print(f"🎉 Cache is working! Speed improvement observed.")
        else:
            print(f"⚠️ Cache may not be working as expected.")
            
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()