from lib.recipe import Recipe

class RecipeRepository():
    
     def __init__(self, connection):
        self.connection = connection
        
     
     def all(self):
        rows = self.connection.execute('SELECT * FROM recipe_directory')
        print(rows)
        recipe = []
        for row in rows:
            book = Recipe(row['id'], row['name'], row['time'], row['rating'])
            recipe.append(book)
        return recipe   
    
