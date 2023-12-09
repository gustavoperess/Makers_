from lib.user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection
        self.existing_user = False
         
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            user = User(row['id'], row['user_name'], row['user_password'])
            users.append(user)
        return users
    
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        
        if rows:
            row = rows[0]
            return User(row['id'], row['user_name'], row['user_password'])
        else:
            return None
    
    
    
    def find_by_name(self, user_name):
        rows = self._connection.execute(
            'SELECT * from users WHERE user_name = %s', [user_name])
         
        if rows:
            row = rows[0]
            return User(row['id'], row['user_name'], row['user_password'])
        else:
            return None

    def create(self, user):
        user_already_exist = self.find_by_name(user.user_name)
        if not user_already_exist:
            rows = self._connection.execute('INSERT INTO users (user_name, user_password) VALUES (%s, %s) RETURNING id', [
                                            user.user_name, user.user_password])
            
            row = rows[0]
            user.id = self._generate_next_id()
            user.id = row["id"]
            return True, user 
        else:
            return False, None 
    
    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None
    
    def _generate_next_id(self):
        users = self.all()
        return max([user.id for user in users], default=0) + 1