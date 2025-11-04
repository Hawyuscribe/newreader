from django.core.management.base import BaseCommand
from django.db import transaction, connection
from mcq.models import MCQ
import json
import os
from collections import defaultdict
import hashlib

class Command(BaseCommand):
    help = 'Verify and import all MCQs, ensuring none are missed'

    def create_question_hash(self, question_text):
        """Create a hash of the question text for comparison"""
        # Normalize the text: remove extra spaces, lowercase
        normalized = ' '.join(question_text.lower().split())
        return hashlib.md5(normalized.encode()).hexdigest()

    def handle(self, *args, **options):
        self.stdout.write("=== MCQ Import Verification and Import ===\n")
        
        # Step 1: Count MCQs in source files
        consolidated_dir = '/Users/tariqalmatrudi/NEWreader/consolidated_mcqs'
        source_mcqs = []
        source_stats = defaultdict(int)
        
        self.stdout.write("Loading MCQs from source files...")
        for filename in sorted(os.listdir(consolidated_dir)):
            if filename.endswith('.json') and not filename.startswith('.'):
                filepath = os.path.join(consolidated_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        mcqs = data.get('mcqs', [])
                        source_mcqs.extend(mcqs)
                        source_stats[filename] = len(mcqs)
                        self.stdout.write(f"  {filename}: {len(mcqs)} MCQs")
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"  Error loading {filename}: {str(e)}"))
        
        total_source = len(source_mcqs)
        self.stdout.write(f"\nTotal MCQs in source files: {total_source}")
        
        # Step 2: Count MCQs in database
        db_count = MCQ.objects.count()
        self.stdout.write(f"Total MCQs in database: {db_count}")
        self.stdout.write(f"Difference: {total_source - db_count} MCQs\n")
        
        # Step 3: Find missing MCQs
        self.stdout.write("Analyzing missing MCQs...")
        
        # Get all question texts from database (using hash for comparison)
        db_question_hashes = set()
        for mcq in MCQ.objects.all():
            db_question_hashes.add(self.create_question_hash(mcq.question_text))
        
        missing_mcqs = []
        duplicate_count = 0
        
        for mcq_data in source_mcqs:
            question_hash = self.create_question_hash(mcq_data.get('question_text', ''))
            if question_hash not in db_question_hashes:
                missing_mcqs.append(mcq_data)
            else:
                duplicate_count += 1
        
        self.stdout.write(f"\nFound {len(missing_mcqs)} missing MCQs")
        self.stdout.write(f"Found {duplicate_count} duplicate MCQs (already in database)")
        
        # Step 4: Analyze why MCQs are missing
        if missing_mcqs:
            self.stdout.write("\nAnalyzing missing MCQs...")
            issues = defaultdict(list)
            
            for mcq in missing_mcqs[:10]:  # Sample first 10
                # Check correct_answer length
                correct_answer = str(mcq.get('correct_answer', '')).strip()
                if len(correct_answer) > 5:
                    issues['long_correct_answer'].append({
                        'question': mcq.get('question_text', '')[:100] + '...',
                        'correct_answer': correct_answer,
                        'length': len(correct_answer)
                    })
                
                # Check options format
                options = mcq.get('options', {})
                if isinstance(options, list):
                    issues['list_options'].append({
                        'question': mcq.get('question_text', '')[:100] + '...'
                    })
                
                # Check for missing required fields
                if not mcq.get('question_text'):
                    issues['missing_question'].append(mcq)
                
            # Print issues summary
            for issue_type, examples in issues.items():
                self.stdout.write(f"\n{issue_type}: {len(examples)} cases")
                if examples and len(examples) > 0:
                    self.stdout.write(f"  Example: {examples[0]}")
        
        # Step 5: Import missing MCQs with enhanced error handling
        if missing_mcqs:
            self.stdout.write(f"\nImporting {len(missing_mcqs)} missing MCQs...")
            
            created_count = 0
            error_count = 0
            error_details = defaultdict(int)
            
            with transaction.atomic():
                for idx, mcq_data in enumerate(missing_mcqs):
                    try:
                        # Enhanced correct_answer cleaning
                        correct_answer = str(mcq_data.get('correct_answer', '')).strip()
                        
                        # Handle various formats
                        if correct_answer.lower().startswith('option '):
                            correct_answer = correct_answer.replace('Option ', '').replace('option ', '').strip()
                        elif correct_answer.lower().startswith('answer '):
                            correct_answer = correct_answer.replace('Answer ', '').replace('answer ', '').strip()
                        elif ' ' in correct_answer and len(correct_answer) > 5:
                            # Try to extract just the letter
                            parts = correct_answer.split()
                            for part in parts:
                                if len(part) <= 5 and part.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
                                    correct_answer = part.upper()
                                    break
                        
                        # Final cleanup
                        correct_answer = correct_answer[:5]  # Ensure max 5 chars
                        
                        # Handle options
                        options = mcq_data.get('options', {})
                        if isinstance(options, list):
                            # Convert list to dict
                            options_dict = {}
                            for opt in options:
                                if isinstance(opt, dict) and 'letter' in opt and 'text' in opt:
                                    options_dict[opt['letter'].upper()] = opt['text']
                                elif isinstance(opt, str):
                                    # Try to parse "A. Text" format
                                    if '. ' in opt[:3]:
                                        letter, text = opt.split('. ', 1)
                                        options_dict[letter.upper()] = text
                            options = options_dict
                        
                        # Handle explanation sections
                        explanation_sections = mcq_data.get('explanation_sections', {})
                        
                        # Map common variations to standard keys
                        if 'option_analysis' in mcq_data and mcq_data['option_analysis']:
                            explanation_sections['option_analysis'] = mcq_data['option_analysis']
                        
                        # Standardize section keys
                        standardized_sections = {}
                        key_mappings = {
                            'conceptual_foundation': ['conceptual foundation', 'Conceptual Foundation'],
                            'pathophysiological_mechanisms': ['pathophysiology', 'Pathophysiology', 'pathophysiological mechanisms'],
                            'clinical_correlation': ['clinical correlation', 'Clinical Correlation', 'clinical context'],
                            'classification_and_nosology': ['classification and neurology', 'classification and nosology'],
                            'diagnostic_approach': ['diagnostic approach', 'Diagnostic Approach'],
                            'management_principles': ['management principles', 'Management Principles'],
                            'option_analysis': ['option analysis', 'Option Analysis', 'options analysis'],
                            'clinical_pearls': ['clinical pearls', 'Clinical Pearls', 'key insight'],
                            'current_evidence': ['current evidence', 'Current Evidence', 'quick reference']
                        }
                        
                        for standard_key, variations in key_mappings.items():
                            # Check if standard key exists
                            if standard_key in explanation_sections:
                                standardized_sections[standard_key] = explanation_sections[standard_key]
                            else:
                                # Check variations
                                for var in variations:
                                    if var in explanation_sections:
                                        standardized_sections[standard_key] = explanation_sections[var]
                                        break
                        
                        # Copy any other keys
                        for key, value in explanation_sections.items():
                            if key not in standardized_sections and value:
                                standardized_sections[key] = value
                        
                        # Ensure we have a question_text
                        question_text = mcq_data.get('question_text', '').strip()
                        if not question_text:
                            raise ValueError("Empty question text")
                        
                        # Create MCQ
                        mcq = MCQ(
                            question_text=question_text,
                            options=options or {},
                            correct_answer=correct_answer,
                            explanation=mcq_data.get('explanation', ''),
                            explanation_sections=standardized_sections,
                            subspecialty=mcq_data.get('subspecialty', 'Other/Unclassified'),
                            exam_type=mcq_data.get('exam_type', ''),
                            exam_year=mcq_data.get('exam_year', ''),
                            question_number=mcq_data.get('question_number', ''),
                            source_file=mcq_data.get('source_file', ''),
                            image_url=mcq_data.get('image_url', ''),
                            correct_answer_text=mcq_data.get('correct_answer_text', '')
                        )
                        mcq.save()
                        created_count += 1
                        
                        if created_count % 100 == 0:
                            self.stdout.write(f"  Progress: {created_count}/{len(missing_mcqs)} imported...")
                            
                    except Exception as e:
                        error_count += 1
                        error_type = type(e).__name__
                        error_details[error_type] += 1
                        
                        if error_count <= 5:  # Show first 5 errors
                            self.stdout.write(
                                self.style.ERROR(
                                    f"  Error {error_count}: {str(e)}\n"
                                    f"  Question: {mcq_data.get('question_text', '')[:100]}...\n"
                                    f"  Correct Answer: {mcq_data.get('correct_answer', '')}"
                                )
                            )
            
            # Final import summary
            self.stdout.write(self.style.SUCCESS(f"\n=== Import Complete ==="))
            self.stdout.write(f"Successfully imported: {created_count}")
            self.stdout.write(f"Errors: {error_count}")
            
            if error_details:
                self.stdout.write("\nError breakdown:")
                for error_type, count in error_details.items():
                    self.stdout.write(f"  {error_type}: {count}")
        
        # Step 6: Final verification
        final_db_count = MCQ.objects.count()
        self.stdout.write(self.style.SUCCESS(f"\n=== Final Status ==="))
        self.stdout.write(f"Total MCQs in source files: {total_source}")
        self.stdout.write(f"Total MCQs in database: {final_db_count}")
        self.stdout.write(f"Difference: {total_source - final_db_count}")
        
        # Show subspecialty distribution
        self.stdout.write("\n=== Subspecialty Distribution ===")
        from django.db.models import Count
        subspecialty_counts = MCQ.objects.values('subspecialty').annotate(
            count=Count('subspecialty')
        ).order_by('-count')
        
        for item in subspecialty_counts:
            self.stdout.write(f"  {item['subspecialty']}: {item['count']} MCQs")