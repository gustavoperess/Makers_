
def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product

# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24

# it does not work with aeiou because every time that iterates throught the below function it increase the index
# example first time is a indext 0 -> aeiou, removes a[0]eiou removes [a]
# next time starts at index one ei[1]ou removes i
# next time starts at index two eou[2] removes u
# the remaining is eo which is what the function retunrs to you

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i + 1:] # only add the index if the this is false 
            else:
                i += 1
        
        return self.text

# File: lib/vowel_remover.py

# challenge exercise 


# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1 # starts counting from 0 
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char] # don't need to add at the end. 
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]