#!/bin/bash

# Arrêter le script en cas d'erreur
set -e
# Activer l'environnement virtuel
source /env/bin/activate

# Exécuter la commande donnée
exec "$@"
# Attendre que PostgreSQL soit prêt
until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "Attente de PostgreSQL..."
  sleep 2
done




python manage.py makemigrations
python manage.py migrate

# Démarrer le serveur Django
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
