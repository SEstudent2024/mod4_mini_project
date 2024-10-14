
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters and Setters for encapsulation
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"{self.__name} (ID: {self.__library_id}) - 
        Borrowed books: {[book.get_title() for book in self.__borrowed_books]}"