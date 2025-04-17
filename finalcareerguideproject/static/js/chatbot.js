/**
 * JavaScript for the AI-powered CareerBot functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const suggestedQuestions = document.querySelectorAll('.suggested-question');
    
    // Function to add a message to the chat
    function addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = isUser ? 'message user-message' : 'message bot-message';
        
        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        
        const icon = document.createElement('i');
        icon.className = isUser ? 'fas fa-user' : 'fas fa-robot';
        avatarDiv.appendChild(icon);
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = content;
        
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);
        
        chatMessages.appendChild(messageDiv);
        
        // Scroll to the bottom of the chat
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to show typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-message';
        typingDiv.id = 'typing-indicator';
        
        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        
        const icon = document.createElement('i');
        icon.className = 'fas fa-robot';
        avatarDiv.appendChild(icon);
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content typing-indicator';
        
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('div');
            dot.className = 'typing-dot';
            contentDiv.appendChild(dot);
        }
        
        typingDiv.appendChild(avatarDiv);
        typingDiv.appendChild(contentDiv);
        
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    // Function to send user message to the server and get a response
    async function sendMessage(message) {
        try {
            // Show typing indicator
            showTypingIndicator();
            
            // Get CSRF token
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            
            // Send the message to the server
            const response = await fetch('/ask_bot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ question: message }),
            });
            
            if (!response.ok) {
                throw new Error('Failed to get response from server');
            }
            
            const data = await response.json();
            
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add bot response
            if (data.error) {
                addMessage(`<p class="text-danger">Error: ${data.error}</p>`, false);
            } else {
                // Format the response text with paragraphs
                const formattedResponse = data.response
                    .split('\n\n')
                    .map(paragraph => `<p>${paragraph}</p>`)
                    .join('');
                
                addMessage(formattedResponse, false);
            }
        } catch (error) {
            console.error('Error:', error);
            removeTypingIndicator();
            addMessage('<p class="text-danger">Sorry, there was an error processing your request. Please try again later.</p>', false);
        }
    }
    
    // Handle form submission
    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const message = userInput.value.trim();
        
        if (message === '') {
            return;
        }
        
        // Add user message to chat
        addMessage(`<p>${message}</p>`, true);
        
        // Clear input field
        userInput.value = '';
        
        // Send message to server
        sendMessage(message);
    });
    
    // Handle suggested questions
    suggestedQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const message = this.textContent.trim();
            
            // Add user message to chat
            addMessage(`<p>${message}</p>`, true);
            
            // Send message to server
            sendMessage(message);
        });
    });
    
    // Handle Enter key in input field
    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            chatForm.dispatchEvent(new Event('submit'));
        }
    });
    
    // Focus on input field when the page loads
    userInput.focus();
});
