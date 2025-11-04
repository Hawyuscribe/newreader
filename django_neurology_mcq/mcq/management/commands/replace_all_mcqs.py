import json
import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ


class Command(BaseCommand):
    help = 'Replace all MCQs with new ones from the specified directory'

    def add_arguments(self, parser):
        parser.add_argument(
            '--source-dir',
            type=str,
            default='/Users/tariqalmatrudi/Documents/FFF/output_by_specialty',
            help='Directory containing the new MCQ JSON files'
        )
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirm deletion of all existing MCQs'
        )

    def handle(self, *args, **options):
        source_dir = options['source_dir']
        confirm = options['confirm']
        
        # Check current MCQ count
        current_count = MCQ.objects.count()
        self.stdout.write(f"Current MCQ count in database: {current_count}")
        
        if current_count > 0 and not confirm:
            self.stdout.write(self.style.WARNING(
                "WARNING: There are existing MCQs in the database!"
                "\nRun with --confirm to delete them and import new ones."
            ))
            return
        
        # Delete all existing MCQs
        if current_count > 0:
            self.stdout.write("Deleting all existing MCQs...")
            MCQ.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Deleted {current_count} MCQs"))
        
        # Import new MCQs
        imported_count = 0
        errors = []
        
        # Get all JSON files in the directory
        json_files = sorted(Path(source_dir).glob('*.json'))
        self.stdout.write(f"Found {len(json_files)} JSON files to process")
        
        with transaction.atomic():
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    mcqs = data.get('mcqs', [])
                    subspecialty = data.get('specialty', data.get('subspecialty', 'Unknown'))
                    
                    self.stdout.write(f"\nProcessing {json_file.name}: {subspecialty} with {len(mcqs)} MCQs")
                    
                    for mcq_data in mcqs:
                        try:
                            # Process explanation - handle both unified and structured formats
                            explanation = ""
                            explanation_sections = None
                            unified_explanation = None
                            
                            # Check for unified explanation first
                            if 'unified_explanation' in mcq_data and mcq_data['unified_explanation']:
                                unified_explanation = mcq_data['unified_explanation']
                                explanation = unified_explanation  # Also store in main explanation field
                            
                            # Check for structured explanation sections
                            if 'explanation' in mcq_data and isinstance(mcq_data['explanation'], dict):
                                explanation_sections = {}
                                explanation_parts = []
                                
                                for section, content in mcq_data['explanation'].items():
                                    # Ensure content is a string and not empty
                                    if content and isinstance(content, str) and not content.startswith("This section information is included"):
                                        explanation_sections[section] = content
                                        # Format section name for display
                                        section_title = section.replace('_', ' ').title()
                                        explanation_parts.append(f"**{section_title}**\n{content}")
                                
                                # If no unified explanation, build from sections
                                if not unified_explanation:
                                    explanation = "\n\n".join(explanation_parts)
                            
                            # Create MCQ with all the new fields
                            mcq = MCQ(
                                question_number=mcq_data.get('question_number', ''),
                                question_text=mcq_data.get('question', mcq_data.get('question_text', '')),  # Handle both 'question' and 'question_text'
                                options=mcq_data.get('options', []),
                                correct_answer=mcq_data.get('correct_answer', ''),
                                correct_answer_text=mcq_data.get('correct_answer_text', ''),
                                subspecialty=subspecialty,
                                exam_type=mcq_data.get('exam_type', ''),
                                exam_year=mcq_data.get('exam_year', mcq_data.get('year', '')),
                                source_file=mcq_data.get('source_file', ''),
                                ai_generated=mcq_data.get('ai_generated', False),
                                explanation=explanation,
                                explanation_sections=explanation_sections,
                                unified_explanation=unified_explanation,
                                word_count=mcq_data.get('word_count'),
                                image_url=mcq_data.get('image_url'),
                                # Keep legacy fields for backward compatibility
                                primary_category=mcq_data.get('topic', ''),
                                difficulty_level=mcq_data.get('difficulty'),
                                key_concept=mcq_data.get('key_concepts', [''])[0] if mcq_data.get('key_concepts') else '',
                                verification_confidence=mcq_data.get('verification_confidence')
                            )
                            
                            # Handle fixed_at timestamp if present
                            if 'fixed_at' in mcq_data and mcq_data['fixed_at']:
                                try:
                                    from django.utils.dateparse import parse_datetime
                                    fixed_at = parse_datetime(mcq_data['fixed_at'])
                                    if fixed_at:
                                        mcq.fixed_at = fixed_at
                                except (ValueError, TypeError):
                                    pass  # Skip invalid timestamps
                            mcq.save()
                            imported_count += 1
                            
                            if imported_count % 100 == 0:
                                self.stdout.write(f"  Imported {imported_count} MCQs so far...")
                            
                        except Exception as e:
                            error_msg = f"Error importing MCQ from {json_file.name}: {str(e)}"
                            errors.append(error_msg)
                            self.stdout.write(self.style.ERROR(f"  ERROR: {error_msg}"))
                            
                except Exception as e:
                    error_msg = f"Error processing file {json_file.name}: {str(e)}"
                    errors.append(error_msg)
                    self.stdout.write(self.style.ERROR(f"ERROR: {error_msg}"))
        
        # Print summary
        self.stdout.write("\n" + "="*50)
        self.stdout.write(self.style.SUCCESS(f"Import complete!"))
        self.stdout.write(f"Total MCQs imported: {imported_count}")
        self.stdout.write(f"Total errors: {len(errors)}")
        
        if errors:
            self.stdout.write(self.style.ERROR("\nErrors encountered:"))
            for error in errors[:10]:  # Show first 10 errors
                self.stdout.write(f"- {error}")
            if len(errors) > 10:
                self.stdout.write(f"... and {len(errors) - 10} more errors")
        
        # Final count verification
        final_count = MCQ.objects.count()
        self.stdout.write(f"\nFinal MCQ count in database: {final_count}")