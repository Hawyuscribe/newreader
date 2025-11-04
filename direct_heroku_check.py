#!/usr/bin/env python3
import subprocess
import sys

def run_heroku_command(cmd):
    """Run a Heroku command and return the output."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return None
        return result.stdout
    except Exception as e:
        print(f"Error running command: {e}")
        return None

def main():
    app_name = 'mcq-reader'
    
    # Check app info
    print("Checking Heroku app info...")
    info_output = run_heroku_command(f"heroku apps:info --app {app_name}")
    if info_output:
        print(info_output)
    
    # Check current configuration
    print("\nChecking Heroku config...")
    config_output = run_heroku_command(f"heroku config --app {app_name}")
    if config_output:
        print(config_output)
    
    # Run simple Python command to test the environment
    print("\nTesting Python environment...")
    test_output = run_heroku_command(f"heroku run \"python --version\" --app {app_name}")
    if test_output:
        print(test_output)
    
    # Check directories
    print("\nListing directories on Heroku...")
    dir_output = run_heroku_command(f"heroku run \"ls -la\" --app {app_name}")
    if dir_output:
        print(dir_output)
    
    # Check if we have django_neurology_mcq directory
    print("\nChecking for Django app directory...")
    django_output = run_heroku_command(f"heroku run \"ls -la django_neurology_mcq 2>/dev/null || echo 'Directory not found'\" --app {app_name}")
    if django_output:
        print(django_output)

if __name__ == "__main__":
    main()