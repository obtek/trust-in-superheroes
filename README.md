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

## Docker

The repo contains a `Dockerfile` and a `docker-compose.yml` service configuration. The Flask app context is created in `wsgi.py` and the container will serve up the application via Gunicorn instead of the standard Werkzeug development server used by the Flask framework. The bash script `cmd.sh` does two things, namely:	

- Attempt to load the database migration (looping until the PostgreSQL container is actually available).	

- Launch the Flask application via Gunicorn with 4 worker threads.	

To build and run the containers locally, first add the following configuration to your `app.config` file.	

```python	
POSTGRES = {	
    'user': 'superhero_user',	
    'pw': '1qaz2wsx3edc',	
    'db': 'superheroes',	
    'host': 'postgres',	
    'port': '5432',	
}	
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(**POSTGRES)	
DEBUG = True	
SQLALCHEMY_TRACK_MODIFICATIONS = False	
```	

Then assuming that `Docker` and `docker-compose` are both installed, build the Docker container via the command:	

```bash	
docker-compose build	
```	

If everything went well, a message similar to the one shown below will be displayed.	

```bash	
Step 10/10 : ENTRYPOINT [ "/superheroes/cmd.sh" ]	
 ---> Using cache	
 ---> c9fbfa693a8a	
Successfully built c9fbfa693a8a	
Successfully tagged reginafcompton/trust-in-superheroes:1.0.0	
```	

Finally, run the service (PostgreSQL and API containers) by excuting the command:	

```bash	
docker-compose up -d	
```	

The optional `-d` flag will run the containers in the background (or daemon mode). Voila! Now the API will respond to requests on localhost port 8000.

## Team

* Greg Mundy
* Regina Compton
