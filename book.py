
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
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn}) - 
        {'Available' if self.__available else 'Borrowed'}"