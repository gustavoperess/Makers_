from lib.main import *

# test to check if the len of the function is bigger than 0 
import pytest
def test_to_check_lenght_bigger_than_zero():
    with pytest.raises(Exception) as e:
        time_manager("")
    error_message = str(e.value)
    assert error_message == "We can't estimate the time for an empty text"    

# test to check if the returning statement is correct

def test_to_check_returning_statement():
    result = time_manager(" is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")   # lenght of 9 / 200 
    assert result == "This text/book took me 0:00:45 to read" # lenght of the text divided by 200 and converted to hours:minutes:seconds


#As a user So that I can improve my grammar
#I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

# check if somethgin is passed, otherwise raise an error:
def test_check_if_len_bigger_than_zero():
    with pytest.raises(Exception) as e:
        capital_letter("")
    error_message = str(e.value)
    assert error_message == "Nothing has been passed!"  

# check if starts with upper case and ends with exclamation mark '!!`
def test_if_starts_with_capital_letter_and_exclamation():
    result = capital_letter("My text is working!")
    assert result == "My text is working!"

# check if starts with upper case and ends with question mark '??`
def test_if_starts_with_capital_letter_and_questionmark():
    result = capital_letter("My text is working?")
    assert result == "My text is working?"

# check if starts with upper case and ends with dot '..`
def test_if_starts_with_capital_letter_and_questionmark():
    result = capital_letter("My text is working.")
    assert result == "My text is working."

# check if both requirements are missing 
def test_if_both_requirements_are_missing():
    result = capital_letter("my text is working")
    assert result == "The text is missing both requirements"

# check if uppercase is missing
def test_if_upper_case_is_missing():
    result = capital_letter("my text is working!")
    assert result ==  "The text is not starting wiht upper case"

# check if ponctuation is missing
def test_if_ponctuation_case_is_missing():
    result = capital_letter("My text is working")
    assert result ==  "The text is not ending wiht ponctuation"