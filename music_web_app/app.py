import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.music_library_repository import MusicLibraryRepository
from lib.music_library import MusicLibrary
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

app = Flask(__name__)

@app.route('/albums', methods=['GET'])
def get_all_albums():
    connection = get_flask_database_connection(app)
    repository = MusicLibraryRepository(connection)
    return "\n".join([
            str(album) for album in repository.all()
        ])

@app.route('/albums', methods=['POST'])
def post_new_album():
    connection = get_flask_database_connection(app)
    repository = MusicLibraryRepository(connection)
    album = MusicLibrary(None, request.form['title'], request.form['release_year'], request.form['artist_id'])    
    album = repository.create(album)
    return ""

@app.route('/artists', methods=['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join([
            str(artists) for artists in repository.all()
        ])

@app.route('/artists', methods=['POST'])
def post_new_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])    
    artist = repository.create(artist)
    return ""


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))




