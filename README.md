# Rule-Based Chatbot - CODSOFT AI Internship Task 1

## 📋 Project Overview

A sophisticated rule-based chatbot that uses pattern matching and predefined rules to engage in natural conversations. Built as part of the CODSOFT Artificial Intelligence internship program.

## ✨ Features

### Core Capabilities
- **Pattern Matching**: Uses regular expressions to identify user intents
- **Natural Conversation Flow**: Maintains context and conversation history
- **Dynamic Responses**: Provides varied responses to avoid repetition
- **Name Recognition**: Captures and remembers user names during conversation
- **Time & Date Queries**: Responds with current time and date
- **Basic Calculations**: Performs simple arithmetic operations
- **Multi-Category Support**: Handles 20+ different conversation categories

### Conversation Categories
1. **Greetings**: Hi, hello, good morning, etc.
2. **Farewells**: Bye, goodbye, see you, etc.
3. **Identity**: Bot name, purpose, creator information
4. **Wellbeing**: How are you, emotional responses
5. **Help**: Capabilities and features
6. **Time & Date**: Current time and date queries
7. **Weather**: Weather information (with limitations)
8. **Mathematics**: Basic arithmetic calculations
9. **Thanks**: Gratitude expressions
10. **Bot Information**: How the bot works, its creation
11. **Age**: Bot's age queries
12. **Jokes**: Programming and tech jokes
13. **Hobbies**: Bot's interests
14. **Compliments**: Positive feedback handling
15. **Negative Feedback**: Constructive criticism handling
16. **Affirmation**: Yes/no responses
17. **Programming**: Code and development topics
18. **AI/ML**: Artificial intelligence discussions

## 🛠️ Technical Implementation

### Technologies Used
- **Python 3.9+**
- **Regular Expressions (re module)**: For pattern matching
- **datetime module**: For time and date functionality
- **random module**: For response variation
- **Type hints**: For better code documentation

### Key Components

#### 1. RuleBasedChatbot Class
Main class that handles all chatbot functionality.

```python
class RuleBasedChatbot:
    def __init__(self, bot_name: str = "AssistBot")
    def get_response(self, user_input: str) -> str
    def start_conversation(self)
```

#### 2. Pattern Matching System
Uses regex patterns organized by category:

```python
patterns = {
    "category_name": [
        (r'pattern_regex', ['response1', 'response2', ...]),
        ...
    ]
}
```

#### 3. Response Formatting
Dynamically formats responses with:
- Current time/date
- Captured names
- Calculation results
- Context-aware personalization

## 📦 Installation & Usage

### Prerequisites
- Python 3.9 or higher
- Flask (`pip install Flask`)

### Running the Web Application

I have completely upgraded this project to be a full-stack Web Application with a premium UI.

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Start the Local Web Server**:
```bash
python app.py
```

3. **Open Your Browser**:
Head over to `http://127.0.0.1:5000` in your web browser. You will be greeted by a modern, minimalist dark-mode interface where you can chat with AssistBot organically!

*(Note: If you still want to run the raw terminal version without the UI, you can still execute `python chatbot.py`)*

## 💡 Example Conversations

### Basic Greeting
```
You: Hello!
Bot: Hi there! What can I do for you?

You: My name is Shounak
Bot: Nice to meet you, Shounak!

You: How are you?
Bot: I'm functioning perfectly! Thanks for asking. How are you?
```

### Calculations
```
You: What is 15 plus 27?
Bot: The sum of 15 and 27 is 42.

You: What is 100 divided by 5?
Bot: 100 divided by 5 is 20.0.
```

### Time and Date
```
You: What's the time?
Bot: The current time is 03:45 PM.

You: What's today's date?
Bot: Today's date is April 28, 2026.
```

### Entertainment
```
You: Tell me a joke
Bot: Why don't programmers like nature? It has too many bugs! 🐛

You: That's funny!
Bot: Thank you so much! That makes me happy! 😊
```

## 🏗️ Architecture

### Class Structure
```
RuleBasedChatbot
├── __init__()              # Initialize bot with patterns
├── _initialize_patterns()  # Setup all conversation patterns
├── _match_pattern()        # Match user input to patterns
├── _format_response()      # Format dynamic responses
├── get_response()          # Main response generation
├── _get_default_response() # Fallback responses
├── start_conversation()    # Interactive chat loop
├── get_conversation_history() # Retrieve chat history
└── clear_history()         # Reset conversation
```

### Data Flow
```
User Input
    ↓
Pattern Matching
    ↓
Category Identification
    ↓
Response Selection
    ↓
Dynamic Formatting
    ↓
Bot Response
```

## 🎯 Learning Outcomes

This project demonstrates understanding of:

1. **Natural Language Processing**
   - Text pattern recognition
   - Intent classification
   - Context management

2. **Software Design**
   - Object-oriented programming
   - Clean code principles
   - Type annotations
   - Error handling

3. **Conversation Flow**
   - Multi-turn conversations
   - Context preservation
   - Dynamic response generation

4. **Python Programming**
   - Regular expressions
   - Data structures
   - String manipulation
   - Control flow

## 📈 Future Enhancements

Potential improvements for version 2.0:

1. **Sentiment Analysis**: Detect user emotions and respond appropriately
2. **Learning Capability**: Save and learn from conversations
3. **Multi-language Support**: Add support for other languages
4. **Voice Integration**: Add speech-to-text and text-to-speech
5. **API Integration**: Connect to real weather, news, or other APIs
6. **Web Interface**: Build a GUI or web interface
7. **Database Integration**: Store conversations in a database
8. **Advanced NLP**: Implement word embeddings or transformers

## 🐛 Known Limitations

1. No real machine learning - uses predefined rules only
2. Cannot handle complex, nuanced conversations
3. No real-time data access (weather, news, etc.)
4. Limited context understanding across multiple turns
5. Cannot learn from interactions without code updates

## 📝 Code Quality

- **Type Hints**: Used throughout for better documentation
- **Docstrings**: All functions have detailed documentation
- **Clean Code**: Follows PEP 8 style guidelines
- **Error Handling**: Robust exception handling
- **Modularity**: Well-organized, reusable code structure

## 👨‍💻 Development

### Testing the Chatbot

Test various scenarios:

```python
# Create a bot instance
bot = RuleBasedChatbot()

# Test individual responses
response = bot.get_response("Hello!")
print(response)

# View conversation history
history = bot.get_conversation_history()
print(history)

# Clear history
bot.clear_history()
```

### Adding New Patterns

To add new conversation patterns:

```python
# In _initialize_patterns() method, add:
"new_category": [
    (r'regex_pattern', [
        "Response 1",
        "Response 2",
        "Response 3"
    ])
]
```

## 📄 License

This project is created for educational purposes as part of the CODSOFT AI internship program.

## 🤝 Contributing

This is an internship project, but suggestions for improvements are welcome!

## 📞 Contact

- **Project**: CODSOFT AI Internship Task 1
- **Topic**: Rule-Based Chatbot
- **Date**: April 2026

## 🙏 Acknowledgments

- CODSOFT for the internship opportunity
- Python community for excellent documentation
- Fellow interns for inspiration and support

---

**Note**: This is a rule-based chatbot for learning purposes. For production applications, consider using machine learning-based approaches like transformers or neural networks.
