from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

# Define models at module level
class Professeur(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    cours = relationship("Cours", back_populates="professeur")  # Back-reference

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom
        }

class Cours(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titre: Mapped[str] = mapped_column(String(100), nullable=False)
    professeur_id: Mapped[int] = mapped_column(Integer, ForeignKey('professeur.id'), nullable=False)
    professeur = relationship("Professeur", back_populates="cours")  # Relationship to Professeur

    def to_dict(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'professeur_id': self.professeur_id
        }

class Classe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    niveau: Mapped[str] = mapped_column(String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'niveau': self.niveau
        }

class Etudiant(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom
        }

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passer@localhost/gestion_etablissement'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/')
    def index():
        cours = Cours.query.all()
        professeurs = Professeur.query.all()
        return render_template('index.html', cours=cours, professeurs=professeurs)

    # Register Blueprints
    from services.classes.route_classe import classe_bp
    from services.classes.route_professeur import prof_bp
    from services.classes.route_cours import cours_bp
    from services.classes.route_etudiant import etudiant_bp

    with app.app_context():
        db.create_all()
        print("✅ Connexion Flask/PostgreSQL OK !")
        print("Tables créées ou vérifiées !")
        app.register_blueprint(classe_bp)
        app.register_blueprint(prof_bp)
        app.register_blueprint(cours_bp)
        app.register_blueprint(etudiant_bp)
        print("Routes enregistrées :")
        for rule in app.url_map.iter_rules():
            print(rule)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)