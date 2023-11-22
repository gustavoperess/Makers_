def make_snippet_five_letters(string):
    x = slice(5)
    balance_left = len(string) - 5
    my_string = string[x]
    starts = balance_left * "*"
    return my_string + starts


def make_snippet_five_words(string):
    splited_words = string.split(" ")
    if len(splited_words) > 5:
        word = splited_words[:5]
        words = (" ").join(word) + " ..."
        return words
    else:
        return string


def count_words(string):
    word_length = len(string)
    return str(word_length)



def time_manager(text):
    # a function that takes a text and count how many words are inside of it. 
    # assuming that we can read 200 words per minute we will divide the length by 200(time to read each word) to check how long
    # it took to read my whole text / book 
    
    # Parameters: (takes the text and split it to check how many words divide by 200 and convert this to hours:minutes:seconds)
    # eg a text with 563 words will take 0:00:45 to read 

    if len(text) == 0:
        raise Exception("We can't estimate the time for an empty text")
    else:
        len_of_text = len(text.split(" "))
        time_count = int(round(len_of_text / 200, 2) * 100)
        seconds = time_count % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        formatted_hours = ("%d:%02d:%02d" % (hour, minutes, seconds))
        return (f"This text/book took me {formatted_hours} to read")




def capital_letter(text):

    # a simple function that tests if the text is starting with upper case and ending with a correct ponctuation ['!','?','.']
    # if not met the requirements it will return what is missing 

    if len(text) == 0:
        raise Exception("Nothing has been passed!")
    else:
        split_text = text.split()
        all_words_together = "".join(split_text)
        if all_words_together[0].isupper() and all_words_together[-1] in ['!','?','.']:
            return f"My text is working{all_words_together[-1]}"
        elif all_words_together[0].islower() and all_words_together[-1] not in ['!','?','.']:
            return "The text is missing both requirements"
        elif all_words_together[0].islower():
            return "The text is not starting wiht upper case"
        elif all_words_together[-1] not in ['!','?','.']:
            return "The text is not ending wiht ponctuation"



