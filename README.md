# Trust in Superheroes

A simple Flask API.

## Get started

[Create a virtual environment](https://virtualenvwrapper.readthedocs.io/en/latest/install.html), and install the requirements:

```bash
mkvirtualenv superheroes
pip install -r requirements.txt
```

```
cp app_config.py.example app_config.py
```

```
createdb superheroes
```

This tool uses `flask_migrate` (a wrapper around Alembic) for data management. A custom `manage.py` file enables easeful use of `flask_migrate`. (N.b., this command helped to initialize the database with migrations: `python manage.py db init` and `python manage.py db migrate`.) Newcomers! Use this command to apply migrations to your database:

```
python manage.py db upgrade
```

