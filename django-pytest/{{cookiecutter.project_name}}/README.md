After running cookiecutter

# Install python packages
```
$ cd {{cookiecutter.project_name}}
$ pipenv install
$ pipenv shell
```

# Create PG database and superuser

```
$ cd website
$ sh ./finish_setup.sh
```

# Start your server:

```
$ python manage.py runserver
```
