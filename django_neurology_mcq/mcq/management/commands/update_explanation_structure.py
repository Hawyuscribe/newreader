from django.core.management.base import BaseCommand
from django.db import transaction
from mcq.models import MCQ
import json

class Command(BaseCommand):
    help = 'Update explanation structure to match MCQ data format'

    def handle(self, *args, **options):
        self.stdout.write("Updating explanation sections in the database...")
        
        # Define the mapping from various formats to the standard format
        section_mappings = {
            'conceptual_foundation': ['conceptual foundation', 'Conceptual Foundation'],
            'pathophysiological_mechanisms': ['pathophysiology', 'Pathophysiology', 'pathophysiological mechanisms', 'Pathophysiological Mechanisms'],
            'clinical_correlation': ['clinical correlation', 'Clinical Correlation', 'clinical context', 'Clinical Context'],
            'classification_and_nosology': ['classification and neurology', 'Classification and Neurology', 'classification and nosology', 'Classification and Nosology'],
            'diagnostic_approach': ['diagnostic approach', 'Diagnostic Approach'],
            'management_principles': ['management principles', 'Management Principles'],
            'option_analysis': ['option analysis', 'Option Analysis', 'options analysis', 'answer analysis'],
            'clinical_pearls': ['clinical pearls', 'Clinical Pearls', 'key insight', 'Key Insight'],
            'current_evidence': ['current evidence', 'Current Evidence', 'quick reference', 'Quick Reference', 'application and recall', 'Application and Recall']
        }
        
        updated_count = 0
        
        with transaction.atomic():
            for mcq in MCQ.objects.all():
                if mcq.explanation_sections:
                    updated = False
                    new_sections = {}
                    
                    # Process each section
                    for standard_key, variations in section_mappings.items():
                        # Check if any variation exists
                        for variation in variations:
                            if variation in mcq.explanation_sections and mcq.explanation_sections[variation]:
                                new_sections[standard_key] = mcq.explanation_sections[variation]
                                if variation != standard_key:
                                    updated = True
                                break
                        
                        # If standard key exists, use it
                        if standard_key in mcq.explanation_sections and mcq.explanation_sections[standard_key]:
                            new_sections[standard_key] = mcq.explanation_sections[standard_key]
                    
                    # Copy any other keys that might exist
                    for key, value in mcq.explanation_sections.items():
                        if key not in new_sections and value:
                            # Check if it's not a variation we already handled
                            handled = False
                            for variations in section_mappings.values():
                                if key in variations:
                                    handled = True
                                    break
                            if not handled:
                                new_sections[key] = value
                    
                    if updated or len(new_sections) != len(mcq.explanation_sections):
                        mcq.explanation_sections = new_sections
                        mcq.save()
                        updated_count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Updated {updated_count} MCQs with standardized explanation sections"))
        
        # Show a sample of the standardized sections
        sample_mcq = MCQ.objects.filter(explanation_sections__isnull=False).first()
        if sample_mcq:
            self.stdout.write("\nSample standardized sections:")
            for key in sorted(sample_mcq.explanation_sections.keys()):
                self.stdout.write(f"  - {key}")
        
        # Create template update file
        self.create_template_update()
        self.create_css_update()
        
        self.stdout.write(self.style.SUCCESS("\nDone! Please review the generated files and update your templates accordingly."))
    
    def create_template_update(self):
        """Create an updated template for displaying explanations"""
        
        template_content = '''<!-- Updated explanation display section for mcq.html -->
<!-- Replace the existing explanation tab content with this -->

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
    <!-- Fallback to old explanation format -->
    <div class="explanation-content p-3">
        <div class="d-flex align-items-center mb-3">
            <i class="bi bi-journal-medical text-primary me-2 fs-4"></i>
            <h4 class="m-0">Detailed Explanation</h4>
        </div>
        <div id="explanation-content-wrapper">
            <div id="formatted-explanation">{{ mcq.explanation|safe }}</div>
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
        
        with open('explanation_template_update.html', 'w') as f:
            f.write(template_content)
        
        self.stdout.write("Created explanation_template_update.html - use this to update the mcq.html template")
    
    def create_css_update(self):
        """Create CSS styles for the new explanation sections"""
        
        css_content = '''/* Add these styles to your existing CSS */

/* Explanation sections styling */
.explanation-section {
    border-left: 3px solid #e9ecef;
    padding-left: 1rem;
    transition: border-color 0.3s ease;
}

.explanation-section:hover {
    border-left-color: #007bff;
}

.section-header {
    border-bottom: 2px solid #f8f9fa;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
}

.section-content {
    color: #495057;
    line-height: 1.8;
}

/* Clinical pearls special styling */
.clinical-pearls {
    background-color: #fff9e6;
    padding: 1rem;
    border-radius: 0.5rem;
    border: 1px solid #ffc107;
}

.clinical-pearls strong {
    color: #856404;
}

/* Option analysis styling */
.option-analysis-item {
    margin-bottom: 1rem;
    padding: 0.5rem;
    background-color: #f8f9fa;
    border-radius: 0.25rem;
}

/* Evidence section styling */
.current-evidence ul {
    list-style-type: none;
    padding-left: 0;
}

.current-evidence li {
    padding-left: 1.5rem;
    position: relative;
    margin-bottom: 0.5rem;
}

.current-evidence li:before {
    content: "•";
    color: #17a2b8;
    font-weight: bold;
    position: absolute;
    left: 0;
}'''
        
        with open('explanation_styles.css', 'w') as f:
            f.write(css_content)
        
        self.stdout.write("Created explanation_styles.css - add these styles to your CSS")