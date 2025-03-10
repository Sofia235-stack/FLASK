# routes.py
from flask import Blueprint, jsonify, request

class_routes = Blueprint('class_routes', __name__)

# Simuler une base de données en mémoire
classes = []

# Route pour récupérer toutes les classes
@class_routes.route('/', methods=['GET'])
def get_classes():
    return jsonify(classes), 200

# Route pour ajouter une classe
@class_routes.route('/', methods=['POST'])
def add_class():
    print("📌 Requête POST reçue :", request.json)  # Debugging
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Le nom de la classe est requis'}), 400
    new_class = {'id': len(classes) + 1, 'name': data['name']}
    classes.append(new_class)
    print("📌 Nouvelle classe ajoutée :", new_class)  # Debugging
    return jsonify(new_class), 201

@class_routes.route('/test', methods=['POST'])
def test_post():
    print("📌 Requête POST test reçue")
    return jsonify({"message": "POST reçu"}), 200



