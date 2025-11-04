import sys
import os

print("Python version:", sys.version)
print("Python path:", sys.path)
print("Current directory:", os.getcwd())
print("Directory listing:")
for item in os.listdir('.'):
    print(f"  - {item}")

try:
    import django
    print("Django version:", django.get_version())
    print("Django settings module:", os.environ.get('DJANGO_SETTINGS_MODULE'))
    
    # Try to import the mcq models
    try:
        import mcq.models
        print("Successfully imported mcq.models")
    except ImportError as e:
        print(f"Failed to import mcq.models: {e}")
        
        # Try alternative approaches
        try:
            sys.path.append('.')
            import mcq.models
            print("Successfully imported mcq.models after path adjustment")
        except ImportError as e:
            print(f"Still failed to import mcq.models: {e}")
            
except ImportError as e:
    print(f"Failed to import Django: {e}")