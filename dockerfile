# Utiliser une image Python légère comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier les dossiers et fichiers nécessaires
COPY app/ ./app/
COPY templates/ ./templates/

# Exposer le port 5000 (port par défaut de Flask)
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["python", "app/app.py"]
