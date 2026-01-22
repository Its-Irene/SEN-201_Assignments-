SEN 201 ASSIGNMENT
Project Title: Library Management System
This project is a Library Management System developed using Python. The aim of this project is to help understand the basic stages of software development and how a simple system can be designed and implemented using programming.
The system allows books to be added to a library and also displays the books that are available.
Software Development Life Cycle (SDLC)
1. Requirement Analysis
At this stage, the problem that needs to be solved was identified.
The system should be able to:
- Add books to the library
- Store the book title, author, and book ID
- Display all the books in the library
The system is meant for students and library staff who want to keep simple records of books.
2. System Design
System Name: LibraryManagementSystem
Design Description:
- A list is used to store all book records
- Each book is stored as a dictionary
- Two main functions are used:
  - add_book() to add books
  - display_books() to show all books
3. Implementation
File Name: library_management_system.py
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
4. Testing
The program was tested by adding different books and checking if the books display correctly. The system worked as expected without errors.
5. Deployment
The project was deployed by uploading the source code to GitHub so it can be accessed and submitted easily.
6. Maintenance
In the future, the system can be improved by adding features such as deleting books, updating records, and saving data to a file or database.


