import joblib

def load_model(path="model/sentiment_model.joblib"):
    """Loads the model from a file."""
    return joblib.load(path)

def predict_sentiment(text, model):
    """Makes a sentiment prediction (dummy)."""
    if not isinstance(text, str) or not text.strip():
        return "Invalid Input"

    # The actual prediction logic would be here.
    # For this demo, we'll keep it simple.
    return "positive" if "good" in text.lower() else "negative"

if __name__ == "__main__":
    # This part is for local testing only.
    try:
        model = load_model()
        prediction = predict_sentiment("This is a very good day.", model)
        print(f"Sentiment prediction: {prediction}")
    except FileNotFoundError:
        print("Model not found. Ensure the file 'model/sentiment_model.joblib' exists.")