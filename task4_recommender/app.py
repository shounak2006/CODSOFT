from flask import Flask, request, jsonify, render_template
from recommender import MovieRecommender

app = Flask(__name__)

ai_engine = MovieRecommender(data_path="movies.csv")

@app.route("/")
def home():
    """Serves the Netflix-style search interface."""
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    """
    Expects JSON payload:
    {"movie": "The Dark Knight"}
    """
    data = request.json
    movie_query = data.get("movie")
    
    if not movie_query:
        return jsonify({"error": "No movie title provided"}), 400
        
    results = ai_engine.get_recommendations(movie_query)
        
    return jsonify(results)

if __name__ == "__main__":
    print("Recommendation Engine running on http://127.0.0.1:5003")
    app.run(debug=True, port=5003)
