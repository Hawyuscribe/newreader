#!/usr/bin/env python3
"""
MCQ Processor Launcher
Simple launcher script with dependency checking and setup.
"""

import os
import sys
import subprocess


def check_and_install_dependencies():
    """Check and install required dependencies."""
    print("Checking dependencies...")
    
    required_packages = {
        'openai': 'openai',
        'tiktoken': 'tiktoken', 
        'backoff': 'backoff',
        'tkinter': None  # Built-in, just check
    }
    
    missing = []
    
    for module, package in required_packages.items():
        try:
            if module == 'tkinter':
                import tkinter
            else:
                __import__(module)
            print(f"✓ {module} is installed")
        except ImportError:
            if package:
                missing.append(package)
                print(f"✗ {module} is not installed")
            else:
                print(f"✗ {module} is not available (may need system package)")
    
    if missing:
        print(f"\nInstalling missing packages: {', '.join(missing)}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing)
        print("✓ Dependencies installed successfully")
    
    return True


def check_api_key():
    """Check if OpenAI API key is set."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("\n⚠️  OpenAI API Key not found!")
        print("\nTo set your API key:")
        print("  macOS/Linux: export OPENAI_API_KEY='your-key-here'")
        print("  Windows: set OPENAI_API_KEY=your-key-here")
        print("\nYou can also enter it in the GUI after launching.")
        return False
    else:
        print("✓ OpenAI API key found")
        return True


def main():
    """Main launcher function."""
    print("MCQ Processor Launcher")
    print("=" * 50)
    
    # Check dependencies
    if not check_and_install_dependencies():
        print("\nFailed to install dependencies. Please install manually.")
        sys.exit(1)
    
    # Check API key (optional - can be set in GUI)
    check_api_key()
    
    print("\n" + "=" * 50)
    print("Launching MCQ Processor GUI...")
    print("\nFeatures:")
    print("• O3-mini high reasoning mode for maximum accuracy")
    print("• Concurrent processing with 5 workers")
    print("• Real-time progress monitoring")
    print("• Robust error handling and retry logic")
    print("• Comprehensive logging")
    
    print("\n" + "=" * 50)
    
    try:
        # Import and launch GUI
        from mcq_processor_gui import main as launch_gui
        launch_gui()
    except Exception as e:
        print(f"\nError launching GUI: {str(e)}")
        print("\nTrying command-line mode...")
        
        try:
            from mcq_processor import main as launch_cli
            launch_cli()
        except Exception as e2:
            print(f"Error launching CLI: {str(e2)}")
            sys.exit(1)


if __name__ == "__main__":
    main()