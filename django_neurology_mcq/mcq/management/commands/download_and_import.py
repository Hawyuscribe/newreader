import os
import sys
import gzip
import json
import shutil
import tempfile
import urllib.request
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Download explanations from a URL and import them'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL to download explanations from')
        parser.add_argument('--batch-size', type=int, default=50, 
                           help='Number of MCQs to process in each batch')
        parser.add_argument('--sleep', type=int, default=2, 
                           help='Seconds to sleep between batches')
        parser.add_argument('--dry-run', action='store_true', 
                           help='Download file but don\'t import')

    def handle(self, *args, **options):
        url = options['url']
        batch_size = options['batch_size']
        sleep_time = options['sleep']
        dry_run = options['dry_run']
        
        # Create directories
        os.makedirs('fixtures', exist_ok=True)
        os.makedirs('logs', exist_ok=True)
        
        # Create timestamp for filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_log = f"logs/download_{timestamp}.log"
        
        with open(download_log, 'w') as log:
            log.write(f"Download started at {datetime.now()}\n")
            log.write(f"URL: {url}\n")
        
        # Download file to temporary location
        self.stdout.write(f"Downloading from {url}...")
        
        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_path = temp_file.name
                
                with urllib.request.urlopen(url) as response:
                    # Check if file is gzipped
                    is_gzipped = url.endswith('.gz')
                    
                    if is_gzipped:
                        # Download gzipped file directly
                        shutil.copyfileobj(response, temp_file)
                    else:
                        # Download regular file
                        shutil.copyfileobj(response, temp_file)
            
            self.stdout.write(f"Download complete, saved to {temp_path}")
            
            # Process the downloaded file
            target_path = f"fixtures/explanations_{timestamp}.json"
            
            if is_gzipped:
                self.stdout.write("Unzipping file...")
                # Unzip the file
                with gzip.open(temp_path, 'rb') as f_in:
                    with open(target_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                self.stdout.write(f"File unzipped to {target_path}")
            else:
                # Just copy the file
                shutil.copy(temp_path, target_path)
                self.stdout.write(f"File saved to {target_path}")
            
            # Clean up the temporary file
            os.unlink(temp_path)
            
            # Log the download info
            with open(download_log, 'a') as log:
                log.write(f"Download completed at {datetime.now()}\n")
                log.write(f"Target file: {target_path}\n")
            
            # Check if the file is valid JSON
            try:
                with open(target_path, 'r') as f:
                    data = json.load(f)
                self.stdout.write(f"File is valid JSON with {len(data)} items")
                with open(download_log, 'a') as log:
                    log.write(f"File contains {len(data)} items\n")
            except json.JSONDecodeError as e:
                self.stderr.write(self.style.ERROR(f"Invalid JSON file: {e}"))
                with open(download_log, 'a') as log:
                    log.write(f"Invalid JSON file: {e}\n")
                return
            
            # Import the explanations if not dry run
            if not dry_run:
                self.stdout.write("Starting import process...")
                
                with open(download_log, 'a') as log:
                    log.write(f"Import started at {datetime.now()}\n")
                
                # Call the import_explanations command
                call_command('import_explanations', 
                             target_path, 
                             batch_size=batch_size,
                             sleep=sleep_time)
                
                with open(download_log, 'a') as log:
                    log.write(f"Import completed at {datetime.now()}\n")
            else:
                self.stdout.write(self.style.WARNING(
                    "Dry run mode - file downloaded but import skipped"))
                with open(download_log, 'a') as log:
                    log.write("Dry run mode - import skipped\n")
            
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {str(e)}"))
            with open(download_log, 'a') as log:
                log.write(f"Error: {str(e)}\n")
            raise CommandError(f"Failed to download and import explanations: {str(e)}")