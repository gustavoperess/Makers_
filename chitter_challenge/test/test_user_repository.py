from lib.user_repository import UserRepository
from lib.user import User
    

"""
When we call UserRepository#all
We find all users from the database.
"""

def test_all_users(db_connection):
    db_connection.seed("seeds/users.sql") 
    repository = UserRepository(db_connection) 
    
    users = repository.all()
    
    assert users == [
        User(1, 'Gustavo', 'Gustavo123'),
        User(2, 'Ashley', 'Ashley123'),
        User(3, 'Mario', 'Mario123'),
        User(4, 'Rosangela', 'Rosangela123')
    ]


"""
When we call UserRepository#find
We find a user from the database.
"""

def test_find_single_user(db_connection):
    db_connection.seed("seeds/users.sql")  # Seed our database with some test data
    repository = UserRepository(db_connection)  # Create a new ArtistRepository

    user = repository.find(1)
    assert user == User(1, "Gustavo", "Gustavo123")
    

"""
When we call UserRepository#find
We find a user from the database by name.
"""

def test_find_user_by_name(db_connection):
    db_connection.seed("seeds/users.sql")  # Seed our database with some test data
    repository = UserRepository(db_connection)  # Create a new ArtistRepository

    user = repository.find_by_name("Gustavo")
    assert user == User(1, "Gustavo", "Gustavo123")


"""
When we call UserRepository#find_by_name and the name is not found returns None
We remove a record from the database.
"""

def test_find_user_by_name_with_none(db_connection):
    db_connection.seed("seeds/users.sql")  # Seed our database with some test data
    repository = UserRepository(db_connection)  # Create a new ArtistRepository

    user = repository.find_by_name("notInTheDatabase")
    assert user == None


"""
When we call UserRepository#create
We create a record from the database.
"""

def test_create_user(db_connection):
    db_connection.seed("seeds/users.sql")  # Seed our database with some test data
    repository = UserRepository(db_connection)  # Create a new ArtistRepository
    
    create_user = repository.create(User(None, 'Gabriel', 'Gabriel123'))
    assert create_user == (True, User(5, 'Gabriel', 'Gabriel123'))
    
    all_users = repository.all()
    assert  all_users == [
        User(1, 'Gustavo', 'Gustavo123'),
        User(2, 'Ashley', 'Ashley123'),
        User(3, 'Mario', 'Mario123'),
        User(4, 'Rosangela', 'Rosangela123'),
        User(5, 'Gabriel', 'Gabriel123')
    ]
    
"""
When we call UserRepository#delete
We remove a record from the database.
"""

# NEED TO COME BACK TO HANDLE HOW TO DELETE BOTH THE USER IS DELETED 

# def test_delete_record(db_connection):
#     db_connection.seed("seeds/users.sql")
#     repository = UserRepository(db_connection)

#     assert repository.delete(2) == None
#     assert repository.all() == [
#         User(1, 'Gustavo', 'Gustavo123'),
#         User(3, 'Mario', 'Mario123'),
#         User(4, 'Rosangela', 'Rosangela123'),
#     ]


