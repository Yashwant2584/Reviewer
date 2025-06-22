from app.services.sentiment import predict_sentiment

def test_sentiment_positive():
    result = predict_sentiment("I love this product!")
    assert result[0]["label"] == "POSITIVE"
