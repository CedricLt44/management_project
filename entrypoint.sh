#!/bin/bash

# Arrêter le script en cas d'erreur
set -e

# Activer l'environnement virtuel
# Vérifier l'OS et activer l'environnement virtuel en conséquence
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Si c'est Linux, utiliser le chemin bin
    source /env/bin/activate
elif [[ "$OSTYPE" == "msys" ]]; then
    # Si c'est Windows via Git Bash, utiliser le chemin Scripts
    source /env/Scripts/activate
else
    echo "Système d'exploitation non pris en charge."
    exit 1
fi

# Exécuter la collecte des fichiers statiques (c'est une opération courante pour Django avant de démarrer l'application)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Exécuter les migrations de la base de données avant de démarrer l'application (optionnel mais recommandé)
echo "Running migrations..."
python manage.py migrate --noinput

# Vérification de la variable $1
if [ "$1" == "gunicorn" ]; then
    # Lancer Gunicorn si l'argument est 'gunicorn'
    echo "Starting Gunicorn..."
    exec gunicorn management_project.wsgi:application -b 0.0.0.0:8000
else
    # Sinon, lancer le serveur de développement Django (à éviter en production)
    echo "Starting Django development server..."
    exec python manage.py runserver 0.0.0.0:8000
fi
