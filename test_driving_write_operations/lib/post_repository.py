from lib.post import *


class PostRepository():
    
    def __init__(self, connection):
        self.connection = connection
        
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        
        recipe = []
        for row in rows:
            book = Post(row['id'], row["post_title"], row["post_content"], row["post_number_of_viwes"], row["user_id"])
            recipe.append(book)
       
        return recipe
    
    
    def find(self, id):
        rows = self.connection.execute('SELECT * from posts WHERE id = %s', [id])
        row = rows[0]
        return Post(row['id'], row["post_title"], row["post_content"], row["post_number_of_viwes"], row["user_id"])