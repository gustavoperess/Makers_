import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.music_library_repository import MusicLibraryRepository
from lib.music_library import MusicLibrary
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')


@app.route('/goodbye', methods=["GET"])
def say_goodbye():
    return render_template("goodbye.html", goodbye="BYE")


@app.route('/albums', methods=['GET'])
def get_all_albums():
    connection = get_flask_database_connection(app)
    repository = MusicLibraryRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)


@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = MusicLibraryRepository(connection)
    albums = repository.find(id)
    return render_template("albums/selected_album.html", album=albums)



@app.route('/details/<int:id>', methods=['GET'])
def get_artist_album(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    album_repo = MusicLibraryRepository(connection)
    artists = repository.find(id)
    albums = album_repo.find(id)
    return render_template("artists/index.html", artists=artists, albums=albums)


@app.route('/artist/<int:id>', methods=['GET'])
def get_artits_page(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    album_repo = MusicLibraryRepository(connection)
    artists = repository.find(id)
    albums = album_repo.find(id)
    return render_template("artists/artist.html", artists=artists, albums=albums)


@app.route('/artists', methods=['GET'])
def get_single_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists/artists.html", artists=artists)



# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
