# services/classes/models.py
from services.classes.app import db

class Cours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    professeur_id = db.Column(db.Integer, db.ForeignKey('professeur.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'professeur_id': self.professeur_id
        }

class Professeur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)

    def to_dict(self):  # Added
        return {
            'id': self.id,
            'nom': self.nom
        }

class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    niveau = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'niveau': self.niveau
        }

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)

    def to_dict(self):  # Added
        return {
            'id': self.id,
            'nom': self.nom
        }