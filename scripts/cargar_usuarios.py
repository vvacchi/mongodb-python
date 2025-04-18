import json 
import os
from conectar_db import get_db_collection

usuarios = get_db_collection()

#Creamos un índice para evitar duplicados, teniendo en cuenta el "username"
usuarios.create_index("username", unique=True)

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "instagram.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    usuarios_data = json.load(f)

insertados = 0
duplicados = 0

#Insertar usuarios si no existen
for usuario in usuarios_data:
    if not usuarios.find_one({"username": usuario["username"]}):
        usuarios.insert_one(usuario)
        insertados += 1
    else:
        print(f"El nombre de usuario '{usuario['username']}' ya existe.")
        duplicados += 1

print(f"\n Usuarios insertados correctamente: {insertados}")
print(f" Usuarios duplicados ignorados (no ingresados 2 veces): {duplicados}")