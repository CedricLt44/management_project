# Utiliser l'image de base Python 3
FROM python:3

# Désactiver le buffer pour la sortie de Python
ENV PYTHONUNBUFFERED 1

# Empêcher Python de générer des fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Créer un répertoire pour l'application
RUN mkdir /app

# Définir le répertoire de travail
WORKDIR /app

# Copier uniquement le fichier requirements.txt pour profiter du cache Docker
COPY requirements.txt /app/

# Créer un environnement virtuel dans /env
RUN python -m venv /env


# Mettre à jour pip avant d'installer les dépendances
RUN python -m pip install --upgrade pip

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt

# Copier le reste du code de l'application
COPY . /app

# Exposer le port sur lequel l'application sera accessible
EXPOSE 8000
# Copier le script start.sh dans le conteneur
COPY start.sh /app/entrypoint.sh

# Rendre le script exécutable
RUN chmod +x /app/entrypoint.sh
# Définir la commande par défaut qui sera exécutée (peut être surchargée par le fichier bash)
CMD ["bash", "/app/entrypoint.sh"]
