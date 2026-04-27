import os
from flask import Flask, request, jsonify, render_template
from captioner import ImageCaptioner

app = Flask(__name__)

# Boot the heavy transformer pipeline into memory when the server starts
print("Booting Vision-Transformer backend API...")
bot = ImageCaptioner()

@app.route("/")
def home():
    """Serves the Drag & Drop web interface."""
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    """Endpoint to receive an image payload and return an AI caption."""
    if 'image' not in request.files:
        return jsonify({"error": "No image provided."}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "Empty file."}), 400
    
    # Process the image directly from RAM buffer
    caption = bot.generate_caption(file.stream)
    
    return jsonify({
        "status": "success",
        "caption": caption
    })

if __name__ == "__main__":
    # Running on Port 5002 to avoid collision with Task 1 and 2
    print("AI Image Captioning Server running on http://127.0.0.1:5002")
    app.run(debug=True, port=5002)
