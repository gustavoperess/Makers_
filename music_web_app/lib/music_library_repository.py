from lib.music_library import MusicLibrary


class MusicLibraryRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection
    
    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = MusicLibrary(row["id"], row["title"], row["release_year"])
            albums.append(item)
        return albums