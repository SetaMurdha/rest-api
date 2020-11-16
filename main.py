from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine 
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Author(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(20))
	specialisation = db.Column(db.String(50))

	def __init__(self, name, specialisation):
		self.name = name
		self.specialisation = specialisation
	def __repr__(self):
		return '<Product %d>' % self.id
db.create_all()

class AuthorSchema(ModelSchema):
	class Meta(ModelSchema.Meta):
		model = Authors
		sqla_session = db.session 

	id = fields.Number(dump_only=True)
	name = fields.String(required=True)
	specialisation = fields.String(required=True)


@app.route('/authors', methods=['GET'])

def index():
	get_authors = Authors.query.all()
	author_schema = AuthorSchema(many=True)
	authors, error = author_schema.dump(get_authors)
	return make_response(jsonify({'authors':authors}))

if __name__ == '__main__':
	app.run(debug = True)