# services/classes/route_professeurs.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.classes.models import Professeur
from services.classes.app import db

professeur_bp = Blueprint('professeur', __name__)

# READ (Liste des professeurs)
@professeur_bp.route('/professeurs')
def list_professeurs():
    professeurs = Professeur.query.all()
    return render_template('professeurs/list.html', professeurs=professeurs)

# CREATE (Ajouter un professeur)
@professeur_bp.route('/professeurs/add', methods=['GET', 'POST'])
def add_professeur():
    if request.method == 'POST':
        nom = request.form.get('nom')
        if not nom:
            flash('Le nom est requis !', 'error')
            return redirect(url_for('professeur.add_professeur'))
        professeur = Professeur(nom=nom)
        db.session.add(professeur)
        db.session.commit()
        flash('Professeur ajouté avec succès !', 'success')
        return redirect(url_for('professeur.list_professeurs'))
    return render_template('professeurs/add.html')

# UPDATE (Modifier un professeur)
@professeur_bp.route('/professeurs/edit/<int:id>', methods=['GET', 'POST'])
def edit_professeur(id):
    professeur = Professeur.query.get_or_404(id)
    if request.method == 'POST':
        nom = request.form.get('nom')
        if not nom:
            flash('Le nom est requis !', 'error')
            return redirect(url_for('professeur.edit_professeur', id=id))
        professeur.nom = nom
        db.session.commit()
        flash('Professeur modifié avec succès !', 'success')
        return redirect(url_for('professeur.list_professeurs'))
    return render_template('professeurs/edit.html', professeur=professeur)

# DELETE (Supprimer un professeur)
@professeur_bp.route('/professeurs/delete/<int:id>', methods=['POST'])
def delete_professeur(id):
    professeur = Professeur.query.get_or_404(id)
    db.session.delete(professeur)
    db.session.commit()
    flash('Professeur supprimé avec succès !', 'success')
    return redirect(url_for('professeur.list_professeurs'))

def init_routes(app):
    app.register_blueprint(professeur_bp)