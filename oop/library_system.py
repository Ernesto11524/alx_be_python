class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    books = []
    def init(self):
        pass

    def add_book(self, book):
        Library.books.append(book)

    def list_books(self):
        for book in Library.books:
            if isinstance(book, EBook):
                print(f"Ebook: {book.title} by {book.author}, File Size: {book.file_size}KB")

            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")

            elif isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")