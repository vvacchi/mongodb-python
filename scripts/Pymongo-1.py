from pymongo import MongoClient
########Conexión a la base de datos en el servidor local########
client = MongoClient("mongodb://localhost:27017/")
db = client["Instagram"]
usuarios = db["Usuarios"]

#Se crea un indice para evitar duplicados en base al nombre de usuario
usuarios.create_index("username", unique = True) 

if not usuarios.find_one({"nombre": "Valentino Vacchini"}):
    usuarios.insert_one({"nombre": "Valentino Vacchini","username": "vacchi_valentino" , "edad": 22,"Seguidores": 450,"Seguidos": 189 , "Publicaciones": 3})
else:
    print("El nombre de usuario ya existe.")

#####Ingresar mas documentos######
usuarios_data = [
    {
        "nombre": "Nicolas Maidana",
        "edad": 45,
        "Seguidores": 300,
        "Seguidos": 150,
        "Publicaciones": 10,
        "username": "nicom25",
        "mail": "nicom25@gmail.com"
    },
    {
        "nombre": "Carla Rojas",
        "edad": 28,
        "Seguidores": 800,
        "Seguidos": 670,
        "Publicaciones": 45,
        "username": "carlarj",
        "mail": "carlarj@hotmail.com"
    },
    {
        "nombre": "Facundo Moran",
        "edad": 32,
        "Seguidores": 1230,
        "Seguidos": 400,
        "Publicaciones": 9,
        "username": "mfacu",
        "mail": "mfacundo@uade.com"
    },
    {
        "nombre": "Sofia Iglesias",
        "edad": 21,
        "Seguidores": 27340,
        "Seguidos": 115,
        "Publicaciones": 5,
        "username": "sofiglesias_",
        "mail": "sofiglesias21@gmail.com"
    },
    {
        "nombre": "Joaquin Estabillo",
        "edad": 27,
        "Seguidores": 2344,
        "Seguidos": 715,
        "Publicaciones": 10,
        "username": "joacocarp",
        "mail": "joaquinestabillo@gmail.com"
    },
    {
        "nombre": "Facundo Garompolo",
        "edad": 54,
        "Seguidores": 340,
        "Seguidos": 715,
        "Publicaciones": 6,
        "username": "facugarompolo",
        "mail": "facundog@gmail.com"
    },
    {
        "nombre": "Bautista Iannini",
        "edad": 18,
        "Seguidores": 340,
        "Seguidos": 315,
        "Publicaciones": 1,
        "username": "bautistaiannini",
        "mail": "bautistaiannini@gmail.com"
    }]

for usuario in usuarios_data:
    if not usuarios.find_one({"username": usuario["username"]}):
        usuarios.insert_one(usuario)
    else:
        print("El nombre de usuario ya existe.")

for usuario in usuarios.find({}, {"_id":0}):
    print(usuario)


######## Consultas con filtros ########
print("#############Consultas con filtros#############")

print("\n USUARIOS CON MÁS DE 1000 SEGUIDORES:")
for u in usuarios.find({"Seguidores": {"$gt": 1000}}, {"_id": 0}):
    print(u)

print("\nUSUARIOS CON MENOS DE 20 PUBLICACIONES:")
for i in usuarios.find({"Publicaciones": {"$lt": 20}}, {"_id": 0}):
    print(i)

print("\nUSUARIO CON NOMBRE 'Juan_Perez':")
resultado = list(usuarios.find({"nombre": "Juan_Perez"}, {"_id": 0}))
if resultado:
    for i in resultado:
        print(i)
else:
    print("Usuario no encontrado.")

print("\nUSUARIOS CON SEGUIDORES ENTRE 400 Y 1000:")
for i in usuarios.find({"Seguidores": {"$gte": 400, "$lte": 1000}}, {"_id": 0}):
    print(i)

print("\nUSUARIOS CON MÁS DE 10 PUBLICACIONES ORDENADOS POR SEGUIDORES (ASC):")
for i in usuarios.find({"Publicaciones": {"$gt": 10}}, {"_id": 0}).sort("Seguidores", 1):
    print(i)

print("\nUSUARIOS CON 0 PUBLICACIONES:")
for i in usuarios.find({"Publicaciones": 0}, {"_id": 0}):
    print(i)

print("\nUSUARIOS CON MÁS DE 1000 SEGUIDORES Y MÁS DE 1000 SEGUIDOS:")
for i in usuarios.find({"Seguidores": {"$gt": 1000}, "Seguidos": {"$gt": 1000}}, {"_id": 0}):
    print(i)

print("\nUSUARIOS CON EMAIL @gmail.com:")
for i in usuarios.find({"mail": {"$regex": "@gmail\\.com$"}}, {"_id": 0}):
    print(i)


