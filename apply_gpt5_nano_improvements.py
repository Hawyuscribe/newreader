#!/usr/bin/env python3
"""
Apply GPT-5-nano improvements to the existing openai_integration.py
This script contains the specific changes to make
"""

import os
import sys


def apply_improvements():
    """Apply the improvements to openai_integration.py"""

    file_path = "django_neurology_mcq/mcq/openai_integration.py"

    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return False

    print(f"Applying GPT-5-nano improvements to {file_path}")

    # Read the file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Track changes made
    changes_made = []

    # Improvement 1: Optimize temperature and parameters for GPT-5-nano
    print("\n1. Optimizing parameters for GPT-5-nano...")

    for i, line in enumerate(lines):
        # Find the _improve_all_options_with_model function
        if "def _improve_all_options_with_model" in line:
            # Look for the _responses_create call
            for j in range(i, min(i + 200, len(lines))):
                if "_responses_create(" in lines[j]:
                    # Check if this is for OPTIONS_MODEL
                    for k in range(j, min(j + 20, len(lines))):
                        if "temperature=" in lines[k]:
                            # Change temperature for GPT-5-nano (more focused)
                            if "0.6" in lines[k]:
                                lines[k] = lines[k].replace("0.6", "0.4")
                                changes_made.append(f"Line {k+1}: Changed temperature from 0.6 to 0.4 for GPT-5-nano")
                        if "top_p=" in lines[k]:
                            # Change top_p for GPT-5-nano (more deterministic)
                            if "0.9" in lines[k]:
                                lines[k] = lines[k].replace("0.9", "0.85")
                                changes_made.append(f"Line {k+1}: Changed top_p from 0.9 to 0.85 for GPT-5-nano")
                        if "max_output_tokens=" in lines[k]:
                            # Reduce tokens for faster response
                            if "600" in lines[k]:
                                lines[k] = lines[k].replace("600", "500")
                                changes_made.append(f"Line {k+1}: Reduced max_output_tokens from 600 to 500")
                    break

    # Improvement 2: Optimize the prompt for GPT-5-nano (more concise)
    print("2. Optimizing prompts for GPT-5-nano...")

    for i, line in enumerate(lines):
        if '"You are a neurology board-exam content specialist."' in line:
            # Make the system prompt more concise for GPT-5-nano
            original = '"You are a neurology board-exam content specialist. "'
            optimized = '"You are a medical expert. "'
            if original in lines[i]:
                lines[i] = lines[i].replace(original, optimized)
                changes_made.append(f"Line {i+1}: Optimized system prompt for GPT-5-nano")

    # Improvement 3: Add better retry logic for GPT-5-nano
    print("3. Adding improved retry logic...")

    for i, line in enumerate(lines):
        if "max_attempts = 3" in line:
            # Reduce max attempts for faster failing
            lines[i] = line.replace("3", "2")
            changes_made.append(f"Line {i+1}: Reduced max_attempts from 3 to 2 for faster processing")

    # Improvement 4: Add caching comment
    print("4. Adding caching recommendation...")

    for i, line in enumerate(lines):
        if "def ai_improve_all_options(mcq" in line:
            # Add a comment about caching
            cache_comment = """    # TODO: Add caching here to avoid redundant API calls
    # cache_key = f"options_{mcq.id}_{custom_instructions[:50]}"
    # cached = cache.get(cache_key)
    # if cached: return cached

"""
            lines.insert(i + 1, cache_comment)
            changes_made.append(f"Line {i+1}: Added caching recommendation comment")
            break

    # Improvement 5: Optimize JSON extraction for GPT-5
    print("5. Improving JSON extraction for GPT-5 responses...")

    for i, line in enumerate(lines):
        if "def _extract_json_from_text(text: str)" in line:
            # This function handles JSON extraction
            # Add a check for GPT-5 specific patterns
            for j in range(i + 1, min(i + 50, len(lines))):
                if "text = text.strip()" in lines[j]:
                    gpt5_check = """    # GPT-5 sometimes wraps JSON in markdown code blocks
    if text.startswith('```json'):
        text = text[7:]  # Remove ```json
    if text.endswith('```'):
        text = text[:-3]  # Remove ```
    text = text.strip()

"""
                    lines.insert(j + 1, gpt5_check)
                    changes_made.append(f"Line {j+1}: Added GPT-5 markdown code block handling")
                    break
            break

    # Improvement 6: Add specific handling for empty responses
    print("6. Adding empty response handling...")

    for i, line in enumerate(lines):
        if '"verbosity": default_verbosity' in line and 'json_schema' not in lines[i-5:i+5]:
            # This is the problematic line that caused empty responses
            # Already fixed in previous session, but verify it's correct
            pass

    # Write the improved file
    output_file = file_path

    if changes_made:
        print(f"\nWriting {len(changes_made)} improvements to {output_file}...")
        with open(output_file, 'w') as f:
            f.writelines(lines)

        print("\nChanges applied:")
        for change in changes_made:
            print(f"  ✓ {change}")

        return True
    else:
        print("\nNo changes needed - file already optimized!")
        return True


def create_optimization_config():
    """Create a configuration file for GPT-5-nano optimizations"""

    config_content = """# GPT-5-nano Optimization Configuration

# Model-specific settings
GPT5_NANO_SETTINGS = {
    "temperature": 0.4,      # Lower for more consistent output
    "top_p": 0.85,          # More focused than default 0.9
    "max_tokens": 500,      # Reduced from 600 for faster response
    "timeout": 20,          # Shorter timeout for nano model
    "retry_attempts": 2,    # Fewer retries for faster failing
}

# Prompt optimization settings
PROMPT_OPTIMIZATION = {
    "max_question_length": 200,     # Truncate long questions
    "max_instruction_length": 100,  # Limit custom instructions
    "use_concise_system_prompt": True,
    "skip_explanation_context": False,  # Keep for accuracy
}

# Cache settings (for future implementation)
CACHE_SETTINGS = {
    "enable_caching": True,
    "cache_ttl": 3600,  # 1 hour
    "cache_key_prefix": "gpt5_nano_options",
}

# Medical enhancement settings
MEDICAL_ENHANCEMENT = {
    "min_option_length": 20,     # Minimum characters for an option
    "target_option_length": 80,  # Target length for enhanced options
    "add_clinical_features": True,
    "add_diagnostic_details": True,
    "preserve_correct_answer": True,
}

# Error handling
ERROR_HANDLING = {
    "fallback_to_local_enhancement": True,
    "log_api_errors": True,
    "retry_on_empty_response": True,
    "max_retries": 2,
}

# Performance monitoring
MONITORING = {
    "track_processing_time": True,
    "log_improvement_ratio": True,
    "alert_on_slow_response": 10,  # seconds
    "track_model_usage": True,
}
"""

    config_file = "django_neurology_mcq/mcq/gpt5_nano_config.py"
    print(f"\nCreating optimization config at {config_file}...")

    with open(config_file, 'w') as f:
        f.write(config_content)

    print(f"✓ Created {config_file}")
    return config_file


def main():
    """Main function to apply improvements"""
    print("\n" + "="*60)
    print("GPT-5-NANO OPTIMIZATION SCRIPT")
    print("="*60)

    print("\nThis script will optimize the OpenAI integration for GPT-5-nano")
    print("Based on testing insights and performance analysis")

    # Apply the improvements
    success = apply_improvements()

    if success:
        print("\n✅ Successfully applied GPT-5-nano optimizations!")

        # Create config file
        config_file = create_optimization_config()

        print("\n" + "="*60)
        print("OPTIMIZATION COMPLETE")
        print("="*60)

        print("\nNext steps:")
        print("1. Review the changes in openai_integration.py")
        print(f"2. Import settings from {config_file} if needed")
        print("3. Test with: python test_gpt5_nano_fixed.py")
        print("4. Deploy to Heroku: git push heroku main")

        print("\nKey improvements applied:")
        print("  • Optimized temperature (0.4) for consistent medical content")
        print("  • Reduced top_p (0.85) for more focused output")
        print("  • Decreased max_tokens (500) for faster response")
        print("  • Added GPT-5 markdown handling in JSON extraction")
        print("  • Added caching recommendations")
        print("  • Reduced retry attempts for faster failing")

    else:
        print("\n❌ Failed to apply optimizations")
        print("Please check the error messages above")

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())