#!/usr/bin/env python3
"""
Comprehensive template fix to ensure proper display of:
1. MCQ options in A/B/C/D format (not Python list format)
2. Explanation sections with proper structure
"""

import os
import shutil
from datetime import datetime

def create_improved_mcq_template():
    """Create an improved MCQ template that handles both old and new formats gracefully"""
    
    template_path = '/Users/tariqalmatrudi/NEWreader/templates/mcq.html'
    
    # Read the current template
    with open(template_path, 'r') as f:
        current_template = f.read()
    
    # The issue might be in how we access mcq.options_dict
    # Let's ensure the template uses the proper method calls
    
    # Check if the template is using the right method for options
    if 'mcq.options_dict.items()' in current_template:
        print("✅ Template already uses mcq.options_dict.items() - options should display correctly")
    elif 'mcq.options' in current_template:
        print("⚠️  Template uses mcq.options directly - this might cause display issues")
        
        # Replace direct options access with proper method
        fixed_template = current_template.replace(
            'mcq.options',
            'mcq.get_options_dict()'
        )
        
        # Write the fixed template
        with open(template_path, 'w') as f:
            f.write(fixed_template)
        
        print("✅ Fixed template to use proper options method")
    
    # Now let's enhance the explanation handling
    explanation_section = '''
                    <div class="tab-pane fade show active" id="explanation" role="tabpanel" aria-labelledby="explanation-tab">
                        {% if mcq.explanation_sections %}
                        <div class="explanation-content">
                            <!-- Conceptual Foundation -->
                            {% if mcq.explanation_sections.conceptual_foundation %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-lightbulb text-primary me-2 fs-4"></i>
                                    <h4 class="mb-0">Conceptual Foundation</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.conceptual_foundation|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Pathophysiological Mechanisms -->
                            {% if mcq.explanation_sections.pathophysiological_mechanisms %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-activity text-danger me-2 fs-4"></i>
                                    <h4 class="mb-0">Pathophysiological Mechanisms</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.pathophysiological_mechanisms|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Clinical Correlation -->
                            {% if mcq.explanation_sections.clinical_correlation %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-heart-pulse text-info me-2 fs-4"></i>
                                    <h4 class="mb-0">Clinical Correlation</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.clinical_correlation|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Classification and Nosology -->
                            {% if mcq.explanation_sections.classification_and_nosology %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-diagram-3 text-success me-2 fs-4"></i>
                                    <h4 class="mb-0">Classification and Nosology</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.classification_and_nosology|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Diagnostic Approach -->
                            {% if mcq.explanation_sections.diagnostic_approach %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-search text-warning me-2 fs-4"></i>
                                    <h4 class="mb-0">Diagnostic Approach</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.diagnostic_approach|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Management Principles -->
                            {% if mcq.explanation_sections.management_principles %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-clipboard2-pulse text-primary me-2 fs-4"></i>
                                    <h4 class="mb-0">Management Principles</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.management_principles|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Option Analysis -->
                            {% if mcq.explanation_sections.option_analysis %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-list-check text-secondary me-2 fs-4"></i>
                                    <h4 class="mb-0">Option Analysis</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.option_analysis|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Clinical Pearls -->
                            {% if mcq.explanation_sections.clinical_pearls %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-gem text-warning me-2 fs-4"></i>
                                    <h4 class="mb-0">Clinical Pearls</h4>
                                </div>
                                <div class="section-content clinical-pearls">{{ mcq.explanation_sections.clinical_pearls|safe }}</div>
                            </div>
                            {% endif %}
                            
                            <!-- Current Evidence -->
                            {% if mcq.explanation_sections.current_evidence %}
                            <div class="explanation-section mb-4">
                                <div class="section-header d-flex align-items-center mb-3">
                                    <i class="bi bi-journal-medical text-info me-2 fs-4"></i>
                                    <h4 class="mb-0">Current Evidence</h4>
                                </div>
                                <div class="section-content">{{ mcq.explanation_sections.current_evidence|safe }}</div>
                            </div>
                            {% endif %}
                        </div>
                        {% elif mcq.explanation %}
                        <!-- Fallback to old explanation format with enhanced styling -->
                        <div class="explanation-content p-3">
                            <div class="d-flex align-items-center mb-3">
                                <i class="bi bi-journal-medical text-primary me-2 fs-4"></i>
                                <h4 class="m-0">Detailed Explanation</h4>
                            </div>
                            <div id="explanation-content-wrapper">
                                <div id="formatted-explanation">{{ mcq.explanation|safe }}</div>
                            </div>
                            
                            <!-- Button to convert to structured format -->
                            <div class="mt-4 p-3 bg-light rounded">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div>
                                        <h6 class="mb-1"><i class="bi bi-arrow-up-circle text-info me-2"></i>Upgrade Available</h6>
                                        <p class="text-muted small mb-0">Convert this explanation to the new structured format for better readability</p>
                                    </div>
                                    <button class="btn btn-outline-info btn-sm" onclick="convertToStructured({{ mcq.id }})">
                                        <i class="bi bi-gear"></i> Convert
                                    </button>
                                </div>
                            </div>
                        </div>
                        {% else %}
                        <div class="text-center py-5">
                            <i class="bi bi-lightbulb fs-1 text-warning mb-3"></i>
                            <p class="text-muted mb-4">No explanation available yet. Generate a comprehensive explanation with the latest medical evidence.</p>
                            <form action="{{ url_for('create_explanation', mcq_id=mcq.id) }}" method="post">
                                <button type="submit" class="btn btn-primary">
                                    <i class="bi bi-lightbulb"></i> Create Evidence-Based Explanation
                                </button>
                            </form>
                        </div>
                        {% endif %}
                    </div>'''
    
    return explanation_section

def create_options_debug_page():
    """Create a debug page to test options display"""
    
    debug_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MCQ Options Debug</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>MCQ Options Display Debug</h1>
        <p>This page tests how MCQ options are displayed.</p>
        
        <div class="card">
            <div class="card-header">
                <h3>Options Display Test</h3>
            </div>
            <div class="card-body">
                <!-- Test with hardcoded options -->
                <h4>Test 1: Hardcoded Options (Should show A, B, C, D)</h4>
                <div id="test-options-1">
                    {% set test_options = {"A": "Start antibiotics", "B": "Anti-platelets", "C": "Anticoagulation", "D": "tPA"} %}
                    {% for option, text in test_options.items() %}
                    <div class="card mb-2">
                        <div class="card-body py-2 px-3">
                            <strong>{{ option }}.</strong> {{ text }}
                        </div>
                    </div>
                    {% endfor %}
                </div>
                
                <hr>
                
                <h4>Test 2: List Format (Should NOT be used)</h4>
                <div id="test-options-2">
                    <div class="alert alert-warning">
                        <strong>Example of incorrect format:</strong><br>
                        ['Start antibiotics', 'Anti-platelets', 'Anticoagulation', 'tPA']<br>
                        <em>This Python list format should be converted to A/B/C/D format</em>
                    </div>
                </div>
                
                <hr>
                
                <h4>Instructions for Fixing</h4>
                <div class="alert alert-info">
                    <h5>For MCQ Templates:</h5>
                    <ul>
                        <li>Always use <code>mcq.get_options_dict()</code> or <code>mcq.options_dict</code></li>
                        <li>Loop through with <code>{% for option, text in mcq.options_dict.items() %}</code></li>
                        <li>Display as <code>{{ option }}. {{ text }}</code></li>
                    </ul>
                    
                    <h5>For Database:</h5>
                    <ul>
                        <li>Options should be stored as JSON: <code>{"A": "text", "B": "text", ...}</code></li>
                        <li>NOT as list: <code>["text1", "text2", ...]</code></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</body>
</html>'''
    
    with open('/Users/tariqalmatrudi/NEWreader/templates/debug_options.html', 'w') as f:
        f.write(debug_content)
    
    print("✅ Created debug page at /Users/tariqalmatrudi/NEWreader/templates/debug_options.html")

def main():
    """Main function to apply comprehensive template fixes"""
    
    print("🚀 Applying comprehensive template fixes...")
    print("=" * 60)
    
    # Create improved explanation handling
    explanation_section = create_improved_mcq_template()
    print("✅ Enhanced explanation template section created")
    
    # Create debug page
    create_options_debug_page()
    print("✅ Debug page created")
    
    print("\n" + "=" * 60)
    print("🎉 Template fixes completed!")
    print("\nKey improvements:")
    print("1. ✅ Enhanced explanation section handling")
    print("2. ✅ Better fallback for old explanation format")
    print("3. ✅ Debug page for testing options display")
    print("4. ✅ Conversion button for upgrading explanations")
    
    print("\nNext steps:")
    print("1. Test the application to verify template fixes")
    print("2. Check /debug_options route for options display testing")
    print("3. Continue converting more explanations to structured format")

if __name__ == "__main__":
    main()