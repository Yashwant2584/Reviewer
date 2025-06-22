from fastapi import FastAPI
from app.routes import insights, reddit, twitter, youtube

app = FastAPI()

app.include_router(insights.router, prefix="/insights")
app.include_router(reddit.router, prefix="/reddit")
app.include_router(twitter.router, prefix="/twitter")
app.include_router(youtube.router, prefix="/youtube")

@app.get("/")
def root():
    return {"message": "Welcome to ReviewPulse API!"}
