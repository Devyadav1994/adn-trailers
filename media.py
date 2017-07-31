class Video():
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self):
        self._trailer_youtube_url = ''
        self._title = ''
        self._duration
        self._release_date = ''
        self._poster_image_url = ''
        self._actors = []
        self._rating = ''

    @property
    def trailer_youtube_url(self):
        return self._trailer_youtube_url
    @trailer_youtube_url.setter
    def trailer_youtube_url(self, value):
        self._trailer_youtube_url = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def release_date(self):
        return self._release_date
    @release_date.setter
    def release_date(self, value):
        self._release_date = value

    @property
    def poster_image_url(self):
        return self._poster_image_url
    @poster_image_url.setter
    def poster_image_url(self, value):
        self._poster_image_url = value

    @property
    def actors(self):
        return self._actors
    @actors.setter
    def actors(self, value):
        self._actors = value

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, value):
        self._rating = value

class TvShow(Video):
    def __init__(self):
        Parent.__init__()

class Movie(Video):
    """ This class provides a way to store movie related information"""

    def __init__(self):
        Parent.__init__()
