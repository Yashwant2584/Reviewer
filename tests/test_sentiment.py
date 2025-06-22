"""
Unit tests for sentiment analysis logic.
"""
import unittest
from app.services.sentiment import predict_sentiment

class TestSentiment(unittest.TestCase):
    def test_positive(self):
        result = predict_sentiment("I love this product!")
        self.assertTrue(result[0]['label'] == 'POSITIVE')

    def test_negative(self):
        result = predict_sentiment("I hate this product!")
        self.assertTrue(result[0]['label'] == 'NEGATIVE')

if __name__ == "__main__":
    unittest.main()
