"""
Twitter scraper route using Tweepy.
"""
from fastapi import APIRouter, Query
from app.services.scraper_utils import fetch_twitter_reviews

router = APIRouter()

@router.get("/reviews")
def get_twitter_reviews(product: str = Query(..., description="Product name to search on Twitter")):
    return fetch_twitter_reviews(product)
