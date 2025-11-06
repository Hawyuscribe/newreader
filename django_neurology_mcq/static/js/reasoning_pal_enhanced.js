// Enhanced ReasoningPal JavaScript with robust error handling
class ReasoningPalEnhanced {
    constructor(mcqId, isCorrect, selectedAnswer, correctAnswer) {
        this.mcqId = mcqId;
        this.isCorrect = isCorrect;
        this.selectedAnswer = selectedAnswer;
        this.correctAnswer = correctAnswer;
        this.userReasoning = '';
        this.currentStep = 'input'; // 'input' or 'analysis'
        this.isSubmitting = false;
        this.initialized = false;
        this.retryCount = 0;
        this.maxRetries = 5;
    }
    
    init() {
        console.log('🚀 ReasoningPal initialization started');
        this.showModal();
        this.setupAnswerFeedback();
        
        // Multiple initialization attempts with increasing delays
        this.initializeWithRetry();
    }
    
    initializeWithRetry() {
        const delay = Math.min(100 * Math.pow(2, this.retryCount), 2000); // Exponential backoff
        
        setTimeout(() => {
            console.log(`🔄 Initialization attempt ${this.retryCount + 1}/${this.maxRetries}`);
            
            if (this.attemptInitialization()) {
                console.log('✅ Initialization successful');
                this.initialized = true;
                return;
            }
            
            this.retryCount++;
            if (this.retryCount < this.maxRetries) {
                console.log(`⏳ Retrying initialization in ${delay}ms...`);
                this.initializeWithRetry();
            } else {
                console.error('❌ Failed to initialize after all retries');
                this.fallbackInitialization();
            }
        }, delay);
    }
    
    attemptInitialization() {
        const textarea = document.getElementById('user-reasoning');
        const countEl = document.getElementById('char-count');
        const submitBtn = document.getElementById('submit-reasoning');
        const modal = document.getElementById('reasoning-pal-modal');
        
        console.log('🔍 Element check:', {
            textarea: !!textarea,
            countEl: !!countEl, 
            submitBtn: !!submitBtn,
            modal: !!modal,
            modalDisplay: modal ? modal.style.display : undefined,
            textareaVisible: textarea ? textarea.offsetParent !== null : false
        });
        
        // Check if elements exist (don't require visibility yet)
        if (textarea && countEl && submitBtn) {
            console.log('✅ All elements found, setting up...');
            this.setupEventListeners();
            this.forceUpdateDisplay();
            return true;
        }
        
        return false;
    }
    
    fallbackInitialization() {
        console.log('🆘 Using fallback initialization');
        // Force DOM query and setup with alternative methods
        this.setupEventListenersWithMutationObserver();
        this.forceUpdateDisplay();
    }
    
    showModal() {
        const modal = document.getElementById('reasoning-pal-modal');
        if (modal) {
            console.log('📱 Showing modal...');
            modal.style.display = 'flex';
            modal.style.visibility = 'visible';
            modal.style.opacity = '1';
            
            // Force immediate element access
            setTimeout(() => {
                modal.classList.add('show');
                this.focusTextarea();
                
                // Force element visibility and initialization
                this.forceElementsVisible();
                
                // Multiple initialization attempts
                setTimeout(() => this.forceUpdateDisplay(), 50);
                setTimeout(() => this.forceUpdateDisplay(), 200);
                setTimeout(() => this.forceUpdateDisplay(), 500);
            }, 10);
        } else {
            console.error('❌ Modal not found!');
        }
    }
    
    forceElementsVisible() {
        console.log('👁️ Forcing elements visible...');
        
        const textarea = document.getElementById('user-reasoning');
        const charCount = document.getElementById('char-count');
        const submitBtn = document.getElementById('submit-reasoning');
        
        if (textarea) {
            textarea.style.display = 'block';
            textarea.style.visibility = 'visible';
            textarea.style.opacity = '1';
        }
        
        if (charCount) {
            charCount.style.display = 'inline';
            charCount.style.visibility = 'visible';
            charCount.style.opacity = '1';
        }
        
        if (submitBtn) {
            submitBtn.style.display = 'block';
            submitBtn.style.visibility = 'visible';
            submitBtn.style.opacity = '1';
        }
        
        console.log('👁️ Elements forced visible:', {
            textarea: !!textarea,
            charCount: !!charCount,
            submitBtn: !!submitBtn
        });
    }
    
    hideModal() {
        const modal = document.getElementById('reasoning-pal-modal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => modal.style.display = 'none', 300);
        }
    }
    
    focusTextarea() {
        const textarea = document.getElementById('user-reasoning');
        if (textarea) {
            textarea.focus();
            // Force initial character count update
            setTimeout(() => {
                this.forceUpdateDisplay();
            }, 50);
        }
    }
    
    forceUpdateDisplay() {
        console.log('🔧 Force updating display...');
        this.updateCharacterCount();
        this.validateInput();
        
        // Force immediate DOM updates
        this.ensureElementsVisible();
        this.debugElementStates();
    }
    
    ensureElementsVisible() {
        const countEl = document.getElementById('char-count');
        const submitBtn = document.getElementById('submit-reasoning');
        
        if (countEl) {
            countEl.style.display = 'inline';
            countEl.style.visibility = 'visible';
        }
        
        if (submitBtn) {
            submitBtn.style.display = 'block';
            submitBtn.style.visibility = 'visible';
        }
    }
    
    debugElementStates() {
        const textarea = document.getElementById('user-reasoning');
        const countEl = document.getElementById('char-count');
        const submitBtn = document.getElementById('submit-reasoning');
        
        const textareaState = {
            exists: !!textarea,
            value: textarea ? textarea.value : 'N/A',
            visible: textarea ? textarea.offsetParent !== null : false,
            disabled: textarea ? textarea.disabled : undefined
        };
        const countState = {
            exists: !!countEl,
            textContent: countEl ? countEl.textContent : 'N/A',
            innerHTML: countEl ? countEl.innerHTML : 'N/A',
            visible: countEl ? countEl.offsetParent !== null : false
        };
        const submitState = {
            exists: !!submitBtn,
            disabled: submitBtn ? submitBtn.disabled : undefined,
            innerHTML: submitBtn ? submitBtn.innerHTML : 'N/A',
            visible: submitBtn ? submitBtn.offsetParent !== null : false
        };

        console.log('🔍 Debug element states:', {
            textarea: {
                exists: textareaState.exists,
                value: textareaState.value,
                visible: textareaState.visible,
                disabled: textareaState.disabled
            },
            charCount: {
                exists: countState.exists,
                textContent: countState.textContent,
                innerHTML: countState.innerHTML,
                visible: countState.visible
            },
            submitBtn: {
                exists: submitState.exists,
                disabled: submitState.disabled,
                innerHTML: submitState.innerHTML,
                visible: submitState.visible
            }
        });
    }
    
    setupEventListenersWithMutationObserver() {
        console.log('🔧 Setting up mutation observer fallback');
        
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.type === 'childList' || mutation.type === 'attributes') {
                    // Check if our elements are now available
                    const textarea = document.getElementById('user-reasoning');
                    if (textarea && !this.initialized) {
                        console.log('🎯 Elements detected via mutation observer');
                        this.setupEventListeners();
                        this.forceUpdateDisplay();
                        this.initialized = true;
                        observer.disconnect();
                    }
                }
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            attributes: true
        });
        
        // Disconnect after 10 seconds to prevent memory leaks
        setTimeout(() => observer.disconnect(), 10000);
    }
    
    setupEventListeners() {
        // Close button
        const closeBtn = document.querySelector('.reasoning-pal-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => this.hideModal());
        }
        
        // Close modal button
        const closeModalBtn = document.querySelector('.close-modal-btn');
        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', () => this.hideModal());
        }
        
        // Click outside to close
        const modal = document.getElementById('reasoning-pal-modal');
        if (modal) {
            modal.addEventListener('click', (e) => {
                if (e.target.id === 'reasoning-pal-modal') {
                    this.hideModal();
                }
            });
        }
        
        // Enhanced textarea input handling
        const textarea = document.getElementById('user-reasoning');
        if (textarea) {
            console.log('✅ Setting up textarea event listeners');
            
            // Create bound handlers to maintain context
            const handleInput = () => {
                console.log('📝 Textarea input detected:', textarea.value.length, 'characters');
                setTimeout(() => {
                    this.forceUpdateDisplay();
                }, 10);
            };
            
            const handleResize = () => {
                textarea.style.height = 'auto';
                textarea.style.height = Math.min(textarea.scrollHeight, 300) + 'px';
            };
            
            // Multiple event types to ensure we catch all input
            ['input', 'keyup', 'keydown', 'paste', 'change', 'blur', 'focus'].forEach(eventType => {
                textarea.addEventListener(eventType, handleInput, { passive: true });
            });
            
            // Auto-resize textarea
            textarea.addEventListener('input', handleResize, { passive: true });
            
            // Manual polling as fallback (checks every 500ms)
            this.startInputPolling();
            
        } else {
            console.warn('⚠️ Textarea not found during event listener setup');
        }
        
        // Direct event binding as fallback
        this.bindDirectEvents();
        
        // Submit button
        const submitBtn = document.getElementById('submit-reasoning');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => this.submitReasoning());
        }
        
        // Back to edit button
        const backBtn = document.getElementById('back-to-input');
        if (backBtn) {
            backBtn.addEventListener('click', () => this.showInputStep());
        }
        
        // Feedback buttons
        document.querySelectorAll('.feedback-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.selectFeedback(e.target.closest('.feedback-btn'));
                const rating = e.target.closest('.feedback-btn').dataset.rating;
                this.submitFeedback(rating);
            });
        });
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.hideModal();
            }
            if (e.ctrlKey && e.key === 'Enter') {
                if (this.currentStep === 'input') {
                    this.submitReasoning();
                }
            }
        });
    }
    
    setupAnswerFeedback() {
        const banner = document.querySelector('.answer-feedback-banner');
        if (!banner) return;
        
        const statusClass = this.isCorrect ? 'correct' : 'incorrect';
        const statusIcon = this.isCorrect ? '✓' : '✗';
        const statusText = this.isCorrect ? 'Correct Answer!' : 'Incorrect Answer';
        const statusMessage = this.isCorrect 
            ? `Great job! You selected option ${this.selectedAnswer}.`
            : `You selected option ${this.selectedAnswer}, but the correct answer is ${this.correctAnswer}.`;
        
        banner.className = `answer-feedback-banner ${statusClass}`;
        banner.innerHTML = `
            <div class="answer-status-icon">
                ${statusIcon}
            </div>
            <div class="answer-status-content">
                <h4>${statusText}</h4>
                <p>${statusMessage}</p>
            </div>
        `;
    }
    
    startInputPolling() {
        // Fallback polling mechanism
        this.pollingInterval = setInterval(() => {
            const textarea = document.getElementById('user-reasoning');
            if (textarea && this.lastKnownValue !== textarea.value) {
                console.log('🔄 Polling detected value change');
                this.lastKnownValue = textarea.value;
                this.forceUpdateDisplay();
            }
        }, 500);
    }
    
    bindDirectEvents() {
        // Direct DOM manipulation as ultimate fallback
        setTimeout(() => {
            const textarea = document.querySelector('#user-reasoning, [id="user-reasoning"]');
            if (textarea) {
                console.log('🔧 Binding direct events as fallback');
                textarea.oninput = () => this.forceUpdateDisplay();
                textarea.onkeyup = () => this.forceUpdateDisplay();
                textarea.onpaste = () => setTimeout(() => this.forceUpdateDisplay(), 20);
            }
        }, 1000);
    }
    
    updateCharacterCount() {
        const textarea = document.getElementById('user-reasoning');
        const countEl = document.getElementById('char-count');
        
        console.log('🔢 Updating character count...', { textarea: !!textarea, countEl: !!countEl });
        
        if (textarea && countEl) {
            const count = textarea.value.length;
            const maxChars = 1500;
            
            // Multiple methods to ensure display updates
            countEl.textContent = count;
            countEl.innerHTML = count;
            countEl.innerText = count;
            
            // Force DOM reflow
            countEl.style.display = 'none';
            countEl.offsetHeight; // Trigger reflow
            countEl.style.display = 'inline';
            
            console.log('✅ Character count updated to:', count);
            
            // Update styling based on character count
            const countContainer = countEl.parentElement;
            if (countContainer) {
                countContainer.classList.remove('warning', 'danger');
                
                if (count > maxChars * 0.9) {
                    countContainer.classList.add('danger');
                } else if (count > maxChars * 0.75) {
                    countContainer.classList.add('warning');
                }
            }
            
            // Prevent input beyond max
            if (count > maxChars) {
                textarea.value = textarea.value.substring(0, maxChars);
                this.updateCharacterCount(); // Recursive call to update display
            }
            
            return count;
        } else {
            console.warn('⚠️ Character count elements not found:', {
                textarea: !!textarea,
                countEl: !!countEl,
                textareaValue: textarea ? textarea.value : 'N/A'
            });
            
            // Try alternative selectors
            this.tryAlternativeSelectors();
            return 0;
        }
    }
    
    tryAlternativeSelectors() {
        console.log('🔍 Trying alternative selectors...');
        
        const alternatives = [
            { selector: '#user-reasoning', name: 'textarea' },
            { selector: 'textarea[id="user-reasoning"]', name: 'textarea-attr' },
            { selector: '.reasoning-textarea', name: 'textarea-class' },
            { selector: '#char-count', name: 'charcount' },
            { selector: 'span[id="char-count"]', name: 'charcount-attr' },
            { selector: '.character-count span', name: 'charcount-nested' }
        ];
        
        alternatives.forEach(alt => {
            const el = document.querySelector(alt.selector);
            console.log(`${alt.name}: ${!!el}`, el);
        });
    }
    
    validateInput() {
        const textarea = document.getElementById('user-reasoning');
        const submitBtn = document.getElementById('submit-reasoning');
        
        console.log('🔍 Validating input...', { textarea: !!textarea, submitBtn: !!submitBtn });
        
        if (textarea && submitBtn) {
            const reasoning = textarea.value.trim();
            const isValid = reasoning.length >= 10; // Minimum 10 characters
            
            console.log('📋 Validation result:', { 
                textLength: reasoning.length, 
                isValid,
                isSubmitting: this.isSubmitting 
            });
            
            // Force button state update
            submitBtn.disabled = !isValid || this.isSubmitting;
            
            // Multiple methods to ensure button updates
            if (isValid && !this.isSubmitting) {
                submitBtn.innerHTML = '<i class="bi bi-cpu"></i> Analyze My Reasoning';
                submitBtn.className = 'btn btn-primary btn-lg';
                submitBtn.style.pointerEvents = 'auto';
                console.log('✅ Button enabled');
            } else {
                const needed = Math.max(0, 10 - reasoning.length);
                submitBtn.innerHTML = `<i class="bi bi-cpu"></i> Need ${needed} more characters`;
                submitBtn.className = 'btn btn-secondary btn-lg';
                submitBtn.style.pointerEvents = this.isSubmitting ? 'none' : 'auto';
                console.log('❌ Button disabled, need', needed, 'more characters');
            }
            
            // Force DOM reflow
            submitBtn.style.display = 'none';
            submitBtn.offsetHeight; // Trigger reflow
            submitBtn.style.display = 'block';
            
        } else {
            console.warn('⚠️ Validation elements not found:', {
                textarea: !!textarea,
                submitBtn: !!submitBtn
            });
        }
    }
    
    cleanup() {
        console.log('🧹 Cleaning up ReasoningPal resources');
        if (this.pollingInterval) {
            clearInterval(this.pollingInterval);
        }
    }
    
    hideModal() {
        const modal = document.getElementById('reasoning-pal-modal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.style.display = 'none';
                this.cleanup();
            }, 300);
        }
    }
    
    async submitReasoning() {
        if (this.isSubmitting) return;
        
        const textarea = document.getElementById('user-reasoning');
        const reasoning = textarea.value.trim();
        
        if (reasoning.length < 10) {
            this.showError('Please provide at least 10 characters of reasoning.');
            return;
        }
        
        this.userReasoning = reasoning;
        this.isSubmitting = true;
        
        // Show analysis step with loading
        this.showAnalysisStep();
        this.showLoading();
        
        try {
            const response = await this.callReasoningAPI();
            this.displayAnalysis(response);
        } catch (error) {
            console.error('Error submitting reasoning:', error);
            this.showError('Failed to analyze reasoning. Please try again.');
            this.showInputStep();
        } finally {
            this.isSubmitting = false;
        }
    }
    
    showInputStep() {
        this.currentStep = 'input';
        document.getElementById('reasoning-input-step').style.display = 'block';
        document.getElementById('reasoning-analysis-step').style.display = 'none';
        this.focusTextarea();
        this.validateInput();
    }
    
    showAnalysisStep() {
        this.currentStep = 'analysis';
        document.getElementById('reasoning-input-step').style.display = 'none';
        document.getElementById('reasoning-analysis-step').style.display = 'block';
    }
    
    showLoading() {
        const responseContainer = document.getElementById('reasoning-response');
        responseContainer.innerHTML = `
            <div class="loading-spinner text-center py-4">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Analyzing...</span>
                </div>
                <p class="mt-3 text-muted">Analyzing your clinical reasoning...</p>
                <small class="text-muted">This may take a few moments</small>
            </div>
        `;
    }
    
    async callReasoningAPI() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        const response = await fetch('/reasoning-pal/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                mcq_id: this.mcqId,
                user_reasoning: this.userReasoning,
                is_correct: this.isCorrect,
                selected_answer: this.selectedAnswer,
                correct_answer: this.correctAnswer
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }
    
    displayAnalysis(data) {
        const responseContainer = document.getElementById('reasoning-response');
        
        if (data.success && data.analysis) {
            responseContainer.innerHTML = `
                <div class="analysis-content">
                    ${this.formatAnalysisText(data.analysis)}
                </div>
            `;
        } else {
            this.showError(data.error || 'Failed to analyze reasoning.');
            this.showInputStep();
        }
    }
    
    formatAnalysisText(text) {
        // Simple formatting for better readability
        return text
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>')
            .replace(/^/, '<p>')
            .replace(/$/, '</p>')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>');
    }
    
    selectFeedback(button) {
        // Remove selected class from all feedback buttons
        document.querySelectorAll('.feedback-btn').forEach(btn => {
            btn.classList.remove('selected');
        });
        
        // Add selected class to clicked button
        button.classList.add('selected');
    }
    
    async submitFeedback(rating) {
        try {
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            
            await fetch('/reasoning-feedback/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({
                    mcq_id: this.mcqId,
                    rating: rating,
                    user_reasoning: this.userReasoning
                })
            });
        } catch (error) {
            console.error('Error submitting feedback:', error);
        }
    }
    
    showError(message) {
        // Simple error display
        const errorDiv = document.createElement('div');
        errorDiv.className = 'alert alert-danger alert-dismissible fade show mt-3';
        errorDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        // Insert after textarea
        const textarea = document.getElementById('user-reasoning');
        if (textarea) {
            textarea.parentNode.insertBefore(errorDiv, textarea.nextSibling);
            
            // Auto-remove after 5 seconds
            setTimeout(() => {
                if (errorDiv.parentNode) {
                    errorDiv.remove();
                }
            }, 5000);
        }
    }
}

// Global function to open ReasoningPal
function openReasoningPal(mcqId, isCorrect, selectedAnswer, correctAnswer) {
    if (window.currentReasoningPal) {
        window.currentReasoningPal.hideModal();
    }
    
    window.currentReasoningPal = new ReasoningPalEnhanced(mcqId, isCorrect, selectedAnswer, correctAnswer);
    window.currentReasoningPal.init();
}
