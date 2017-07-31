import pickle
import os
import re
import pprint

from media import Movie, TvShow
from fresh_tomatoes import open_movies_page

ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

if not os.path.exists(os.path.join(RESOURCES_DIR, 'adn_trailers.db')):
    db_handler = open(os.path.join(RESOURCES_DIR, 'adn_trailers.db'), 'w')
    movies = []

    for i in range(5):
        movie_obj = Movie()
        movie_obj.title = 'Kung Fu Panda'
        movie_obj.trailer_youtube_url = 'https://www.youtube.com/watch?v=PXi3Mv6KMzY'
        movie_obj.poster_image_url = 'http://ia.media-imdb.com/images/M/MV5BMTIxOTY1NjUyN15BMl5BanBnXkFtZTcwMjMxMDk1MQ@@._V1_SX214_AL_.jpg'
        movie_obj.release_date = '2008'
        movie_obj.storyline = 'The Dragon Warrior has to clash against the savage Tai Lung as China\'s fate hangs in the balance: However, the Dragon Warrior mantle is supposedly mistaken to be bestowed upon an obese panda who is a tyro in martial arts.'
        movie_obj.actors = []

        movies.append(movie_obj)

    pickle.dump(movies, db_handler)

db_handler = open(os.path.join(RESOURCES_DIR, 'adn_trailers.db'), 'rb')
movies = pickle.load(db_handler)

open_movies_page(movies)
