class Book:
    def __init__(self, title, author):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._is_checked_out = False    # Private attribute

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return  # Book checked out, exit
        # If not available or not found, do nothing

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return  # Book returned, exit
        # If not found or already available, do nothing

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
