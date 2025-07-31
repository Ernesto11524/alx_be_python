class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library():
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    print("Book is already checkout out.")
                else:
                    book._is_checked_out = True
                return
        print("Book not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                else:
                    print("Book is already available.") 
                return
        print("Book not found in the library.")  

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")      

lib = Library()
lib.add_book(Book("I am great", "Ernest"))
lib.add_book(Book("University", "Calvin"))
lib.list_available_books()