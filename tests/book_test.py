
import unittest
from models.book import Book
from models.book_list import *

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book(1, "Harry Potter", "J.K. Rowling", "Fantasy")
        self.book2 = Book(2, "Dumb Stuff", "Ben Dover", "Silly")
        self.books = books

    def test_book_has_name(self):
        self.assertEqual("Harry Potter", self.book1.title)

    def test_book_can_be_added_to_list(self):
        new_book = Book(5, "Eat, Pray, Love", "some person", "silly")
        add_new_book(new_book)
        self.assertEqual(5, len(self.books))

    def test_book_can_be_removed_from_list(self):
        remove_book("Terror Tombe")
        remove_book("Animal Farm")
        self.assertEqual(3, len(self.books))
        print(books)
