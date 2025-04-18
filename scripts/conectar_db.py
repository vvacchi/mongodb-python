from pymongo import MongoClient

def get_db_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Instagram"]
    return db["Usuarios"]
