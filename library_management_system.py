class LibraryManagementSystem:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, book_id):
        book = {
            "title": title,
            "author": author,
            "book_id": book_id
        }
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print("Book Title:", book["title"])
                print("Author:", book["author"])
                print("Book ID:", book["book_id"])
                print("-------------------------")

library = LibraryManagementSystem()
library.add_book("Introduction to Software Engineering", "Ian Sommerville", "LIB001")
library.add_book("Python Programming", "John Zelle", "LIB002")

library.display_books()
