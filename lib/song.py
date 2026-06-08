class Song:
    # Class Attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance Attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Triggering class methods upon creation
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds any new genres to a class attribute genres. Ensure there are only unique genres."""
        if cls.genres is None:
            cls.genres = []
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds any new artists to a class attribute artists. Ensure there are only unique artists."""
        if cls.artists is None:
            cls.artists = []
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates class attribute genre_count. Increments genre key by 1, if genre doesn't exist, set to 1."""
        if cls.genre_count is None:
            cls.genre_count = {}
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Updates class attribute artists_count and artist_count. Increments artists key by 1, if artist doesn't exist, set to 1."""
        if cls.artist_count is None:
            cls.artist_count = {}
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

        if cls.artists_count is None:
            cls.artists_count = {}
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Alias for add_to_artists_count to handle naming variations."""
        cls.add_to_artists_count(artist)
