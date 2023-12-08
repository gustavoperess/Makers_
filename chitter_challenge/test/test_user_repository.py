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