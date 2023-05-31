#!/bin/sh

pipenv install
pipenv install --dev

echo "creating databases"

psql postgres << EOF
create database {{cookiecutter.project_name}};
create database {{cookiecutter.project_name}}_test;
EOF

python manage.py makemigrations
python manage.py migrate

# replace the cookiecutter stuff in the templates
find {{cookiecutter.project_name}}/templates -type f -exec sed -i 's/{% raw %}{{cookiecutter.project_name}}{% endraw %}/{{cookiecutter.project_name}}/g' {} +
