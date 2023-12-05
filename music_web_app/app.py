import os
from flask import Flask, request
from lib.database_connection import DatabaseConnection
from lib.music_library_repository import MusicLibraryRepository
from lib.music_library import MusicLibrary

# Create a new Flask app
app = Flask(__name__)

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/albums', methods=['GET'])
def get_all_albums():
    connection = DatabaseConnection(app)
    repository = MusicLibraryRepository(connection)
    return "\n".join([
            str(book) for book in repository.all()
        ])



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))




