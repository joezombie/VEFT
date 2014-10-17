from flask import Flask, request, render_template
from flask.ext.restful import Api, Resource, reqparse
import json
import memcache

memcached_host = '127.0.0.1:11211'
client = memcache.Client([memcached_host], debug=True)

client.set('left', 0)
client.set('right', 0)

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('left', type=int)
parser.add_argument('right', type=int)

@app.route('/')
def Index():
	return render_template('index.html', left=client.get('left'), right=client.get('right'))

class Left(Resource):
	def get(self):
		return {'left': client.get('left')}
	def post(self):
		client.incr('left')
		return ({'left': client.get('left')}, 201)

api.add_resource(Left, '/balance/left')


class Right(Resource):
	def get(self):
		return {'right': client.get('right')}
	def post(self):
		client.incr('right')
		return ({'right': client.get('right')}, 201)

api.add_resource(Right, '/balance/right')

if __name__ == '__main__':
	app.run(debug=True)
