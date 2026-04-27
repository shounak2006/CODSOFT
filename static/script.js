document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatWindow = document.getElementById('chat-window');
    const typingIndicator = document.getElementById('typing-indicator');

    // Function to scroll to the bottom of the chat
    const scrollToBottom = () => {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    };

    // Construct the DOM elements for a message
    const appendMessage = (text, sender) => {
        // Group container
        const groupDiv = document.createElement('div');
        groupDiv.classList.add('message-group');
        groupDiv.classList.add(sender === 'user' ? 'user-group' : 'bot-group');

        // Bubble container
        const bubbleDiv = document.createElement('div');
        bubbleDiv.classList.add('chat-bubble');
        bubbleDiv.classList.add(sender === 'user' ? 'user-bubble' : 'bot-bubble');
        
        // Use innerHTML for bot to support basic bolding if desired, textContent for user safety
        if (sender === 'user') {
            bubbleDiv.textContent = text;
        } else {
            bubbleDiv.innerHTML = text.replace(/\n/g, '<br>');
        }

        groupDiv.appendChild(bubbleDiv);
        
        // Insert before typing indicator so the indicator is always at the bottom
        chatWindow.insertBefore(groupDiv, typingIndicator);
        scrollToBottom();
    };

    const showTyping = () => {
        typingIndicator.classList.remove('hidden');
        scrollToBottom();
    };

    const hideTyping = () => {
        typingIndicator.classList.add('hidden');
    };

    // Handle form submission
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = chatInput.value.trim();
        if (!message) return;

        // Render user message & clear input
        appendMessage(message, 'user');
        chatInput.value = '';
        chatInput.focus();

        // Show typing indicator
        showTyping();

        try {
            // API call to the Flask backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            
            // Artificial delay to make it feel more "human" and let animation play
            setTimeout(() => {
                hideTyping();
                appendMessage(data.response, 'bot');
            }, 600 + Math.random() * 400); // Between 600ms and 1000ms

        } catch (error) {
            console.error("Error communicating with AI:", error);
            hideTyping();
            appendMessage("⚠️ Connection error. Make sure the Flask server is running.", 'bot');
        }
    });

    // Make sure initial layout is scrolled correctly
    scrollToBottom();
});
