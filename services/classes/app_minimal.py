# services/classes/app_minimal.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passer@localhost/gestion_etablissement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

# Define a simple model inline
class Cours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    cours = Cours.query.all()
    return f"Cours: {[c.titre for c in cours]}"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tables created")
    app.run(debug=True, port=5001)