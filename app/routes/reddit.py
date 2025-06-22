"""
Reddit scraper route using PRAW.
"""
from fastapi import APIRouter, Query
from app.services.scraper_utils import fetch_reddit_reviews

router = APIRouter()

@router.get("/reviews")
def get_reddit_reviews(product: str = Query(..., description="Product name to search on Reddit")):
    return fetch_reddit_reviews(product)
