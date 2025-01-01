"""
server.py

A Flask application for emotion detection using the EmotionDetection module.
It includes routes for detecting emotions and error handling.
"""

from collections import OrderedDict  # Standard library import
from flask import Flask, request, jsonify  # Third-party imports
from EmotionDetection import emotion_detector  # Local import

app = Flask(__name__)

def create_response(result):
    """
    Create a formatted response from the emotion_detector output.

    Args:
        result (dict): Output from the emotion_detector function.

    Returns:
        OrderedDict: Formatted result with ordered keys.
    """
    return OrderedDict([
        ("anger", result.get("anger", 0)),
        ("disgust", result.get("disgust", 0)),
        ("fear", result.get("fear", 0)),
        ("joy", result.get("joy", 0)),
        ("sadness", result.get("sadness", 0)),
        ("dominant_emotion", result.get("dominant_emotion", "none"))
    ])

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Endpoint to detect emotions in a given text.

    Returns:
        Response: A JSON object with the detected emotions or an error message.
    """
    data = request.get_json()
    text = data.get("text", "")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    return jsonify(create_response(result))

@app.route("/")
def render_index_page():
    """
    Endpoint to render the index page.

    Returns:
        str: A simple HTML page with instructions.
    """
    return "<h1>Emotion Detection API</h1><p>Send POST requests to /emotionDetector</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
