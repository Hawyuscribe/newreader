// Verify with AI - Enhanced version
document.addEventListener('DOMContentLoaded', function() {
    const verifyAnswerBtn = document.getElementById('verifyAnswerBtn');
    const aiAnalysis = document.getElementById('aiAnalysis');
    const analysisContent = document.getElementById('analysisContent');
    
    if (verifyAnswerBtn && aiAnalysis && analysisContent) {
        verifyAnswerBtn.addEventListener('click', function() {
            // Show the analysis card and scroll to it
            aiAnalysis.classList.remove('hidden');
            aiAnalysis.scrollIntoView({ behavior: 'smooth', block: 'center' });
            
            // Set loading state
            analysisContent.innerHTML = `
                <div class="d-flex justify-content-center align-items-center p-4">
                    <div class="spinner-border text-primary me-3" role="status" style="color: #2c3e50 !important;">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <div>
                        <div class="h5 mb-1">Analyzing MCQ...</div>
                        <div class="text-muted small">
                            <i class="bi bi-info-circle"></i> Consulting current guidelines and evidence to verify the answer
                        </div>
                    </div>
                </div>
            `;
            
            // Get the current MCQ ID from the URL
            const currentPath = window.location.pathname;
            const mcqIdMatch = currentPath.match(/\/mcq\/(\d+)\//);
            const mcqId = mcqIdMatch ? mcqIdMatch[1] : null;
            
            if (!mcqId) {
                analysisContent.innerHTML = `
                    <div class="alert alert-danger">
                        <i class="bi bi-exclamation-triangle-fill"></i> 
                        Could not determine the MCQ ID from the current URL.
                    </div>
                `;
                return;
            }
            
            // Get CSRF token
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            
            // Prepare form data instead of using JSON content type
            const formData = new FormData();
            formData.append('csrfmiddlewaretoken', csrfToken);
            
            // Make API request
            fetch(`/mcq/${mcqId}/verify_answer/`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'  // This helps Django identify AJAX requests
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                // Check if we have response data
                if (!data || !data.analysis) {
                    throw new Error('No analysis data received from server');
                }
                
                // Log data for debugging
                console.log("Verify answer response received:", data);
                
                // If the analysis is already wrapped in a div, use it directly
                if (data.analysis.trim().startsWith('<div class="alert')) {
                    analysisContent.innerHTML = data.analysis;
                    return;
                }
                
                // Create styled HTML for verification results
                const verificationStyles = `
                    <style>
                        .verification-report {
                            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                        }
                        .verification-section {
                            margin-bottom: 1.5rem;
                            border-radius: 8px;
                            overflow: hidden;
                            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                        }
                        .verification-header {
                            padding: 0.8rem 1rem;
                            font-weight: 600;
                            font-size: 1.1rem;
                            display: flex;
                            align-items: center;
                        }
                        .verification-header i {
                            margin-right: 0.5rem;
                        }
                        .verification-content {
                            padding: 1rem;
                            background-color: white;
                            line-height: 1.6;
                        }
                        .verification-title {
                            font-weight: 600;
                            font-size: 1.5rem;
                            margin-bottom: 1.5rem;
                            padding-bottom: 0.5rem;
                            border-bottom: 2px solid #2c3e50;
                            color: #2c3e50;
                        }
                        .evidence-section {
                            border-left: 5px solid #3498db;
                        }
                        .evidence-section .verification-header {
                            background-color: rgba(52, 152, 219, 0.1);
                            color: #3498db;
                        }
                        .correct-section {
                            border-left: 5px solid #2ecc71;
                        }
                        .correct-section .verification-header {
                            background-color: rgba(46, 204, 113, 0.1);
                            color: #2ecc71;
                        }
                        .incorrect-section {
                            border-left: 5px solid #e74c3c;
                        }
                        .incorrect-section .verification-header {
                            background-color: rgba(231, 76, 60, 0.1);
                            color: #e74c3c;
                        }
                        .verification-list {
                            padding-left: 1rem;
                            margin-bottom: 1rem;
                        }
                        .verification-list li {
                            margin-bottom: 0.5rem;
                        }
                        .option-badge {
                            display: inline-flex;
                            align-items: center;
                            justify-content: center;
                            width: 24px;
                            height: 24px;
                            border-radius: 50%;
                            margin-right: 5px;
                            font-weight: bold;
                            font-size: 0.8rem;
                        }
                        .evidence-badge {
                            display: inline-block;
                            border-radius: 4px;
                            padding: 2px 5px;
                            font-weight: 600;
                            font-size: 0.8rem;
                            background-color: #f8f9fa;
                            border: 1px solid #dee2e6;
                            color: #6c757d;
                        }
                        .option-A { background-color: #0d6efd; color: white; }
                        .option-B { background-color: #198754; color: white; }
                        .option-C { background-color: #ffc107; color: black; }
                        .option-D { background-color: #dc3545; color: white; }
                        .option-E { background-color: #6c757d; color: white; }
                    </style>
                `;
                
                // Process the content
                let processedAnalysis = data.analysis;
                
                try {
                    // Basic markdown to HTML conversion
                    processedAnalysis = processedAnalysis.replace(/^### (.*?)$/gm, '<h4>$1</h4>');
                    processedAnalysis = processedAnalysis.replace(/^## (.*?)$/gm, '<h3>$1</h3>');
                    processedAnalysis = processedAnalysis.replace(/^# (.*?)$/gm, '<h2>$1</h2>');
                    
                    // Format lists
                    processedAnalysis = processedAnalysis.replace(/^- (.*?)$/gm, '<li>$1</li>');
                    processedAnalysis = processedAnalysis.replace(/^(\d+)\. (.*?)$/gm, '<li>$1. $2</li>');
                    
                    // Wrap lists
                    processedAnalysis = processedAnalysis.replace(/(<li>.*?<\/li>)+/gs, '<ul class="verification-list">$&</ul>');
                    
                    // Format bold and italic
                    processedAnalysis = processedAnalysis.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
                    processedAnalysis = processedAnalysis.replace(/\*(.*?)\*/g, '<em>$1</em>');
                    
                    // Handle options
                    ['A', 'B', 'C', 'D', 'E'].forEach(option => {
                        processedAnalysis = processedAnalysis.replace(
                            new RegExp(`Option ${option}:`, 'g'), 
                            `<span class="option-badge option-${option}">${option}</span> Option ${option}:`
                        );
                    });
                    
                    // Handle evidence levels
                    processedAnalysis = processedAnalysis.replace(
                        /Level (I+V?)(-[A-D])?/g, 
                        '<span class="evidence-badge">Level $1$2</span>'
                    );
                    
                    // Handle tables more robustly
                    const tableRegex = /\|\s*(.*?)\s*\|\n\|\s*[-:]+\s*\|\s*[-:]+\s*\|\s*[-:]+\s*\|\s*[-:]+\s*\|(?:\s*[-:]+\s*\|)?(?:\s*[-:]+\s*\|)?[\s\S]*?(?=\n\n|\n#|\n$)/g;
                    
                    // Try to process tables, but with error handling
                    try {
                        processedAnalysis = processedAnalysis.replace(tableRegex, function(table) {
                            try {
                                const rows = table.trim().split('\n');
                                if (rows.length < 3) return table; // Not a proper table
                                
                                let html = '<div class="table-responsive mb-4"><table class="table table-bordered table-striped">';
                                
                                // Process the header
                                const headerCells = rows[0].split('|').filter(s => s.trim().length > 0).map(s => s.trim());
                                html += '<thead><tr>';
                                headerCells.forEach(cell => {
                                    html += `<th scope="col">${cell}</th>`;
                                });
                                html += '</tr></thead><tbody>';
                                
                                // Skip the separator row (row[1]) and process the data rows
                                for (let i = 2; i < rows.length; i++) {
                                    const cells = rows[i].split('|').filter(s => s.trim().length > 0).map(s => s.trim());
                                    html += '<tr>';
                                    cells.forEach((cell, index) => {
                                        // First column often contains the feature/aspect name
                                        if (index === 0) {
                                            html += `<th scope="row">${cell}</th>`;
                                        } else {
                                            // Add badge styling for specific texts
                                            if (cell.includes('correct') || cell.includes('yes') || cell.includes('✓')) {
                                                html += `<td><span class="badge bg-success">${cell}</span></td>`;
                                            } else if (cell.includes('incorrect') || cell.includes('no') || cell.includes('✗')) {
                                                html += `<td><span class="badge bg-danger">${cell}</span></td>`;
                                            } else if (cell.match(/^[A-E]$/)) {
                                                html += `<td><span class="option-badge option-${cell}">${cell}</span></td>`;
                                            } else {
                                                html += `<td>${cell}</td>`;
                                            }
                                        }
                                    });
                                    html += '</tr>';
                                }
                                
                                html += '</tbody></table></div>';
                                return html;
                            } catch (e) {
                                console.error('Error processing table:', e);
                                return table; // Return the original table if processing fails
                            }
                        });
                    } catch (e) {
                        console.error('Error processing tables:', e);
                        // Tables won't be formatted but we continue
                    }
                    
                    // Create main report container
                    let verificationHTML = `
                        <div class="verification-report">
                            <h2 class="verification-title"><i class="bi bi-shield-check me-2"></i>MCQ Verification Report</h2>
                    `;
                    
                    // Create sections with cards
                    const sections = [
                        { title: "EVIDENCE SYNTHESIS", class: "evidence-section", icon: "bi-journal-text" },
                        { title: "CORRECT ANSWER VERIFICATION", class: "correct-section", icon: "bi-check-circle-fill" },
                        { title: "ANALYSIS OF INCORRECT OPTIONS", class: "incorrect-section", icon: "bi-x-circle-fill" }
                    ];
                    
                    // For each expected section
                    let sectionFound = false;
                    sections.forEach(section => {
                        // Look for section header
                        const sectionTitle = section.title.toLowerCase();
                        const sectionRegex = new RegExp(`<h[23]>.*?${sectionTitle}.*?</h[23]>`, 'i');
                        const match = processedAnalysis.match(sectionRegex);
                        
                        if (match) {
                            sectionFound = true;
                            // Get the index of the section heading
                            const sectionStartIndex = processedAnalysis.indexOf(match[0]);
                            
                            // Get the content after this heading
                            let sectionContent = processedAnalysis.slice(sectionStartIndex + match[0].length);
                            
                            // Find the next section heading
                            let nextSectionIndex = Infinity;
                            for (const nextSection of sections) {
                                if (nextSection.title !== section.title) {
                                    const nextRegex = new RegExp(`<h[23]>.*?${nextSection.title.toLowerCase()}.*?</h[23]>`, 'i');
                                    const nextMatch = sectionContent.match(nextRegex);
                                    
                                    if (nextMatch) {
                                        const index = sectionContent.indexOf(nextMatch[0]);
                                        if (index < nextSectionIndex) {
                                            nextSectionIndex = index;
                                        }
                                    }
                                }
                            }
                            
                            // Extract content up to the next section
                            sectionContent = nextSectionIndex !== Infinity ? 
                                            sectionContent.slice(0, nextSectionIndex) : 
                                            sectionContent;
                            
                            // Add section HTML
                            verificationHTML += `
                                <div class="verification-section ${section.class}">
                                    <div class="verification-header">
                                        <i class="bi ${section.icon}"></i> ${section.title}
                                    </div>
                                    <div class="verification-content">
                                        ${sectionContent}
                                    </div>
                                </div>
                            `;
                        }
                    });
                    
                    // If no sections found, just use the full content
                    if (!sectionFound) {
                        verificationHTML += `
                            <div class="verification-section">
                                <div class="verification-content">
                                    ${processedAnalysis}
                                </div>
                            </div>
                        `;
                    }
                    
                    // Close the verification report
                    verificationHTML += `</div>`;
                    
                    // Add extra CSS to ensure all formatting is applied
                    analysisContent.innerHTML = verificationStyles + verificationHTML;
                } catch (e) {
                    // If any error occurs in processing, just show the raw response
                    console.error('Error processing analysis:', e);
                    analysisContent.innerHTML = `
                        <div class="alert alert-warning">
                            <h4><i class="bi bi-exclamation-triangle"></i> Error formatting the analysis</h4>
                            <p>Showing raw response:</p>
                        </div>
                        <pre class="bg-light p-3 rounded">${data.analysis}</pre>
                    `;
                }
            })
            .catch(error => {
                console.error('Error:', error);
                analysisContent.innerHTML = `
                    <div class="alert alert-danger">
                        <i class="bi bi-exclamation-triangle-fill"></i> 
                        An error occurred while verifying the MCQ: ${error.message || 'Unknown error'}
                    </div>
                    <div class="mt-3">
                        <h5>Troubleshooting steps:</h5>
                        <ol>
                            <li>Check your internet connection</li>
                            <li>Refresh the page and try again</li>
                            <li>If the problem persists, try using one of the other learning tools available on this page</li>
                        </ol>
                        <div class="d-grid gap-2 mt-3">
                            <button class="btn btn-outline-primary" onClick="location.reload()">
                                <i class="bi bi-arrow-clockwise"></i> Refresh Page
                            </button>
                            <button class="btn btn-outline-secondary" id="hideVerificationBtn">
                                <i class="bi bi-x-circle"></i> Hide Verification Panel
                            </button>
                        </div>
                    </div>
                `;
                
                // Add event listener for the hide button
                const hideVerificationBtn = document.getElementById('hideVerificationBtn');
                if (hideVerificationBtn) {
                    hideVerificationBtn.addEventListener('click', function() {
                        const aiAnalysis = document.getElementById('aiAnalysis');
                        if (aiAnalysis) {
                            aiAnalysis.classList.add('hidden');
                        }
                    });
                }
            });
        });
    }
});