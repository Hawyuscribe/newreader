#!/usr/bin/env python3
"""
MCQ Processor with OpenAI O3-mini
Processes MCQs to verify correct answers and explanations using O3-mini high reasoning mode.
"""

import json
import os
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from queue import Queue
import logging

# Third-party imports
try:
    from openai import OpenAI
except ImportError:
    print("Installing required packages...")
    os.system(f"{sys.executable} -m pip install openai tiktoken backoff")
    from openai import OpenAI

import backoff

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mcq_processor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MCQProcessor:
    """Processes MCQs using OpenAI O3-mini with high reasoning mode."""
    
    def __init__(self, api_key: str, input_dir: str, output_dir: str = None):
        """Initialize the MCQ processor."""
        self.client = OpenAI(
            api_key=api_key,
            timeout=600.0  # 10 minutes timeout for API calls
        )
        self.input_dir = Path(input_dir)
        # For in-place editing, we don't need separate output directory
        self.output_dir = self.input_dir  # Edit files in place
        
        # Processing statistics
        self.stats = {
            'total': 0,
            'processed': 0,
            'corrected': 0,
            'failed': 0,
            'errors': []
        }
        
        # Thread-safe queue for progress updates
        self.progress_queue = Queue()
        
        # Lock for thread-safe file operations
        self.file_lock = threading.Lock()
        
    def get_all_mcq_files(self) -> List[Path]:
        """Get all JSON files from the input directory."""
        return list(self.input_dir.glob("*.json"))
    
    def load_mcqs(self, filepath: Path) -> Dict:
        """Load MCQs from a JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading {filepath}: {str(e)}")
            return None
    
    def save_mcqs(self, data: Dict, filepath: Path):
        """Save processed MCQs back to the original file."""
        try:
            with self.file_lock:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Updated original file: {filepath}")
        except Exception as e:
            logger.error(f"Error saving {filepath}: {str(e)}")
    
    def create_mcq_prompt(self, mcq: Dict) -> str:
        """Create a comprehensive prompt for O3-mini to analyze the MCQ."""
        # Check if MCQ has options
        has_options = 'options' in mcq and mcq['options']
        
        prompt = f"""You are an expert medical educator and neurologist. Analyze this medical question carefully:

QUESTION: {mcq['question']}
"""
        
        if has_options:
            prompt += "\nOPTIONS:\n"
            for i, option in enumerate(mcq['options']):
                letter = chr(65 + i)  # A, B, C, D...
                prompt += f"{letter}. {option}\n"
            
            prompt += f"""
CURRENT MARKED ANSWER: {mcq.get('correct_answer', 'None')} - {mcq.get('correct_answer_text', '')}
"""
        else:
            prompt += "\nNOTE: This question has no multiple choice options, only explanation.\n"
        
        prompt += f"""
CURRENT EXPLANATION:
{json.dumps(mcq.get('explanation', {}), indent=2)}

TASK:
1. {"Verify if the marked correct answer is actually correct. If not, identify the truly correct answer." if has_options else "Review the explanation for accuracy."}
2. Review all explanation sections for factual accuracy{"and alignment with the correct answer" if has_options else ""}.
3. IMPORTANT: Only suggest changes if there are actual errors. If everything is correct, set is_correction_needed to false.
4. NEVER change the original question or option phrasing, even if incomplete or grammatically imperfect.

RESPONSE FORMAT (JSON):
{{
  "analysis": "Your detailed reasoning",
  {"\"correct_answer\": \"A/B/C/D or same as current\"," if has_options else ""}
  {"\"correct_answer_text\": \"The text of the correct option or same as current\"," if has_options else ""}
  "is_correction_needed": true/false,
  "explanation": {{
    "option_analysis": "{"Only provide if corrections needed" if has_options else "Analysis of the topic"}",
    "conceptual_foundation": "Only provide if corrections needed",
    "pathophysiology": "Only provide if corrections needed",
    "clinical_manifestation": "Only provide if corrections needed",
    "diagnostic_approach": "Only provide if corrections needed",
    "management_principles": "Only provide if corrections needed",
    "follow_up_guidelines": "Only provide if corrections needed",
    "clinical_pearls": ["Only provide if corrections needed"],
    "references": "Only provide if corrections needed"
  }},
  "corrections_made": "Summary of corrections or 'None - all content is accurate'"
}}

If is_correction_needed is false, the explanation field can be empty or contain the original values."""
        
        return prompt
    
    @backoff.on_exception(
        backoff.expo,
        Exception,
        max_tries=3,
        max_time=600  # 10 minutes timeout
    )
    def process_single_mcq(self, mcq: Dict, mcq_index: int, file_name: str) -> Tuple[Dict, bool]:
        """Process a single MCQ with O3-mini."""
        try:
            # Store original MCQ for comparison
            original_mcq = json.loads(json.dumps(mcq))  # Deep copy
            
            prompt = self.create_mcq_prompt(mcq)
            
            # Call O3-mini with high reasoning mode
            response = self.client.chat.completions.create(
                model="o3-mini",
                messages=[
                    {
                        "role": "developer", 
                        "content": "You are a medical expert specializing in neurology. Provide accurate, evidence-based analysis. Only suggest corrections if there are actual errors."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_completion_tokens=5000,
                reasoning_effort="high"  # Use high reasoning mode for accuracy
                # Note: O3-mini doesn't support temperature parameter
            )
            
            # Parse the response
            result = self.parse_o3_response(response.choices[0].message.content)
            
            # Check if MCQ has options
            has_options = 'options' in mcq and mcq['options']
            
            # Update MCQ ONLY if corrections are needed
            if result.get('is_correction_needed', False):
                # Preserve original question and options
                mcq['question'] = original_mcq['question']
                if has_options:
                    mcq['options'] = original_mcq['options']
                    
                    # Update answer if provided and different
                    if 'correct_answer' in result and result['correct_answer'] != original_mcq.get('correct_answer'):
                        mcq['correct_answer'] = result['correct_answer']
                        mcq['correct_answer_text'] = result['correct_answer_text']
                
                # Update explanation sections only if provided
                if 'explanation' in result and result['explanation']:
                    # Only update sections that have new content
                    for section, content in result['explanation'].items():
                        if content and content != "Only provide if corrections needed":
                            if 'explanation' not in mcq:
                                mcq['explanation'] = {}
                            mcq['explanation'][section] = content
                
                mcq['ai_corrected'] = True
                mcq['correction_details'] = result.get('corrections_made', '')
                mcq['processing_date'] = datetime.now().isoformat()
                
                logger.info(f"Corrected MCQ {mcq_index} in {file_name}: {result.get('corrections_made', '')}")
                return mcq, True
            else:
                # No corrections needed - preserve original MCQ completely
                # Only add metadata
                mcq['ai_verified'] = True
                mcq['processing_date'] = datetime.now().isoformat()
                
                logger.info(f"Verified MCQ {mcq_index} in {file_name}: No corrections needed")
                return mcq, False
            
        except Exception as e:
            logger.error(f"Error processing MCQ {mcq_index} in {file_name}: {str(e)}")
            self.stats['errors'].append({
                'file': file_name,
                'mcq_index': mcq_index,
                'error': str(e)
            })
            raise
    
    def parse_o3_response(self, response_text: str) -> Dict:
        """Parse O3-mini response with robust error handling."""
        try:
            # Try to extract JSON from the response
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                return json.loads(json_str)
            
            # If no JSON found, try to parse the structured response
            result = self.parse_structured_response(response_text)
            return result
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            # Fallback parsing logic
            return self.parse_structured_response(response_text)
        except Exception as e:
            logger.error(f"Response parsing error: {e}")
            raise
    
    def parse_structured_response(self, text: str) -> Dict:
        """Parse structured text response when JSON parsing fails."""
        result = {
            "is_correction_needed": False,
            "explanation": {}
        }
        
        # Extract sections using regex patterns
        sections = {
            'option_analysis': r'option.?analysis[:\s]*(.*?)(?=\n\n|\Z)',
            'conceptual_foundation': r'conceptual.?foundation[:\s]*(.*?)(?=\n\n|\Z)',
            'pathophysiology': r'pathophysiology[:\s]*(.*?)(?=\n\n|\Z)',
            'clinical_manifestation': r'clinical.?manifestation[:\s]*(.*?)(?=\n\n|\Z)',
            'diagnostic_approach': r'diagnostic.?approach[:\s]*(.*?)(?=\n\n|\Z)',
            'management_principles': r'management.?principles[:\s]*(.*?)(?=\n\n|\Z)',
            'follow_up_guidelines': r'follow.?up.?guidelines[:\s]*(.*?)(?=\n\n|\Z)',
            'references': r'references[:\s]*(.*?)(?=\n\n|\Z)'
        }
        
        for section, pattern in sections.items():
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                result['explanation'][section] = match.group(1).strip()
        
        # Extract clinical pearls
        pearls_match = re.search(r'clinical.?pearls[:\s]*(.*?)(?=\n\n|\Z)', text, re.IGNORECASE | re.DOTALL)
        if pearls_match:
            pearls_text = pearls_match.group(1)
            # Split by bullet points or numbers
            pearls = re.findall(r'[•\-\d]+\s*(.+?)(?=[•\-\d]+\s*|\Z)', pearls_text, re.DOTALL)
            result['explanation']['clinical_pearls'] = [p.strip() for p in pearls if p.strip()]
        
        # Extract correct answer
        answer_match = re.search(r'correct.?answer[:\s]*([A-Z])', text, re.IGNORECASE)
        if answer_match:
            result['correct_answer'] = answer_match.group(1)
            result['is_correction_needed'] = True
        
        return result
    
    def process_file(self, file_path: Path) -> Dict:
        """Process all MCQs in a single file."""
        file_name = file_path.name
        logger.info(f"Processing file: {file_name}")
        
        # Load MCQs
        data = self.load_mcqs(file_path)
        if not data:
            return {'status': 'failed', 'file': file_name, 'error': 'Failed to load file'}
        
        # Create a deep copy of original data to preserve structure
        original_data = json.loads(json.dumps(data))
        
        mcqs = data.get('mcqs', [])
        total_mcqs = len(mcqs)
        corrected_count = 0
        verified_count = 0
        
        # Process each MCQ
        for i, mcq in enumerate(mcqs):
            try:
                processed_mcq, was_corrected = self.process_single_mcq(mcq, i, file_name)
                mcqs[i] = processed_mcq
                
                if was_corrected:
                    corrected_count += 1
                else:
                    verified_count += 1
                
                # Update progress
                self.progress_queue.put({
                    'file': file_name,
                    'current': i + 1,
                    'total': total_mcqs,
                    'corrected': corrected_count
                })
                
            except Exception as e:
                logger.error(f"Failed to process MCQ {i} in {file_name}: {str(e)}")
                # Keep original MCQ if processing fails
                mcqs[i] = original_data['mcqs'][i]
                continue
        
        # Update data and save back to original file
        data['mcqs'] = mcqs
        data['processing_info'] = {
            'processed_date': datetime.now().isoformat(),
            'total_mcqs': total_mcqs,
            'verified_mcqs': verified_count,
            'corrected_mcqs': corrected_count,
            'processor': 'O3-mini-high-reasoning',
            'note': 'Files updated in place - originals modified'
        }
        
        self.save_mcqs(data, file_path)  # Save back to original file
        
        return {
            'status': 'completed',
            'file': file_name,
            'total': total_mcqs,
            'verified': verified_count,
            'corrected': corrected_count
        }
    
    def process_all_files(self, max_workers: int = 5):
        """Process all MCQ files with concurrent workers."""
        files = self.get_all_mcq_files()
        self.stats['total'] = sum(len(self.load_mcqs(f).get('mcqs', [])) for f in files if self.load_mcqs(f))
        
        logger.info(f"Starting processing of {len(files)} files with {self.stats['total']} total MCQs")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all files for processing
            future_to_file = {executor.submit(self.process_file, f): f for f in files}
            
            # Process completed futures
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    result = future.result()
                    if result['status'] == 'completed':
                        self.stats['processed'] += result['total']
                        self.stats['corrected'] += result['corrected']
                    else:
                        self.stats['failed'] += 1
                        
                except Exception as e:
                    logger.error(f"Error processing {file_path}: {str(e)}")
                    self.stats['failed'] += 1
        
        logger.info(f"Processing complete. Stats: {self.stats}")
        
        # Save final statistics
        self.save_statistics()
    
    def save_statistics(self):
        """Save processing statistics."""
        stats_file = self.output_dir / 'processing_statistics.json'
        with open(stats_file, 'w') as f:
            json.dump({
                'statistics': self.stats,
                'processing_date': datetime.now().isoformat(),
                'errors': self.stats['errors']
            }, f, indent=2)


def main():
    """Main entry point."""
    # Configuration
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Please set OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    input_dir = "/Users/tariqalmatrudi/Documents/FFF/output_by_specialty"
    
    # Create processor (no separate output directory - edit in place)
    processor = MCQProcessor(api_key, input_dir)
    
    # Process all files
    processor.process_all_files(max_workers=5)


if __name__ == "__main__":
    main()