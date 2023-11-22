# File: lib/music_library.py

class MusicLibrary:
    def __init__(self):
        self.tracks = []


    def add(self, track):
        self.tracks.append(track)
        
    def search(self, keyword):
        return [track for track in self.tracks if track.matches(keyword)] 
            

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artits = artist

    def matches(self, keyword):
        keyword_lower = keyword.lower()
        title_lower = self.title.lower()
        artist_lower = self.artits.lower()
        return keyword_lower in title_lower or keyword_lower in artist_lower
    
    
    # CHALLENGE FOR MOCKING BITES ONE
   

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

class Task:
    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def is_complete(self):
        return self.complete
    