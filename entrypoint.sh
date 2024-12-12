#!/bin/bash

# Arrêter le script en cas d'erreur
set -e

# Attendre que PostgreSQL soit prêt
until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "Attente de PostgreSQL..."
  sleep 2
done

# Activer l'environnement virtuel
source /env/bin/activate

# Appliquer les migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Démarrer le serveur Django
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
