#!/usr/bin/env python3
"""
Monitor Background MCQ Processing
Displays real-time status and allows easy control.
"""

import json
import os
import signal
import time
from pathlib import Path
from datetime import datetime


class ProcessingMonitor:
    """Monitor background processing status."""
    
    def __init__(self):
        self.progress_file = Path('background_processing_progress.json')
        self.failed_mcqs_file = Path('failed_mcqs.json')
        self.error_summary_file = Path('error_summary.json')
    
    def get_processor_pid(self):
        """Find the background processor PID."""
        try:
            import psutil
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if proc.info['cmdline'] and 'background_mcq_processor.py' in ' '.join(proc.info['cmdline']):
                    return proc.info['pid']
        except ImportError:
            # Fallback - check for common PID patterns
            pass
        return None
    
    def load_progress(self):
        """Load current progress."""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}
    
    def load_error_summary(self):
        """Load error summary."""
        if self.error_summary_file.exists():
            try:
                with open(self.error_summary_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}
    
    def get_failed_count(self):
        """Get count of failed MCQs."""
        if self.failed_mcqs_file.exists():
            try:
                with open(self.failed_mcqs_file, 'r') as f:
                    failed = json.load(f)
                    return len(failed)
            except:
                pass
        return 0
    
    def display_status(self):
        """Display current status."""
        progress = self.load_progress()
        error_summary = self.load_error_summary()
        failed_count = self.get_failed_count()
        pid = self.get_processor_pid()
        
        if not progress:
            print("❌ No processing progress found. Make sure background processor is running.")
            return
        
        # Calculate rates and ETA
        total_attempted = progress.get('processed_mcqs', 0) + failed_count
        success_rate = (progress.get('processed_mcqs', 0) / max(total_attempted, 1)) * 100
        
        # Calculate processing rate
        if progress.get('start_time'):
            start_time = datetime.fromisoformat(progress['start_time'])
            elapsed = (datetime.now() - start_time).total_seconds()
            rate = progress.get('processed_mcqs', 0) / max(elapsed, 1)
            rate_per_hour = rate * 3600
        else:
            rate_per_hour = 0
        
        print(f"""
🔄 MCQ BACKGROUND PROCESSING MONITOR
{'='*60}
Process ID: {pid if pid else 'Not found'}
Current File: {progress.get('current_file', 'Unknown')}
Status: {'🟢 RUNNING' if pid else '🔴 STOPPED'}

PROGRESS:
├─ Files: {progress.get('processed_files', 0)}/{progress.get('total_files', 0)}
├─ MCQs: {progress.get('processed_mcqs', 0)}/{progress.get('total_mcqs', 0)}
│  ├─ Verified: {progress.get('verified_mcqs', 0)}
│  ├─ Corrected: {progress.get('corrected_mcqs', 0)}
│  └─ Failed: {failed_count}
├─ Success Rate: {success_rate:.1f}%
├─ Rate: {rate_per_hour:.1f} MCQs/hour
└─ ETA: {progress.get('estimated_remaining', 'Calculating...')}

ERROR BREAKDOWN:
├─ API Errors: {error_summary.get('api_errors', 0)}
├─ Parsing Errors: {error_summary.get('parsing_errors', 0)}
├─ Timeout Errors: {error_summary.get('timeout_errors', 0)}
├─ File Errors: {error_summary.get('file_errors', 0)}
└─ Unknown Errors: {error_summary.get('unknown_errors', 0)}

RECENT ACTIVITY:
""")
        
        # Show last few lines of log
        try:
            with open('background_processing.log', 'r') as f:
                lines = f.readlines()
                for line in lines[-5:]:
                    print(f"  {line.strip()}")
        except:
            print("  No recent activity logged")
        
        if pid:
            print(f"""
CONTROL COMMANDS:
├─ Pause:  kill -USR1 {pid}
├─ Resume: kill -USR2 {pid}
├─ Stop:   kill {pid}
└─ Monitor: python monitor_processing.py watch
""")
        else:
            print("""
CONTROL COMMANDS:
└─ Start: python background_mcq_processor.py
""")
    
    def watch_processing(self):
        """Watch processing in real-time."""
        print("🔍 Watching processing in real-time (Ctrl+C to exit)...")
        print("Refreshing every 30 seconds...\n")
        
        try:
            while True:
                os.system('clear')  # Clear screen
                self.display_status()
                time.sleep(30)
        except KeyboardInterrupt:
            print("\n👋 Monitoring stopped")
    
    def pause_processing(self):
        """Pause background processing."""
        pid = self.get_processor_pid()
        if pid:
            os.kill(pid, signal.SIGUSR1)
            print(f"⏸️  Paused processing (PID: {pid})")
        else:
            print("❌ No background processor found")
    
    def resume_processing(self):
        """Resume background processing."""
        pid = self.get_processor_pid()
        if pid:
            os.kill(pid, signal.SIGUSR2)
            print(f"▶️  Resumed processing (PID: {pid})")
        else:
            print("❌ No background processor found")
    
    def stop_processing(self):
        """Stop background processing."""
        pid = self.get_processor_pid()
        if pid:
            os.kill(pid, signal.SIGTERM)
            print(f"🛑 Stopped processing (PID: {pid})")
        else:
            print("❌ No background processor found")


def main():
    """Main entry point."""
    monitor = ProcessingMonitor()
    
    if len(os.sys.argv) > 1:
        command = os.sys.argv[1]
        
        if command == 'watch':
            monitor.watch_processing()
        elif command == 'pause':
            monitor.pause_processing()
        elif command == 'resume':
            monitor.resume_processing()
        elif command == 'stop':
            monitor.stop_processing()
        else:
            print("""
Usage:
  python monitor_processing.py           # Show current status
  python monitor_processing.py watch     # Watch in real-time
  python monitor_processing.py pause     # Pause processing
  python monitor_processing.py resume    # Resume processing
  python monitor_processing.py stop      # Stop processing
""")
    else:
        monitor.display_status()


if __name__ == "__main__":
    main()