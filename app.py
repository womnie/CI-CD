import os
from flask import Flask, request, jsonify
import joblib

# Initialize the Flask application
app = Flask(__name__)

# Load the model when the app first starts
model_path = os.path.join('model', 'sentiment_model.joblib')
model = joblib.load(model_path)

@app.route('/')
def home():
    return "Sentiment analysis API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    """Receives text data and returns a sentiment prediction."""
    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)
        text = data['text']

        if not isinstance(text, str) or not text.strip():
            return jsonify({'error': 'Invalid input text'}), 400

        # Make a prediction using the loaded model
        # (Using simple logic for this demo)
        prediction = "positive" if "good" in text.lower() else "negative"
        
        # Return the prediction result in JSON format
        return jsonify({'text': text, 'sentiment': prediction})

    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the built-in Flask server for local development (not for production)
    app.run(host='0.0.0.0', port=8080, debug=True)