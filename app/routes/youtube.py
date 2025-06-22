"""
YouTube comment fetcher route.
"""
from fastapi import APIRouter, Query
from app.services.scraper_utils import fetch_youtube_comments

router = APIRouter()

@router.get("/comments")
def get_youtube_comments(product: str = Query(..., description="Product name to search on YouTube")):
    return fetch_youtube_comments(product)
