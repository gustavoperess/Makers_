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
        
    