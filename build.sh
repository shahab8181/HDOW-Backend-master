#!/usr/bin/env bash
# exit on error

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py makemigrations core
python manage.py migrate core
python manage.py makemigrations core
python manage.py makemigrations technician
python manage.py makemigrations client
python manage.py makemigrations
python manage.py migrate
# python manage.py createsuperuser --noinput
