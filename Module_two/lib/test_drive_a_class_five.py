class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contests = contents
        self.new_content_added = [] # added 
        self.new_content_removed = [] # removed
        self.my_fun_times_called = 1

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contests}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.contests.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if self.count_words() == 0:
            raise Exception("We can't estimate the time for an empty text")
        else:
            time_count = (self.count_words() / wpm)
            seconds = time_count % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            formatted_hours = ("%d:%02d:%02d" % (hour, minutes, seconds))
            if formatted_hours == "0:00:00":
                return "This text/book took me less that a second to read"
            else:
                return f"This text/book took me {formatted_hours} to read"

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
        if self.count_words() == 0:
            raise Exception("We can't estimate the time for an empty text")
        else:
            result = int(minutes / wpm)
            start_index = (self.my_fun_times_called - 1) * result
        
            
            words = self.contests.split(" ")

            if start_index < self.count_words():
                chunk = " ".join(words[start_index:start_index + result])
                self.my_fun_times_called += 1
                return chunk
            else:
                self.my_fun_times_called = 1
                return " ".join(words[:result])
                

                

diary = DiaryEntry("my_title", "in this contents I have 11 words to test my code")
tes = diary.reading_chunk(1, 5)
tes_two = diary.reading_chunk(1, 5)
tes_three = diary.reading_chunk(1, 5)




class GrammarStats:
    def __init__(self):
        self.list_of_pass = []
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if len(text) == 0:
            raise Exception("Nothing has been passed!")
        else:
            split_text = text.split()
            all_words_together = "".join(split_text)
            if all_words_together[0].isupper() and all_words_together[-1] in ['!','?','.']:
                self.list_of_pass.append("True")
                return True
            else:
                self.list_of_pass.append("False")
                return False
        
        
    def percentage_good(self):
        length = len(self.list_of_pass)
        true_items = []
        for items in self.list_of_pass:
            if items == "True":
                true_items.append(items)

        len_of_true_items = len(true_items)
        print(len_of_true_items, length)
        my_result = round((len_of_true_items / length) * 100,1)
        return f"{my_result}%"

grammar = GrammarStats()
check_one = grammar.check("My text is working.")
check_two = grammar.check("My text is working.")
check_three = grammar.check("My text is working")
print(grammar.percentage_good())