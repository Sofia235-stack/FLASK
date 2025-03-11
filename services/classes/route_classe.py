from flask import Blueprint, jsonify, request
from services.classes.app import db, Classe  # Import Classe from app.py

classe_bp = Blueprint('classe', __name__)

@classe_bp.route('/classes/', methods=['GET'])
def get_classes():
    classes = Classe.query.all()
    return jsonify([classe.to_dict() for classe in classes]), 200

@classe_bp.route('/classes/<int:classe_id>', methods=['GET'])
def get_classe(classe_id):
    classe = Classe.query.get_or_404(classe_id)
    return jsonify(classe.to_dict()), 200

@classe_bp.route('/classes/', methods=['POST'])
def add_classe():
    data = request.json
    if not all(k in data for k in ('nom', 'niveau')):
        return jsonify({'error': 'Tous les champs sont obligatoires'}), 400

    new_classe = Classe(nom=data['nom'], niveau=data['niveau'])
    db.session.add(new_classe)
    db.session.commit()
    return jsonify(new_classe.to_dict()), 201

@classe_bp.route('/classes/<int:classe_id>', methods=['PUT'])
def update_classe(classe_id):
    classe = Classe.query.get(classe_id)
    if not classe:
        return jsonify({'error': 'Classe non trouvée'}), 404

    data = request.json
    if 'nom' in data:
        classe.nom = data['nom']
    if 'niveau' in data:
        classe.niveau = data['niveau']

    db.session.commit()
    return jsonify({'message': 'Classe mise à jour avec succès', 'classe': classe.to_dict()}), 200

@classe_bp.route('/classes/<int:classe_id>', methods=['DELETE'])
def delete_classe(classe_id):
    classe = Classe.query.get(classe_id)
    if not classe:
        return jsonify({'error': 'Classe non trouvée'}), 404

    db.session.delete(classe)
    db.session.commit()
    return jsonify({'message': 'Classe supprimée avec succès'}), 200