from lib.book import *

def test_book():

    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'