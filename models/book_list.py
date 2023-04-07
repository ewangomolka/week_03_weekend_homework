from models.book import *

book1 = Book(1, "Terror Tombe", "Garth Marenghi", "Dark Comedy", True)
book2 = Book(2, "Animal Farm", "George Orwell", "Political Satire", False)
book3 = Book(3, "American Gods", "Neil Gaiman", "Fantasy", True)
book4 = Book(4, "The Witcher: Blood of Elves", "Andrzej Sapkowski", "Fantasy", False)

books = [book1, book2, book3, book4]

def add_new_book(new_book):
    books.append(new_book)

def remove_book(book_title):
    book_to_remove = None
    for book in books:
        if book.title == book_title:
            book_to_remove = book
            break
    books.remove(book_to_remove)