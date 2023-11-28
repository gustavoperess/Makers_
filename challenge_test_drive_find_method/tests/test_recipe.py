from lib.recipe import *

def test_recepit():
    recipe = Recipe(1, "name", 5, 5)
    assert recipe.id == 1
    assert recipe.name == "name"
    assert recipe.time == 5
    assert recipe.rating == 5