"""
FastAPI entry point for ReviewPulse.
"""
from fastapi import FastAPI
from app.routes import reddit, twitter, youtube, insights

app = FastAPI(title="ReviewPulse API")

# Include routers
app.include_router(reddit.router, prefix="/reddit", tags=["Reddit"])
app.include_router(twitter.router, prefix="/twitter", tags=["Twitter"])
app.include_router(youtube.router, prefix="/youtube", tags=["YouTube"])
app.include_router(insights.router, prefix="/insights", tags=["Insights"])

@app.get("/")
def root():
    return {"message": "Welcome to ReviewPulse API!"}
