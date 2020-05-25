#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "waiting for the Postgres instance to be healthy before starting Gunciorn"

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"
