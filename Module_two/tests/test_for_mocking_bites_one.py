from unittest.mock import Mock
from lib.mocking_bites_one import *


def test_if_search_for_the_keyword():
    track = Track("Scorpion", "Drake")
    result = track.matches("Drake")
    assert result == True
    

def test_if_the_add_track_with_fakes():
    music_library = MusicLibrary()
    fake_matching = fake_matching_track()
    fake_not_matching = fake_not_matching_track()
    music_library.add(fake_matching)
    music_library.add(fake_not_matching)
    assert music_library.search("Drake") == [fake_matching]  
 
class fake_matching_track():
    def matches(self, keyword):
        if keyword == "Drake": 
            return True


class fake_not_matching_track():
    def matches(self, keyword):
        if keyword != "Drake":
            return False
  

def test_partial_title():
    track = Track("Drake", "after dark")
    result = track.matches("after")
    assert result == True  

def test_partial_artist():
    track = Track("Drake Moreira", "after dark")
    result = track.matches("Moreira")
    assert result == True      
    
    
 # CHALLENGES FOR MOCKING BITES ONE   
    
def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]


def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True

def test_constructs():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"


def test_can_be_marked_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.is_complete() == True

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_for_all_completed():
    task_list = TaskList()
    fake_matichg_completed = fake_matching_task()
    task_list.add(fake_matichg_completed)
    assert task_list.all_complete() == True
 
class fake_matching_task():
    def is_complete(self):
        return True
    

    