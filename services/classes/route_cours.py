from flask import Blueprint, jsonify, redirect, url_for, request
from services.classes.app import db, Cours  # Import Cours from app.py

cours_bp = Blueprint('cours', __name__)

@cours_bp.route('/cours/', methods=['GET'])
def get_cours():
    cours = Cours.query.all()
    return jsonify([c.to_dict() for c in cours]), 200

@cours_bp.route('/cours/<int:cours_id>', methods=['GET'])
def get_cours_by_id(cours_id):
    cours = Cours.query.get_or_404(cours_id)
    return jsonify(cours.to_dict()), 200

@cours_bp.route('/cours/', methods=['POST'])
def add_cours():
    data = request.form if request.form else request.json
    if not all(k in data for k in ('titre', 'professeur_id')):
        return jsonify({'error': 'Tous les champs sont obligatoires'}), 400

    new_cours = Cours(titre=data['titre'], professeur_id=int(data['professeur_id']))
    db.session.add(new_cours)
    db.session.commit()
    if request.headers.get('Accept') == 'application/json':
        return jsonify(new_cours.to_dict()), 201
    return redirect(url_for('index'))  # Redirect to index after form submission

@cours_bp.route('/cours/<int:cours_id>', methods=['DELETE'])
def delete_cours(cours_id):
    cours = Cours.query.get(cours_id)
    if not cours:
        return jsonify({'error': 'Cours non trouvé'}), 404
    db.session.delete(cours)
    db.session.commit()
    if request.headers.get('Accept') == 'application/json':
        return jsonify({'message': 'Cours supprimé avec succès'}), 200
    return redirect(url_for('index'))

@cours_bp.route('/cours/<int:cours_id>', methods=['POST'])
def delete_cours_post(cours_id):
    if request.form.get('_method') == 'DELETE':
        return delete_cours(cours_id)  # Handles DELETE via POST from index.html
    return jsonify({'error': 'Méthode non supportée'}), 405