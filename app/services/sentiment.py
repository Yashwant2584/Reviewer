"""
Sentiment prediction and aggregation logic.
"""
from app.models.sentiment_model import get_sentiment_pipeline
from app.services.scraper_utils import fetch_reddit_reviews, fetch_twitter_reviews, fetch_youtube_comments
from app.services.preprocess import clean_text

MAX_LEN = 512  # BERT/DistilBERT max token length

def truncate_text(text, max_len=MAX_LEN):
    return text[:max_len]

def predict_sentiment(text: str):
    """Predict sentiment for a single text."""
    pipe = get_sentiment_pipeline()
    return pipe(truncate_text(text))

def predict_sentiments(texts):
    """Predict sentiment for a list of texts."""
    pipe = get_sentiment_pipeline()
    return pipe([truncate_text(t) for t in texts])

def aggregate_insights(product: str):
    """Fetch reviews/comments, predict sentiment, and aggregate insights for a product."""
    reddit = fetch_reddit_reviews(product)
    twitter = fetch_twitter_reviews(product)
    youtube = fetch_youtube_comments(product)
    reddit_texts = [clean_text(r['text']) for r in reddit.get('reviews', [])]
    twitter_texts = [clean_text(r['text']) for r in twitter.get('reviews', [])]
    youtube_texts = [clean_text(c['text']) for c in youtube.get('comments', [])]
    all_texts = reddit_texts + twitter_texts + youtube_texts
    sentiments = predict_sentiments(all_texts) if all_texts else []
    counts = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}
    sentiment_map = []
    for text, sent in zip(all_texts, sentiments):
        label = sent['label'].upper()
        if label not in counts:
            if label == 'NEUTRAL':
                counts['NEUTRAL'] += 1
            elif label == 'POSITIVE':
                counts['POSITIVE'] += 1
            elif label == 'NEGATIVE':
                counts['NEGATIVE'] += 1
            else:
                counts[label] = 1
        else:
            counts[label] += 1
        sentiment_map.append({'text': text, 'sentiment': label, 'score': sent['score']})
    top_positive = sorted([s for s in sentiment_map if s['sentiment'] == 'POSITIVE'], key=lambda x: -x['score'])[:5]
    top_negative = sorted([s for s in sentiment_map if s['sentiment'] == 'NEGATIVE'], key=lambda x: -x['score'])[:5]
    return {
        'product': product,
        'counts': counts,
        'total': len(all_texts),
        'top_positive': top_positive,
        'top_negative': top_negative,
        'all_sentiments': sentiment_map,
        'sources': {
            'reddit': reddit,
            'twitter': twitter,
            'youtube': youtube
        }
    }
