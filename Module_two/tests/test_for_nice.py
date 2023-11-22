from lib.nine import *
import pytest


def test_for_adding_information_for_user():
    user = User()
    ux = Diary_entry("My day", "Today I went for a walk")
    todo = User_Todo("I need to wak my dog")
    contacts = User_Phone_Book("Ashley", "7782396089")
    user.add(ux)
    user.add(todo)
    user.add(contacts)
    result = user.user_info()
    assert result == [ux, todo, contacts]
    

def test_for_user_reading_diary(): 
    user = User()
    ux_01 = Diary_entry("My First", "Today I went for a walk")
    ux_02 = Diary_entry("My Second", "Today I went to buy groceries")
    ux_03 = Diary_entry("My Third", "Today I washed my car")  
    user.add(ux_01)
    user.add(ux_02)
    user.add(ux_03)
    result = user.user_past_experiences()
    assert result == ["Today I went for a walk", "Today I went to buy groceries", "Today I washed my car"]

def test_to_check_how_many_words_in(): 
    user = User()
    ux_01 = Diary_entry("My First", "Today I went for a walk")
    user.add(ux_01)
    result = ux_01.count_words()
    assert result == 6    


def test_to_check_the_reading_time(): 
    user = User()
    ux_01 = Diary_entry("My First", "Today I went for a walk")
    user.add(ux_01)
    result = ux_01.reading_time(1)
    assert result == '0:06:00'
    
def test_to_find_out_the_best_entry_based_on_my_reading_time():
    user = User()
    ux_01 = Diary_entry("My First", "one two three four five")
    ux_02 = Diary_entry("My Second", "one two three four five six seven eight")
    ux_03 = Diary_entry("My Third", "one two three four five six seven eight nine ten")  
    user.add(ux_01)
    user.add(ux_02)
    user.add(ux_03)
    result = user.find_best_entry_for_reading_time(5, 5)
    assert result == "one two three four five"
    
def test_to_find_out_the_best_entry_based_on_my_reading_two():
    user = User()
    ux_01 = Diary_entry("My First", "one two three four five")
    ux_02 = Diary_entry("My Second", "one two three four five six seven eight")
    ux_03 = Diary_entry("My Third", "one two three four five six seven eight nine ten")  
    user.add(ux_01)
    user.add(ux_02)
    user.add(ux_03)
    result = user.find_best_entry_for_reading_time(5, 10)
    assert result == "one two three four five six seven eight nine ten"    
    
def test_if_you_dont_have_enought_time_to_read_anything():
    user = User()
    entry1 = Diary_entry("Entry 1", "one two three four")
    entry2 = Diary_entry("Entry 2", "five six seven")
    user.add(entry1)
    user.add(entry2)
    with pytest.raises(ValueError) as e:
        user.find_best_entry_for_reading_time(1, 2)
    error_message = str(e.value)
    assert error_message == "There is nothing you can read with this time"
    
def test_if_reading_if_value_passed_is_zero():
    user = User()
    entry1 = Diary_entry("Entry 1", "one two three four")
    entry2 = Diary_entry("Entry 2", "five six seven")
    user.add(entry1)
    user.add(entry2)
    with pytest.raises(ValueError) as e:
        user.find_best_entry_for_reading_time(0, 2)
    error_message = str(e.value)
    assert error_message == "We can't estimate the time for 0"
    
def test_for_incompleted_tasks():
    user = User()
    entry1 = User_Todo("Go to the park")
    entry2 = User_Todo("walk the dog")
    entry3 = User_Todo("Wash the car")
    user.add(entry1)
    user.add(entry2)
    user.add(entry3)
    result = user.incomplete()
    assert result == ['Go to the park', 'walk the dog', 'Wash the car']
    
def test_for_completed_tasks():
    user = User()
    entry1 = User_Todo("Go to the park")
    entry2 = User_Todo("walk the dog")
    entry3 = User_Todo("Wash the car")
    user.add(entry1)
    user.add(entry2)
    user.add(entry3)
    entry1.mark_complete() 
    result = user.complete()
    assert result == ["Go to the park"]    

def test_to_check_all_my_mobile_numbers():
    user = User()
    user_info_one = User_Phone_Book("Gustavo", "7783179738")
    user_info_two = User_Phone_Book("Ashley", "7782396080")
    user.add(user_info_one)
    user.add(user_info_two)
    result = user.all_my_contacts()
    assert result == {"Gustavo": "7783179738", "Ashley": "7782396080"}
    
def test_to_check_if_there_are_phone_number_inside_of_my_diary_entry():
    user = User()
    entry1 = Diary_entry("Entry 1", "Today I talked to Gustavo and he gave me his number 7783179738")
    entry2 = Diary_entry("Entry 2", "Today I talked to ashley and she gave me his number 7782396080")
    user_info_one = User_Phone_Book("Gustavo", "7783179738")
    user_info_two = User_Phone_Book("Ashley", "7782396080")
    user.add(entry1)
    user.add(entry2)
    user.add(user_info_one)
    user.add(user_info_two)
    result = user.numbers_in_my_diary_match_my_contact()
    assert result == ["7783179738", "7782396080"]
  
  
def test_to_check_if_there_are_phone_number_inside_of_my_diary_entry():
    user = User()
    entry1 = Diary_entry("Entry 1", "Today I talked to Gustavo and he gave me his number 7783179738")
    entry2 = Diary_entry("Entry 2", "Ashley's number is 7782396080 she is going to the gym today ")
    user.add(entry1)
    user.add(entry2)
    result = user.check_if_mobile_number()
    assert result == ["7783179738", "7782396080"]