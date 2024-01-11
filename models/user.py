
from pydantic import BaseModel
from config.db import get_mongodb

db = get_mongodb()
# Pydantic models
class User(BaseModel):
    username: str
    email: str
    password: str

users_collection = db["users"]