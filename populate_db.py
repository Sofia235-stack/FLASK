# populate_db.py
from services.classes.app import db, Professeur, Cours, create_app
from sqlalchemy import text

app = create_app()
with app.app_context():
    # Step 1: Add and commit professors first
    prof1 = Professeur(nom="Prof A")
    prof2 = Professeur(nom="Prof B")
    db.session.add_all([prof1, prof2])
    db.session.commit()  # Ensure professors are in the database
    print(f"Added Prof A with ID: {prof1.id}")
    print(f"Added Prof B with ID: {prof2.id}")

    # Step 2: Prepare course updates with valid professeur_id
    updates = [
        {"professeur_id": prof1.id, "cours_id": 2},
        {"professeur_id": prof1.id, "cours_id": 4},
        {"professeur_id": prof2.id, "cours_id": 5},
    ]

    # Step 3: Execute batched updates using SQLAlchemy's Connection.execute()
    with db.engine.connect() as connection:
        update_stmt = text("UPDATE cours SET professeur_id = :professeur_id WHERE cours.id = :cours_id")
        connection.execute(update_stmt, updates)
        connection.commit()  # Commit the updates

    # Step 4: Verify
    print("Professeurs:", Professeur.query.all())
    print("Cours:", Cours.query.all())