from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

from . import create_app

app = create_app()
db = SQLAlchemy(app)

from api.models import SuperHero, Status

@app.route('/heroes', methods=['GET'])
def heroes_list():
	superheroes = SuperHero.query.all()
	superheroes_lst = [hero.serialize() for hero in superheroes]

	return jsonify(superheroes_lst), 200

@app.route('/heroes', methods=['POST'])
def heroes_create():
	hero_json = request.get_json()

	status = Status.query.filter_by(status=hero_json['status']).first()

	if not status:
		status = Status(status=hero_json['status'])
		db.session.add(status)
		db.session.commit()
	
	# https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators
	hero = db.session.query(SuperHero).filter(or_(SuperHero.superhero_alias == hero_json.get('superhero_alias'),
						    		   			  SuperHero.email_address == hero_json.get('email_address')))

	if not hero:
		new_hero = SuperHero(superhero_alias=hero_json.get('superhero_alias'),
							 email_address=hero_json.get('email_address'),
							 first_name=hero_json.get('first_name'),
							 last_name=hero_json.get('last_name'),
							 started_on=hero_json.get('started_on'),
							 finished_on=hero_json.get('finished_on'),
							 income=hero_json.get('income'),
							 status=status)

		db.session.add(new_hero)
		db.session.commit()

		return 'KER-SPLOOSH! New hero added to the data trust.', 201
	else:
		# https://httpstatuses.com/409
		return 'ZOWIE! A hero with the same superhero_alias or email_address already exists.', 409

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def heroes_detail(hero_id):
	hero = db.session.query(SuperHero).get(hero_id)

	if hero:
		return jsonify(hero.serialize()), 200
	else:
		return 'Not found', 404

@app.route('/api/health', methods=['GET'])
def health():

	return 'BAM! Successful request.', 201

if __name__ == '__main__':
	app.run()