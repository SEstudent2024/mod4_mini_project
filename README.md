#book class
class Book:
    def __init__(self, title, author, isbn, publication_date):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__available = True

    # Getters and Setters for encapsulation
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def __str__(self):
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn}) - {'Available' if self.__available else 'Borrowed'}"

#user class

class Book:
    def __init__(self, title, author, isbn, publication_date):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__available = True

    # Getters and Setters for encapsulation
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def __str__(self):
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn}) - {'Available' if self.__available else 'Borrowed'}"

# author class

class Author:
    def __init__(self, name, biography=""):
        self.__name = name
        self.__biography = biography

    # Getters and Setters for encapsulation
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def __str__(self):
        return f"{self.__name} - {self.__biography}"

# genre class

class Genre:
    def __init__(self, name, description=""):
        self.__name = name
        self.__description = description

    # Getters and Setters for encapsulation
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def __str__(self):
        return f"{self.__name} - {self.__description}"

# Menu Display

def main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")

def book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

def author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

def genre_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")

# Handling Menu

def handle_main_menu():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            handle_book_menu()
        elif choice == '2':
            handle_user_menu()
        elif choice == '3':
            handle_author_menu()
        elif choice == '4':
            handle_genre_menu()
        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_book_menu():
    while True:
        book_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_books()
        else:
            print("Returning to main menu...")
            break

def handle_user_menu():
    while True:
        user_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_user()
        elif choice == '3':
            display_users()
        else:
            print("Returning to main menu...")
            break

def handle_author_menu():
    while True:
        author_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_author()
        elif choice == '2':
            view_author()
        elif choice == '3':
            display_authors()
        else:
            print("Returning to main menu...")
            break

def handle_genre_menu():
    while True:
        genre_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_genre()
        elif choice == '2':
            view_genre()
        elif choice == '3':
            display_genres()
        else:
            print("Returning to main menu...")
            break

  # Adding New Book

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    book = Book(title, author, isbn, publication_date)
    library_books.append(book)
    print(f"Book '{title}' added successfully!")

# Borrowing a Book

def borrow_book():
    isbn = input("Enter ISBN of the book to borrow: ")
    book = next((b for b in library_books if b.get_isbn() == isbn), None)
    if book:
        if book.is_available():
            user_id = input("Enter your library ID: ")
            user = next((u for u in library_users if u.get_library_id() == user_id), None)
            if user:
                if user.borrow_book(book):
                    print(f"You have successfully borrowed '{book.get_title()}'.")
                else:
                    print("Failed to borrow the book.")
            else:
                print("User not found.")
        else:
            print("Book is not available.")
    else:
        print("Book not found.")

  # Returning a Book

  def return_book():
    isbn = input("Enter ISBN of the book to return: ")
    book = next((b for b in library_books if b.get_isbn() == isbn), None)
    if book:
        user_id = input("Enter your library ID: ")
        user = next((u for u in library_users if u.get_library_id() == user_id), None)
        if user:
            if user.return_book(book):
                print(f"You have successfully returned '{book.get_title()}'.")
            else:
                print("Failed to return the book.")
        else:
            print("User not found.")
    else:
        print("Book not found.")

  # Searching for a Book

  def search_book():
    search_term = input("Enter title or ISBN to search: ")
    book = next((b for b in library_books if b.get_title() == search_term or b.get_isbn() == search_term), None)
    if book:
        print(book)
    else:
        print("Book not found.")

  # Display all books

  def display_books():
    if library_books:
        for book in library_books:
            print(book)
    else:
        print("No books available.")

  library_books = []
library_users = []
library_authors = []
library_genres = []

if __name__ == "__main__":
    handle_main_menu()

    
