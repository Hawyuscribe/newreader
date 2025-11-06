#!/usr/bin/env python3
"""
Script to consolidate all MCQs from specialty JSON files into a single file
that can be imported to Heroku.
"""

import json
import os
from pathlib import Path
from datetime import datetime

def consolidate_mcqs():
    """Read all specialty JSON files and create consolidated MCQ data"""
    
    specialty_dir = Path('/Users/tariqalmatrudi/Documents/FFF/output_by_specialty')
    
    if not specialty_dir.exists():
        print(f"❌ Directory not found: {specialty_dir}")
        return
    
    print(f"📁 Reading MCQs from: {specialty_dir}")
    
    all_mcqs = []
    file_stats = {}
    
    # Get all JSON files
    json_files = list(specialty_dir.glob('*.json'))
    print(f"Found {len(json_files)} JSON files")
    
    for json_file in sorted(json_files):
        print(f"\n📄 Processing: {json_file.name}")
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            specialty = data.get('specialty', json_file.stem.replace('_mcqs', '').replace('_', ' ').title())
            mcqs = data.get('mcqs', [])
            
            print(f"   Specialty: {specialty}")
            print(f"   MCQs: {len(mcqs)}")
            
            file_stats[json_file.name] = {
                'specialty': specialty,
                'mcq_count': len(mcqs),
                'file_size': json_file.stat().st_size
            }
            
            # Process each MCQ
            for mcq in mcqs:
                # Ensure required fields are present
                processed_mcq = {
                    'question_number': mcq.get('question_number', ''),
                    'question': mcq.get('question', ''),
                    'options': mcq.get('options', []),
                    'correct_answer': mcq.get('correct_answer', ''),
                    'correct_answer_text': mcq.get('correct_answer_text', ''),
                    'subspecialty': mcq.get('subspecialty', specialty),
                    'source_file': json_file.name,
                    'exam_type': mcq.get('exam_type', ''),
                    'exam_year': mcq.get('exam_year', ''),
                    'ai_generated': mcq.get('ai_generated', False),
                    'explanation': mcq.get('explanation', {}),
                    'unified_explanation': mcq.get('unified_explanation', ''),
                    'image_url': mcq.get('image_url', '')
                }
                
                all_mcqs.append(processed_mcq)
                
        except Exception as e:
            print(f"   ❌ Error processing {json_file.name}: {e}")
            continue
    
    print(f"\n{'='*60}")
    print(f"📊 CONSOLIDATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total MCQs collected: {len(all_mcqs)}")
    print(f"Files processed: {len(file_stats)}")
    
    print(f"\n📋 File breakdown:")
    for filename, stats in file_stats.items():
        print(f"  {filename:<40} {stats['mcq_count']:>4} MCQs ({stats['specialty']})")
    
    # Create consolidated file
    consolidated_data = {
        'metadata': {
            'total_mcqs': len(all_mcqs),
            'source_files': len(file_stats),
            'generated_date': datetime.now().isoformat(),
            'source_directory': str(specialty_dir)
        },
        'file_stats': file_stats,
        'mcqs': all_mcqs
    }
    
    # Save to multiple locations
    output_paths = [
        Path(__file__).parent / 'consolidated_all_mcqs.json',
        Path('/Users/tariqalmatrudi/NEWreader/consolidated_all_mcqs.json')
    ]
    
    for output_path in output_paths:
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(consolidated_data, f, indent=2, ensure_ascii=False)
            print(f"\n✅ Consolidated MCQs saved to: {output_path}")
            print(f"   File size: {output_path.stat().st_size / (1024*1024):.1f} MB")
        except Exception as e:
            print(f"❌ Error saving to {output_path}: {e}")
    
    return len(all_mcqs)

if __name__ == '__main__':
    total_mcqs = consolidate_mcqs()
    print(f"\n🎉 Consolidation complete! {total_mcqs} MCQs ready for import.")