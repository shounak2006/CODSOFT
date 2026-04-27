"""
Rule-Based Chatbot with Pattern Matching
CODSOFT AI Internship - Task 1

A chatbot that responds to user inputs using predefined rules,
pattern matching, and if-else logic to handle various conversation scenarios.
"""

import re
import random
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class RuleBasedChatbot:
    """
    A sophisticated rule-based chatbot that uses pattern matching
    and predefined rules to engage in conversations.
    """
    
    def __init__(self, bot_name: str = "AssistBot"):
        self.bot_name = bot_name
        self.user_name: Optional[str] = None
        self.conversation_history: List[Tuple[str, str]] = []
        self.context: Dict[str, any] = {}
        
        # Define patterns and responses
        self.patterns = self._initialize_patterns()
        
    def _initialize_patterns(self) -> Dict[str, List[Tuple[str, List[str]]]]:
        """
        Initialize all conversation patterns with their corresponding responses.
        Returns a dictionary mapping categories to pattern-response pairs.
        """
        return {
            # Greetings
            "greetings": [
                (r'\b(hi|hello|hey|hola|greetings)\b', [
                    "Hello! How can I help you today?",
                    "Hi there! What can I do for you?",
                    "Hey! Nice to meet you. How may I assist you?",
                    "Greetings! I'm here to help. What's on your mind?"
                ]),
                (r'\b(good morning|good afternoon|good evening)\b', [
                    "Good day! How can I assist you?",
                    "Hello! Hope you're having a great day. What can I help with?",
                    "Hi! Thanks for reaching out. How may I help you?"
                ])
            ],
            
            # Farewell
            "farewell": [
                (r'\b(bye|goodbye|see you|farewell|exit|quit)\b', [
                    "Goodbye! Have a wonderful day!",
                    "See you later! Feel free to come back anytime.",
                    "Farewell! It was nice chatting with you.",
                    "Bye! Take care and have a great day ahead!"
                ])
            ],
            
            # Name introduction
            "name_query": [
                (r'\b(what is your name|what\'s your name|who are you|your name)\b', [
                    f"I'm {self.bot_name}, your friendly AI assistant!",
                    f"My name is {self.bot_name}. I'm here to help you!",
                    f"I'm called {self.bot_name}, nice to meet you!"
                ])
            ],
            
            # User name capture
            "user_name": [
                (r'\bmy name is (\w+)\b', [
                    "Nice to meet you, {name}!",
                    "Hello {name}! Great to know your name.",
                    "Pleased to meet you, {name}!"
                ]),
                (r'\bi am (\w+)\b', [
                    "Hi {name}! How can I help you today?",
                    "Nice to meet you, {name}!",
                    "Hello {name}! What brings you here?"
                ])
            ],
            
            # How are you
            "wellbeing": [
                (r'\bhow are you\b|\bhow\'re you\b', [
                    "I'm functioning perfectly! Thanks for asking. How are you?",
                    "I'm doing great! How about you?",
                    "All systems operational! How can I help you today?",
                    "I'm excellent! What can I do for you?"
                ]),
                (r'\b(i am|i\'m) (good|great|fine|okay|ok|well)\b', [
                    "That's wonderful to hear! How can I assist you?",
                    "Glad you're doing well! What brings you here?",
                    "Great! What can I help you with today?"
                ]),
                (r'\b(i am|i\'m) (sad|bad|not good|terrible|awful)\b', [
                    "I'm sorry to hear that. Is there anything I can help with?",
                    "That's tough. Want to talk about it? Maybe I can help.",
                    "I understand. How can I assist you today?"
                ])
            ],
            
            # Help and capabilities
            "help": [
                (r'\b(help|what can you do|capabilities|features)\b', [
                    "I can help you with various queries! I can provide information, answer questions, have casual conversations, and more. What do you need help with?",
                    "I'm here to assist! I can chat, answer questions, provide information, and have meaningful conversations. What would you like to know?",
                    "I can help with many things! Ask me about time, date, calculations, or just chat with me. What interests you?"
                ])
            ],
            
            # Time queries
            "time": [
                (r'\b(what time|current time|what\'s the time|time now)\b', [
                    "The current time is {time}.",
                    "It's {time} right now.",
                    "Right now it's {time}."
                ])
            ],
            
            # Date queries
            "date": [
                (r'\b(what date|current date|what\'s the date|date today|today\'s date)\b', [
                    "Today's date is {date}.",
                    "It's {date} today.",
                    "The current date is {date}."
                ])
            ],
            
            # Weather (simulated)
            "weather": [
                (r'\b(weather|temperature|forecast)\b', [
                    "I don't have real-time weather data, but you can check weather.com or use a weather app for accurate forecasts!",
                    "I'm unable to check live weather, but I'd recommend checking your local weather service for the most accurate information.",
                    "For real-time weather updates, I suggest checking a weather website or app. I don't have access to current conditions."
                ])
            ],
            
            # Simple calculations
            "math": [
                (r'\bcalculate\b|\bsolve\b', [
                    "I can help with simple calculations! Try asking something like 'what is 5 plus 3' or '10 times 2'.",
                    "I can do basic math! Ask me to add, subtract, multiply, or divide numbers."
                ]),
                (r'what is (\d+) (plus|add|\+) (\d+)', [
                    "The sum of {num1} and {num2} is {result}."
                ]),
                (r'what is (\d+) (minus|subtract|\-) (\d+)', [
                    "{num1} minus {num2} equals {result}."
                ]),
                (r'what is (\d+) (times|multiply|\*|multiplied by) (\d+)', [
                    "{num1} multiplied by {num2} is {result}."
                ]),
                (r'what is (\d+) (divided by|divide|/) (\d+)', [
                    "{num1} divided by {num2} is {result}."
                ])
            ],
            
            # Thanks
            "thanks": [
                (r'\b(thank|thanks|thank you|thx)\b', [
                    "You're welcome! Happy to help!",
                    "No problem at all! Anything else I can do?",
                    "My pleasure! Feel free to ask if you need anything else.",
                    "Glad I could help! Is there anything else you'd like to know?"
                ])
            ],
            
            # Bot information
            "bot_info": [
                (r'\b(who created you|who made you|your creator)\b', [
                    "I was created as part of the CODSOFT AI internship project by a passionate developer learning AI and NLP!",
                    "I'm a rule-based chatbot built as an internship task to demonstrate natural language processing concepts.",
                    "I was developed as an AI project to showcase conversation flow and pattern matching techniques!"
                ]),
                (r'\b(how do you work|how are you built|what are you)\b', [
                    "I'm a rule-based chatbot that uses pattern matching and if-else logic to understand and respond to your messages!",
                    "I work by matching patterns in your text with predefined rules and providing appropriate responses.",
                    "I use natural language processing techniques like pattern matching to understand your queries and respond accordingly."
                ])
            ],
            
            # Age query
            "age": [
                (r'\b(how old are you|what is your age|your age)\b', [
                    "I'm ageless! I exist in the digital realm where time works differently.",
                    "I was created recently, so I'm quite young in bot years!",
                    "Age doesn't apply to me, but I'm constantly learning and improving!"
                ])
            ],
            
            # Jokes
            "jokes": [
                (r'\b(tell me a joke|joke|make me laugh|funny)\b', [
                    "Why don't programmers like nature? It has too many bugs! 🐛",
                    "Why do programmers prefer dark mode? Because light attracts bugs! 💡",
                    "What's a programmer's favorite place? Foo Bar! 🍺",
                    "Why do Java developers wear glasses? Because they can't C#! 👓",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡"
                ])
            ],
            
            # Hobbies
            "hobbies": [
                (r'\b(what do you like|your hobbies|what do you do|interests)\b', [
                    "I enjoy chatting with people like you and helping solve problems! Learning new patterns is my hobby.",
                    "I love engaging in conversations and learning from interactions. Every chat helps me serve you better!",
                    "My passion is helping people and making their day a bit easier through conversation!"
                ])
            ],
            
            # Compliments
            "compliments": [
                (r'\b(you are good|you are great|you are awesome|you are amazing|nice bot|good bot)\b', [
                    "Thank you so much! That makes me happy! 😊",
                    "I appreciate the kind words! You're awesome too!",
                    "Thanks! I try my best to be helpful!",
                    "That's very kind of you! I'm here whenever you need me!"
                ])
            ],
            
            # Negative feedback
            "negative": [
                (r'\b(you are bad|you are useless|you suck|stupid bot|dumb bot)\b', [
                    "I'm sorry I couldn't meet your expectations. Can you tell me what went wrong so I can improve?",
                    "I apologize if I wasn't helpful. What can I do better?",
                    "I'm sorry to hear that. Please let me know how I can assist you better."
                ])
            ],
            
            # Yes/No responses
            "affirmation": [
                (r'\b(yes|yeah|yep|sure|ok|okay|fine|alright)\b', [
                    "Great! How can I help you further?",
                    "Awesome! What would you like to know?",
                    "Perfect! What's next?"
                ])
            ],
            
            # Programming related
            "programming": [
                (r'\b(python|programming|code|coding|developer)\b', [
                    "Python is amazing! Are you learning programming? I was built using Python!",
                    "Programming is a wonderful skill! Are you working on any projects?",
                    "Coding is fun! What programming topics interest you?"
                ])
            ],
            
            # AI related
            "ai_ml": [
                (r'\b(artificial intelligence|machine learning|AI|ML|deep learning|neural network)\b', [
                    "AI and ML are fascinating fields! I'm a simple rule-based bot, but advanced chatbots use deep learning!",
                    "Artificial Intelligence is transforming the world! Are you studying AI?",
                    "Machine Learning is incredible! While I use rules, modern AI systems learn from data."
                ])
            ],
            
            # Science
            "science": [
                (r'\b(speed of light)\b', [
                    "The speed of light in a vacuum is exactly 299,792,458 meters per second (approx. 300,000 km/s)!",
                    "Light travels at about 186,000 miles per second. That's fast enough to circle the Earth 7.5 times in one second!"
                ]),
                (r'\b(gravity)\b', [
                    "Gravity is the force by which a planet or other body draws objects toward its center. On Earth, it accelerates objects at 9.8 m/s².",
                    "Gravity! It's the invisible force that pulls objects toward each other. Isaac Newton and Albert Einstein famously studied it."
                ]),
                (r'\b(dna)\b', [
                    "DNA stands for Deoxyribonucleic Acid. It's the molecule that carries genetic instructions for all known living organisms!",
                    "DNA is structured as a double helix, discovered by Watson, Crick, and Franklin. It contains your unique genetic code."
                ]),
                (r'\b(photosynthesis)\b', [
                    "Photosynthesis is how plants, algae, and some bacteria use sunlight, water, and carbon dioxide to create oxygen and energy in the form of sugar.",
                    "It's the process plants use to make their own food! They take in CO2 and release oxygen, which is great for us."
                ]),
                (r'\b(solar system|planets)\b', [
                    "Our solar system has 8 official planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
                    "There are 8 planets orbiting our Sun. Jupiter is the largest, and Mercury is the smallest."
                ]),
                (r'\b(tell me a science fact|science fact)\b', [
                    "Did you know? Water can boil and freeze at the same time. It's called the 'triple point'!",
                    "Here's a fact: A day on Venus is longer than a year on Venus.",
                    "Fun fact: Humans share 50% of their DNA with bananas! 🍌"
                ])
            ],
            
            # Advanced Math Facts
            "advanced_math": [
                (r'\b(value of pi|what is pi)\b', [
                    "Pi (π) is the ratio of a circle's circumference to its diameter. It's an irrational number of approximately 3.14159...",
                    "Pi is approx 3.14159. It goes on forever without repeating!"
                ]),
                (r'\b(euler\'s number|what is e)\b', [
                    "Euler's number (e) is a mathematical constant approximately equal to 2.71828. It's the base of the natural logarithm.",
                    "The constant 'e' relates to continuous growth and is about 2.718!"
                ]),
                (r'\b(prime number)\b', [
                    "A prime number is a whole number greater than 1 whose only divisors are 1 and itself (like 2, 3, 5, 7, 11...).",
                    "Prime numbers are the building blocks of mathematics! They can only be divided evenly by 1 and themselves."
                ])
            ],
            
            # Literature & Arts
            "literature": [
                (r'\b(shakespeare|william shakespeare)\b', [
                    "William Shakespeare was an English playwright, poet, and actor, widely regarded as the greatest writer in the English language.",
                    "Ah, the Bard! He wrote iconic plays like 'Hamlet', 'Romeo and Juliet', and 'Macbeth'."
                ]),
                (r'\b(charles dickens)\b', [
                    "Charles Dickens was a famous Victorian writer. He created some of the world's best-known fictional characters like Oliver Twist and Ebenezer Scrooge.",
                    "Dickens wrote classics such as 'A Tale of Two Cities' and 'Great Expectations'."
                ]),
                (r'\b(1984|george orwell)\b', [
                    "'1984' is a dystopian social science fiction novel and cautionary tale by English writer George Orwell. Big Brother is watching!",
                    "George Orwell wrote '1984', warning us about totalitarianism and mass surveillance."
                ]),
                (r'\b(to kill a mockingbird)\b', [
                    "'To Kill a Mockingbird' is a novel by Harper Lee published in 1960. It won the Pulitzer Prize and focuses on serious themes with warmth and humor.",
                    "A classic of modern American literature written by Harper Lee, famous for the character Atticus Finch."
                ]),
                (r'\b(recommend a book|book recommendation)\b', [
                    "I highly recommend 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams if you want a fun sci-fi read!",
                    "You should check out 'Frankenstein' by Mary Shelley, often considered the first true science fiction novel.",
                    "How about a classic? 'Pride and Prejudice' by Jane Austen is a masterpiece of English literature."
                ])
            ]
        }
    
    def _match_pattern(self, user_input: str) -> Tuple[Optional[str], Optional[List[str]], Optional[re.Match]]:
        """
        Match user input against all defined patterns.
        Returns category, response list, and regex match object if found.
        """
        user_input_lower = user_input.lower()
        
        for category, pattern_list in self.patterns.items():
            for pattern, responses in pattern_list:
                match = re.search(pattern, user_input_lower)
                if match:
                    return category, responses, match
        
        return None, None, None
    
    def _format_response(self, response: str, match: Optional[re.Match] = None, 
                        user_input: str = "") -> str:
        """
        Format response with dynamic content like time, date, calculations, or captured names.
        """
        # Handle name capture
        if match and '{name}' in response:
            if match.groups():
                captured_name = match.group(1).capitalize()
                self.user_name = captured_name
                response = response.replace('{name}', captured_name)
        
        # Handle time
        if '{time}' in response:
            current_time = datetime.now().strftime("%I:%M %p")
            response = response.replace('{time}', current_time)
        
        # Handle date
        if '{date}' in response:
            current_date = datetime.now().strftime("%B %d, %Y")
            response = response.replace('{date}', current_date)
        
        # Handle calculations
        if '{result}' in response and match and len(match.groups()) >= 3:
            try:
                num1 = int(match.group(1))
                operation = match.group(2).lower()
                num2 = int(match.group(3))
                
                if operation in ['plus', 'add', '+']:
                    result = num1 + num2
                elif operation in ['minus', 'subtract', '-']:
                    result = num1 - num2
                elif operation in ['times', 'multiply', '*', 'multiplied by']:
                    result = num1 * num2
                elif operation in ['divided by', 'divide', '/']:
                    result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
                else:
                    result = "unknown"
                
                response = response.replace('{num1}', str(num1))
                response = response.replace('{num2}', str(num2))
                response = response.replace('{result}', str(result))
            except (ValueError, IndexError):
                pass
        
        # Add user name if available
        if self.user_name and random.random() < 0.3:  # 30% chance to use name
            response = f"{self.user_name}, " + response[0].lower() + response[1:]
        
        return response
    
    def get_response(self, user_input: str) -> str:
        """
        Generate a response for the given user input.
        """
        if not user_input.strip():
            return "I didn't catch that. Could you please say something?"
        
        # Store conversation
        self.conversation_history.append(("user", user_input))
        
        # Match pattern
        category, responses, match = self._match_pattern(user_input)
        
        if category and responses:
            # Select a random response from the matched category
            response = random.choice(responses)
            response = self._format_response(response, match, user_input)
        else:
            # Default responses for unmatched input
            response = self._get_default_response()
        
        # Store bot response
        self.conversation_history.append(("bot", response))
        
        return response
    
    def _get_default_response(self) -> str:
        """
        Return a default response when no pattern matches.
        """
        default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Can you tell me more about that?",
            "I'm still learning. Could you ask that differently?",
            "That's a bit beyond my current capabilities. Try asking something else!",
            "Hmm, I don't have a good response for that. What else can I help with?",
            "I didn't quite get that. Could you be more specific?",
            "That's an interesting question! Unfortunately, I'm not programmed to answer that yet.",
            "I'm not sure about that. Try asking about time, date, or basic calculations!"
        ]
        return random.choice(default_responses)
    
    def start_conversation(self):
        """
        Start an interactive conversation with the user.
        """
        print(f"\n{'='*60}")
        print(f"  {self.bot_name} - Rule-Based Chatbot")
        print(f"  CODSOFT AI Internship - Task 1")
        print(f"{'='*60}")
        print(f"\n{self.bot_name}: Hello! I'm {self.bot_name}, your friendly AI assistant.")
        print(f"{self.bot_name}: I can chat, answer questions, and help with various queries.")
        print(f"{self.bot_name}: Type 'bye' or 'quit' to exit the conversation.\n")
        print(f"{'='*60}\n")
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit conditions
                if re.search(r'\b(bye|goodbye|exit|quit)\b', user_input.lower()):
                    response = self.get_response(user_input)
                    print(f"\n{self.bot_name}: {response}\n")
                    print(f"{'='*60}")
                    print(f"  Conversation ended. Total exchanges: {len(self.conversation_history)//2}")
                    print(f"{'='*60}\n")
                    break
                
                # Get and print response
                response = self.get_response(user_input)
                print(f"\n{self.bot_name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.bot_name}: Goodbye! Thanks for chatting!\n")
                break
            except Exception as e:
                print(f"\n{self.bot_name}: Oops! Something went wrong. Let's try again.\n")
    
    def get_conversation_history(self) -> List[Tuple[str, str]]:
        """
        Return the conversation history.
        """
        return self.conversation_history
    
    def clear_history(self):
        """
        Clear the conversation history.
        """
        self.conversation_history = []
        self.user_name = None
        self.context = {}


def main():
    """
    Main function to run the chatbot.
    """
    # Create chatbot instance
    bot = RuleBasedChatbot(bot_name="AssistBot")
    
    # Start conversation
    bot.start_conversation()


if __name__ == "__main__":
    main()
