from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


names = {"seta":{"age":19, "gender": "male"}, "murdha":{"age":21, "gender":"male"}}


class HelloWorld(Resource):
	def get(self,name):
		return names[name]
		
api.add_resource(HelloWorld, "/helloworl/<string:name>")

if __name__ == "__main__":
	app.run(debug=True, port = 5001)