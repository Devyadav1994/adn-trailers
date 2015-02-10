import pickle
import os
import re
import pprint

from movie import Movie
from fresh_tomatoes import open_movies_page

ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'test.txt')
testFile=open(filename)
print(testFile.read())

if not os.path.exists(os.path.join(RESOURCES_DIR, 'adn_trailers.db')):
    db_handler = open(os.path.join(RESOURCES_DIR, 'adn_trailers.db'), 'r+')
    movies = []
    print("somethin")
    for i in range(5):
        movie = Movie()
        movie.title = 'Kung Fu Panda'
        movie.trailer_youtube_url = 'https://www.youtube.com/watch?v=PXi3Mv6KMzY'
        movie.poster_image_url = 'http://ia.media-imdb.com/images/M/MV5BMTIxOTY1NjUyN15BMl5BanBnXkFtZTcwMjMxMDk1MQ@@._V1_SX214_AL_.jpg'
        movie.release_date = '2008'
        movie.actors = []

        movies.append(movie)

    pickle.dump(movies, db_handler)

print(db_handler)
# db_handler = open(RESOURCES_DIR + 'adn_trailers.db', 'rb')
# movies = pickle.load(db_handler)

# open_movies_page(movies)
