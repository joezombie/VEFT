from models import Movie
from db import Session

session = Session()
session.add(Movie(title='Terminator', year=1995))
session.add(Movie(title='Terminator 2', year=1997))
session.add(Movie(title='Alien', year=1987))
session.add(Movie(title='Terminator vs Alien', year=2023))
session.add(Movie(title='Star Wars Jar Jar the Jedi', year=2018))
session.add(Movie(title='Terminator 45', year=2045))
session.commit()