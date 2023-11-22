from lib.eight import *
import pytest

def test_for_count_words():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three")
    entry2 = DiaryEntry("Entry 2", "four five six")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.all()
    assert result == [entry1, entry2]


def test_for_count_words():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four")
    entry2 = DiaryEntry("Entry 2", "five six seven")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.count_words()
    assert result == 7

def test_for_count_reading_time_less_than_a_second():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four")
    entry2 = DiaryEntry("Entry 2", "five six seven")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.reading_time(10)  
    assert result == "This text/book took me less that a second to read"
    

def test_if_you_dont_have_enought_time_to_read_anything():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four")
    entry2 = DiaryEntry("Entry 2", "five six seven")
    diary.add(entry1)
    diary.add(entry2)
    with pytest.raises(ValueError) as e:
        diary.find_best_entry_for_reading_time(1, 2)
    error_message = str(e.value)
    assert error_message == "There is nothing you can read with this time"
    
def test_if_reading_if_value_passed_is_zero():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four")
    entry2 = DiaryEntry("Entry 2", "five six seven")
    diary.add(entry1)
    diary.add(entry2)
    with pytest.raises(ValueError) as e:
        diary.find_best_entry_for_reading_time(0, 2)
    error_message = str(e.value)
    assert error_message == "We can't estimate the time for 0"


def test_for_find_best_entry_for_reading_time():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four")
    entry2 = DiaryEntry("Entry 2", "five six seven")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.find_best_entry_for_reading_time(1, 3)  
    assert result == "five six seven"
    
def test_for_find_best_entry_for_reading_time_two():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four")
    entry2 = DiaryEntry("Entry 2", "five six seven")
    diary.add(entry1)
    diary.add(entry2)
    result = diary.find_best_entry_for_reading_time(1, 4)  
    assert result == "one two three four"    
    

def test_for_reading_chuck_one():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four")
    diary.add(entry1)
    result = entry1.reading_chunk(1, 3)  
    assert result == "one two three"    
    
def test_for_reading_chuck_two():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four five six seven eight nine ten")
    diary.add(entry1)
    entry1.reading_chunk(1, 3)  
    result = entry1.reading_chunk(1, 3)  
    assert result == "four five six"        
    
def test_for_reading_chuck_two():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four five six seven eight nine ten")
    diary.add(entry1)
    entry1.reading_chunk(1, 3)
    entry1.reading_chunk(1, 3)  
    result = entry1.reading_chunk(1, 2)  
    assert result == "seven eight"          

def test_for_reading_chuck_if_restarts_the_function():
    diary  = Diary()
    entry1 = DiaryEntry("Entry 1", "one two three four five six seven eight nine ten")
    diary.add(entry1)
    entry1.reading_chunk(1, 3)
    entry1.reading_chunk(1, 3)  
    entry1.reading_chunk(1, 4)  
    result = entry1.reading_chunk(1, 5)  
    assert result == "one two three four five"    
    

# tests for challenges 

def test_for_incompleted_tasks():
    todo = TodoList()
    task_01 = Todo("Go to the park")
    task_02 = Todo("walk the dog")
    task_03 = Todo("Wash the car")
    todo.add(task_01)
    todo.add(task_02)
    todo.add(task_03)
    result = todo.incomplete()
    assert result == ['Go to the park', 'walk the dog', 'Wash the car']
    
def test_for_completed_tasks():
    todo = TodoList()
    task_01 = Todo("Complete assignment 1")
    task_02 = Todo("Read a book")
    task_03 = Todo("Go for a run")
    todo.add(task_01)
    todo.add(task_02)
    todo.add(task_03)
    task_01.mark_complete() 
    result = todo.complete()
    assert result == ["Complete assignment 1"]




