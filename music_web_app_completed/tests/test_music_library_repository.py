from lib.music_library_repository import MusicLibraryRepository
from lib.music_library import MusicLibrary

"""
When we call Musiclibaray #all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_albums(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/albums.sql") # Seed our database with some test data
    repository = MusicLibraryRepository(db_connection) # Create a new BookRepository
    

    albums = repository.all() # Get all books

    # Assert on the results
    assert albums == [
        MusicLibrary(1,'Doolittle', 1989, 1),
        MusicLibrary(2,'Surfer Rosa', 1988, 2),
        MusicLibrary(3,'Waterloo', 1972, 3),
        MusicLibrary(4,'Bossanova', 1990, 1),
        MusicLibrary(5,'Lover', 2019, 1)
        
    ]



"""
# When we call Musiclibaray#find
# We get a single album object reflecting the seed data.
# """
def test_get_single_album(db_connection):
    db_connection.seed("seeds/albums.sql")
    repository = MusicLibraryRepository(db_connection)

    book = repository.find(3)
    assert book == MusicLibrary(3, "Waterloo", 1972, 3)

"""
When we call Musiclibaray#create
We get a new album in the database.
"""
def test_create_album(db_connection):
    db_connection.seed("seeds/albums.sql")
    repository = MusicLibraryRepository(db_connection)

    repository.create(MusicLibrary(6, "Born in babylon", 2010, 2))

    result = repository.all()
    assert result == [
        MusicLibrary(1,'Doolittle', 1989, 1),
        MusicLibrary(2,'Surfer Rosa', 1988, 2),
        MusicLibrary(3,'Waterloo', 1972, 3),
        MusicLibrary(4,'Bossanova', 1990, 1),
        MusicLibrary(5,'Lover', 2019, 1),
        MusicLibrary(6,'Born in babylon', 2010, 2)
    ]

"""
When we call Musiclibaray#delete
We remove an album from the database.
"""
def test_delete_album(db_connection):
    db_connection.seed("seeds/albums.sql")
    repository = MusicLibraryRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        MusicLibrary(1,'Doolittle', 1989, 1),
        MusicLibrary(2,'Surfer Rosa', 1988, 2),
        MusicLibrary(4,'Bossanova', 1990, 1),
        MusicLibrary(5,'Lover', 2019, 1),
    ]

