from lib.post_repository import *
from lib.post import *

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    post = repository.all() # Get all users

    # Assert on the results
    assert post == [
        Post(1, "title01", "content01", 145, None),
        Post(2, "title02", "content02", 245, None),
        Post(3, "title03", "content03", 45, None),
    ]

def test_to_check_for_a_single_album(db_connection):
    db_connection.seed("seeds/social_network.sql")
    a_repository = PostRepository(db_connection)
    
    albums = a_repository.find(2)
    assert albums == Post(2, "title02", "content02", 245, None)
    