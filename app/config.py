"""
Configuration file for API keys, MongoDB URI, and settings.
"""
import os
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

