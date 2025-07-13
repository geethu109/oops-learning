from book import Book

class Booktracker:
    def __int__(self):
        self.books=[]

    def add_book(self, title, author):
        new_book=Book(title,author)
        self.books.append(new_book)
        print(f"Added '{title}' to your collection!")
    
    def show_all_books(self):
        if not self.books:
            print("No books in your collection.")
            return
        
        print("\nYour Books:")
        for book in self.books:
            print(book.get_info())

# new=Book("Notebook", "Jane Hauston")
# print(new.get_info())
    def mark_book_read(self,title):
        for book in self.books:
            if book.title.lower()==title.lower() ###
            book.mark_as_read()
            return
    print(f"Book '{title}' not found in your collection.")

    def save_to_file(self):
        print("saving your books...")
        try:
            with open("books.txt", "w") as file:
                for book in self.books:
                    line = f"{book.title}|{book.author}|{book.is_read}\n"
                    file.write(line)
            print("Books saved successfully!")
            print("Try this: Open 'books.txt' in your file explorer or text editor to see how your data is stored!")
        expect Exception as error:
            print(f"Error saving books: {error}")
    
    def load_from_file(self):
        # Load books from the text file
        print("Looking for saved books...")
        try:  # Try to load, but handle errors if file doesn't exist
            with open("books.txt", "r") as file:  # Open file for reading
                self.books = []  # Clear current books before loading
                for line in file:
                    line = line.strip()  # Remove extra whitespace and newline characters
                    if line:  # If line is not empty
                        # Split the line back into parts using the | character
                        parts = line.split("|")
                        if len(parts) == 3:  # Make sure we have all three parts
                            title, author, is_read = parts
                            book = Book(title, author)
                            # Convert the string "True" or "False" back to a boolean
                            book.is_read = (is_read == "True")
                            self.books.append(book)
            print(f"Loaded {len(self.books)} books from file!")
        except FileNotFoundError:  # If file doesn't exist yet
            print("No saved books found. Starting fresh!")
            print("💡 Hint: After you add some books and save them, a 'books.txt' file will appear in your project folder!")
        except Exception as error:  # If loading fails for other reasons
            print(f"Error loading books: {error}")