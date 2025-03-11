# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances et les installer (éviter le cache pour s'assurer de l'installation)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Exposer le port
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "-m", "services.classes.app"]