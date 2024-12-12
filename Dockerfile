FROM python:3.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Combiner les installations système
RUN apt-get update \
    && apt-get install -y postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire et définir le workdir en une seule étape
WORKDIR /app

# Configurer l'environnement virtuel et installer les dépendances
COPY requirements.txt .
RUN python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install -r requirements.txt

# Copier le reste du code de l'application
COPY . /app

COPY .env /app/.env

# Rendre le script d'entrée exécutable
RUN chmod +x entrypoint.sh

# Définir la commande par défaut
CMD ["bash", "/app/entrypoint.sh"]
