#!/usr/bin/env python3
"""
MCQ Processor GUI
A graphical interface for monitoring MCQ processing with O3-mini.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import queue
import json
import os
import sys
from datetime import datetime
from pathlib import Path
import time

# Import the processor
from mcq_processor import MCQProcessor


class MCQProcessorGUI:
    """GUI for MCQ processing monitoring."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Processor - O3-mini High Reasoning Mode")
        self.root.geometry("1200x800")
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        
        # Variables
        self.api_key_var = tk.StringVar(value=os.getenv('OPENAI_API_KEY', ''))
        self.input_dir_var = tk.StringVar(value="/Users/tariqalmatrudi/Documents/FFF/output_by_specialty")
        self.is_processing = False
        self.processor = None
        self.processing_thread = None
        
        # Progress tracking
        self.file_progress = {}
        self.overall_stats = {
            'total_files': 0,
            'processed_files': 0,
            'total_mcqs': 0,
            'processed_mcqs': 0,
            'corrected_mcqs': 0,
            'failed_mcqs': 0
        }
        
        self.setup_ui()
        
        # Start progress monitor
        self.monitor_progress()
    
    def setup_ui(self):
        """Set up the user interface."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Header
        header_label = ttk.Label(main_frame, text="MCQ Processor with O3-mini", 
                                font=('Arial', 18, 'bold'))
        header_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Configuration Section
        config_frame = ttk.LabelFrame(main_frame, text="Configuration", padding="10")
        config_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        config_frame.columnconfigure(1, weight=1)
        
        # API Key
        ttk.Label(config_frame, text="OpenAI API Key:").grid(row=0, column=0, sticky=tk.W, pady=5)
        api_key_entry = ttk.Entry(config_frame, textvariable=self.api_key_var, show="*")
        api_key_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Input Directory (files will be modified in place)
        ttk.Label(config_frame, text="MCQ Directory:").grid(row=1, column=0, sticky=tk.W, pady=5)
        input_frame = ttk.Frame(config_frame)
        input_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        input_frame.columnconfigure(0, weight=1)
        
        ttk.Entry(input_frame, textvariable=self.input_dir_var).grid(
            row=0, column=0, sticky=(tk.W, tk.E), padx=(5, 0))
        ttk.Button(input_frame, text="Browse", command=self.browse_input_dir).grid(
            row=0, column=1, padx=5)
        
        # Warning label
        warning_label = ttk.Label(config_frame, 
                                 text="⚠️ WARNING: Original files will be modified in place",
                                 foreground="red")
        warning_label.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Control Buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
        self.start_button = ttk.Button(control_frame, text="Start Processing", 
                                      command=self.start_processing,
                                      style='Accent.TButton')
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(control_frame, text="Stop Processing", 
                                     command=self.stop_processing,
                                     state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=5)
        
        ttk.Button(control_frame, text="View Statistics", 
                  command=self.show_statistics).grid(row=0, column=2, padx=5)
        
        # Progress Section
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        progress_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        progress_frame.columnconfigure(0, weight=1)
        progress_frame.rowconfigure(2, weight=1)
        
        # Overall Progress
        overall_frame = ttk.Frame(progress_frame)
        overall_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        overall_frame.columnconfigure(1, weight=1)
        
        ttk.Label(overall_frame, text="Overall Progress:").grid(row=0, column=0, sticky=tk.W)
        self.overall_progress = ttk.Progressbar(overall_frame, mode='determinate')
        self.overall_progress.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=10)
        self.overall_label = ttk.Label(overall_frame, text="0/0 MCQs")
        self.overall_label.grid(row=0, column=2)
        
        # File Progress
        ttk.Label(progress_frame, text="File Progress:").grid(row=1, column=0, sticky=tk.W, pady=(10, 5))
        
        # Create Treeview for file progress
        tree_frame = ttk.Frame(progress_frame)
        tree_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        self.file_tree = ttk.Treeview(tree_frame, columns=('Status', 'Progress', 'Corrected', 'Time'), 
                                     show='tree headings', height=10)
        self.file_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure columns
        self.file_tree.heading('#0', text='File')
        self.file_tree.heading('Status', text='Status')
        self.file_tree.heading('Progress', text='Progress')
        self.file_tree.heading('Corrected', text='Corrected')
        self.file_tree.heading('Time', text='Time')
        
        self.file_tree.column('#0', width=300)
        self.file_tree.column('Status', width=100)
        self.file_tree.column('Progress', width=150)
        self.file_tree.column('Corrected', width=100)
        self.file_tree.column('Time', width=100)
        
        # Scrollbar for tree
        tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.file_tree.yview)
        tree_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.file_tree.configure(yscrollcommand=tree_scroll.set)
        
        # Log Section
        log_frame = ttk.LabelFrame(main_frame, text="Processing Log", padding="10")
        log_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        log_frame.columnconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=8, wrap=tk.WORD)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Status Bar
        self.status_var = tk.StringVar(value="Ready to process MCQs")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def browse_input_dir(self):
        """Browse for input directory."""
        directory = filedialog.askdirectory(initialdir=self.input_dir_var.get())
        if directory:
            self.input_dir_var.set(directory)
    
    
    def log(self, message: str, level: str = "INFO"):
        """Add message to log."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {level}: {message}\n"
        self.log_text.insert(tk.END, log_message)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def start_processing(self):
        """Start processing MCQs."""
        # Validate inputs
        if not self.api_key_var.get():
            messagebox.showerror("Error", "Please enter your OpenAI API key")
            return
        
        if not os.path.exists(self.input_dir_var.get()):
            messagebox.showerror("Error", "MCQ directory does not exist")
            return
        
        # Confirm with user about modifying original files
        if not messagebox.askyesno("Confirm", 
                                  "This will modify your original MCQ files in place.\n"
                                  "Make sure you have backups!\n\n"
                                  "Do you want to continue?"):
            return
        
        # Update UI state
        self.is_processing = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_var.set("Processing MCQs...")
        
        # Clear previous progress
        self.file_tree.delete(*self.file_tree.get_children())
        self.file_progress.clear()
        
        # Create processor (no output dir - edit in place)
        self.processor = MCQProcessor(
            api_key=self.api_key_var.get(),
            input_dir=self.input_dir_var.get()
        )
        
        # Start processing in separate thread
        self.processing_thread = threading.Thread(target=self.run_processing)
        self.processing_thread.daemon = True
        self.processing_thread.start()
        
        self.log("Started processing MCQs with O3-mini high reasoning mode")
    
    def run_processing(self):
        """Run the processing in a separate thread."""
        try:
            # Get all files
            files = self.processor.get_all_mcq_files()
            self.overall_stats['total_files'] = len(files)
            
            # Initialize file progress
            for file in files:
                file_name = file.name
                self.file_progress[file_name] = {
                    'item': self.file_tree.insert('', 'end', text=file_name,
                                                 values=('Pending', '0/0', '0', '-')),
                    'start_time': None,
                    'status': 'pending'
                }
            
            # Process files
            self.processor.process_all_files(max_workers=5)
            
            # Mark as complete
            self.is_processing = False
            self.status_var.set("Processing complete!")
            self.log("Processing completed successfully", "SUCCESS")
            
        except Exception as e:
            self.is_processing = False
            self.status_var.set("Processing failed!")
            self.log(f"Processing error: {str(e)}", "ERROR")
            messagebox.showerror("Processing Error", str(e))
        
        finally:
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
    
    def stop_processing(self):
        """Stop processing MCQs."""
        if messagebox.askyesno("Confirm", "Are you sure you want to stop processing?"):
            self.is_processing = False
            self.status_var.set("Processing stopped by user")
            self.log("Processing stopped by user", "WARNING")
            # Note: Actual thread stopping would require more sophisticated handling
    
    def monitor_progress(self):
        """Monitor progress from the processor."""
        if self.is_processing and self.processor:
            try:
                # Get progress updates from queue
                while not self.processor.progress_queue.empty():
                    update = self.processor.progress_queue.get_nowait()
                    self.update_file_progress(update)
            except:
                pass
        
        # Schedule next check
        self.root.after(100, self.monitor_progress)
    
    def update_file_progress(self, update: dict):
        """Update progress for a specific file."""
        file_name = update['file']
        if file_name in self.file_progress:
            item = self.file_progress[file_name]['item']
            
            # Update start time if needed
            if self.file_progress[file_name]['start_time'] is None:
                self.file_progress[file_name]['start_time'] = time.time()
                self.file_progress[file_name]['status'] = 'processing'
            
            # Calculate elapsed time
            elapsed = time.time() - self.file_progress[file_name]['start_time']
            time_str = f"{elapsed:.1f}s"
            
            # Update tree item
            progress_str = f"{update['current']}/{update['total']}"
            self.file_tree.item(item, values=('Processing', progress_str, 
                                             str(update['corrected']), time_str))
            
            # Update overall progress
            self.update_overall_progress()
    
    def update_overall_progress(self):
        """Update overall progress bar."""
        if self.processor and self.processor.stats['total'] > 0:
            progress = (self.processor.stats['processed'] / self.processor.stats['total']) * 100
            self.overall_progress['value'] = progress
            self.overall_label.config(
                text=f"{self.processor.stats['processed']}/{self.processor.stats['total']} MCQs"
            )
    
    def show_statistics(self):
        """Show processing statistics."""
        if not self.processor:
            messagebox.showinfo("Statistics", "No processing statistics available yet")
            return
        
        stats = self.processor.stats
        message = f"""Processing Statistics:
        
Total MCQs: {stats['total']}
Processed: {stats['processed']}
Corrected: {stats['corrected']}
Failed: {stats['failed']}
Error Count: {len(stats['errors'])}

Success Rate: {(stats['processed'] / max(stats['total'], 1)) * 100:.1f}%
Correction Rate: {(stats['corrected'] / max(stats['processed'], 1)) * 100:.1f}%"""
        
        messagebox.showinfo("Processing Statistics", message)


def main():
    """Main entry point for GUI."""
    root = tk.Tk()
    app = MCQProcessorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()