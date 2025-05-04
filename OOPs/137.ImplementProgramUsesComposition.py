#Implement a program that uses composition, e.g., a Library class that has a list of Book objects.

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title)

lib = Library()
lib.add_book(Book("1984"))
lib.add_book(Book("Python Basics"))
lib.add_book(Book("NCERT Book"))
lib.show_books()
