from pymongo import MongoClient

client = MongoClient('mongodb+srv://raulmalbuquerque2015:admin1234@portfolio-api.0fqot3o.mongodb.net/?retryWrites=true&w=majority&appName=portfolio-api')

db = client.portfolio_db

collection_name = db ['portfolio_collection']