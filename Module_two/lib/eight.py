# File: lib/diary.py

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
       self.entries.append(entry)
            
    def all(self):
        return self.entries
        
    def count_words(self):
        count = 0
        for entry in self.entries:
            count += entry.count_words()

        return count

    def reading_time(self, wpm):
        time_count = (self.count_words() / wpm)
        seconds = time_count % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        formatted_hours = ("%d:%02d:%02d" % (hour, minutes, seconds))
        if formatted_hours == "0:00:00":
            return "This text/book took me less that a second to read"
        else:
            return f"This text/book took me {formatted_hours} to read"
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if wpm == 0 or minutes == 0:
            raise ValueError("We can't estimate the time for 0")
        else:
            my_minutes = minutes / wpm
            hour, remaining_minutes = divmod(my_minutes, 60)
            seconds, my_minutes = divmod(remaining_minutes, 60)
            formatted_hours = ("%d:%02d:%02d" % (hour, minutes, seconds))
            dic_of_items = {}
            for entry in self.entries:
                reading_time = entry.reading_time(wpm)
                if reading_time <= formatted_hours:
                    dic_of_items[entry.contents] = reading_time

            if len(dic_of_items) == 0:
                raise ValueError("There is nothing you can read with this time")
            else:
                final_result = max(dic_of_items.items(), key=lambda x: x[1])
                return final_result[0]
       

# File: lib/diary_entry.py

class DiaryEntry:
    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.my_fun_times_called = 1
        self.my_fun_word_counts = []

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        time_count = (self.count_words() / wpm) * 60
        seconds = time_count % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        formatted_hours = ("%d:%02d:%02d" % (hour, minutes, seconds))
        return formatted_hours

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split(" ")
        result = int(minutes * wpm)

        start_index = sum(self.my_fun_word_counts[:self.my_fun_times_called])
        self.my_fun_word_counts.append(result)

        if start_index < len(words):
            chunk = " ".join(words[start_index:start_index + result])
            self.my_fun_times_called += 1
            return chunk
        else:
            self.my_fun_times_called = 0
            return " ".join(words[:result])
        

# CHALLENGE ----

# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.list_of_tasks = []


    def add(self, todo):
        self.list_of_tasks.append(todo)
      
    def incomplete(self):
        list_of_incompleted = []
        for items in self.list_of_tasks:
            if not items.completed:
                list_of_incompleted.append(items.task)

        return list_of_incompleted
        
    def complete(self):
        list_of_completed = []
        for items in self.list_of_tasks:
            if items.completed:
                list_of_completed.append(items.task)

        return list_of_completed

    def give_up(self):
        for items in self.list_of_tasks:
            items.mark_complete()


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        self.task = task
        self.completed = False
        

    def mark_complete(self):
        self.completed = True        