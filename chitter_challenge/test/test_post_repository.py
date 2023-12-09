from lib.post_repository import *
from lib.post import *

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/users.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    post = repository.all() # Get all users

    # Assert on the results
    assert post == [
        Post(1, "title01", "content01", 145, 1),
        Post(2, "title02", "content02", 245, 1),
        Post(3, "title03", "content03", 45, 2),
    ]

def test_to_check_for_a_single_album(db_connection):
    db_connection.seed("seeds/users.sql")
    a_repository = PostRepository(db_connection)
    
    albums = a_repository.find(2)
    assert albums == Post(2, "title02", "content02", 245, 1)

def test_to_create(db_connection):
    db_connection.seed("seeds/users.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository
    
    post = Post(4, "title04", "content04",55, 3)
    assert repository.create(post) == None
    assert repository.all() == [
        Post(1, "title01", "content01", 145, 1),
        Post(2, "title02", "content02", 245, 1),
        Post(3, "title03", "content03", 45, 2),
        Post(4, "title04", "content04",55, 3)
        
    ]

def test_to_delete(db_connection):
    db_connection.seed("seeds/users.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository
   
    assert repository.delete(1) == None
    assert repository.all() == [
        Post(2, "title02", "content02", 245, 1),
        Post(3, "title03", "content03", 45, 2),
    ]

def test_to_update(db_connection):
    db_connection.seed("seeds/users.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository
    
    post = repository.find(1)
    post.id = 1
    assert repository.update(post) == None
    assert repository.all() == [
        Post(1, "title01", "content01", 145, 1),
        Post(2, "title02", "content02", 245, 1),
        Post(3, "title03", "content03", 45, 2),     
    ]