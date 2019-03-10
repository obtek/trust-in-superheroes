#!/bin/bash

until python manage.py db upgrade; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

gunicorn -b 0.0.0.0 -w 4 wsgi