from flask import Flask

from app_config import DB_CONN

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONN

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()