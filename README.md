# Trust in Superheroes

This simple Flask API contains endpoints for viewing, creating, and filtering super heroes affiliated with the prestigious Super Hero University. 

## Get started

[Create a virtual environment](https://virtualenvwrapper.readthedocs.io/en/latest/install.html), and install the requirements:

```bash
mkvirtualenv superheroes
pip install -r requirements.txt
```

Copy the example `app_config.py`, and customize it to your needs. The example `app_config.py` comes with everything you need for local development – so, for now, you likely do not need to modify it.

```
cp api/app_config.py.example api/app_config.py
```

Create a database (n.b., the name of your database should match the one given in app_config.py).

```
createdb superheroes
```

This tool uses `flask_migrate` (a wrapper around Alembic) for data management. A custom `manage.py` file enables easeful use of `flask_migrate`. (N.b., this command helped to initialize the database with migrations: `python manage.py db init` and `python manage.py db migrate`.) 

Apply migrations to your database like so:

```
python manage.py db upgrade
```

The api itself lives in the `api` directory. Run it!
```
cd api
flask run
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

## Team

* Greg Mundy
* Regina Compton
