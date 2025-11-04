// Main JavaScript for Neurology MCQ Reader

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Add current year to footer
    const yearEl = document.querySelector('.footer-year');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }
    
    // Handle flash message dismissal
    const flashMessages = document.querySelectorAll('.alert-dismissible');
    flashMessages.forEach(function(alert) {
        const closeBtn = alert.querySelector('.btn-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                alert.remove();
            });
            
            // Auto-dismiss after 5 seconds
            setTimeout(function() {
                alert.remove();
            }, 5000);
        }
    });
});