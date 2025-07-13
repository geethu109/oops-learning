# book.py
class Book:
    def __init__(self, title, author):
        # When someone creates a Book, they must give us a title and author
        self.title = title      # self.title means "this book's title"
        self.author = author    # self.author means "this book's author"
        self.is_read = False    # Every new book starts as unread
    
    def mark_as_read(self):
        # This is a method - something the book can do
        self.is_read = True
        print(f"You've finished reading '{self.title}'!")
    
    def get_info(self):
        # This method returns information about the book
        status = "Read" if self.is_read else "Not read yet"
        return f"'{self.title}' by {self.author} - {status}"
    
# Test it out
my_book = Book("Harry Potter", "J.K. Rowling")  # Create a book object
print(my_book.get_info())  # Print book information
my_book.mark_as_read()     # Mark it as read
print(my_book.get_info())  # Print again to see the change