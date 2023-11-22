from lib.test_drive_a_class_five import *
import pytest

def test_for_format():
    diary = DiaryEntry("my_title", "my_contents")
    result = diary.format()
    assert result == "my_title: my_contents"


def test_for_the_lentght():
    diary = DiaryEntry("my_title", "in this contents I have 7 words")
    result = diary.count_words()
    assert result == 7

def test_to_check_the_reding_time_for_less_than_a_second():
    diary = DiaryEntry("my_title", "in this contents I have 11 words to test my code")
    result = diary.reading_time(100) # wpm dived by leng(11) converted to time 
    assert result == "This text/book took me less that a second to read"

def test_to_check_the_reding_time_for_more_than_a_second():
    diary = DiaryEntry("my_title", "in this contents I have 11 words to test my code")
    result = diary.reading_time(1) # wpm dived by leng(11) converted to time 
    assert result == "This text/book took me 0:00:11 to read"    


def test_to_check_the_reding_time_with_minutes():
    lis = []
    for words in range(120):
        words = "word"
        lis.append(words)
    final_list = " ".join(lis)   
    diary = DiaryEntry("my_title", final_list)
    result = diary.reading_time(1) # wpm dived by leng(11) converted to time 
    assert result == "This text/book took me 0:02:00 to read"    


def test_to_check_the_reding_time_with_hours():
    lis = []
    for words in range(5000):
        words = "word"
        lis.append(words)
    final_list = " ".join(lis)   
    diary = DiaryEntry("my_title", final_list)
    result = diary.reading_time(1) # wpm dived by leng(11) converted to time 
    assert result == "This text/book took me 1:23:20 to read"  


def test_to_check_the_reding_chunck():
    diary = DiaryEntry("my_title", "in this contents I have 11 words to test my code")
    result = diary.reading_chunk(1, 11) # minutes divided by words per minute. I have 1 minute to read 11 words, so it retunrs 11 words
    assert result == "in this contents I have 11 words to test my code"   

def test_to_check_the_reding_partial_of_the_code():
    diary = DiaryEntry("my_title", "one two three four five six seven eight nine ten")
    result = diary.reading_chunk(1, 7) # minutes divided by words per minute. I have 1 minute to read 11 words, so it retunrs 11 words
    assert result == "one two three four five six seven"   


def test_to_check_the_reding_chunck_with_more_words():
    lis = []
    for words in range(5000):
        words = "word"
        lis.append(words)
    final_list = " ".join(lis)   
    diary = DiaryEntry("my_title", final_list)
    result = diary.reading_chunk(1, 2500) # minutes divided by words per minute. I have 1 minute to read 2500 words, so it retunrs 11 words
    assert result == " ".join(lis[2500:])  



def test_if_test_chunck_is_called_more_than_once():
    diary = DiaryEntry("my_title", "in this contents I have 11 words to test my code")
    diary.reading_chunk(1, 5) 
    diary.reading_chunk(1, 5)
    result = diary.reading_chunk(1,5)
    assert result == "code" 
    
# CHALLENGE -----------------


def test_check_if_len_bigger_than_zero():
    capital_letter = GrammarStats()
    with pytest.raises(Exception) as e:
        capital_letter.check("")
    error_message = str(e.value)
    assert error_message == "Nothing has been passed!"  

# check if starts with upper case and ends with exclamation mark '!!`
def test_if_starts_with_capital_letter_and_exclamation():
    capital_letter = GrammarStats()
    result = capital_letter.check("My text is working!")
    assert result == True

# check if starts with upper case and ends with question mark '??`
def test_if_starts_with_capital_letter_and_questionmark():
    capital_letter = GrammarStats()
    result = capital_letter.check("My text is working?")
    assert result == True

# check if starts with upper case and ends with dot '..`
def test_if_starts_with_capital_letter_and_questionmark():
    capital_letter = GrammarStats()
    result = capital_letter.check("My text is working.")
    assert result == True

# check if both requirements are missing 
def test_if_both_requirements_are_missing():
    capital_letter = GrammarStats()
    result = capital_letter.check("my text is not working")
    assert result == False

# check if uppercase is missing
def test_if_upper_case_is_missing():
    capital_letter = GrammarStats()
    result = capital_letter.check("my text is not working!")
    assert result ==  False

# check if ponctuation is missing
def test_if_ponctuation_case_is_missing():
    capital_letter = GrammarStats()
    result = capital_letter.check("My text is not working")
    assert result ==  False


def test_if_function_works():
    capital_letter = GrammarStats()
    capital_letter.check("My text is working.")
    capital_letter.check("My text is working.")
    capital_letter.check("my text is working")
    result = capital_letter.percentage_good()
    assert result == "66.7%"