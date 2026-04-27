"""
Test Script for Rule-Based Chatbot
CODSOFT AI Internship - Task 1

This script demonstrates the chatbot's capabilities through automated testing.
"""

from chatbot import RuleBasedChatbot


def print_separator(title=""):
    """Print a formatted separator line."""
    if title:
        print(f"\n{'='*70}")
        print(f"  {title}")
        print(f"{'='*70}\n")
    else:
        print(f"{'='*70}\n")


def test_interaction(bot, user_input, description=""):
    """Test a single interaction and display results."""
    if description:
        print(f"[{description}]")
    print(f"You: {user_input}")
    response = bot.get_response(user_input)
    print(f"Bot: {response}\n")


def run_comprehensive_tests():
    """Run comprehensive tests covering all chatbot capabilities."""
    
    print_separator("RULE-BASED CHATBOT - COMPREHENSIVE TEST SUITE")
    
    # Create bot instance
    bot = RuleBasedChatbot(bot_name="TestBot")
    
    # Test 1: Greetings
    print_separator("Test 1: Greeting Patterns")
    test_interaction(bot, "Hello!", "Basic greeting")
    test_interaction(bot, "Good morning", "Time-based greeting")
    test_interaction(bot, "Hey there", "Casual greeting")
    
    # Test 2: Name Introduction
    print_separator("Test 2: Name Recognition")
    test_interaction(bot, "My name is Shounak", "User introduces themselves")
    test_interaction(bot, "What is your name?", "Asking bot's name")
    
    # Test 3: Wellbeing
    print_separator("Test 3: Wellbeing Exchange")
    test_interaction(bot, "How are you?", "Asking bot's status")
    test_interaction(bot, "I'm doing great!", "User feeling good")
    test_interaction(bot, "I'm feeling sad", "User feeling down")
    
    # Test 4: Help and Capabilities
    print_separator("Test 4: Help Queries")
    test_interaction(bot, "What can you do?", "Asking capabilities")
    test_interaction(bot, "Help me", "General help request")
    
    # Test 5: Time and Date
    print_separator("Test 5: Time & Date Queries")
    test_interaction(bot, "What time is it?", "Current time")
    test_interaction(bot, "What's today's date?", "Current date")
    
    # Test 6: Calculations
    print_separator("Test 6: Mathematical Calculations")
    test_interaction(bot, "What is 25 plus 17?", "Addition")
    test_interaction(bot, "What is 100 minus 35?", "Subtraction")
    test_interaction(bot, "What is 12 times 8?", "Multiplication")
    test_interaction(bot, "What is 144 divided by 12?", "Division")
    
    # Test 7: Weather Query
    print_separator("Test 7: Weather Information")
    test_interaction(bot, "What's the weather like?", "Weather query")
    
    # Test 8: Bot Information
    print_separator("Test 8: Bot Identity & Information")
    test_interaction(bot, "Who created you?", "Creator query")
    test_interaction(bot, "How do you work?", "Functionality query")
    test_interaction(bot, "How old are you?", "Age query")
    
    # Test 9: Entertainment
    print_separator("Test 9: Entertainment Features")
    test_interaction(bot, "Tell me a joke", "Joke request")
    test_interaction(bot, "What do you like to do?", "Hobbies query")
    
    # Test 10: Feedback
    print_separator("Test 10: Feedback Handling")
    test_interaction(bot, "You are awesome!", "Positive feedback")
    test_interaction(bot, "Thank you so much", "Gratitude")
    
    # Test 11: Topic-Specific
    print_separator("Test 11: Topic-Specific Conversations")
    test_interaction(bot, "I love Python programming", "Programming topic")
    test_interaction(bot, "Tell me about artificial intelligence", "AI topic")
    
    # Test 12: Affirmation
    print_separator("Test 12: Affirmation Responses")
    test_interaction(bot, "Yes", "Simple yes")
    test_interaction(bot, "Okay, sure", "Affirmative response")
    
    # Test 13: Unknown Input
    print_separator("Test 13: Unrecognized Input Handling")
    test_interaction(bot, "xyzabc random text", "Random input")
    test_interaction(bot, "Quantum mechanics of superposition", "Complex unknown topic")
    
    # Test 14: Farewell
    print_separator("Test 14: Conversation Ending")
    test_interaction(bot, "Goodbye!", "Farewell")
    
    # Display Statistics
    print_separator("Test Results Summary")
    history = bot.get_conversation_history()
    print(f"Total Exchanges: {len(history) // 2}")
    print(f"User Messages: {len([x for x in history if x[0] == 'user'])}")
    print(f"Bot Responses: {len([x for x in history if x[0] == 'bot'])}")
    print(f"\nAll tests completed successfully! ✓")
    print_separator()


def demonstrate_features():
    """Demonstrate key features with explanatory text."""
    
    print_separator("CHATBOT FEATURES DEMONSTRATION")
    
    bot = RuleBasedChatbot(bot_name="DemoBot")
    
    print("Feature 1: PATTERN MATCHING")
    print("The bot uses regex patterns to understand different ways of asking the same thing.\n")
    test_interaction(bot, "hi", "Variation 1")
    test_interaction(bot, "hello there", "Variation 2")
    test_interaction(bot, "hey", "Variation 3")
    
    print("\nFeature 2: CONTEXT AWARENESS")
    print("The bot remembers your name and uses it in conversations.\n")
    test_interaction(bot, "I am Shounak", "Name introduction")
    test_interaction(bot, "How are you?", "Bot may use your name")
    
    print("\nFeature 3: DYNAMIC RESPONSES")
    print("The bot provides different responses to avoid repetition.\n")
    for i in range(3):
        test_interaction(bot, "Hello", f"Greeting attempt {i+1}")
    
    print("\nFeature 4: REAL-TIME DATA")
    print("The bot can provide current time and date.\n")
    test_interaction(bot, "What time is it?", "Live time")
    test_interaction(bot, "What's the date?", "Live date")
    
    print("\nFeature 5: CALCULATIONS")
    print("The bot can perform mathematical operations.\n")
    test_interaction(bot, "What is 15 plus 25?", "Math processing")
    
    print("\nFeature 6: CONVERSATION FLOW")
    print("The bot maintains natural conversation flow.\n")
    test_interaction(bot, "Tell me a joke", "Entertainment")
    test_interaction(bot, "That's funny!", "Response to joke")
    test_interaction(bot, "Thanks", "Gratitude")
    
    print_separator("Features demonstration completed!")


def show_conversation_history_example():
    """Demonstrate conversation history tracking."""
    
    print_separator("CONVERSATION HISTORY TRACKING")
    
    bot = RuleBasedChatbot()
    
    # Have a conversation
    conversation = [
        "Hello!",
        "My name is John",
        "What can you do?",
        "Tell me a joke",
        "Thanks!"
    ]
    
    print("Having a sample conversation...\n")
    for msg in conversation:
        response = bot.get_response(msg)
        print(f"User: {msg}")
        print(f"Bot: {response}\n")
    
    # Show history
    print("\nConversation History:")
    print("-" * 70)
    history = bot.get_conversation_history()
    for i, (speaker, message) in enumerate(history, 1):
        speaker_label = "User" if speaker == "user" else "Bot"
        print(f"{i}. {speaker_label}: {message}")
    
    print(f"\n{'-' * 70}")
    print(f"Total messages in history: {len(history)}")
    print_separator()


def main():
    """Main function to run all demonstrations."""
    
    print("\n" + "="*70)
    print("  CHATBOT TEST & DEMONSTRATION SUITE")
    print("  CODSOFT AI Internship - Task 1")
    print("="*70)
    
    print("\nChoose an option:")
    print("1. Run comprehensive tests")
    print("2. Feature demonstration")
    print("3. Conversation history example")
    print("4. Interactive chat")
    print("5. Run all (1, 2, and 3)")
    
    try:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            run_comprehensive_tests()
        elif choice == "2":
            demonstrate_features()
        elif choice == "3":
            show_conversation_history_example()
        elif choice == "4":
            bot = RuleBasedChatbot()
            bot.start_conversation()
        elif choice == "5":
            run_comprehensive_tests()
            demonstrate_features()
            show_conversation_history_example()
        else:
            print("Invalid choice. Running interactive chat...")
            bot = RuleBasedChatbot()
            bot.start_conversation()
            
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()
