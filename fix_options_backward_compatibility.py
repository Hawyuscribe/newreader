#!/usr/bin/env python3
"""
Fix options editing to work with existing frontend that expects async job response.
Creates a compatibility layer that simulates async behavior while using direct calls.
"""

import os
import sys
import shutil
from datetime import datetime


def fix_backward_compatibility():
    """Update views.py to simulate async behavior for frontend compatibility"""

    file_path = "django_neurology_mcq/mcq/views.py"

    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found")
        return False

    print(f"Fixing backward compatibility in {file_path}...")

    # Create backup
    backup_path = f"{file_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    print(f"✓ Created backup: {backup_path}")

    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Find the ai_edit_mcq_options function
        function_start = -1
        function_end = -1
        indent_level = 0

        for i, line in enumerate(lines):
            if "def ai_edit_mcq_options(request, mcq_id):" in line:
                function_start = i - 2  # Include decorators
                indent_level = len(line) - len(line.lstrip())
            elif function_start > 0 and line.strip().startswith("def ") and len(line) - len(line.lstrip()) == indent_level:
                function_end = i
                break

        if function_start < 0:
            print("❌ Could not find ai_edit_mcq_options function")
            return False

        if function_end < 0:
            function_end = len(lines)

        # Create new function that handles both async (for frontend) and direct modes
        new_function = '''@staff_required_json
@require_POST
def ai_edit_mcq_options(request, mcq_id):
    """
    Use AI to improve MCQ options.
    Supports both async mode (for existing frontend) and direct mode.
    """
    import logging
    import uuid
    from django.core.cache import cache

    logger = logging.getLogger(__name__)
    mcq = get_object_or_404(MCQ, id=mcq_id)

    try:
        data = json.loads(request.body)
        mode = data.get('mode', 'fill_missing')
        custom_instructions = data.get('custom_instructions', '').strip()
        use_async = data.get('use_async', True)  # Default to async for backward compatibility

        logger.info(f"AI edit options request for MCQ #{mcq_id}, mode: {mode}, async: {use_async}")

        # Import the new direct function
        from .openai_integration import ai_edit_options_direct, api_key, client

        # Check if OpenAI is available
        if not api_key or not client:
            return JsonResponse({
                'success': False,
                'error': 'OpenAI API is not configured.'
            }, status=503)

        # If frontend expects async behavior, simulate it
        if use_async:
            # Generate a job ID
            job_id = str(uuid.uuid4())

            # Do the work synchronously but store result in cache
            try:
                # Get AI-improved options (direct call)
                improved_options = ai_edit_options_direct(mcq, mode, custom_instructions)

                # Check for auto-regenerate explanations
                auto_regenerate = data.get('auto_regenerate_explanations', True)
                improved_explanations = None

                if auto_regenerate:
                    from .openai_integration import regenerate_unified_explanation
                    try:
                        # Update MCQ options temporarily for explanation generation
                        original_options = mcq.options
                        mcq.options = json.dumps(improved_options)

                        improved_explanations = regenerate_unified_explanation(mcq)

                        # Restore original options
                        mcq.options = original_options

                        logger.info(f"Regenerated explanations for MCQ #{mcq_id}")
                    except Exception as e:
                        logger.warning(f"Failed to regenerate explanations: {e}")

                # Store the result in cache for the job endpoint to retrieve
                result = {
                    'status': 'completed',
                    'result': {
                        'improved_options': improved_options,
                        'improved_explanations': improved_explanations,
                        'message': f'AI has improved options using mode: {mode}'
                    }
                }
                cache.set(f'ai_job_{job_id}', result, timeout=300)  # Cache for 5 minutes

                logger.info(f"AI edit options successful for MCQ #{mcq_id}, job_id: {job_id}")

                # Return job_id for frontend to poll
                return JsonResponse({
                    'success': True,
                    'job_id': job_id,
                    'message': 'Options editing job queued'
                })

            except Exception as e:
                # Store error in cache
                error_result = {
                    'status': 'failed',
                    'error': str(e)
                }
                cache.set(f'ai_job_{job_id}', error_result, timeout=300)

                return JsonResponse({
                    'success': True,
                    'job_id': job_id,
                    'message': 'Options editing job queued (will fail)'
                })

        else:
            # Direct mode (not used by current frontend but available)
            improved_options = ai_edit_options_direct(mcq, mode, custom_instructions)

            # Check for auto-regenerate explanations
            auto_regenerate = data.get('auto_regenerate_explanations', True)
            improved_explanations = None

            if auto_regenerate:
                from .openai_integration import regenerate_unified_explanation
                try:
                    original_options = mcq.options
                    mcq.options = json.dumps(improved_options)
                    improved_explanations = regenerate_unified_explanation(mcq)
                    mcq.options = original_options
                    logger.info(f"Regenerated explanations for MCQ #{mcq_id}")
                except Exception as e:
                    logger.warning(f"Failed to regenerate explanations: {e}")

            return JsonResponse({
                'success': True,
                'improved_options': improved_options,
                'improved_explanations': improved_explanations,
                'message': f'AI has improved options using mode: {mode}'
            })

    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in ai_edit_mcq_options: {e}")
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except ValueError as e:
        logger.error(f"Value error in ai_edit_mcq_options for MCQ #{mcq_id}: {e}")
        return JsonResponse({'success': False, 'error': str(e)})
    except Exception as e:
        logger.error(f"Error in ai_edit_mcq_options for MCQ #{mcq_id}: {e}", exc_info=True)
        return JsonResponse({'error': f'Error: {str(e)}'}, status=500)


'''

        # Replace the function
        new_lines = lines[:function_start] + [new_function] + lines[function_end:]

        # Write back
        with open(file_path, 'w') as f:
            f.writelines(new_lines)

        print("✓ Updated ai_edit_mcq_options with backward compatibility")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Restoring from backup: {backup_path}")
        shutil.copy2(backup_path, file_path)
        return False


def main():
    print("="*60)
    print("FIXING BACKWARD COMPATIBILITY FOR OPTIONS EDITING")
    print("="*60)
    print("\nThis fix:")
    print("  • Maintains compatibility with existing frontend")
    print("  • Simulates async behavior using cache")
    print("  • Returns job_id for frontend to poll")
    print("  • Stores results in cache for retrieval")
    print()

    if fix_backward_compatibility():
        print("\n✅ Successfully added backward compatibility!")
        print("\nNext steps:")
        print("  1. Commit: git add . && git commit -m 'Add backward compatibility for options editing'")
        print("  2. Deploy: git push heroku main")
        return 0
    else:
        print("\n❌ Failed to add backward compatibility")
        return 1


if __name__ == "__main__":
    sys.exit(main())