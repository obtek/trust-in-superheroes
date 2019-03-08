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

## Get, create, and search heroes

Use the following endpoints to interact with the data trust API.

```
# get all heroes
curl http://127.0.0.1:5000/heroes
```

```
# add a new hero
curl -X POST -H "Content-Type: application/json" -d '{"email_address": "wonder@woman.us", "first_name": "Wonder", "last_name": "Woman", "income": "95000.99", "status": "Graduated", "superhero_alias": "Wonder Woman"}' http://127.0.0.1:5000/heroes
```

```
# query heroes (example)
curl http://127.0.0.1:5000/heroes?status='Active'&started_after=2000-01-01
```
