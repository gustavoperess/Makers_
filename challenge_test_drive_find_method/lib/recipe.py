class Recipe:

    def __init__(self, id, name, time, rating):
        self.id = id
        self.name = name
        self.time  = time
        self.rating = rating
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"({self.id}, {self.name}, {self.time}, {self.rating})"
