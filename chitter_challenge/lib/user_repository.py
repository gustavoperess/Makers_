from lib.user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection
         
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            user = User(row['id'], row['user_name'], row['user_password'])
            users.append(user)
        return users
    
    def find(self, user_id):
        row = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        
        row = row[0]
        return User(row['id'], row['user_name'], row['user_password'])
    
    def find_by_name(self, user_name):
        row = self._connection.execute(
            'SELECT * from users WHERE user_name = %s', [user_name])
        
        row = row[0]
        return User(row['id'], row['user_name'], row['user_password'])
    
    
    
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (user_name, user_password) VALUES (%s, %s) RETURNING id', [
                                        user.user_name, user.user_password])
        
        row = rows[0]
        user.id = row["id"]
        return user
    
    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None