"""
Upload exported files to a temporary file sharing service
"""
import os
import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Upload exported files to file.io for easy download'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='File to upload')

    def handle(self, *args, **options):
        filename = options['filename']
        
        if not os.path.exists(filename):
            self.stdout.write(self.style.ERROR(f"File {filename} not found"))
            return
        
        try:
            # Upload to file.io - free temporary file hosting
            with open(filename, 'rb') as f:
                response = requests.post('https://file.io', files={'file': f})
                
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    download_url = data.get('link')
                    self.stdout.write(self.style.SUCCESS(f"File uploaded successfully!"))
                    self.stdout.write(f"Download URL: {download_url}")
                    self.stdout.write(f"This link will expire after one download")
                else:
                    self.stdout.write(self.style.ERROR("Upload failed"))
            else:
                self.stdout.write(self.style.ERROR(f"Upload failed with status {response.status_code}"))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error uploading file: {str(e)}"))