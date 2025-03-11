from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from services.classes.app import db, Professeur

prof_bp = Blueprint('professeur', __name__)

@prof_bp.route('/professeurs/', methods=['GET'])
def get_professeurs():
    professeurs = Professeur.query.all()
    if request.headers.get('Accept') == 'application/json':
        return jsonify([prof.to_dict() for prof in professeurs]), 200
    return render_template('professeurs.html', professeurs=professeurs)

@prof_bp.route('/professeurs/', methods=['POST'])
def add_professeur():
    data = request.form if request.form else request.json
    if 'nom' not in data:
        return jsonify({'error': 'Le champ nom est obligatoire'}), 400

    new_prof = Professeur(nom=data['nom'])
    db.session.add(new_prof)
    db.session.commit()
    if request.headers.get('Accept') == 'application/json':
        return jsonify(new_prof.to_dict()), 201
    return redirect(url_for('professeur.get_professeurs'))

@prof_bp.route('/professeurs/<int:prof_id>', methods=['PUT'])
@prof_bp.route('/professeurs/<int:prof_id>', methods=['GET'])
def get_professeur(prof_id):
    prof = Professeur.query.get_or_404(prof_id)
    if request.headers.get('Accept') == 'application/json':
        return jsonify(prof.to_dict()), 200
    return render_template('professeur_detail.html', prof=prof)
def update_professeur(prof_id):
    prof = Professeur.query.get(prof_id)
    if not prof:
        return jsonify({'error': 'Professeur non trouvé'}), 404

    data = request.json
    if 'nom' in data:
        prof.nom = data['nom']

    db.session.commit()
    return jsonify({'message': 'Professeur mis à jour avec succès', 'professeur': prof.to_dict()}), 200

@prof_bp.route('/professeurs/<int:prof_id>', methods=['DELETE'])
def delete_professeur(prof_id):
    prof = Professeur.query.get(prof_id)
    if not prof:
        return jsonify({'error': 'Professeur non trouvé'}), 404

    db.session.delete(prof)
    db.session.commit()
    return jsonify({'message': 'Professeur supprimé avec succès'}), 200