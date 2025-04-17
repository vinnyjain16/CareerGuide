/**
 * JavaScript for the career assessment functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Get all question sections
    const questionSections = document.querySelectorAll('.question-section');
    const totalQuestions = questionSections.length;
    const progressBar = document.getElementById('progressBar');
    
    // Current question index (0-based)
    let currentQuestionIndex = 0;
    
    // Update progress bar
    function updateProgress() {
        const progressPercentage = Math.round(((currentQuestionIndex + 1) / totalQuestions) * 100);
        progressBar.style.width = progressPercentage + '%';
        progressBar.setAttribute('aria-valuenow', progressPercentage);
        progressBar.textContent = progressPercentage + '%';
    }
    
    // Show a specific question
    function showQuestion(index) {
        // Hide all questions
        questionSections.forEach(section => {
            section.style.display = 'none';
        });
        
        // Show the current question
        questionSections[index].style.display = 'block';
        
        // Update progress
        currentQuestionIndex = index;
        updateProgress();
        
        // Scroll to top of question
        window.scrollTo({
            top: document.getElementById('assessmentForm').offsetTop - 100,
            behavior: 'smooth'
        });
    }
    
    // Handle "Next" button clicks
    const nextButtons = document.querySelectorAll('.next-question-btn');
    nextButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the current question section
            const currentSection = questionSections[currentQuestionIndex];
            
            // Check if the question has been answered
            const radioButtons = currentSection.querySelectorAll('input[type="radio"]');
            let answered = false;
            
            radioButtons.forEach(radio => {
                if (radio.checked) {
                    answered = true;
                }
            });
            
            // If not answered, show validation message
            if (!answered) {
                // Add validation styling or message
                const options = currentSection.querySelector('.options');
                options.classList.add('is-invalid');
                
                // Create or update validation message
                let validationMessage = currentSection.querySelector('.invalid-feedback');
                if (!validationMessage) {
                    validationMessage = document.createElement('div');
                    validationMessage.className = 'invalid-feedback';
                    validationMessage.textContent = 'Please select an option before continuing.';
                    options.after(validationMessage);
                    validationMessage.style.display = 'block';
                }
                
                return;
            }
            
            // Move to next question if answered
            if (currentQuestionIndex < totalQuestions - 1) {
                showQuestion(currentQuestionIndex + 1);
            }
        });
    });
    
    // Handle "Previous" button clicks
    const prevButtons = document.querySelectorAll('.prev-question-btn');
    prevButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (currentQuestionIndex > 0) {
                showQuestion(currentQuestionIndex - 1);
            }
        });
    });
    
    // Add event listeners for radio buttons to remove validation styling
    questionSections.forEach(section => {
        const radioButtons = section.querySelectorAll('input[type="radio"]');
        const options = section.querySelector('.options');
        
        radioButtons.forEach(radio => {
            radio.addEventListener('change', function() {
                if (options.classList.contains('is-invalid')) {
                    options.classList.remove('is-invalid');
                    const validationMessage = section.querySelector('.invalid-feedback');
                    if (validationMessage) {
                        validationMessage.style.display = 'none';
                    }
                }
            });
        });
    });
    
    // Form submission validation
    const assessmentForm = document.getElementById('assessmentForm');
    if (assessmentForm) {
        assessmentForm.addEventListener('submit', function(event) {
            // Check if all questions are answered
            let allAnswered = true;
            questionSections.forEach((section, index) => {
                const questionId = section.id.replace('question-', '');
                const radioName = `q${questionId}`;
                const answered = document.querySelector(`input[name="${radioName}"]:checked`);
                
                if (!answered) {
                    allAnswered = false;
                    // Show the first unanswered question
                    if (currentQuestionIndex !== index) {
                        showQuestion(index);
                    }
                    
                    // Add validation styling
                    const options = section.querySelector('.options');
                    options.classList.add('is-invalid');
                    
                    // Create validation message
                    let validationMessage = section.querySelector('.invalid-feedback');
                    if (!validationMessage) {
                        validationMessage = document.createElement('div');
                        validationMessage.className = 'invalid-feedback';
                        validationMessage.textContent = 'Please select an option.';
                        options.after(validationMessage);
                        validationMessage.style.display = 'block';
                    }
                }
            });
            
            if (!allAnswered) {
                event.preventDefault();
                return false;
            }
            
            // Show loading indicator
            const submitButton = document.querySelector('button[type="submit"]');
            submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Processing...';
            submitButton.disabled = true;
            
            return true;
        });
    }
    
    // Initialize the first question
    showQuestion(0);
});
