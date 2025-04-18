from pymongo import MongoClient
from conectar_db import get_db_collection
from pprint import pprint
usuarios = get_db_collection()

"""######## Propuestas de actualización (update) ########
#Actualizar el correo de un documento especifico a traves de su username 
usuarios.update_one({"username": "mferrari"}, {"$set": {"mail": "meferrari@gmail.com"}})
#Sumar 100 seguidores a todos los documentos con mas de 400 seguidores
usuarios.update_many({"Seguidores": {"$gt": 400}}, {"$inc": {"Seguidores": 100}})
#Agregar un campo de "verificado" en False por defecto
usuarios.update_many({}, {"$set": {"Verificado": False}})
#Marcar "verificado" True si el documento tiene mas de 1000 seguidores
usuarios.update_many({"Seguidores": {"$gt": 1000}}, {"$set": {"Verificado": True}})
#Cambiar un nombre de un documento específico
usuarios.update_one({"nombre": "Valentino Vacchini"}, {"$set": {"nombre": "Vacchini Valentino"}})
#Actualizar los mails con dominio hotmail a gmail
usuarios.update_many({"mail": {"$regex": "@hotmail\\.com"}}, {"$set": {"mail": "@gmail\\.com"}})
#Agregar un campo de "activo" con valor True a todos los documentos
usuarios.update_many({}, {"$set": {"Activo": True}})


usuarios.update_one({"username": "vacchi_valentino"}, {"$set": {"mail": "vacchini123@gmail.com"}})
usuarios.update_one({"username": "carlarj"}, {"$set": {"mail": "carlarojas1997@gmail.com"}})

usuarios.update_many(
    {"tipo de cuenta": {"exists": True}},
    [
        {
            "$set": {"tipo_cuenta": "$tipo de cuenta"},
        },
        {
            "$unset": "tipo de cuenta"
        }
    ]
)

print("Campo renombrado exitosamente.")

ejemplo = usuarios.find_one()
pprint(ejemplo)


resultado = usuarios.update_many(
    {"tipo de cuenta": {"$exists": True}},
    [
        {"$set": {"tipo_cuenta": "$tipo de cuenta"}},
        {"$unset": "tipo de cuenta"}
    ]
)

print("Documentos modificados:", resultado.modified_count)"""