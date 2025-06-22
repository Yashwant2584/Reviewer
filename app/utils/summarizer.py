"""
Optional: Hugging Face summarizer utility.
"""
from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_summarizer():
    return pipeline("summarization")

def summarize_text(text: str):
    summarizer = get_summarizer()
    return summarizer(text)
