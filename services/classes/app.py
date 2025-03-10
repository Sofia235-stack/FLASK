from flask import Flask
from routes import class_routes
from database import init_db, db  # Import direct de `db`
from sqlalchemy import text

app = Flask(__name__)
app.config.from_object('config')

# Initialisation de la base de données
init_db(app)

# Enregistrement des routes
app.register_blueprint(class_routes, url_prefix='/classes')

print("Routes enregistrées :")
for rule in app.url_map.iter_rules():
    print(rule)

# Vérification de la connexion à la base de données
try:
    with app.app_context():
        db.session.execute(text('SELECT 1'))
        print("✅ Connexion Flask/PostgreSQL OK !")

except Exception as e:
    print(f"❌ Erreur de connexion Flask/PostgreSQL : {e}")

# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
