from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Initialise la base de données avec Flask"""
    db.init_app(app)  # Associe SQLAlchemy avec l'application Flask
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas