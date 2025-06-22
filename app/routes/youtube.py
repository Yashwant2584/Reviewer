from fastapi import APIRouter, Query
from app.services.scraper_utils import fetch_youtube_comments

router = APIRouter()

@router.get("/")
def youtube_reviews(product: str = Query(...)):
    return fetch_youtube_comments(product)
