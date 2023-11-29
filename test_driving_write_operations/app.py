from lib.database_connection import DatabaseConnection
from lib.post_repository import *
from lib.user_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")


recipe_repository = PostRepository(connection)
recipes = recipe_repository.all()

for recipe in recipes:
    print(recipe)


