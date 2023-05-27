#!/bin/sh
echo "creating databases"

psql postgres << EOF
create database {{cookiecutter.project_name}};
create database {{cookiecutter.project_name}}_test;
EOF

python manage.py makemigrations
python manage.py migrate
