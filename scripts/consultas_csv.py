import pandas as pd
from pprint import pprint
from conectar_db import get_db_collection

usuarios = get_db_collection()

#Documento con menos de 25 años y mas de 3500 seguidores
print("####################Documento con menos de 25 años y mas de 3500 seguidores####################\n")
try:
    filtro1 = {"edad": {"$lt": 25}, "seguidores": {"$gt": 3500}}
    resultado1 = list(usuarios.find(filtro1, {"_id":0}))
    for usuario in resultado1:
        print(usuario)
    pd.DataFrame(resultado1).to_csv("../data/usuarios_menos25años_mas3500seguidores.csv", index=False, encoding="utf-8")
except Exception as e:
    print("Error en la consulta 1 o al exportar a CSV:", e)

#Promedio de publicaciones por tipo de cuenta
print("\n####################Promedio de publicaciones por tipo de cuenta####################\n")
try:
    pipeline2 = [{"$group": {"_id": "$tipo_cuenta", "promedio_publicaciones": {"$avg": "$publicaciones"}}}]
    resultado2 = list(usuarios.aggregate(pipeline2))
    pprint(resultado2)
    pd.DataFrame(resultado2).to_csv("../data/promedio_publicaciones_por_tipocuenta.csv", index=False, encoding="utf_8")
except Exception as e:
    print("Error en la consulta 2 o al exportar a CSV:", e)


#Cuantos usuarios hay por tipo de cuenta
print("\n####################Cuantos usuarios hay por tipo de cuenta####################\n")
try:
    pipeline3 = [{"$group": {"_id": "$tipo_cuenta", "cantidad": {"$sum": 1}}}]
    resultado3 = list(usuarios.aggregate(pipeline3))
    pprint(resultado3)
    pd.DataFrame(resultado3).to_csv("../data/cantidad_usuarios_por_tipo.csv", index=False, encoding="utf-8")
except Exception as e:
    print("Error en la consulta 3 o al exportar a CSV:", e)


#Listar usuarios que sigan a mas de 1000 personas y tengan menos de 500 seguidores
print("\n####################Listar usuarios que sigan a mas de 1000 personas y tengan menos de 500 seguidores####################\n")
try:
    filtro4 = {"seguidos": {"$gt": 1000}, "seguidores": {"$lt": 500}}
    resultado4 = list(usuarios.find(filtro4, {"_id":0}))
    for usuario in resultado4:
        print(usuario)
    pd.DataFrame(resultado4).to_csv("../data/usuarios_mas1000seguidos_menos500seguidores.csv", index=False, encoding="utf-8")
except Exception as e:
    print("Error en la consulta 4 o al exportar a CSV:", e)

#Listar los usuarios cuyo mail no termina en @gmail.com
print("\n####################Listar los usuarios cuyo mail no termina en @gmail.com####################\n")
try:
    filtro5 = {"mail": {"$not": {"$regex": "@gmail\\.com$"}}}
    resultado5 = list(usuarios.find(filtro5, {"_id":0}))
    for usuario in resultado5:
        print(usuario)
    pd.DataFrame(resultado5).to_csv("../data/usuarios_mail_no_gmail.csv", index=False, encoding="utf-8")
except Exception as e:
    print("Error en la consulta 5 o al exportar a CSV:", e)
