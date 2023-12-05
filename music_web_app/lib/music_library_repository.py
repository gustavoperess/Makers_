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
            item = MusicLibrary(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    # Find a single album by its id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return MusicLibrary(row["id"], row["title"], row["release_year"], row["artist_id"])

    def create(self, albums):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                                 albums.title, albums.release_year, albums.artist_id])
        
        return None
    
    
    # Delete an album by its id
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None