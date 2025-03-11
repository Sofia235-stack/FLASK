import os

class Config:
    """Configuration principale de l'application"""

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:passer@localhost/gestion_etablissement?client_encoding=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")  # Pour sécuriser les sessions et JWT si besoin
