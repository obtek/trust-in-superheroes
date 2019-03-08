POSTGRES = {
    'user': '',
    'pw': '',
    'db': 'superheroes',
    'host': 'localhost',
    'port': '5432',
}

DB_CONN = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(**POSTGRES)