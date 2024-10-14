def borrow_book(user, book):
    try:
        if book.is_available():
            user.borrow_book(book)
        else:
            raise Exception("Book is already borrowed.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Book borrowed successfully!")
    finally:
        print("Operation completed.")