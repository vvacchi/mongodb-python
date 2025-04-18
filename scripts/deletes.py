from pymongo import MongoClient
########Conexión a la base de datos en el servidor local########
client = MongoClient("mongodb://localhost:27017/")
db = client["Instagram"]
usuarios = db["Usuarios"]


######## Propuestas de eliminación (delete) ########
#Eliminar un documento especifico
usuarios.delete_one({"username": "vacchi_valentino"})
#Eliminar un documento con edad menor a 18
usuarios.delete_one({"edad":{"$lt":18}})
#Eliminar varios documentos con seguidores menores a 100
usuarios.delete_many({"Seguidores": {"$lt":100}})
#Eliminar todos los documentos distintos a gmail o hotmail
usuarios.delete_many({"mail": {"$not": {"$regex": "@(gmail|hotmail)\\.com$"}}})
#Eliminar un documento sin campo mail
usuarios.delete_many({"mail": {"$exists": False}})

del_cero_seguidores = usuarios.delete_many({"Seguidores": 0, "Seguidos": 0})
print(f"Documentos eliminados (con 0 seguidores y 0 seguidos): {del_cero_seguidores.deleted_count}")

del_cero_publicaciones = usuarios.delete_many({"Publicaciones": {"$exists": False}})
print(f"Documentos eliminados (sin campo Publicaciones): {del_cero_publicaciones.deleted_count}")