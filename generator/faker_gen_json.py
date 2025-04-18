from faker import Faker
import json 
import random
import os

NUM_USUARIOS = 100
DOMINIOS = ["gmail.com", "hotmail.com", "outlook.com"]
TIPOS_CUENTA = ["Empresa", "Blog personal", "Salud/Belleza", "Tecnología", "Comida"]
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "instagram.json")

fake = Faker("es-AR")

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

def generar_username(first, last):
    opciones = [
        f"{first.lower()}{last.lower()}",
        f"{first.lower()}{random.randint(1,99)}",
        f"{last.lower()}{random.randint(1,99)}",
        f"{first.lower()}_{last.lower()}",
        f"{first[0].lower()}{last.lower()}",
        f"{first.lower()}.{last.lower()}",
        f"{first.lower()}{last.lower()}{random.randint(1,99)}",
    ]
    return random.choice(opciones)

data = []
for _ in range(NUM_USUARIOS):
    first = fake.first_name()
    last = fake.last_name()
    nombre = f"{first} {last}"
    edad = random.randint(18,65)
    seguidores = random.randint(0, 45000)
    seguidos = random.randint(100,5000)
    publicaciones = random.randint(0,1000)
    username = generar_username(first, last)
    mail = f"{username}@{random.choice(DOMINIOS)}"
    tipo_cuenta = random.choice(TIPOS_CUENTA)

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "seguidores": seguidores,
        "seguidos": seguidos,
        "publicaciones": publicaciones,
        "username": username,
        "mail": mail,
        "tipo de cuenta": tipo_cuenta
    }
    data.append(usuario)

#Guardar en archivo JSON
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Generados {NUM_USUARIOS} usuarios en:\n   {OUTPUT_PATH}")