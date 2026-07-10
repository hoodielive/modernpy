class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        return f"Title: {self.title}, author: {self.author}, pages: {self.pages}"

my_book = Book("Harry Potter", "J.K. Rowling", 200)
print(my_book.book_info())
