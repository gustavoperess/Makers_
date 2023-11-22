# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

class Todo:
    def __init__(self):
        self.list_of_todos = [] # list of items within the list 
        self.list_of_items = {}

    def adding_input_to_list(self, user_input):
        self.list_of_todos.append(user_input)
        self.list_of_items = {}
        for number, items in enumerate(self.list_of_todos, 1):
            self.list_of_items[number] = items

        
    def returning_list_of_items(self):      
        return self.list_of_items

    def removing_completed_items(self, item_to_remove):
        if item_to_remove == " " or item_to_remove == 0:
            raise Exception("Number cannot be 0 or empty")
        else:    
            new_dict = {}
            for number, items, in self.list_of_items.items():
                if number != item_to_remove:
                    new_dict[number] = items

            self.list_of_items = new_dict





# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.



class Music_tracker:
    def __init__(self):
        self.list_of_musics = []

    def adding_to_list(self, music_to_add):
        self.list_of_musics.append(music_to_add)
    
    def musics(self):
       return self.list_of_musics