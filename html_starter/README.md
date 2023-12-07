
This documentation provides an overview of a simple Flask website created to showcase my ability to use Flask, create forms, conduct tests with pytest, and interact with a database using SQL. The website manages a music library, allowing users to view albums and artists, add new albums, and create new artists.

Project Structure
The project structure consists of the following main components:

app.py: The main Flask application file containing route definitions and server configuration.
lib: A directory containing custom Python modules for database connection, repositories, and model classes.
templates: A directory containing HTML templates for rendering pages.
tests: A directory containing test files for pytest.
Dependencies
Make sure to install the necessary dependencies by running the following command:


pip install Flask pytest
Running the Application
To run the application, execute the following command in the terminal:


python app.py
The application will run on http://localhost:5001/ by default.

Routes
GET /emoji

Returns a smiley face in HTML.
Example: http://localhost:5001/emoji
GET /goodbye

Returns a goodbye message.
Example: http://localhost:5001/goodbye
GET /albums

Displays a list of all albums.
Example: http://localhost:5001/albums
GET /albums/int:id

Displays details of a specific album.
Example: http://localhost:5001/albums/1
GET /details/int:id

Displays artists and albums associated with a specific artist ID.
Example: http://localhost:5001/details/1
GET /artist/int:id

Displays details of a specific artist.
Example: http://localhost:5001/artist/1
GET /artists

