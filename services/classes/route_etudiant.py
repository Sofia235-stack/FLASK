from flask import Blueprint, jsonify, request
from services.classes.app import db, Etudiant  # Import Etudiant from app.py

etudiant_bp = Blueprint('etudiant', __name__)

# Get all students
@etudiant_bp.route('/etudiants/', methods=['GET'])
def get_etudiants():
    etudiants = Etudiant.query.all()
    return jsonify([etudiant.to_dict() for etudiant in etudiants]), 200

# Get a specific student by ID
@etudiant_bp.route('/etudiants/<int:etudiant_id>', methods=['GET'])
def get_etudiant(etudiant_id):
    etudiant = Etudiant.query.get_or_404(etudiant_id)
    return jsonify(etudiant.to_dict()), 200

# Add a new student (optional, added for completeness)
@etudiant_bp.route('/etudiants/', methods=['POST'])
def add_etudiant():
    data = request.json
    if 'nom' not in data:
        return jsonify({'error': 'Le champ nom est obligatoire'}), 400

    new_etudiant = Etudiant(nom=data['nom'])
    db.session.add(new_etudiant)
    db.session.commit()
    return jsonify(new_etudiant.to_dict()), 201

# Update a student (optional, added for completeness)
@etudiant_bp.route('/etudiants/<int:etudiant_id>', methods=['PUT'])
def update_etudiant(etudiant_id):
    etudiant = Etudiant.query.get(etudiant_id)
    if not etudiant:
        return jsonify({'error': 'Etudiant non trouvé'}), 404

    data = request.json
    if 'nom' in data:
        etudiant.nom = data['nom']

    db.session.commit()
    return jsonify({'message': 'Etudiant mis à jour avec succès', 'etudiant': etudiant.to_dict()}), 200

# Delete a student (optional, added for completeness)
@etudiant_bp.route('/etudiants/<int:etudiant_id>', methods=['DELETE'])
def delete_etudiant(etudiant_id):
    etudiant = Etudiant.query.get(etudiant_id)
    if not etudiant:
        return jsonify({'error': 'Etudiant non trouvé'}), 404

    db.session.delete(etudiant)
    db.session.commit()
    return jsonify({'message': 'Etudiant supprimé avec succès'}), 200