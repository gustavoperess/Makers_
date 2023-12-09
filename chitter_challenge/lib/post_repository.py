from lib.post import Post

class PostRepository():
    
    def __init__(self, connection):
        self.connection = connection
        
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM posts ORDER BY id ASC')
        
        recipe = []
        for row in rows:
            book = Post(row['id'], row["post_title"], row["post_content"], row["post_number_of_viwes"], row["user_id"])
            recipe.append(book)
       
        return recipe
    
    
    def find(self, id):
        rows = self.connection.execute('SELECT * from posts WHERE id = %s', [id])
        row = rows[0]
        return Post(row['id'], row["post_title"], row["post_content"], row["post_number_of_viwes"], row["user_id"])
    
    
    def create(self, post):
        self.connection.execute(
            "INSERT INTO posts (post_title, post_content, post_number_of_viwes, user_id) VALUES (%s, %s, %s, %s)",
            [post.title, post.content, post.number_views, post.user_id]
        )
        return None
    
    def delete(self, id):
        self.connection.execute(
            "DELETE FROM posts WHERE id = %s",
            [id]
        )
        return None
    
    def update(self, post):
        self.connection.execute(
            "UPDATE posts SET post_title = %s, post_content =%s, post_number_of_viwes =%s, user_id =%s WHERE id= %s",
            [post.id, post.title, post.content, post.number_views, post.user_id]
        )
