// MCQ Admin JavaScript Enhancements

document.addEventListener('DOMContentLoaded', function() {
    console.log('MCQ Admin JS loaded');
    
    // Add visual indicators for populated fields
    const explanationFields = [
        'id_conceptual_foundation',
        'id_option_analysis',
        'id_clinical_context',
        'id_key_insight',
        'id_quick_reference',
        'id_application_and_recall'
    ];
    
    explanationFields.forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) {
            // Check if CKEditor is initialized
            if (typeof CKEDITOR !== 'undefined' && CKEDITOR.instances[fieldId]) {
                const editor = CKEDITOR.instances[fieldId];
                
                // Add indicator if field has content
                if (editor.getData().trim()) {
                    const container = field.closest('.form-row');
                    if (container && !container.querySelector('.content-indicator')) {
                        const indicator = document.createElement('span');
                        indicator.className = 'content-indicator';
                        indicator.innerHTML = '✓ Has content';
                        indicator.style.color = 'green';
                        indicator.style.fontWeight = 'bold';
                        indicator.style.float = 'right';
                        
                        const label = container.querySelector('label');
                        if (label) {
                            label.appendChild(indicator);
                        }
                    }
                }
                
                // Add change listener
                editor.on('change', function() {
                    const hasContent = editor.getData().trim() !== '';
                    const container = field.closest('.form-row');
                    let indicator = container.querySelector('.content-indicator');
                    
                    if (hasContent && !indicator) {
                        indicator = document.createElement('span');
                        indicator.className = 'content-indicator';
                        indicator.innerHTML = '✓ Has content';
                        indicator.style.color = 'green';
                        indicator.style.fontWeight = 'bold';
                        indicator.style.float = 'right';
                        
                        const label = container.querySelector('label');
                        if (label) {
                            label.appendChild(indicator);
                        }
                    } else if (!hasContent && indicator) {
                        indicator.remove();
                    }
                });
            }
        }
    });
    
    // Add a button to parse text explanation
    const explanationFieldset = document.querySelector('#fieldset-3');
    if (explanationFieldset) {
        const parseButton = document.createElement('button');
        parseButton.type = 'button';
        parseButton.className = 'button';
        parseButton.innerHTML = '🔄 Parse Text Explanation';
        parseButton.style.marginBottom = '20px';
        parseButton.style.backgroundColor = '#6c5ce7';
        parseButton.style.color = 'white';
        parseButton.style.border = 'none';
        parseButton.style.padding = '10px 20px';
        parseButton.style.borderRadius = '5px';
        parseButton.style.cursor = 'pointer';
        
        parseButton.addEventListener('click', function() {
            const explanationField = document.getElementById('id_explanation');
            if (explanationField && explanationField.value) {
                const text = explanationField.value;
                
                // Parse sections
                const sections = {
                    'conceptual_foundation': extractSection(text, ['Conceptual Foundation', 'Basic Concepts']),
                    'option_analysis': extractSection(text, ['Option Analysis', 'Answer Analysis']),
                    'clinical_context': extractSection(text, ['Clinical Context', 'Clinical Correlation']),
                    'key_insight': extractSection(text, ['Key Insight', 'Differential Diagnosis']),
                    'quick_reference': extractSection(text, ['Quick Reference', 'Clinical Pearls', 'Memory Aid']),
                    'application_and_recall': extractSection(text, ['Application and Recall', 'Take-Home Points', 'Current Evidence'])
                };
                
                // Populate fields
                Object.keys(sections).forEach(key => {
                    if (sections[key] && CKEDITOR.instances['id_' + key]) {
                        CKEDITOR.instances['id_' + key].setData(sections[key]);
                    }
                });
                
                alert('Text explanation parsed into sections!');
            } else {
                alert('No text explanation found to parse.');
            }
        });
        
        explanationFieldset.insertBefore(parseButton, explanationFieldset.firstChild.nextSibling);
    }
    
    function extractSection(text, headers) {
        for (let header of headers) {
            const regex = new RegExp(`${header}[:\\s]*\\n+([\\s\\S]*?)(?=\\n[A-Z][^a-z]*[:\\s]*\\n|$)`, 'i');
            const match = text.match(regex);
            if (match) {
                return match[1].trim();
            }
        }
        return '';
    }
});