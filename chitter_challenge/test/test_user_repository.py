# from lib.user_repository import UserRepository
# from lib.user import User
    

# """
# When we call UserRepository#all
# We find all users from the database.
# """

# def test_all_users(db_connection):
#     db_connection.seed("seeds/users.sql")
#     repository = UserRepository(db_connection)

#     initial_user_count = repository.get_user_count()

#     users = repository.all()

#     expected_users = [
#         User(i, f'User{i}', f'Password{i}') for i in range(1, initial_user_count + 1)
#     ]

#     # Assert that the returned users match the expected result
#     assert users == expected_users

# """
# When we call UserRepository#find
# We find a user from the database.
# """

# def test_find_single_user(db_connection):
#     db_connection.seed("seeds/users.sql")  # Seed our database with some test data
#     repository = UserRepository(db_connection)  # Create a new ArtistRepository

#     user = repository.find(1)
#     assert user == User(1, "gustavoperess", "gustavoperess")
    

# """
# When we call UserRepository#find
# We find a user from the database by name.
# """

# def test_find_user_by_name(db_connection):
#     db_connection.seed("seeds/users.sql")  # Seed our database with some test data
#     repository = UserRepository(db_connection)  # Create a new ArtistRepository

#     user = repository.find_by_name("Gustavo")
#     assert user == User(1, "Gustavo", "Gustavo123")


# """
# When we call UserRepository#find_by_name and the name is not found returns None
# We remove a record from the database.
# """

# def test_find_user_by_name_with_none(db_connection):
#     db_connection.seed("seeds/users.sql")  # Seed our database with some test data
#     repository = UserRepository(db_connection)  # Create a new ArtistRepository

#     user = repository.find_by_name("notInTheDatabase")
#     assert user == None


# """
# When we call UserRepository#create
# We create a record from the database.
# """

# def test_create_user(db_connection):
#     db_connection.seed("seeds/users.sql")  # Seed our database with some test data
#     repository = UserRepository(db_connection)  # Create a new ArtistRepository
    
#     create_user = repository.create(User(None, 'Gabriel', 'Gabriel123'))
#     assert create_user == User(3, 'Gabriel', 'Gabriel123')
    
#     all_users = repository.all()
#     assert  all_users == [
#         User(1, 'Gustavo', 'Gustavo123'),
#         User(2, 'Ashley', 'Ashley123'),
#         User(3, 'Gabriel', 'Gabriel123')
#     ]
    
# """
# When we call UserRepository#delete
# We remove a record from the database.
# """

# def test_delete_record(db_connection):
#     db_connection.seed("seeds/users.sql")
#     repository = UserRepository(db_connection)
#     repository.delete(2) 

#     result = repository.all()
#     assert result == [
#         User(1, 'Gustavo', 'Gustavo123'),
#     ]


