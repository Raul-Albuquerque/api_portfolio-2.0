from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://client:client1234@portfolio-api.0fqot3o.mongodb.net/?retryWrites=true&w=majority&appName=portfolio-api"
)

db = client.portfolio_db


# DEVELOPERS COLLECTION

developers_collection = db["developers"]


# PROJECTS COLLECTION

projects_collection = db["projects"]


# EXPERIENCES COLLECTION

experiences_collection = db["experiences"]
