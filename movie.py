class Movie:
    def __init__(self):
        self._trailer_youtube_url = ''
        self._title = ''
        self._release_date = ''
        self._poster_image_url = ''
        self._actors = []

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
