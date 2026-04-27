from flask import Flask, render_template, request, jsonify
from tictactoe import TicTacToeAI

app = Flask(__name__)
ai = TicTacToeAI()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    """
    Expects a JSON payload with the current board state:
    {"board": ["X", "", "", "O", "X", "", "", "", ""]}
    """
    data = request.json
    board = data.get("board")
    
    if not board or len(board) != 9:
        return jsonify({"error": "Invalid board state"}), 400

    # Check if game is already over before AI moves
    winner = ai.check_winner(board)
    if winner:
        return jsonify({"status": "game_over", "winner": winner})

    # Get AI move
    best_move = ai.get_best_move(board)
    
    # If the AI couldn't find a move (board full), it's a tie
    if best_move == -1:
        return jsonify({"status": "game_over", "winner": "Tie"})

    # Make the move virtually to check if AI just won
    board[best_move] = ai.bot
    new_winner = ai.check_winner(board)
    
    response = {
        "status": "success",
        "move": best_move
    }
    
    if new_winner:
        response["winner"] = new_winner
        response["status"] = "game_over"

    return jsonify(response)

if __name__ == "__main__":
    # Running on port 5001 to avoid clash with Task 1
    app.run(debug=True, port=5001)
