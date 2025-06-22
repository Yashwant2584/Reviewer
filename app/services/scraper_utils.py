"""
Utility functions for scraping Reddit, Twitter, and YouTube.
"""
import praw
import tweepy
from googleapiclient.discovery import build
from app.config import (
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT,
    TWITTER_BEARER_TOKEN, YOUTUBE_API_KEY
)

def fetch_reddit_reviews(product: str, limit: int = 20):
    """Fetches recent Reddit submissions and comments mentioning the product. Handles API errors."""
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        reviews = []
        for submission in reddit.subreddit('all').search(product, limit=limit, sort='new'):
            reviews.append({
                'id': submission.id,
                'text': submission.title + '\n' + (submission.selftext or ''),
                'author': str(submission.author),
                'created_utc': submission.created_utc,
                'url': submission.url,
                'score': submission.score
            })
        return {"source": "reddit", "product": product, "reviews": reviews}
    except Exception as e:
        return {"source": "reddit", "product": product, "error": str(e), "reviews": []}

def fetch_twitter_reviews(product: str, limit: int = 20):
    """Fetches recent tweets mentioning the product using Twitter API v2. Handles API errors."""
    try:
        client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
        query = f'{product} -is:retweet lang:en'
        tweets = client.search_recent_tweets(query=query, max_results=min(limit, 100), tweet_fields=["created_at", "author_id", "text", "public_metrics"])
        reviews = []
        if tweets.data:
            for tweet in tweets.data:
                reviews.append({
                    'id': tweet.id,
                    'text': tweet.text,
                    'author_id': tweet.author_id,
                    'created_at': tweet.created_at.isoformat() if tweet.created_at else None,
                    'retweet_count': tweet.public_metrics.get('retweet_count', 0) if tweet.public_metrics else 0,
                    'like_count': tweet.public_metrics.get('like_count', 0) if tweet.public_metrics else 0
                })
        return {"source": "twitter", "product": product, "reviews": reviews}
    except Exception as e:
        return {"source": "twitter", "product": product, "error": str(e), "reviews": []}

def fetch_youtube_comments(product: str, limit: int = 20):
    """Fetches comments from YouTube videos matching the product name. Handles API errors."""
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        search_response = youtube.search().list(
            q=product,
            part='id',
            type='video',
            maxResults=min(limit, 10)
        ).execute()
        comments = []
        for item in search_response.get('items', []):
            video_id = item['id']['videoId']
            comment_response = youtube.commentThreads().list(
                videoId=video_id,
                part='snippet',
                maxResults=limit
            ).execute()
            for thread in comment_response.get('items', []):
                top_comment = thread['snippet']['topLevelComment']['snippet']
                comments.append({
                    'video_id': video_id,
                    'author': top_comment.get('authorDisplayName'),
                    'text': top_comment.get('textDisplay'),
                    'published_at': top_comment.get('publishedAt'),
                    'like_count': top_comment.get('likeCount', 0)
                })
        return {"source": "youtube", "product": product, "comments": comments}
    except Exception as e:
        return {"source": "youtube", "product": product, "error": str(e), "comments": []}

# Test functions (can be run directly)
if __name__ == "__main__":
    import json
    test_product = "iPhone 15"
    print("Reddit:")
    print(json.dumps(fetch_reddit_reviews(test_product), indent=2))
    print("\nTwitter:")
    print(json.dumps(fetch_twitter_reviews(test_product), indent=2))
    print("\nYouTube:")
    print(json.dumps(fetch_youtube_comments(test_product), indent=2))
