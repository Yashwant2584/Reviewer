"""
Analytics endpoints for ReviewPulse.
"""
from fastapi import APIRouter, Query
from app.services.sentiment import aggregate_insights

router = APIRouter()

@router.get("/summary")
def get_insights(product: str = Query(..., description="Product name for insights")):
    return aggregate_insights(product)
