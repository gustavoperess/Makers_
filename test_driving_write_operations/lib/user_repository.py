from lib.user import *


class UserRepository():
    
    def __init__(self, connection):
        self.connection = connection
        
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        recipe = []
        for row in rows:
            book = User(row['id'], row['user_email'], row['user_name'])
            recipe.append(book)
        return recipe   
    
    def find(self, id):
        rows = self.connection.execute('SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["user_email"], row["user_name"])
