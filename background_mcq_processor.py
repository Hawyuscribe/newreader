#!/usr/bin/env python3
"""
Background MCQ Processor with Pause/Resume Functionality
Processes all MCQs in the background with ability to pause and resume.
"""

import json
import os
import sys
import signal
import time
from pathlib import Path
from datetime import datetime
import threading
from queue import Queue
import logging
import traceback
from typing import Dict, List, Any

# Ensure OpenAI API key is available from the environment
if not os.environ.get("OPENAI_API_KEY") and not os.environ.get("OPENAI_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY environment variable must be set before running the background processor."
    )

from mcq_processor import MCQProcessor

# Set up comprehensive logging
class DetailedFormatter(logging.Formatter):
    """Enhanced formatter with more context."""
    def format(self, record):
        # Add thread info and extra context
        if hasattr(record, 'mcq_id'):
            record.msg = f"[MCQ {record.mcq_id}] {record.msg}"
        if hasattr(record, 'file_name'):
            record.msg = f"[{record.file_name}] {record.msg}"
        return super().format(record)

# Set up multiple log files for different purposes
log_formatter = DetailedFormatter('%(asctime)s - %(levelname)s - %(message)s')

# Main processing log
main_handler = logging.FileHandler('background_processing.log')
main_handler.setFormatter(log_formatter)

# Error-specific log
error_handler = logging.FileHandler('processing_errors.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(log_formatter)

# Success log
success_handler = logging.FileHandler('processing_success.log')
success_handler.setLevel(logging.INFO)
success_handler.setFormatter(log_formatter)

# Console output
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

# Configure main logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(main_handler)
logger.addHandler(error_handler)
logger.addHandler(success_handler)
logger.addHandler(console_handler)

# Create separate loggers for different components
error_logger = logging.getLogger('errors')
error_logger.setLevel(logging.ERROR)
error_logger.addHandler(error_handler)

success_logger = logging.getLogger('success')
success_logger.setLevel(logging.INFO)
success_logger.addHandler(success_handler)


class BackgroundMCQProcessor:
    """Background MCQ processor with pause/resume functionality."""
    
    def __init__(self, input_dir: str):
        self.input_dir = Path(input_dir)
        self.processor = None
        self.is_paused = False
        self.is_stopped = False
        self.current_file = None
        self.progress = {
            'total_files': 0,
            'processed_files': 0,
            'total_mcqs': 0,
            'processed_mcqs': 0,
            'corrected_mcqs': 0,
            'verified_mcqs': 0,
            'failed_mcqs': 0,
            'current_file': '',
            'start_time': None,
            'estimated_remaining': 'Calculating...'
        }
        
        # Enhanced error tracking
        self.failed_mcqs = []  # List of failed MCQs with details
        self.error_summary = {
            'api_errors': 0,
            'parsing_errors': 0,
            'file_errors': 0,
            'timeout_errors': 0,
            'unknown_errors': 0
        }
        
        # Progress and error save files
        self.progress_file = Path('background_processing_progress.json')
        self.failed_mcqs_file = Path('failed_mcqs.json')
        self.error_summary_file = Path('error_summary.json')
        
        self.load_progress()
        self.load_failed_mcqs()
        
        # Set up signal handlers for pause/resume
        signal.signal(signal.SIGUSR1, self.pause_handler)  # kill -USR1 <pid> to pause
        signal.signal(signal.SIGUSR2, self.resume_handler)  # kill -USR2 <pid> to resume
        signal.signal(signal.SIGTERM, self.stop_handler)   # kill <pid> to stop gracefully
        signal.signal(signal.SIGINT, self.stop_handler)    # Ctrl+C to stop
    
    def save_progress(self):
        """Save current progress to file."""
        try:
            with open(self.progress_file, 'w') as f:
                json.dump(self.progress, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Failed to save progress: {e}")
    
    def load_progress(self):
        """Load previous progress if available."""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    saved_progress = json.load(f)
                    self.progress.update(saved_progress)
                logger.info("Loaded previous progress")
            except Exception as e:
                logger.error(f"Failed to load progress: {e}")
    
    def save_failed_mcqs(self):
        """Save failed MCQs to file for reprocessing."""
        try:
            with open(self.failed_mcqs_file, 'w') as f:
                json.dump(self.failed_mcqs, f, indent=2, default=str)
            
            with open(self.error_summary_file, 'w') as f:
                json.dump(self.error_summary, f, indent=2)
                
        except Exception as e:
            logger.error(f"Failed to save failed MCQs: {e}")
    
    def load_failed_mcqs(self):
        """Load previously failed MCQs if available."""
        if self.failed_mcqs_file.exists():
            try:
                with open(self.failed_mcqs_file, 'r') as f:
                    self.failed_mcqs = json.load(f)
                logger.info(f"Loaded {len(self.failed_mcqs)} previously failed MCQs")
            except Exception as e:
                logger.error(f"Failed to load failed MCQs: {e}")
        
        if self.error_summary_file.exists():
            try:
                with open(self.error_summary_file, 'r') as f:
                    self.error_summary.update(json.load(f))
            except Exception as e:
                logger.error(f"Failed to load error summary: {e}")
    
    def categorize_error(self, error: Exception) -> str:
        """Categorize error type for tracking."""
        error_str = str(error).lower()
        error_type = type(error).__name__
        
        if 'api' in error_str or 'openai' in error_str or 'rate limit' in error_str:
            return 'api_errors'
        elif 'timeout' in error_str or 'timed out' in error_str:
            return 'timeout_errors'
        elif 'json' in error_str or 'parse' in error_str or 'parsing' in error_str:
            return 'parsing_errors'
        elif 'file' in error_str or 'permission' in error_str or 'io' in error_str:
            return 'file_errors'
        else:
            return 'unknown_errors'
    
    def log_mcq_failure(self, file_name: str, mcq_index: int, mcq: Dict[str, Any], error: Exception):
        """Log detailed information about failed MCQ."""
        error_category = self.categorize_error(error)
        self.error_summary[error_category] += 1
        self.progress['failed_mcqs'] += 1
        
        # Create detailed error record
        failure_record = {
            'timestamp': datetime.now().isoformat(),
            'file_name': file_name,
            'mcq_index': mcq_index,
            'mcq_id': f"{file_name}_{mcq_index}",
            'question_preview': mcq.get('question', '')[:100] + '...' if mcq.get('question', '') else 'No question',
            'error_type': error_category,
            'error_class': type(error).__name__,
            'error_message': str(error),
            'full_traceback': traceback.format_exc(),
            'mcq_data': mcq,  # Full MCQ for reprocessing
            'retry_count': 0
        }
        
        self.failed_mcqs.append(failure_record)
        
        # Log with enhanced context
        error_logger.error(
            f"MCQ PROCESSING FAILED",
            extra={
                'file_name': file_name,
                'mcq_id': f"{file_name}_{mcq_index}"
            }
        )
        
        error_logger.error(
            f"Question: {failure_record['question_preview']}"
        )
        error_logger.error(
            f"Error Type: {error_category} ({type(error).__name__})"
        )
        error_logger.error(
            f"Error Message: {str(error)}"
        )
        error_logger.error(
            f"Full Traceback:\n{traceback.format_exc()}"
        )
        
        # Save failed MCQs immediately
        self.save_failed_mcqs()
    
    def log_mcq_success(self, file_name: str, mcq_index: int, mcq: Dict[str, Any], was_corrected: bool):
        """Log successful MCQ processing."""
        success_logger.info(
            f"MCQ PROCESSED SUCCESSFULLY - {'CORRECTED' if was_corrected else 'VERIFIED'}",
            extra={
                'file_name': file_name,
                'mcq_id': f"{file_name}_{mcq_index}"
            }
        )
        
        if was_corrected:
            success_logger.info(
                f"Correction: {mcq.get('correction_details', 'No details available')}"
            )
    
    def pause_handler(self, signum, frame):
        """Handle pause signal."""
        self.is_paused = True
        logger.info("🟡 PROCESSING PAUSED - Send SIGUSR2 to resume or SIGTERM to stop")
    
    def resume_handler(self, signum, frame):
        """Handle resume signal."""
        self.is_paused = False
        logger.info("🟢 PROCESSING RESUMED")
    
    def stop_handler(self, signum, frame):
        """Handle stop signal."""
        self.is_stopped = True
        logger.info("🔴 STOPPING PROCESSING - Finishing current MCQ...")
    
    def get_all_files(self):
        """Get all MCQ files to process."""
        return list(self.input_dir.glob("*.json"))
    
    def count_total_mcqs(self, files):
        """Count total MCQs across all files."""
        total = 0
        for file in files:
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    total += len(data.get('mcqs', []))
            except Exception as e:
                logger.error(f"Error counting MCQs in {file}: {e}")
        return total
    
    def wait_while_paused(self):
        """Wait while processing is paused."""
        while self.is_paused and not self.is_stopped:
            time.sleep(1)
    
    def process_single_file(self, file_path: Path):
        """Process a single file with pause checks."""
        self.current_file = file_path.name
        self.progress['current_file'] = file_path.name
        
        logger.info(f"📁 Processing file: {file_path.name}")
        
        # Load file to count MCQs
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            file_mcqs = data.get('mcqs', [])
            file_total = len(file_mcqs)
        except Exception as e:
            logger.error(f"Error loading {file_path}: {e}")
            return
        
        # Process each MCQ individually with pause checks
        corrected_in_file = 0
        verified_in_file = 0
        
        for i, mcq in enumerate(file_mcqs):
            # Check for pause/stop
            self.wait_while_paused()
            if self.is_stopped:
                logger.info(f"Stopping at MCQ {i+1}/{file_total} in {file_path.name}")
                break
            
            try:
                # Log attempt
                logger.debug(f"Processing MCQ {i+1}/{file_total}: {mcq.get('question', 'No question')[:50]}...")
                
                # Process single MCQ
                original_mcq = json.loads(json.dumps(mcq))
                processed_mcq, was_corrected = self.processor.process_single_mcq(mcq, i, file_path.name)
                
                # Update MCQ in data
                file_mcqs[i] = processed_mcq
                
                # Log success
                self.log_mcq_success(file_path.name, i, processed_mcq, was_corrected)
                
                # Update counters
                if was_corrected:
                    corrected_in_file += 1
                    self.progress['corrected_mcqs'] += 1
                else:
                    verified_in_file += 1
                    self.progress['verified_mcqs'] += 1
                
                self.progress['processed_mcqs'] += 1
                
                # Log progress every 10 MCQs
                if (i + 1) % 10 == 0:
                    logger.info(f"  📊 Progress: {i+1}/{file_total} MCQs in {file_path.name}")
                
                # Save progress every 25 MCQs
                if (i + 1) % 25 == 0:
                    self.save_progress()
                
            except Exception as e:
                # Comprehensive error logging
                self.log_mcq_failure(file_path.name, i, mcq, e)
                
                # Keep original MCQ in case of failure
                file_mcqs[i] = original_mcq
                
                logger.error(f"❌ Failed MCQ {i+1}/{file_total} in {file_path.name}")
                continue
        
        # Save updated file if not stopped
        if not self.is_stopped:
            try:
                # Update file metadata
                data['mcqs'] = file_mcqs
                data['processing_info'] = {
                    'processed_date': datetime.now().isoformat(),
                    'total_mcqs': file_total,
                    'verified_mcqs': verified_in_file,
                    'corrected_mcqs': corrected_in_file,
                    'processor': 'O3-mini-high-reasoning-background',
                    'note': 'Files updated in place via background processing'
                }
                
                # Save back to original file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                
                logger.info(f"✅ Completed {file_path.name}: {verified_in_file} verified, {corrected_in_file} corrected")
                
            except Exception as e:
                logger.error(f"Error saving {file_path}: {e}")
        
        self.progress['processed_files'] += 1
        self.save_progress()
    
    def calculate_eta(self):
        """Calculate estimated time remaining."""
        if not self.progress['start_time'] or self.progress['processed_mcqs'] == 0:
            return "Calculating..."
        
        start_time = datetime.fromisoformat(self.progress['start_time'])
        elapsed = (datetime.now() - start_time).total_seconds()
        
        rate = self.progress['processed_mcqs'] / elapsed  # MCQs per second
        remaining_mcqs = self.progress['total_mcqs'] - self.progress['processed_mcqs']
        
        if rate > 0:
            eta_seconds = remaining_mcqs / rate
            eta_hours = eta_seconds / 3600
            
            if eta_hours < 1:
                return f"{eta_seconds/60:.1f} minutes"
            else:
                return f"{eta_hours:.1f} hours"
        
        return "Unknown"
    
    def print_status(self):
        """Print current processing status."""
        eta = self.calculate_eta()
        self.progress['estimated_remaining'] = eta
        
        # Calculate success rate
        total_attempted = self.progress['processed_mcqs'] + self.progress['failed_mcqs']
        success_rate = (self.progress['processed_mcqs'] / max(total_attempted, 1)) * 100
        
        print(f"""
📊 BACKGROUND MCQ PROCESSING STATUS
{'='*60}
Current File: {self.progress['current_file']}
Files: {self.progress['processed_files']}/{self.progress['total_files']}
MCQs: {self.progress['processed_mcqs']}/{self.progress['total_mcqs']}
├─ Verified: {self.progress['verified_mcqs']}
├─ Corrected: {self.progress['corrected_mcqs']}
└─ Failed: {self.progress['failed_mcqs']}

Success Rate: {success_rate:.1f}%
ETA: {eta}
Status: {'⏸️  PAUSED' if self.is_paused else '🔄 PROCESSING'}

ERROR BREAKDOWN:
├─ API Errors: {self.error_summary['api_errors']}
├─ Parsing Errors: {self.error_summary['parsing_errors']}
├─ Timeout Errors: {self.error_summary['timeout_errors']}
├─ File Errors: {self.error_summary['file_errors']}
└─ Unknown Errors: {self.error_summary['unknown_errors']}

FILES GENERATED:
├─ background_processing.log (All activity)
├─ processing_errors.log (Errors only)
├─ processing_success.log (Successes only)
├─ failed_mcqs.json (Failed MCQs for retry)
└─ error_summary.json (Error statistics)

COMMANDS:
  kill -USR1 {os.getpid()}  # Pause
  kill -USR2 {os.getpid()}  # Resume  
  kill {os.getpid()}        # Stop gracefully
  tail -f processing_errors.log  # View errors
""")
    
    def run(self):
        """Run the background processing."""
        logger.info("🚀 Starting background MCQ processing")
        
        # Initialize processor
        self.processor = MCQProcessor(
            api_key=os.environ['OPENAI_API_KEY'],
            input_dir=str(self.input_dir)
        )
        
        # Get all files
        files = self.get_all_files()
        if not files:
            logger.error("No JSON files found in directory")
            return
        
        # Initialize progress
        if not self.progress['start_time']:
            self.progress['start_time'] = datetime.now().isoformat()
            self.progress['total_files'] = len(files)
            self.progress['total_mcqs'] = self.count_total_mcqs(files)
        
        logger.info(f"📈 Found {len(files)} files with {self.progress['total_mcqs']} total MCQs")
        self.save_progress()
        
        # Print initial status
        self.print_status()
        
        # Process each file
        try:
            for file_path in files:
                if self.is_stopped:
                    break
                
                self.wait_while_paused()
                if self.is_stopped:
                    break
                
                self.process_single_file(file_path)
                
                # Print status after each file
                self.print_status()
            
            if not self.is_stopped:
                logger.info("🎉 ALL MCQ PROCESSING COMPLETED!")
                self.print_final_summary()
            else:
                logger.info("🛑 Processing stopped by user")
                
        except Exception as e:
            logger.error(f"Fatal error during processing: {e}")
            import traceback
            traceback.print_exc()
        
        finally:
            self.save_progress()
    
    def print_final_summary(self):
        """Print final processing summary."""
        start_time = datetime.fromisoformat(self.progress['start_time'])
        total_time = datetime.now() - start_time
        
        total_attempted = self.progress['processed_mcqs'] + self.progress['failed_mcqs']
        success_rate = (self.progress['processed_mcqs'] / max(total_attempted, 1)) * 100
        
        print(f"""
🎉 PROCESSING COMPLETE!
{'='*60}
Total Files: {self.progress['total_files']}
Total MCQs: {self.progress['total_mcqs']}
├─ Successfully Processed: {self.progress['processed_mcqs']}
│  ├─ Verified (no changes): {self.progress['verified_mcqs']}
│  └─ Corrected: {self.progress['corrected_mcqs']}
└─ Failed: {self.progress['failed_mcqs']}

Success Rate: {success_rate:.1f}%
Total Processing Time: {total_time}
Average per Successful MCQ: {total_time.total_seconds()/max(self.progress['processed_mcqs'], 1):.1f} seconds

ERROR BREAKDOWN:
├─ API Errors: {self.error_summary['api_errors']}
├─ Parsing Errors: {self.error_summary['parsing_errors']}
├─ Timeout Errors: {self.error_summary['timeout_errors']}
├─ File Errors: {self.error_summary['file_errors']}
└─ Unknown Errors: {self.error_summary['unknown_errors']}

📁 FILES GENERATED:
├─ background_processing.log (Complete activity log)
├─ processing_errors.log (Errors only)
├─ processing_success.log (Successes only)
├─ failed_mcqs.json (Failed MCQs with full details)
├─ error_summary.json (Error statistics)
└─ background_processing_progress.json (Final progress)

🔄 NEXT STEPS:
To reprocess failed MCQs:
  python reprocess_failed_mcqs.py analyze    # Analyze failures
  python reprocess_failed_mcqs.py all        # Retry all failed MCQs

All successfully processed files have been updated in place.
""")


def main():
    """Main entry point."""
    input_dir = "/Users/tariqalmatrudi/Documents/FFF/output_by_specialty"
    
    if not Path(input_dir).exists():
        print(f"Error: Directory {input_dir} does not exist")
        sys.exit(1)
    
    print(f"Starting background MCQ processing...")
    print(f"Process ID: {os.getpid()}")
    print(f"Log file: background_processing.log")
    print(f"Progress file: background_processing_progress.json")
    print()
    
    processor = BackgroundMCQProcessor(input_dir)
    processor.run()


if __name__ == "__main__":
    main()
