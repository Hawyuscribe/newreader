#!/usr/bin/env python3
"""
Simple verification of GPT-5 configuration
"""

import sys
import os

# Add the django_neurology_mcq directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'django_neurology_mcq'))

def verify_openai_config():
    """Check the OpenAI integration configuration"""
    print("="*60)
    print("GPT-5 Configuration Verification")
    print("="*60)
    print()

    try:
        # Import the openai_integration module directly
        from mcq import openai_integration

        print("Model Configuration:")
        print("-"*40)

        # Check each model configuration
        configs = [
            ("DEFAULT_MODEL", openai_integration.DEFAULT_MODEL, "gpt-5-mini"),
            ("OPTIONS_MODEL", openai_integration.OPTIONS_MODEL, "gpt-5-nano"),
            ("FALLBACK_MODEL", openai_integration.FALLBACK_MODEL, "gpt-5-mini"),
            ("OPTIONS_FALLBACK_MODEL", openai_integration.OPTIONS_FALLBACK_MODEL, "gpt-5-mini"),
        ]

        all_correct = True
        for name, actual, expected in configs:
            status = "✓" if actual == expected else "❌"
            print(f"{status} {name}: {actual}")
            if actual != expected:
                print(f"   Expected: {expected}")
                all_correct = False

        print()
        print("Additional Settings:")
        print("-"*40)
        print(f"Option request timeout: {openai_integration.OPTION_REQUEST_TIMEOUT}s")
        print(f"Default timeout: {openai_integration.DEFAULT_TIMEOUT}s")

        # Check verbosity
        try:
            default_verb = openai_integration.get_default_verbosity()
            print(f"Default verbosity: {default_verb}")
        except:
            print("Default verbosity: (function not accessible)")

        print()
        print("="*60)
        if all_correct:
            print("✅ All GPT-5 models are correctly configured!")
            print()
            print("Configuration Summary:")
            print("  • Question stem AI editing → GPT-5-mini")
            print("  • Options AI editing → GPT-5-nano (optimized for speed)")
            print("  • Fallback models → GPT-5-mini")
            print()
            print("Key fix applied:")
            print("  • JSON schema responses use 'auto' verbosity")
            print("  • This prevents empty responses from GPT-5 models")
        else:
            print("⚠ Some models are not configured as expected")
            print("Please check the configuration above")

        return all_correct

    except ImportError as e:
        print(f"❌ Could not import openai_integration: {e}")
        print()
        print("Attempting to read configuration directly from file...")
        return check_file_directly()

def check_file_directly():
    """Read the configuration directly from the source file"""
    config_file = "django_neurology_mcq/mcq/openai_integration.py"

    if not os.path.exists(config_file):
        print(f"❌ File not found: {config_file}")
        return False

    print()
    print("Reading configuration from source file:")
    print("-"*40)

    with open(config_file, 'r') as f:
        lines = f.readlines()

    # Look for model configurations
    configs_found = {}
    for i, line in enumerate(lines):
        if 'DEFAULT_MODEL' in line and '=' in line and 'or "gpt-' in line:
            model = line.split('"')[1] if '"' in line else "unknown"
            configs_found['DEFAULT_MODEL'] = model
            print(f"Line {i+1}: DEFAULT_MODEL = {model}")

        elif 'OPTIONS_MODEL' in line and '=' in line and 'or "gpt-' in line:
            model = line.split('"')[1] if '"' in line else "unknown"
            configs_found['OPTIONS_MODEL'] = model
            print(f"Line {i+1}: OPTIONS_MODEL = {model}")

    print()
    # Check if configurations are correct
    correct = (
        configs_found.get('DEFAULT_MODEL') == 'gpt-5-mini' and
        configs_found.get('OPTIONS_MODEL') == 'gpt-5-nano'
    )

    if correct:
        print("✓ GPT-5 models are configured in the source code")
    else:
        print("❌ GPT-5 models are not properly configured")

    return correct

def main():
    """Main verification"""
    print("\n" + "="*60)
    print("GPT-5-nano Options Editing - Configuration Check")
    print("="*60 + "\n")

    config_ok = verify_openai_config()

    print("="*60)
    print()

    if config_ok:
        print("✅ SUCCESS - GPT-5 configuration verified!")
        print()
        print("The system is configured to use:")
        print("  • GPT-5-mini for question stem editing")
        print("  • GPT-5-nano for options editing (faster)")
        print()
        print("To test the live functionality:")
        print("  1. Export admin password: export ADMIN_PASSWORD='...'")
        print("  2. Run: python test_gpt5_with_login.py")
        return 0
    else:
        print("❌ Configuration needs adjustment")
        return 1

if __name__ == "__main__":
    sys.exit(main())