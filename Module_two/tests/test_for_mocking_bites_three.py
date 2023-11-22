from unittest.mock import Mock
from lib.mocking_bites_three import *
import pytest 

def test_read_diary_if_is_locked():
    diary = Mock()
    secret_diary =  SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"
    
    
def test_read_diary_if_is_unlocked():
    diary = Mock()
    diary.read.return_value = "Cool content"
    secret_diary =  SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Cool content"
    diary.read.assert_called()
    

def test_formated_string_for_all_completed_tasks():
    first_task = Mock()
    first_task.title = "task1"
    first_task.is_complete.return_value = True
    task_list = TaskList()
    task_list.add(first_task)
    assert task_list.format() == ["task1 [x]"]
    first_task.is_complete.assert_called_once()
    
def test_formated_string_for_not_completed_tasks():
    first_task = Mock()
    first_task.title = "task1"
    first_task.is_complete.return_value = False
    task_list = TaskList()
    task_list.add(first_task)
    assert task_list.format() == ["task1 [ ]"]
    first_task.is_complete.assert_called_once()