from fastapi import APIRouter, Query
from app.services.scraper_utils import fetch_reddit_reviews

router = APIRouter()

@router.get("/")
def reddit_reviews(product: str = Query(...)):
    return fetch_reddit_reviews(product)
