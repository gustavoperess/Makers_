from lib.user_repository import *
from lib.user import *

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository

    user = repository.all() # Get all users

    # Assert on the results
    assert user == [
        User(1,'gustavo123@gmail.com', "Gustavo"),
        User(2,'ashley123@gmail.com', "Ashley"),
        User(3,'rosangela123@gmail.com', "Rosangela"),
    ]


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository

    user = repository.all() # Get all users

    # Assert on the results
    assert user == [
        User(1,'gustavo123@gmail.com', "Gustavo"),
        User(2,'ashley123@gmail.com', "Ashley"),
        User(3,'rosangela123@gmail.com', "Rosangela"),
    ]


def test_to_check_for_a_single_album(db_connection):
    db_connection.seed("seeds/social_network.sql")
    a_repository = UserRepository(db_connection)
    
    albums = a_repository.find(1)
    assert albums == User(1,'gustavo123@gmail.com', "Gustavo")

def test_to_create(db_connection):
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository
    
    user = User(None, "mario", "mario@gmail.com")
    assert repository.create(user) == None
    assert repository.all() == [
        User(1,'gustavo123@gmail.com', "Gustavo"),
        User(2,'ashley123@gmail.com', "Ashley"),
        User(3,'rosangela123@gmail.com', "Rosangela"),
        User(4, "mario", "mario@gmail.com")
        
    ]

def test_to_delete(db_connection):
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository
   
    assert repository.delete(1) == None
    assert repository.all() == [
        User(2,'ashley123@gmail.com', "Ashley"),
        User(3,'rosangela123@gmail.com', "Rosangela"),
    ]

def test_to_update(db_connection):
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository
    
    user = repository.find(1)
    user.email = "gustavo123@gmail.com"
    assert repository.update(user) == None
    assert repository.all() == [
        User(1,'gustavo123@gmail.com', "Gustavo"),
        User(2,'ashley123@gmail.com', "Ashley"),
        User(3,'rosangela123@gmail.com', "Rosangela"),       
    ]