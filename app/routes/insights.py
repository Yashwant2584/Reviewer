from fastapi import APIRouter, Query
from app.services.sentiment import aggregate_insights

router = APIRouter()

@router.get("/summary")
def get_insights(product: str = Query(..., description="Product name to analyze")):
    try:
        insights = aggregate_insights(product)
        return insights
    except Exception as e:
        return {"error": str(e)}
