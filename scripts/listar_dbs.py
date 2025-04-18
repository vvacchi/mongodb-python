from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
dbs = client.list_database_names()


print("Las bases de datos disponibles con sus colecciones son:")
for db_name in dbs:
    db = client[db_name]
    collections = db.list_collection_names()
    print(f"\nDB: {db_name}")
    for col in collections:
        print(f" Colecctions: -> {col}")
