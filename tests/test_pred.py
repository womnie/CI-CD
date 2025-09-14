import sys
import os

# This allows Python to find the app.py file from the tests folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import predict_sentiment

def test_positive_sentiment():
    """Test for positive sentiment."""
    assert predict_sentiment("The service was very good", None) == "positive"

def test_negative_sentiment():
    """Test for negative sentiment."""
    assert predict_sentiment("This product is unsatisfactory", None) == "negative"

def test_invalid_input():
    """Test for invalid input."""
    assert predict_sentiment("   ", None) == "Invalid Input"