#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_neurology_mcq.settings')
django.setup()

from mcq.models import MCQ
from django.db.models import Count, Q

print("\nAnalyzing MCQ subspecialties and specialties...\n")

# Primary field: subspecialty
print("=== SUBSPECIALTY field ===")
subspecialties = MCQ.objects.values('subspecialty').annotate(count=Count('id')).order_by('subspecialty')
print(f"Total unique subspecialties: {len(subspecialties)}")
print("\nSubspecialty counts:")
for spec in subspecialties:
    print(f"  {spec['subspecialty']}: {spec['count']} MCQs")

# Secondary field: primary_category
print("\n=== PRIMARY_CATEGORY field ===")
primary_categories = MCQ.objects.values('primary_category').annotate(count=Count('id')).order_by('primary_category')
primary_categories_with_data = [p for p in primary_categories if p['primary_category']]
print(f"Total unique primary_categories (non-null): {len(primary_categories_with_data)}")
print("\nPrimary category counts:")
for cat in primary_categories_with_data:
    print(f"  {cat['primary_category']}: {cat['count']} MCQs")

# Secondary field: secondary_category
print("\n=== SECONDARY_CATEGORY field ===")
secondary_categories = MCQ.objects.values('secondary_category').annotate(count=Count('id')).order_by('secondary_category')
secondary_categories_with_data = [s for s in secondary_categories if s['secondary_category']]
print(f"Total unique secondary_categories (non-null): {len(secondary_categories_with_data)}")
print("\nSecondary category counts:")
for cat in secondary_categories_with_data:
    print(f"  {cat['secondary_category']}: {cat['count']} MCQs")

# Check for any MCQs missing subspecialty
print("\n=== MISSING DATA ===")
missing_subspecialty = MCQ.objects.filter(Q(subspecialty__isnull=True) | Q(subspecialty='')).count()
print(f"MCQs with missing subspecialty: {missing_subspecialty}")

# Also check other fields that might be related
print("\n=== EXAM_TYPE field (for reference) ===")
exam_types = MCQ.objects.values('exam_type').annotate(count=Count('id')).order_by('exam_type')
for exam in exam_types:
    print(f"  {exam['exam_type'] or 'None'}: {exam['count']} MCQs")

# Get detailed breakdown for certain common subspecialties
print("\n=== DETAILED BREAKDOWN ===")
subspecialty_sample = MCQ.objects.filter(subspecialty__in=['Epilepsy', 'Movement_Disorders', 'Headache']).values('subspecialty', 'exam_type', 'exam_year').annotate(count=Count('id')).order_by('subspecialty', 'exam_type', 'exam_year')[:20]
print("Sample subspecialties by exam type and year:")
for item in subspecialty_sample:
    print(f"  {item['subspecialty']} - {item['exam_type']} {item['exam_year']}: {item['count']} MCQs")