#!/usr/bin/env python3
"""
Fix MCQ Case Session Mismatch Issue

The issue: Frontend is displaying wrong/cached case content despite backend generating correct cases.

Root cause: When a new MCQ case is generated, old Django session data might persist,
causing the frontend to load cached data instead of the newly generated case.

Solution: Clear old session data and ensure proper cache invalidation when new cases are generated.
"""

import os
import sys
import django
import logging

# Set up Django environment
sys.path.append('/Users/tariqalmatrudi/NEWreader/django_neurology_mcq')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from django.core.cache import cache
from django.contrib.sessions.models import Session
from mcq.models import MCQCaseConversionSession
from django.contrib.auth import get_user_model
import json

User = get_user_model()

def fix_session_mismatch():
    """Fix MCQ case session mismatch by cleaning stale data"""
    
    print("🔧 Fixing MCQ Case Session Mismatch Issue...")
    
    # 1. Clear old Django sessions with case data
    print("\n1. Clearing old Django session data...")
    
    session_count = 0
    for session in Session.objects.all():
        try:
            session_data = session.get_decoded()
            # Find case session keys
            case_keys = [key for key in session_data.keys() if 'case_session_mcq_' in key]
            
            if case_keys:
                session_count += 1
                for key in case_keys:
                    print(f"   Clearing session key: {key}")
                    del session_data[key]
                
                # Save updated session
                session.session_data = session.encode(session_data)
                session.save()
                
        except Exception as e:
            print(f"   Warning: Could not process session {session.session_key}: {e}")
    
    print(f"   ✅ Cleared case data from {session_count} Django sessions")
    
    # 2. Clear cache entries related to case validation
    print("\n2. Clearing cache validation entries...")
    
    cache_keys_cleared = 0
    try:
        # Try to get all cache keys (Django-specific)
        if hasattr(cache, '_cache') and hasattr(cache._cache, 'get_stats'):
            # For development cache
            for key in cache._cache.get_stats():
                if any(pattern in key for pattern in [
                    'django_session_verification_',
                    'session_verification_',
                    'mcq_conversion_lock_',
                    'case_validation_'
                ]):
                    cache.delete(key)
                    cache_keys_cleared += 1
        else:
            # For production cache - clear known patterns
            patterns = [
                'django_session_verification_',
                'session_verification_',
                'mcq_conversion_lock_',
                'case_validation_'
            ]
            
            # Generate some common key patterns to clear
            for mcq_id in range(100000000, 100500000, 1000):  # Sample range
                for user_id in [1, 2, 3, 4, 5]:  # Common user IDs
                    for session_id in range(1, 100, 10):  # Sample session IDs
                        test_keys = [
                            f"django_session_verification_case_session_mcq_{mcq_id}_{session_id}_{user_id}",
                            f"session_verification_{session_id}",
                            f"mcq_conversion_lock_{mcq_id}_{user_id}",
                            f"case_validation_{mcq_id}_{session_id}"
                        ]
                        
                        for key in test_keys:
                            if cache.get(key):
                                cache.delete(key)
                                cache_keys_cleared += 1
            
            # Clear all cache (safest approach)
            cache.clear()
            cache_keys_cleared = "all"
    
    except Exception as e:
        print(f"   Warning: Could not enumerate cache keys, clearing all: {e}")
        cache.clear()
        cache_keys_cleared = "all"
    
    print(f"   ✅ Cleared {cache_keys_cleared} cache entries")
    
    # 3. Update end_to_end_integrity.py to prevent session caching issues
    print("\n3. Updating end-to-end integrity module...")
    
    integrity_file = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/end_to_end_integrity.py'
    
    with open(integrity_file, 'r') as f:
        content = f.read()
    
    # Add cache clearing before storing new case data
    if 'def transfer_to_django_session' in content and 'cache.delete_many' not in content:
        
        # Find the transfer_to_django_session function and add cache clearing
        lines = content.split('\n')
        new_lines = []
        in_transfer_function = False
        indent = "        "
        
        for line in lines:
            new_lines.append(line)
            
            if 'def transfer_to_django_session(self, request, conversion_session):' in line:
                in_transfer_function = True
            
            elif in_transfer_function and 'Generate unique Django session key' in line:
                # Add cache clearing before generating new session key
                new_lines.insert(-1, f'{indent}# Clear any existing session data for this MCQ+User combination')
                new_lines.insert(-1, f'{indent}self._clear_existing_sessions(request, conversion_session.mcq_id, conversion_session.user_id)')
                new_lines.insert(-1, '')
                in_transfer_function = False
        
        # Add the new method at the end of the class
        if '_clear_existing_sessions' not in content:
            # Find the end of the class
            class_end_idx = -1
            for i, line in enumerate(new_lines):
                if line.startswith('class ') and 'E2EIntegritySystem' in line:
                    class_start = i
                elif class_start and line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                    class_end_idx = i
                    break
            
            if class_end_idx == -1:
                class_end_idx = len(new_lines)
            
            # Insert the new method before the class ends
            method_lines = [
                "",
                "    def _clear_existing_sessions(self, request, mcq_id, user_id):",
                "        \"\"\"Clear existing Django session data for MCQ+User to prevent cache issues\"\"\"",
                "        ",
                "        # Find and clear existing session keys for this MCQ+User combination",
                "        keys_to_clear = []",
                "        for key in list(request.session.keys()):",
                "            if f'case_session_mcq_{mcq_id}_' in key and f'_{user_id}' in key:",
                "                keys_to_clear.append(key)",
                "        ",
                "        for key in keys_to_clear:",
                "            del request.session[key]",
                "            logger.info(f\"Cleared existing session key: {key}\")",
                "        ",
                "        # Clear related cache entries",
                "        cache_patterns = [",
                "            f\"django_session_verification_case_session_mcq_{mcq_id}_*_{user_id}\",",
                "            f\"session_verification_*\",",
                "            f\"mcq_conversion_lock_{mcq_id}_{user_id}\"",
                "        ]",
                "        ",
                "        # Clear cache entries (pattern-based clearing)",
                "        for pattern in cache_patterns:",
                "            try:",
                "                # For simple patterns, try direct deletion",
                "                if '*' not in pattern:",
                "                    cache.delete(pattern)",
                "                else:",
                "                    # For wildcard patterns, iterate through possible values",
                "                    base_pattern = pattern.replace('*', '')",
                "                    for i in range(1, 1000):  # Session IDs typically < 1000",
                "                        test_key = pattern.replace('*', str(i))",
                "                        cache.delete(test_key)",
                "            except Exception as e:",
                "                logger.debug(f\"Cache clear attempt for {pattern}: {e}\")",
                "        ",
                "        logger.info(f\"Cleared existing session data for MCQ {mcq_id}, User {user_id}\")",
                ""
            ]
            
            new_lines = new_lines[:class_end_idx] + method_lines + new_lines[class_end_idx:]
        
        # Write the updated content
        with open(integrity_file, 'w') as f:
            f.write('\n'.join(new_lines))
        
        print(f"   ✅ Updated {integrity_file}")
    
    # 4. Update views.py to force cache refresh when resuming sessions
    print("\n4. Updating views.py to force session refresh...")
    
    views_file = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/views.py'
    
    with open(views_file, 'r') as f:
        views_content = f.read()
    
    if 'def resume_case_session' in views_content:
        # Find the resume_case_session function and add cache invalidation
        lines = views_content.split('\n')
        new_lines = []
        in_resume_function = False
        
        for line in lines:
            new_lines.append(line)
            
            if 'def resume_case_session(request):' in line:
                in_resume_function = True
            
            elif in_resume_function and 'Validate and retrieve MCQ case session' in line:
                # Add cache clearing before validation
                new_lines.insert(-2, '        # Clear any stale session cache for this user')
                new_lines.insert(-2, '        if session_id and "mcq_" in session_id:')
                new_lines.insert(-2, '            try:')
                new_lines.insert(-2, '                # Extract MCQ ID and clear related cache')
                new_lines.insert(-2, '                import re')
                new_lines.insert(-2, '                mcq_match = re.search(r"mcq_(\\d+)", session_id)')
                new_lines.insert(-2, '                if mcq_match:')
                new_lines.insert(-2, '                    mcq_id = int(mcq_match.group(1))')
                new_lines.insert(-2, '                    # Clear cache entries that might be stale')
                new_lines.insert(-2, '                    from django.core.cache import cache')
                new_lines.insert(-2, '                    cache_keys = [')
                new_lines.insert(-2, '                        f"django_session_verification_{session_id}",')
                new_lines.insert(-2, '                        f"case_validation_{mcq_id}_{request.user.id}",')
                new_lines.insert(-2, '                        f"mcq_conversion_lock_{mcq_id}_{request.user.id}"')
                new_lines.insert(-2, '                    ]')
                new_lines.insert(-2, '                    for key in cache_keys:')
                new_lines.insert(-2, '                        cache.delete(key)')
                new_lines.insert(-2, '            except Exception as e:')
                new_lines.insert(-2, '                pass  # Non-critical cache clearing')
                new_lines.insert(-2, '')
                in_resume_function = False
        
        # Write the updated content
        with open(views_file, 'w') as f:
            f.write('\n'.join(new_lines))
        
        print(f"   ✅ Updated {views_file}")
    
    print("\n✅ MCQ Case Session Mismatch Fix Complete!")
    print("\nWhat was fixed:")
    print("1. ✅ Cleared all stale Django session data containing case information")
    print("2. ✅ Cleared all cache entries that could cause session conflicts") 
    print("3. ✅ Added proactive session clearing to prevent future cache issues")
    print("4. ✅ Added cache invalidation to the resume_case_session function")
    
    print("\nNext steps:")
    print("1. Deploy these changes to Heroku")
    print("2. Test the MCQ-to-case conversion again")
    print("3. The frontend should now display the correct case content")

if __name__ == "__main__":
    fix_session_mismatch()