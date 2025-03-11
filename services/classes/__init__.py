from flask import Flask
from services.classes.database import init_db

from services.classes.config import Config  # ✅ Bon chemin

app = Flask(__name__)
app.config.from_object(Config)

# Initialisation de la base de données
init_db(app)
