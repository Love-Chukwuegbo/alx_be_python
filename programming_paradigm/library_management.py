class Book:
    def __init__(self,title, author):
        self.title =title
        self.author = author
        self._is_checked_out = False

book1= Book("Brave New World", "Aldous Huxley")

class Library():
    def __init__(self):
        self._books=[]
    
    def add_book(self,book_obj):
        self._books.append(book_obj)
        for book in self._books:
        
            print("{} by {}".format(book.title, book.author))
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out= True
                break
    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                break
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print("{} by {}".format(book.title, book.author))