from lib.book_repository import *
from lib.book import *

def test_return_all(db_connection):

    db_connection.seed('seeds/book_store.sql')
    bookstore_repository = BookRepository(db_connection)

    books = bookstore_repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]
