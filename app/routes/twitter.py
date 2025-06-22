from fastapi import APIRouter, Query
from app.services.scraper_utils import fetch_twitter_reviews

router = APIRouter()

@router.get("/")
def twitter_reviews(product: str = Query(...)):
    return fetch_twitter_reviews(product)
