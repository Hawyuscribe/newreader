import requests
import json
import time
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Upload MCQs to Heroku via the web import endpoint'

    def handle(self, *args, **options):
        # Load local MCQs
        import os
        json_path = '/Users/tariqalmatrudi/NEWreader/consolidated_all_mcqs.json'
        
        if not os.path.exists(json_path):
            self.stdout.write(self.style.ERROR(f'Could not find {json_path}'))
            return
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        mcqs = data['mcqs']
        self.stdout.write(f'Found {len(mcqs)} MCQs to upload')
        
        # Heroku app URL
        heroku_url = 'https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com'
        
        # Clear existing MCQs first
        self.stdout.write('Clearing existing MCQs on Heroku...')
        try:
            response = requests.post(f'{heroku_url}/admin/clear-mcqs/', timeout=30)
            if response.status_code == 200:
                self.stdout.write(self.style.SUCCESS('MCQs cleared successfully'))
            else:
                self.stdout.write(self.style.WARNING(f'Clear request returned {response.status_code}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error clearing MCQs: {e}'))
        
        # Upload MCQs in batches
        batch_size = 50
        total_batches = (len(mcqs) + batch_size - 1) // batch_size
        
        for batch_num in range(total_batches):
            start_idx = batch_num * batch_size
            end_idx = min(start_idx + batch_size, len(mcqs))
            batch_mcqs = mcqs[start_idx:end_idx]
            
            self.stdout.write(f'Uploading batch {batch_num + 1}/{total_batches} (MCQs {start_idx + 1}-{end_idx})')
            
            # Prepare batch data
            batch_data = {
                'mcqs': batch_mcqs,
                'batch_info': {
                    'batch_number': batch_num + 1,
                    'total_batches': total_batches,
                    'batch_size': len(batch_mcqs)
                }
            }
            
            try:
                response = requests.post(
                    f'{heroku_url}/admin/import-mcqs-batch/',
                    json=batch_data,
                    headers={'Content-Type': 'application/json'},
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    self.stdout.write(f'  ✅ Uploaded {result.get("imported", 0)} MCQs')
                else:
                    self.stdout.write(self.style.ERROR(f'  ❌ Batch failed: {response.status_code}'))
                    
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'  ❌ Error uploading batch: {e}'))
            
            # Brief pause between batches
            time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Upload complete!'))