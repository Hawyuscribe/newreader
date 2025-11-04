#!/usr/bin/env python3
"""
Create and execute subspecialty analysis on Heroku.
"""
import subprocess
import json

# First, create an analysis script on Heroku
create_script = '''
heroku run --app radiant-gorge-35079 --no-tty "cat > /tmp/analyze_subspecialties.py << 'EOL'
from mcq.models import MCQ
from django.db.models import Count
import json

# Analyze subspecialties
print('Starting subspecialty analysis...')

# Get distribution
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('-count')
distribution = []
for sub in subspecialties:
    distribution.append({
        'subspecialty': sub['subspecialty'] if sub['subspecialty'] else 'NULL/EMPTY',
        'count': sub['count']
    })

# Analyze unclassified
unclassified_count = MCQ.objects.filter(subspecialty='Other/Unclassified').count()
other_count = MCQ.objects.filter(subspecialty='Other').count()
null_count = MCQ.objects.filter(subspecialty__isnull=True).count()
empty_count = MCQ.objects.filter(subspecialty='').count()

# Get samples of unclassified
samples = []
unclassified_mcqs = MCQ.objects.filter(subspecialty='Other/Unclassified')[:10]
for mcq in unclassified_mcqs:
    samples.append({
        'id': mcq.id,
        'question_number': mcq.question_number,
        'exam_type': mcq.exam_type,
        'exam_year': mcq.exam_year,
        'question_preview': mcq.question_text[:200],
        'source_file': mcq.source_file
    })

# Create report
report = {
    'total_mcqs': MCQ.objects.count(),
    'subspecialty_distribution': distribution,
    'unclassified_analysis': {
        'Other/Unclassified': unclassified_count,
        'Other': other_count,
        'NULL': null_count,
        'Empty': empty_count
    },
    'unclassified_samples': samples
}

# Save report
with open('/tmp/subspecialty_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print('Analysis complete. Report saved to /tmp/subspecialty_report.json')
print(json.dumps(report, indent=2))
EOL"
'''

print("Creating analysis script on Heroku...")
subprocess.run(create_script, shell=True)

# Execute the script
print("\nExecuting analysis script...")
execute_cmd = 'heroku run --app radiant-gorge-35079 --no-tty "cd /app/django_neurology_mcq && python manage.py shell < /tmp/analyze_subspecialties.py"'
result = subprocess.run(execute_cmd, shell=True, capture_output=True, text=True)

# Download the report
print("\nDownloading report...")
download_cmd = 'heroku run --app radiant-gorge-35079 --no-tty "cat /tmp/subspecialty_report.json"'
download_result = subprocess.run(download_cmd, shell=True, capture_output=True, text=True)

# Process the output
output = download_result.stdout
try:
    # Find JSON in output
    json_start = output.find('{')
    json_end = output.rfind('}') + 1
    
    if json_start != -1 and json_end > json_start:
        json_str = output[json_start:json_end]
        report = json.loads(json_str)
        
        # Save report locally
        with open('subspecialty_analysis_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\nReport saved to subspecialty_analysis_report.json")
        
        # Print summary
        print("\n" + "="*60)
        print("SUBSPECIALTY ANALYSIS SUMMARY")
        print("="*60)
        print(f"\nTotal MCQs: {report['total_mcqs']}")
        
        print("\nSUBSPECIALTY DISTRIBUTION:")
        print("-"*40)
        for item in report['subspecialty_distribution']:
            print(f"{item['subspecialty']:<35} {item['count']:>5} MCQs")
        
        print("\nUNCLASSIFIED ANALYSIS:")
        print("-"*40)
        for category, count in report['unclassified_analysis'].items():
            print(f"{category:<20} {count:>5} MCQs")
        
        print("\nSAMPLE UNCLASSIFIED MCQs:")
        print("-"*40)
        for i, sample in enumerate(report['unclassified_samples'][:5], 1):
            print(f"\n{i}. MCQ #{sample['question_number']} (ID: {sample['id']})")
            print(f"   Exam: {sample['exam_type']} {sample['exam_year']}")
            print(f"   Source: {sample['source_file']}")
            print(f"   Question: {sample['question_preview']}...")
            
    else:
        print("Could not find JSON in output")
        print("Raw output:", output[:500])
        
except Exception as e:
    print(f"Error processing report: {e}")
    print("Raw output:", output[:500])