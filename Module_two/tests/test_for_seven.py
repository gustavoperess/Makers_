from lib.seven import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."
    

def test_to_remove_all_vowels():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""    
    

def test_to_check_for_most_commom():
    letter_count = LetterCounter("Digital Punk")
    result = letter_count.calculate_most_common()
    assert result == [2, "i"]
    
def test_to_check_for_most_commom():
    letter_count = LetterCounter("Paralelepipedo")
    result = letter_count.calculate_most_common()
    assert result == [3, "e"]    
    