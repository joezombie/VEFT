from flask import Flask, render_template
from models import Movie
from db import Session


session = Session()


app = Flask(__name__)

@app.route('/')
def index():
	movies = session.query(Movie).all()
	return render_template('index.html', movies=movies)


if __name__ == '__main__':
	app.run(debug=True)