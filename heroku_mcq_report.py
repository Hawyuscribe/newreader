#!/usr/bin/env python3
"""
Generate MCQ classification report from Heroku.
"""
import subprocess
import json

print("Generating MCQ Classification Report from Heroku Website")
print("="*60)

# Create a Python script that will run on Heroku
heroku_script = '''
import json
from mcq.models import MCQ
from django.db.models import Count

# Initialize results
results = {
    'total': MCQ.objects.count(),
    'by_subspecialty': [],
    'by_exam_type': [],
    'by_exam_year': [],
    'by_type_year': [],
    'all_subspecialties': []
}

# Get counts by subspecialty
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
for s in subspecialties:
    results['by_subspecialty'].append({
        'name': s['subspecialty'] or 'Not specified',
        'count': s['count']
    })

# Get counts by exam type
exam_types = MCQ.objects.values('exam_type').annotate(count=Count('id')).order_by('-count')
for e in exam_types:
    results['by_exam_type'].append({
        'name': e['exam_type'] or 'Not specified',
        'count': e['count']
    })

# Get counts by exam year
years = MCQ.objects.values('exam_year').annotate(count=Count('id')).order_by('exam_year')
for y in years:
    results['by_exam_year'].append({
        'name': str(y['exam_year']) if y['exam_year'] else 'Not specified',
        'count': y['count']
    })

# Get counts by exam type and year
combinations = MCQ.objects.values('exam_type', 'exam_year').annotate(count=Count('id')).order_by('exam_type', 'exam_year')
for c in combinations:
    etype = c['exam_type'] or 'Unknown'
    year = str(c['exam_year']) if c['exam_year'] else 'Unknown'
    results['by_type_year'].append({
        'name': f'{etype} - {year}',
        'count': c['count']
    })

# Get all unique subspecialties
all_subspecialties = MCQ.objects.values_list('subspecialty', flat=True).distinct().order_by('subspecialty')
results['all_subspecialties'] = list(all_subspecialties)

# Save to file
with open('/tmp/mcq_report.json', 'w') as f:
    json.dump(results, f)

print("Report saved to /tmp/mcq_report.json")
'''

# Create the script file on Heroku
create_script_cmd = f"echo '{heroku_script}' > /tmp/generate_report.py"
subprocess.run(f'heroku run --app radiant-gorge-35079 --no-tty "{create_script_cmd}"', shell=True)

# Run the script
run_script_cmd = "cd /app/django_neurology_mcq && python manage.py shell < /tmp/generate_report.py"
subprocess.run(f'heroku run --app radiant-gorge-35079 --no-tty "{run_script_cmd}"', shell=True)

# Download the report
download_cmd = "cat /tmp/mcq_report.json"
result = subprocess.run(f'heroku run --app radiant-gorge-35079 --no-tty "{download_cmd}"', shell=True, capture_output=True, text=True)

# Parse and display the results
try:
    # Extract JSON from the output
    output = result.stdout
    json_start = output.find('{')
    json_end = output.rfind('}') + 1
    
    if json_start != -1 and json_end > json_start:
        json_str = output[json_start:json_end]
        data = json.loads(json_str)
        
        print(f"\nTOTAL MCQs: {data['total']}")
        
        print("\n1. MCQs BY SUBSPECIALTY:")
        print("-"*50)
        for item in data['by_subspecialty']:
            print(f"{item['name']:<40} {item['count']:>5} MCQs")
        
        print("\n2. MCQs BY EXAM TYPE:")
        print("-"*50)
        for item in data['by_exam_type']:
            print(f"{item['name']:<40} {item['count']:>5} MCQs")
        
        print("\n3. MCQs BY EXAM YEAR:")
        print("-"*50)
        for item in data['by_exam_year']:
            print(f"{item['name']:<40} {item['count']:>5} MCQs")
        
        print("\n4. MCQs BY EXAM TYPE AND YEAR:")
        print("-"*50)
        for item in data['by_type_year']:
            print(f"{item['name']:<40} {item['count']:>5} MCQs")
        
        print("\n5. ALL SUBSPECIALTIES:")
        print("-"*50)
        print(f"Total unique subspecialties: {len(data['all_subspecialties'])}")
        for i, sub in enumerate(data['all_subspecialties'], 1):
            print(f"{i:>3}. {sub or 'Not specified'}")
        
        # Save the full report
        with open('mcq_classification_report.json', 'w') as f:
            json.dump(data, f, indent=2)
        print("\nFull report saved to: mcq_classification_report.json")
        
    else:
        print("Error: Could not extract JSON data from Heroku output")
        print("Raw output:", output[:500])
        
except Exception as e:
    print(f"Error parsing results: {e}")
    print("Raw output:", result.stdout[:500])