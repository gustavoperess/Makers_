import os
from flask import Flask, request, redirect, render_template
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


@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template("albums/new.html")


@app.route('/albums', methods=['POST'])
def creat_album():
    connection = get_flask_database_connection(app)
    repository = MusicLibraryRepository(connection)
    title = request.form["title"]
    release_year = request.form["release_year"]
    artist_id = request.form["artist_id"]
    album = MusicLibrary(None, title, release_year, artist_id)

    if not album.is_valid():
        error = album.generate_errors()
        return render_template("albums/new.html", errors=error)
    repository.create(album)
    return redirect(f"albums/{album.id}")


@app.route('/artists/new', methods=['GET'])
def get_new_artists():
    return render_template("artists/new.html")


@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form["name"]
    genre = request.form["genre"]
    artist = Artist(None, name, genre)

    if not artist.is_valid():
        error = artist.generate_errors()
        return render_template("artists/new.html", errors=error)
    repository.create(artist)
    return redirect(f"artist/{artist.id}")




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
