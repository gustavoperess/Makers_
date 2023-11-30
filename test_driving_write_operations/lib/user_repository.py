from lib.user import *


class UserRepository():
    
    def __init__(self, connection):
        self.connection = connection
        
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM users ORDER BY id ASC')
        recipe = []
        for row in rows:
            book = User(row['id'], row['user_email'], row['user_name'])
            recipe.append(book)
        return recipe   
    
    def find(self, id):
        rows = self.connection.execute('SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["user_email"], row["user_name"])

    
    def create(self, user):
        self.connection.execute(
            "INSERT INTO users (user_email, user_name) VALUES (%s, %s)",
            [user.email, user.name]
        )
        return None
    
    def delete(self, id):
        self.connection.execute(
            "DELETE FROM users WHERE id = %s",
            [id]
        )
        return None
    
    def update(self, user):
        self.connection.execute(
            "UPDATE users SET user_email = %s, user_name =%s WHERE id= %s",
            [user.email, user.name, user.id]
        )

    