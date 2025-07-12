# Simple Book Tracker - Beginner's OOP Journey

## Why Start Here?

Instead of a complex library system, we'll build a simple book tracker. You'll learn one concept at a time, understand why each piece exists, and see how they connect together.

## What is Object-Oriented Programming?

Think of programming like organizing your room. You could throw everything in one big pile (procedural programming), or you could use boxes, drawers, and containers to organize similar things together (object-oriented programming).

**A class is like a blueprint for making boxes.** It describes what the box can hold and what you can do with it.

**An object is an actual box made from that blueprint.** You can make many boxes from the same blueprint, each holding different things.

## Understanding Basic Concepts

### What is `__init__`?

The `__init__` method is Python's way of saying "when you create a new object, do this setup first." Think of it like assembling a new piece of furniture - you need to put it together before you can use it.

```python
class Book:
    def __init__(self, title, author):  # This runs when you create a new book
        self.title = title    # Give this book a title
        self.author = author  # Give this book an author
```

The word "constructor" just means "something that constructs (builds) objects." The `__init__` method is Python's constructor.

### What are Exceptions?

An exception is Python's way of saying "something went wrong, but I can handle it." Instead of your program crashing, you can catch the problem and do something useful.

```python
try:
    # Try to do something that might fail
    number = int("hello")  # This will fail because "hello" isn't a number
except:
    # If it fails, do this instead
    print("That's not a number!")
```

### What is `super()`?

`super()` is like saying "do what my parent does first, then I'll add my own stuff." We'll see this later when we learn inheritance.

## Project Structure (Simple Version)

```
book_tracker/
├── book.py        # Our Book class
├── tracker.py     # Our BookTracker class  
├── main.py        # Where we run everything
└── books.txt      # Where we save our books
```

No complicated folders yet. Just four simple files.

## Phase 1: Understanding Classes and Objects

### Step 1: Create Your First Class (book.py)

**Concept**: A class is a blueprint. An object is something made from that blueprint.

**Your Task**: Create a simple Book class that can store a title and author.

**Think About This**: What information does every book have? What can you do with a book?

```python
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
```

**Test your understanding**: Create this file and try it in Python:

```python
# Test it out
my_book = Book("Harry Potter", "J.K. Rowling")  # Create a book object
print(my_book.get_info())  # Print book information
my_book.mark_as_read()     # Mark it as read
print(my_book.get_info())  # Print again to see the change
```

**Questions to think about**: Why do we use `self`? What happens if you create two different Book objects?

### Step 2: Understanding File Handling (tracker.py)

**Concept**: Your program needs to remember things even after it closes. Files let you save and load information.

**The Big Picture**: Imagine you're writing in a notebook. When you close the notebook, your writing stays there. Computer files work the same way - they store information permanently on your hard drive.

**Exploration Time**: Before we write code, let's understand how files work. Create a simple text file on your computer called `test.txt` and write "Hello World" in it. Save it in the same folder where you'll put your Python files. Now you have a file that your Python program can read!

**File Operations - The Building Blocks**:

Python has specific syntax for working with files. Think of it like learning the grammar for a new language:

```python
# To OPEN a file (like opening a book to a specific page):
file = open("filename.txt", "r")  # "r" means "read mode"
file = open("filename.txt", "w")  # "w" means "write mode" (erases old content)
file = open("filename.txt", "a")  # "a" means "append mode" (adds to the end)

# To READ from a file:
content = file.read()        # Read everything at once
lines = file.readlines()    # Read all lines into a list
one_line = file.readline()  # Read just one line

# To WRITE to a file:
file.write("Hello World")    # Write text to the file

# To CLOSE a file (very important - like closing a book when done):
file.close()
```

**The Better Way - Using 'with'**: Python has a special syntax that automatically closes files for you, like having an assistant who always puts books back on the shelf:

```python
with open("filename.txt", "r") as file:
    content = file.read()
# File automatically closes here, even if something goes wrong!
```

**Data Storage Exploration**: Before we build our tracker, let's explore different ways to store data. Right now we'll use plain text, but I want you to know what else exists in the programming world.

**Different File Formats You Should Know About**:

Text files (.txt) store information as plain text that humans can read. Open your `test.txt` file in a text editor and you'll see exactly what's stored.

CSV files (.csv) stand for "Comma Separated Values." They're like simple spreadsheets saved as text. Each line is a row, and commas separate the columns. Here's what book data might look like in CSV format:

```
title,author,is_read
Harry Potter,J.K. Rowling,False
1984,George Orwell,True
```

JSON files (.json) store data in a format that's easy for programs to understand. They use curly braces and look like this:

```json
{
  "title": "Harry Potter",
  "author": "J.K. Rowling", 
  "is_read": false
}
```

For now, we'll use simple text files because they're easiest to understand and debug. You can actually open them in any text editor and see exactly what your program saved!

**Your Task**: Create a BookTracker that can save and load books.

**Think About This**: How do you save a book as text? How do you turn that text back into a book? What character should we use to separate the title from the author?

**Hints for Implementation**:
- We'll use the pipe character `|` to separate book information because it's unlikely to appear in book titles
- Each book will be saved on its own line in the file
- To convert from text back to a book, we'll split the line at the `|` character
- We'll handle the case where the file doesn't exist yet (first time running the program)

```python
# tracker.py
from book import Book  # Import our Book class

class BookTracker:
    def __init__(self):
        # When we create a tracker, start with an empty list of books
        self.books = []
        
    def add_book(self, title, author):
        # Create a new book and add it to our list
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added '{title}' to your collection!")
    
    def show_all_books(self):
        # Show information about all books
        if not self.books:  # If the list is empty
            print("No books in your collection yet.")
            return
        
        print("\nYour Books:")
        print("-" * 30)
        for book in self.books:
            print(book.get_info())
    
    def mark_book_read(self, title):
        # Find a book by title and mark it as read
        for book in self.books:
            if book.title.lower() == title.lower():  # Case-insensitive search
                book.mark_as_read()
                return
        print(f"Book '{title}' not found in your collection.")
    
    def save_to_file(self):
        # Save all books to a text file
        print("Saving your books...")
        try:  # Try to save, but handle errors if something goes wrong
            with open("books.txt", "w") as file:  # Open file for writing
                for book in self.books:
                    # Save each book as: title|author|is_read
                    line = f"{book.title}|{book.author}|{book.is_read}\n"
                    file.write(line)
            print("Books saved successfully!")
            print("💡 Try this: Open 'books.txt' in your file explorer or text editor to see how your data is stored!")
        except Exception as error:  # If saving fails
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
```

**Understanding What Just Happened**:

When you call `save_to_file()`, your program creates a text file that looks like this:
```
Harry Potter|J.K. Rowling|False
1984|George Orwell|True
The Hobbit|J.R.R. Tolkien|False
```

Each line represents one book, with the pipe character `|` separating the different pieces of information. This is our simple database format!

**Exploration Challenge**: After running your program and saving some books, navigate to your project folder and double-click on `books.txt`. You'll see exactly how your program stores the data. Try changing one of the "False" values to "True" in the text file, save it, then load it back into your program. You just manually edited your program's data!

**Key File Operation Concepts**:

The `try` and `except` blocks protect your program from crashing. Think of them like safety nets. If something goes wrong (like the file doesn't exist), instead of your program stopping with an error, it catches the problem and does something useful instead.

The `with open()` statement is Python's safe way to work with files. It automatically handles opening the file, and more importantly, it automatically closes the file when you're done, even if something goes wrong in between.

The `split("|")` method is like using scissors to cut a string into pieces wherever you see the pipe character. If you have "Harry Potter|J.K. Rowling|False", splitting on "|" gives you a list: ["Harry Potter", "J.K. Rowling", "False"].

**Why This Approach**: We chose the pipe character `|` as our separator because it's very unlikely to appear in book titles or author names, unlike commas or spaces which might be part of the actual text.

### Step 3: Creating the User Interface (main.py)

**Concept**: Users need a way to interact with your program. A simple menu system works great for learning.

**Your Task**: Create a menu that lets users add books, view books, and mark books as read.

```python
# main.py
from tracker import BookTracker

def show_menu():
    # Display the options to the user
    print("\n" + "="*40)
    print("📚 SIMPLE BOOK TRACKER")
    print("="*40)
    print("1. Add a book")
    print("2. Show all books") 
    print("3. Mark book as read")
    print("4. Save books")
    print("5. Load books")
    print("6. Exit")
    print("="*40)

def main():
    # Create our book tracker
    tracker = BookTracker()
    
    print("Welcome to your Book Tracker!")
    
    # Keep showing the menu until user wants to exit
    while True:
        show_menu()
        choice = input("\nWhat would you like to do? (1-6): ")
        
        if choice == "1":
            # Add a new book
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            tracker.add_book(title, author)
            
        elif choice == "2":
            # Show all books
            tracker.show_all_books()
            
        elif choice == "3":
            # Mark a book as read
            title = input("Enter the title of the book you finished: ")
            tracker.mark_book_read(title)
            
        elif choice == "4":
            # Save books to file
            tracker.save_to_file()
            
        elif choice == "5":
            # Load books from file
            tracker.load_from_file()
            
        elif choice == "6":
            # Exit the program
            print("Thanks for using Book Tracker!")
            break
            
        else:
            # User entered invalid choice
            print("Please enter a number between 1 and 6.")
        
        # Pause so user can read the output
        input("\nPress Enter to continue...")

# This runs the program when you execute main.py
if __name__ == "__main__":
    main()
```

**Key Concepts Explained**:

- **`while True`**: Creates a loop that runs forever until we `break` out of it.
- **`input()`**: Gets text from the user.
- **`if __name__ == "__main__"`**: This is Python's way of saying "only run this code if someone runs this file directly."

## Phase 2: Understanding Inheritance

**Concept**: Sometimes you want to create a new class that's similar to an existing one, but with some differences. Inheritance lets you build on what you already have.

**Real-world example**: A textbook is a type of book, but it has extra features like edition numbers and subjects.

### Step 4: Create a Textbook Class

**Before You Code - Understanding Inheritance**: 

Think about real life for a moment. A textbook is a type of book, right? It has everything a regular book has (title, author, pages), but it also has some extra features like a subject area and edition number. 

In programming, we don't want to rewrite all the book code just to add a few extra features. Inheritance lets us say "make me something like a Book, but with these additions." It's like getting a car that has all the standard features, plus some custom upgrades.

**The Syntax of Inheritance**:

```python
class ChildClass(ParentClass):  # This means "ChildClass inherits from ParentClass"
    # The child automatically gets all methods and properties from the parent
```

When you create a child class, you get everything the parent has for free. Then you can add your own special features or modify existing ones.

**Your Task**: Create a Textbook class that inherits from Book but adds subject and edition.

**Hints for Implementation**:
- Use `class Textbook(Book):` to inherit from Book
- In `__init__`, you'll need to handle both the parent's parameters (title, author) and your new ones (subject, edition)
- Use `super().__init__(title, author)` to let the Book class handle its setup first
- Override the `get_info()` method to include the new information

**What is `super()`**: Think of `super()` as a way to call your parent. When you use `super().__init__(title, author)`, you're saying "Hey parent Book class, please do your initialization first with these title and author values." Then after the parent is done, you can add your own special setup.

```python
# Add this to book.py

class Textbook(Book):  # Textbook inherits from Book
    def __init__(self, title, author, subject, edition):
        # Use the parent class to handle title and author
        super().__init__(title, author)  # This calls Book's __init__
        # Add our own special properties
        self.subject = subject
        self.edition = edition
    
    def get_info(self):
        # Override the parent's get_info method to include our new information
        status = "Read" if self.is_read else "Not read yet"
        return f"'{self.title}' by {self.author} (Subject: {self.subject}, Edition: {self.edition}) - {status}"
```

**What's happening here**:

- **Inheritance**: `Textbook(Book)` means Textbook gets all of Book's methods and properties.
- **`super()`**: Calls the parent class's method. It's like saying "do what Book does, then I'll add my stuff."
- **Method Override**: We replace Book's `get_info()` with our own version that shows more information.

### Step 5: Understanding Polymorphism

**Concept**: Different objects can respond to the same method call in their own way. A Book and Textbook both have `get_info()`, but they show different information.

**Your Task**: Update your tracker to handle both Books and Textbooks.

```python
# Add this method to BookTracker in tracker.py

def add_textbook(self, title, author, subject, edition):
    # Create a new textbook and add it to our list
    new_textbook = Textbook(title, author, subject, edition)
    self.books.append(new_textbook)  # Same list holds both Books and Textbooks
    print(f"Added textbook '{title}' to your collection!")
```

**The amazing part**: Your `show_all_books()` method doesn't need to change! It will automatically call the right `get_info()` method for each object type.

## Phase 3: Understanding Exception Handling Better

**Concept**: Things go wrong in programming. Exception handling lets you deal with problems gracefully instead of crashing.

**Real-World Analogy**: Imagine you're driving and your car breaks down. You could just sit there stranded (program crash), or you could call a tow truck and have a backup plan (exception handling). Exception handling is like having emergency procedures ready for when things don't go as planned.

**Why Exceptions Exist**: Python uses exceptions to communicate what went wrong. Instead of your program just stopping with a confusing error, exceptions give you specific information about the problem so you can decide how to handle it.

**The Basic Exception Syntax**:

```python
try:
    # Code that might cause a problem
    risky_operation()
except SpecificErrorType:
    # What to do if this specific error happens
    handle_specific_error()
except Exception:
    # What to do if any other error happens  
    handle_general_error()
```

**Common Exception Types You Should Know**:

```python
# FileNotFoundError - when you try to open a file that doesn't exist
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File doesn't exist yet!")

# ValueError - when you try to convert invalid data
try:
    number = int("hello")  # Can't convert "hello" to a number
except ValueError:
    print("That's not a valid number!")

# KeyError - when you try to access a dictionary key that doesn't exist
try:
    my_dict = {"name": "John"}
    age = my_dict["age"]  # Key "age" doesn't exist
except KeyError:
    print("That key doesn't exist in the dictionary!")
```

**Creating Your Own Exceptions**: Sometimes the built-in exceptions aren't specific enough for your program's needs. You can create custom exceptions that give more precise information about what went wrong.

**The Syntax for Custom Exceptions**:

```python
class CustomError(Exception):  # Inherit from the base Exception class
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)  # Call the parent Exception class
```

**Why Create Custom Exceptions**: Instead of generic error messages like "Error occurred," you can create specific exceptions like "BookNotFoundError" that immediately tell you and other programmers exactly what went wrong and where in your code the problem happened.

### Step 6: Add Better Error Handling

**Your Task**: Create custom exceptions for specific problems that can occur in your book tracker.

**Think About This**: What specific things can go wrong in a book tracker? What if someone tries to find a book that doesn't exist? What if they try to add the same book twice? Each of these problems deserves its own specific exception.

**Hints for Implementation**:
- Create exceptions that inherit from the base `Exception` class
- Give your exceptions descriptive names that immediately tell you what went wrong
- Include helpful error messages that explain not just what happened, but also give context
- Use these exceptions in your BookTracker methods to provide better error feedback

```python
# Add this to book.py

class BookNotFoundError(Exception):
    # A custom exception for when we can't find a book
    def __init__(self, title):
        self.title = title
        super().__init__(f"Book '{title}' not found in collection")

class DuplicateBookError(Exception):
    # A custom exception for when someone tries to add the same book twice
    def __init__(self, title):
        self.title = title
        super().__init__(f"Book '{title}' already exists in collection")
```

**Why create custom exceptions**: Instead of generic error messages, you can give specific, helpful information about what went wrong.

## Practice Exercises

## Practice Exercises - Learning by Doing

These exercises will help you understand each concept deeply before moving on. Don't skip them - they're designed to make you think and build confidence!

**Exercise 1 - Understanding Object Creation**: 
Create three different Book objects with your favorite books. Print out their information. Then mark one as read and print them all again. Notice how each object maintains its own separate data even though they're all made from the same Book class blueprint.

**Challenge Question**: What happens if you create two Book objects with the same title but different authors? Are they the same object or different objects? Try it and think about why.

**Exercise 2 - File Format Exploration**: 
After saving your books to `books.txt`, try this experiment:
1. Open the file in a text editor and manually add a new book line
2. Load the file back into your program - does your manually added book appear?
3. Try changing the separator from `|` to `,` in both your save and load methods
4. Research: Look up what CSV format looks like and try to modify your program to save in CSV format instead

**Exercise 3 - Error Handling Practice**: 
Try to break your program intentionally:
1. Delete the `books.txt` file and try to load from it - what happens?
2. Manually edit `books.txt` and remove some `|` characters - what happens when you load?
3. Try to mark a book as read that doesn't exist in your collection
Think about how you could make the error messages more helpful for users.

**Exercise 4 - Inheritance Deep Dive**: 
Create a `Magazine` class that inherits from `Book` but adds issue number and publication date. Think about what methods you might want to override. Should a magazine's `get_info()` method show different information than a book's?

**Reflection Questions**: 
- Why is inheritance useful? What would happen if you had to copy all of Book's code into Magazine?
- What's the difference between "has-a" and "is-a" relationships? (A book "has-a" title vs a textbook "is-a" book)

**Exercise 5 - Planning Your Next Feature**: 
Think about what feature you'd like to add next. Maybe a rating system? Categories/genres? A wishlist of books to buy? Plan out:
- What new data would you need to store?
- What new methods would you need?
- How would you modify your file format?
- What could go wrong, and what exceptions might you need?

Don't just read these exercises - actually try them! The best way to learn programming is by writing code, making mistakes, and figuring out how to fix them. Each error you encounter and solve makes you a better programmer.

## Key Learning Points

**Classes and Objects**: A class is a blueprint, an object is made from that blueprint. You can make many objects from one class.

**Methods**: Functions that belong to a class. They define what objects can do.

**Inheritance**: Creating new classes based on existing ones. Child classes get everything from their parent plus their own additions.

**Polymorphism**: Different classes can have methods with the same name that work differently.

**Exception Handling**: Dealing with errors gracefully instead of letting your program crash.

**File Operations**: Saving and loading data so your program remembers things between runs.

## What You've Built

You now have a working book tracker that demonstrates all the core OOP concepts. You understand why each piece exists and how they work together. This foundation will let you build more complex programs with confidence.

Ready to try it? Start with the Book class and work your way through each step. Don't rush - understanding is more important than speed.