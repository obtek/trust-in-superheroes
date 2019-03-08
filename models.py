from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, Numeric, Column, ForeignKey

db = SQLAlchemy()

class SuperHero(db.Model):
    __tablename__ = 'superhero'
    id = Column(Integer, primary_key=True)
    superhero_alias =  Column(String, nullable=False, unique=True)
    email_address = Column(String, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    started_on = Column(DateTime, default=datetime.utcnow()) # YYYY-MM-DD
    finished_on = Column(DateTime) # YYYY-MM-DD
    income = Column(Numeric(asdecimal=True))
    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)

    def __repr__(self):
        return '<SuperHeroModel %r>' % self.superhero_alias

class Status(db.Model):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    status = Column(String)
    heroes = db.relationship('SuperHero', backref='status', lazy=True)
