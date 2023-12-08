from lib.user_repository import UserRepository
from lib.user import User
    
    
def test_all_users(db_connection):
    db_connection.seed("seeds/users.sql") # Seed our database with some test data 
    repository = UserRepository(db_connection) # Create a new ArtistRepository
    
    users = repository.all()
    
    assert users == [
        User(1, 'Gustavo', 'Gustavo123'),
        User(2, 'Ashley', 'Ashley123')
    ]

def test_find_single_user(db_connection):
    db_connection.seed("seeds/users.sql")  # Seed our database with some test data
    repository = UserRepository(db_connection)  # search for a single user 

    user = repository.find(1)
    print("HERE")
    print(user)
    assert user == User(1, "Gustavo", "Gustavo123")