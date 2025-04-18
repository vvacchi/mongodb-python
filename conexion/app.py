from flask import Flask, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Instagram"]
collection = db["Usuarios"]



app = Flask(__name__)


@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = list(collection.find({},{"_id":0}))
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)