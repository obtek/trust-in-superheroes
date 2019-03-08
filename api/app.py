from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, or_
from datetime import datetime

from .app_config import SQLALCHEMY_DATABASE_URI
from . import create_app

app = create_app()
db = SQLAlchemy(app)
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)

from api.models import SuperHero, Status


@app.route('/heroes', methods=['GET'])
def heroes_list():
	query = '''
		SELECT 
			superhero.id,
			superhero_alias, 
			email_address,
			first_name,
			last_name,
			to_char(started_on, 'YYYY-MM-DD') as started_on,
			to_char(finished_on, 'YYYY-MM-DD') as finished_on,
			CAST(income AS VARCHAR) AS income,
			status.status
		FROM superhero
		JOIN status
		ON superhero.status_id=status.id
	'''

	if request.args:
		query += ' WHERE superhero_alias is not null'

		started_after = request.args.get('started_after')
		if started_after:
			query += " AND started_on > to_date('{}', 'YYYY-MM-DD')".format(started_after)
		
		started_before = request.args.get('started_before')
		if started_before:
			query += " AND started_on < to_date('{}', 'YYYY-MM-DD')".format(started_before)

		finished_after = request.args.get('finished_after')
		if finished_after:
			query += " AND finished_on > to_date('{}', 'YYYY-MM-DD')".format(finished_after)

		finished_before = request.args.get('finished_before')
		if finished_before:
			query += " AND finished_on < to_date('{}', 'YYYY-MM-DD')".format(finished_before)

		income_below = request.args.get('income_below')
		if income_below:
			query += ' AND income < {}'.format(income_below)

		income_above = request.args.get('income_above')
		if income_above:
			query += ' AND income > {}'.format(income_above)

		income_equal = request.args.get('income_equal')
		if income_equal:
			query += ' AND income = {}'.format(income_equal)

		status = request.args.get('status')
		if status:
			query += ' AND status = {}'.format(status)

	sql_results = engine.execute(query).fetchall()
	
	jsonify_data = [dict(r) for r in sql_results]

	return jsonify(jsonify_data), 200

@app.route('/heroes', methods=['POST'])
def heroes_create():
	hero_json = request.get_json()

	status = Status.query.filter_by(status=hero_json['status']).first()

	if not status:
		status = Status(status=hero_json['status'])
		db.session.add(status)
		db.session.commit()
	
	# https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators
	hero = db.session.query(SuperHero).filter(or_(SuperHero.superhero_alias == hero_json.get('superhero_alias'),\
						    		   			  SuperHero.email_address == hero_json.get('email_address')))\
									  .first()

	if not hero:
		new_hero = SuperHero(superhero_alias=hero_json.get('superhero_alias'),
							 email_address=hero_json.get('email_address'),
							 first_name=hero_json.get('first_name'),
							 last_name=hero_json.get('last_name'),
							 started_on=hero_json.get('started_on', datetime.utcnow()),
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