# As a user
# So that I can record my experiences
# I want to keep a regular diary

# As a user
# So that I can reflect on my experiences
# I want to read my past diary entries

# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed

# As a user
# So that I can keep track of my tasks
# I want to keep a todo list along with my diary

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries

import re

class User:
    def __init__(self):
        self.user_information = []
     
    def add(self, user_input):
        self.user_information.append(user_input)
    
    def user_info(self):
        return self.user_information    
    
    def user_past_experiences(self):
        list_of_past_experiences = []
        for user in self.user_information:
            list_of_past_experiences.append(user.content)
        
        return list_of_past_experiences
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        if wpm == 0 or minutes == 0:
            raise ValueError("We can't estimate the time for 0")
        else:
            minutes = minutes / wpm
            my_minutes = int(minutes)
            hour, remaining_minutes = divmod(my_minutes, 60)
            minutes, seconds = divmod(remaining_minutes, 60)
            formatted_hours = "%d:%02d:%02d" % (hour, my_minutes, seconds)
            dic_of_items = {}
            for entry in self.user_information:
                reading_time = entry.reading_time(wpm)
                print(reading_time)
                if reading_time <= formatted_hours:
                    dic_of_items[entry.content] = reading_time

            if len(dic_of_items) == 0:
                raise ValueError("There is nothing you can read with this time")
            else:
                final_result = max(dic_of_items.items(), key=lambda x: x[1])
                return final_result[0]
        
    def incomplete(self):
        list_of_incompleted = []
        for items in self.user_information:
            if not items.completed:
                list_of_incompleted.append(items.todo)

        return list_of_incompleted
    
    def complete(self):
        list_of_completed = []
        for items in self.user_information:
            if items.completed:
                list_of_completed.append(items.todo)

        return list_of_completed

    def give_up(self):
        for items in self.user_information:
            items.mark_complete()  
    
    def all_my_contacts(self):
        dic_of_contacts = {}
        for contacts in self.user_information:
            dic_of_contacts[contacts.name] = contacts.phone
        
        return dic_of_contacts
    
    def numbers_in_my_diary_match_my_contact(self):
        phone_numbers = []
        content = []
        final_list = []
        for item in self.user_information:
            if isinstance(item, User_Phone_Book):
                phone_numbers.append(item.phone)
            if isinstance(item, Diary_entry):
                content.append(item.content)
        for y in content:
            for x in phone_numbers:
                if x in y:
                    final_list.append(x)

        return final_list
    
    def check_if_mobile_number(self):
        pattern = re.compile(r'^\d{10}$')
        list_with_number = []
        for item in self.user_information:
            if isinstance(item, Diary_entry):
                number_list = item.content.split(" ")
                for numbers in number_list:
                    match = pattern.search(numbers)
                    if match:
                        list_with_number.append(numbers)

        return list_with_number
    
    
    

class Diary_entry:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def count_words(self):
        return len(self.content.split())

    def reading_time(self, wpm):
        time_count = (self.count_words() / wpm) * 60
        seconds = time_count % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        formatted_hours = ("%d:%02d:%02d" % (hour, minutes, seconds))
        return formatted_hours
    
class User_Todo:
    def __init__(self, todo):
        self.todo = todo
        self.completed = False
        
    def mark_complete(self):
        self.completed = True      
        
class User_Phone_Book:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone        