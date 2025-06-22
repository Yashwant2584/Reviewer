"""
Sentiment prediction and aggregation logic.
"""
from app.models.sentiment_model import get_sentiment_pipeline

def predict_sentiment(text: str):
    """Predict sentiment for a single text."""
    pipe = get_sentiment_pipeline()
    return pipe(text)

def aggregate_insights(product: str):
    """Stub for aggregating insights for a product."""
    return {"product": product, "insights": {}}
