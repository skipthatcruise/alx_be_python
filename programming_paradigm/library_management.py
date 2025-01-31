class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return f"The book has been checked out."

                else:
                    return "The book is already checked out."

    def return_book(self,title):
        for book in self._books:
            if book.title ==title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return "The book has been returned."
                else:
                    return"The book was not checked out."


    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")


