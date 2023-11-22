
class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.is_locked = True
        

    def read(self):
        if self.is_locked:
            raise Exception ("Go away!")
        else:
            return self.diary.read()
                  
    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False



class Diary:
    def __init__(self, contents):
        self.contents = contents

    def read(self):
        return self.contents
    
    
class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def all(self):
        return self.tasks

    def all_complete(self):
        if len(self.tasks) == 0:
            return False
        return all([task.is_complete() for task in self.tasks])
    
    def format(self):
        final_list = []
        for task in self.tasks:
            if task.is_complete():
                final_list.append(f"{task.title} [x]")
            else:
                final_list.append(f"{task.title} [ ]")

        return final_list

class Task:
    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def is_complete(self):
        return self.complete
        