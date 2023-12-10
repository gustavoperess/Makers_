class Post:
    
    def __init__(self, id, post_title, post_content, post_number_of_views, post_time, user_id):
        self.id = id
        self.title = post_title
        self.content = post_content
        self.number_views = post_number_of_views
        self.post_time = post_time
        self.user_id = user_id
       
    
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"({self.id}, {self.title}, {self.content}, {self.number_views}, {self.post_time}, {self.user_id})"