class User:
    
    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name
    
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"({self.id}, {self.email}, {self.name})"