from flask import Flask, jsonify, request
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Instagram"]
collection = db["Usuarios"]



app = Flask(__name__)

#Metodo GET para leer todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = list(collection.find({},{"_id":0}))
    if usuarios:
        return jsonify({"status": "success", "data": usuarios}), 200
    return jsonify({"status": "error", "message": "No se encontraron usuarios."}), 404

#Metodo POST para crear un usuario nuevo chequeando si existe el username
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    nuevo_usuario = request.json
    if not nuevo_usuario or not nuevo_usuario.get("username"):
        return jsonify({"status": "error", "message": "El campo 'username' es obligatorio."}), 400
    if collection.find_one({"username": nuevo_usuario['username']}):
        return jsonify({"status": "error", "message": "El usuario ya existe."}), 400
    collection.insert_one(nuevo_usuario)
    return jsonify({"status": "succes", "message": "Usuario creado exitosamente."}), 201

#Metodo PUT para actualizar un usuario existente
@app.route('/usuarios/<username>', methods=['PUT'])
def update_usuario(username):
    datos_actualizados = request.json
    if not datos_actualizados:
        return jsonify({"status": "error", "message": "No se enviaron datos para actualizar."}), 400
    resultado = collection.update_one({"username": username}, {"$set": datos_actualizados})
    if resultado.matched_count:
        return jsonify({"status": "success", "message": "Usuario actualizado exitosamente."}), 200
    return jsonify({"status": "error", "message": "Usuario no encontrado."}), 404

#Metodo DELETE para eliminar un usuario
@app.route("/usuarios/<username>", methods=['DELETE'])
def delete_usuario(username):
    resultado = collection.delete_one({"username": username})
    if resultado.deleted_count:
        return jsonify({"status": "success", "message": "Usuario eliminado exitosamente."}), 200
    return jsonify({"status": "error", "message": "Usuario no encontrado."}), 404

if __name__ == "__main__":
    app.run(debug=True)