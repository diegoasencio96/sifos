#!/bin/bash
python manage.py collectstatic
python manage.py migrate
python manage.py loaddata database/seeders/*.json
python manage.py runserver 0.0.0.0:8001