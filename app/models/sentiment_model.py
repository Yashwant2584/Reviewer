"""
Loads and manages the Hugging Face sentiment analysis model.
"""
from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_sentiment_pipeline():
    """Load and cache the sentiment analysis pipeline."""
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
