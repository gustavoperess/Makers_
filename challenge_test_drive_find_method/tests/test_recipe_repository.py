from lib.recipe_repository import *
from lib.recipe import *

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipe_directory.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new ArtistRepository

    recepies = repository.all() # Get all artists

    # Assert on the results
    assert recepies == [
        Recipe(1,'Pasta', 1012 , 5),
        Recipe(2,'Sushi', 535, 5),
        Recipe(3,'Pizza', 1515, 4),
        Recipe(4,'Poutine', 330, 3),
        Recipe(5,'Donner', 700, 4)     
    ]






