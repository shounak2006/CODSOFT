from flask import Flask, render_template, request, jsonify
from chatbot import RuleBasedChatbot

app = Flask(__name__)

# Initialize the chatbot engine
bot = RuleBasedChatbot(bot_name="AssistBot")

@app.route("/")
def home():
    """Render the minimalist frontend."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handle incoming chat messages securely via JSON."""
    user_input = request.json.get("message", "")
    
    if not user_input:
        return jsonify({"response": "I didn't catch that."})
    
    # Get response from the Python Rule-based engine
    response = bot.get_response(user_input)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
