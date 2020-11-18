from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/fooddatabase.db'
db = SQLAlchemy(app)

# def no_food(food_id):
# 	if not in food_id:
# 		abort(404, message = "Makanan tidak ditemukan")

class foodModelDB(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), nullable=False)
	jenis = db.Column(db.String(50), nullable=False)
	harga = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Food(name={name}, jenis = {jenis}, harga = {harga})"

food_put_args = reqparse.RequestParser()
food_put_args.add_argument("name", type = str, help="Makanan Belum Masuk", required = True)
food_put_args.add_argument("jenis", type = str, help="Jenis Belum Masuk", required = True)
food_put_args.add_argument("harga", type = int, help="Harga Belum Masuk", required = True)

food_update_args = reqparse.RequestParser()
food_update_args.add_argument("name", type = str, help="Makanan Belum Masuk")
food_update_args.add_argument("jenis", type = str, help="Jenis Belum Masuk")
food_update_args.add_argument("harga", type = int, help="Harga Belum Masuk")

resource_field ={
	'id': fields.Integer,
	'name': fields.String,
	'jenis': fields.String,
	'harga': fields.Integer
}

class food(Resource):
	@marshal_with(resource_field)
	def get(self, food_id):
		hasil = foodModelDB.query.filter_by(id=food_id).first()
		if not hasil:
			abort(404, message="Id tidak ditemukan")
		return hasil

	@marshal_with(resource_field)
	def put(self, food_id):
		args = food_put_args.parse_args()
		hasil = foodModelDB.query.filter_by(id=food_id).first()
		if hasil:
			abort(409, message="id makanan sudah ada")
		makanan = foodModelDB(id=food_id, name=args['name'], jenis=args['jenis'], harga=args['harga'])
		db.session.add(makanan)
		db.session.commit()
		return makanan,201

	@marshal_with(resource_field)
	def patch(self, food_id):
		args = food_update_args.parse_args()
		hasil = foodModelDB.query.filter_by(id=food_id).first()
		if not hasil:
			abort(404, message = "Video tidak ada")

		if args['name']:
			hasil.name = args['name'] 
		if args['jenis']:
			hasil.jenis = args['jenis']
		if args['harga']:
			hasil.harga = args['harga']

		db.session.commit()

		return hasil

	@marshal_with(resource_field)
	def delete(self, food_id):
		hasil = foodModelDB.query.filter_by(id=food_id).first()
		if not hasil:
			abort(409, message = "Makanan tidak ada")
		del hasil
		return '', 204



api.add_resource(food,"/food/<int:food_id>")

if __name__ == "__main__":
	app.run(debug=True)