from django.core.management.base import BaseCommand
from mcq.models import MCQ
import requests
from django.db.models import Q

class Command(BaseCommand):
    help = 'Test all MCQ image URLs and identify problematic ones'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--fix-google-drive',
            action='store_true',
            help='Clear Google Drive URLs (they don\'t work for embedding)',
        )
    
    def handle(self, *args, **options):
        mcqs_with_images = MCQ.objects.exclude(Q(image_url='') | Q(image_url__isnull=True))
        
        self.stdout.write(f"Found {mcqs_with_images.count()} MCQs with image URLs")
        
        google_drive_count = 0
        working_count = 0
        problematic_count = 0
        
        for mcq in mcqs_with_images:
            url = mcq.image_url
            
            # Check for Google Drive URLs
            if 'drive.google.com' in url or 'drive.usercontent.google.com' in url:
                google_drive_count += 1
                self.stdout.write(self.style.ERROR(
                    f"MCQ {mcq.id} ({mcq.question_number}): Google Drive URL (won't work)"
                ))
                
                if options['fix_google_drive']:
                    mcq.image_url = ''
                    mcq.save()
                    self.stdout.write(self.style.SUCCESS(f"  - Cleared URL"))
                continue
            
            # Test the URL
            try:
                response = requests.head(url, timeout=5, allow_redirects=True)
                final_url = response.url
                content_type = response.headers.get('content-type', '')
                
                if response.status_code == 200 and 'image' in content_type:
                    working_count += 1
                    self.stdout.write(self.style.SUCCESS(
                        f"MCQ {mcq.id} ({mcq.question_number}): Working image URL"
                    ))
                else:
                    problematic_count += 1
                    self.stdout.write(self.style.WARNING(
                        f"MCQ {mcq.id} ({mcq.question_number}): Status {response.status_code}, Type: {content_type}"
                    ))
                    
                # Check if URL is actually an image file
                if not any(final_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']):
                    self.stdout.write(self.style.WARNING(
                        f"  - URL doesn't end with image extension: {final_url}"
                    ))
                    
            except Exception as e:
                problematic_count += 1
                self.stdout.write(self.style.ERROR(
                    f"MCQ {mcq.id} ({mcq.question_number}): Error - {str(e)}"
                ))
        
        self.stdout.write("\n" + "="*50)
        self.stdout.write(self.style.SUCCESS(f"Working URLs: {working_count}"))
        self.stdout.write(self.style.ERROR(f"Google Drive URLs: {google_drive_count}"))
        self.stdout.write(self.style.WARNING(f"Other problematic URLs: {problematic_count}"))
        
        if google_drive_count > 0 and not options['fix_google_drive']:
            self.stdout.write("\nTo clear Google Drive URLs, run:")
            self.stdout.write("python manage.py test_image_urls --fix-google-drive")