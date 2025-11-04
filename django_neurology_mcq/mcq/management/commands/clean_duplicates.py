from django.core.management.base import BaseCommand
from django.db.models import Count, Min
from mcq.models import MCQ
import json

class Command(BaseCommand):
    help = 'Clean duplicate MCQs from database, keeping the best version'

    def handle(self, *args, **options):
        self.stdout.write("=== Cleaning Duplicate MCQs ===\n")
        
        # Find duplicate questions
        duplicates = MCQ.objects.values('question_text').annotate(
            count=Count('id'),
            min_id=Min('id')
        ).filter(count__gt=1).order_by('-count')
        
        total_duplicates = sum(d['count'] - 1 for d in duplicates)
        self.stdout.write(f"Found {len(duplicates)} questions with duplicates")
        self.stdout.write(f"Total duplicate entries to remove: {total_duplicates}")
        
        # Analyze duplicates before removing
        self.stdout.write("\n=== Analyzing Duplicates ===")
        removal_count = 0
        
        for dup_info in duplicates[:10]:  # Show first 10
            question_text = dup_info['question_text']
            mcqs = MCQ.objects.filter(question_text=question_text).order_by('id')
            
            self.stdout.write(f"\nQuestion with {dup_info['count']} copies:")
            self.stdout.write(f"  {question_text[:100]}...")
            
            # Keep the one with most complete data
            best_mcq = None
            best_score = -1
            
            for mcq in mcqs:
                score = 0
                if mcq.explanation_sections:
                    score += len(mcq.explanation_sections)
                if mcq.explanation:
                    score += 1
                if mcq.correct_answer:
                    score += 1
                if mcq.subspecialty and mcq.subspecialty != 'Other/Unclassified':
                    score += 2
                if mcq.exam_type:
                    score += 1
                if mcq.exam_year:
                    score += 1
                
                if score > best_score:
                    best_score = score
                    best_mcq = mcq
            
            # Remove all except the best one
            to_remove = []
            for mcq in mcqs:
                if mcq.id != best_mcq.id:
                    to_remove.append(mcq.id)
            
            self.stdout.write(f"  Keeping MCQ ID {best_mcq.id} (score: {best_score})")
            self.stdout.write(f"  Removing {len(to_remove)} duplicates")
        
        # Ask for confirmation
        self.stdout.write(f"\nThis will remove {total_duplicates} duplicate MCQs.")
        response = input("Continue? (yes/no): ")
        
        if response.lower() == 'yes':
            # Remove duplicates
            removed_count = 0
            
            for dup_info in duplicates:
                question_text = dup_info['question_text']
                mcqs = MCQ.objects.filter(question_text=question_text).order_by('id')
                
                # Keep the one with most complete data
                best_mcq = None
                best_score = -1
                
                for mcq in mcqs:
                    score = 0
                    if mcq.explanation_sections:
                        score += len(mcq.explanation_sections)
                    if mcq.explanation:
                        score += 1
                    if mcq.correct_answer:
                        score += 1
                    if mcq.subspecialty and mcq.subspecialty != 'Other/Unclassified':
                        score += 2
                    if mcq.exam_type:
                        score += 1
                    if mcq.exam_year:
                        score += 1
                    
                    if score > best_score:
                        best_score = score
                        best_mcq = mcq
                
                # Remove all except the best one
                for mcq in mcqs:
                    if mcq.id != best_mcq.id:
                        mcq.delete()
                        removed_count += 1
                        
                if removed_count % 50 == 0:
                    self.stdout.write(f"Progress: {removed_count}/{total_duplicates} removed...")
            
            self.stdout.write(self.style.SUCCESS(f"\nSuccessfully removed {removed_count} duplicate MCQs"))
            
            # Final count
            final_count = MCQ.objects.count()
            self.stdout.write(f"\nFinal MCQ count in database: {final_count}")
            
            # Verify no duplicates remain
            remaining_dups = MCQ.objects.values('question_text').annotate(
                count=Count('id')
            ).filter(count__gt=1).count()
            
            if remaining_dups == 0:
                self.stdout.write(self.style.SUCCESS("✓ No duplicates remaining"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠ {remaining_dups} duplicates still remain"))
        else:
            self.stdout.write("Cleanup cancelled.")