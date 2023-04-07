
from app import app
from flask import render_template, redirect, url_for, request
from models.book_list import books, add_new_book, remove_book
from models.book import *

@app.route('/')
def index():
    return redirect(url_for('all_books'))

@app.route('/books')
def all_books():
    return render_template('index.html', books_list=books)

@app.route('/book_info/<int:book_id>')
def single_book(book_id):
    return render_template('show.html', title='Book Info', book=books[book_id-1])

@app.route('/books', methods=["POST"])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    book_available = "available" in request.form
    new_id = len(books) + 1
    new_book = Book(new_id, book_title, book_author, book_genre, book_available)
    add_new_book(new_book)
    return render_template('index.html', books_list=books)

@app.route('/books/delete/<book_title>', methods=['POST'])
def delete(book_title):
    remove_book(book_title)
    return redirect('/books')