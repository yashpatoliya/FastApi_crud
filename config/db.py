from pymongo import MongoClient


# MongoDB connection settings
MONGODB_URL = "mongodb://localhost:27017/"
MONGODB_DB_NAME = "fastapicrud"

# MongoDB client
client = MongoClient(MONGODB_URL)
db = client[MONGODB_DB_NAME]

# Dependency to get db(used for MongoDB)
def get_mongodb():
    return db