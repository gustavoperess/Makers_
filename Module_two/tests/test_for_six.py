from lib.six import *

def test_for_one_item_added():
    todo = Todo()
    todo.adding_input_to_list("something_passed")
    result = todo.returning_list_of_items()
    assert result == {1: "something_passed"}


def test_for_two_item_added():
    todo = Todo()
    todo.adding_input_to_list("Go to the grocery store")
    todo.adding_input_to_list("Go to the gym")
    result = todo.returning_list_of_items()
    assert result == {1 : "Go to the grocery store", 2 : "Go to the gym"}


def test_for_task_completed_one_items():
    todo = Todo()
    todo.adding_input_to_list("Go to the grocery store")
    todo.adding_input_to_list("Go to the gym")
    todo.removing_completed_items(2)
    result = todo.returning_list_of_items()
    assert result == {1 : "Go to the grocery store"}

import pytest
def test_to_check_lenght_bigger_than_zero():
    todo = Todo()
    with pytest.raises(Exception) as e:
        todo.removing_completed_items(0)
    error_message = str(e.value)
    assert error_message == "Number cannot be 0 or empty"


 

def test_for_music_added():
    mt = Music_tracker()
    mt.adding_to_list("pop_music")
    result = mt.musics()
    assert result == ["pop_music"]


def test_for_more_than_one_music():
    mt = Music_tracker()
    mt.adding_to_list("pop_music")
    mt.adding_to_list("rock_music")
    result = mt.musics()
    assert result == ["pop_music", "rock_music"]


    
