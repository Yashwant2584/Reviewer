"""
MongoDB connection and helper functions.
"""
from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["reviewpulse"]

def get_reviews_collection():
    return db["reviews"]
