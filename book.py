# a collection (list) to store books
# a method to add a book
# functinality to display all books
# a method to find a book by title or author or genre or publish date
# a method to sort the books alphabetically by title or author
# editing and deleting a book: We would need a way to uniquely identify each book, so we can select the correct one to edit or delete. Perhaps we could use the ISBN for this purpose since it's unique to each book.
# tagging system (genre)
# recommendation system :  This could be as simple as suggesting books with the same tags or by the same author. We might also consider the user's past interactions to make recommendations.
# storage system (file): We could use a file to store our books. Every time we add, edit, or delete a book, we would update this file. When the program starts, it would read from this file to populate the book collection.
# using ISBN to find books (isbn = International Standard Book Number)



#check if library.json exists:
from gettext import find
from math import e
import os
import json
from random import choice
from turtle import title


books = []

if not os.path.exists('library.json'): 
    books = []
else:
    # proceed to load books from library.json
    def load_books(filename='library.json'):
        try:
            with open(filename, 'r') as file:
                books_data = json.load(file)
                books = [Book.from_dict(book_data) for book_data in books_data]
                return books
            # converts books_data to book objects
        except FileNotFoundError:
            return [] #return an empty list if the file does not exist







#Save books:
def save_books(books, filename='library.json'):
    with open(filename, 'w') as file:
        books_data = [book.to_dict() for book in books]
        json.dump(books_data, file, indent=4)  # Use indent for pretty-printing
    






#Book class:
class Book:
    def __init__(self, title, author, publish_date, pages, summary, genre='General', tags=None):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.summary = summary
        self.genre = genre
        self.tags = tags if tags else []
    
   
    def book_info(self):
        tags_formatted = ', '.join(self.tags) if self.tags else 'No tags'
        return f"{self.title} by {self.author}, published on {self.publish_date}, with {self.pages} pages. Summary: {self.summary}. Genre: {self.genre}. Tags: {tags_formatted}."


    def to_dict(self):
        #method to convert a book object into a dictionary (suitbale for json conversion)
        return{
            'title' : self.title,
            'author': self.author,
            'publish_date': self.publish_date,
            'pages': self.pages,
            'summary': self.summary,
            'genre': self.genre,
            'tags': self.tags,
            }
    
    @classmethod
    def from_dict(cls, data):
        #class method to create a book object from a dictionary:
        return cls(
            title = data['title'],
            author = data['author'],
            publish_date = data['publish_date'],
            pages = data['pages'],
            summary = data['summary'],
            genre = data['genre', 'General'],   #Use get to provide default value if missing
            tags = data.get(['tags',[]])
        )

def add_book():
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    publish_date = input('Enter the publish date of the book: ')
    pages = input('Enter the number of pages of the book: ')
    summary = input('Enter the summary of the book: ')
    genre = input('Enter the genre of the book: ')
    tags = input('Enter the tags of the book: ').split(',')
    #create a new book object
    new_book = Book(title, author, publish_date, pages, summary, genre, tags)
    #add the new book to the list of books
    books.append(new_book)
    #save the books to the library.json file
    save_books(books)

    print(f'Book {title} by {author} has been added to the library.')       


def display_books():
    if not books: # Check if the list of books is empty
        print('No books in the library.')
    else:    
        for book in books:
            print(book.book_info())
            print('-' * 20) # Add a separator between books


def find_book():
    print("Search by: [1] Title, [2] Author, [3] Genre, [4] Publish Date")
    choice = input("Choose a search criterion: ")
    search_term = input("Enter search term: ")

    # Filter books based on the chosen criterion and search term
    if choice == '1':
        matched_books = [book for book in books if search_term.lower() in book.title.lower()]
    elif choice == '2':
        matched_books = [book for book in books if search_term.lower() in book.author.lower()]
    elif choice == '3':
        matched_books = [book for book in books if search_term.lower() in book.genre.lower()]
    elif choice == '4':
        matched_books = [book for book in books if search_term in book.publish_date]
    else:
        print("Invalid choice.")
        return

    if matched_books:
        print("Found the following books:")
        for book in matched_books:
            print(book.book_info())
    else:
        print("No books matched your search.")

def sort_books():
    print("Sort by: [1] Title, [2] Author")
    choice = input("Choose a sort criterion: ")

    if choice == '1':
        sorted_books = sorted(books, key=lambda book: book.title.lower())
    elif choice == '2':
        sorted_books = sorted(books, key=lambda book: book.author.lower())
    else:
        print("Invalid choice.")
        return

    print("Books sorted:")
    for book in sorted_books:
        print(book.book_info())


def edit_book():
    title = input("Enter the title of the book to edit: ")
    found = False
    for book in books:
        if book.title.lower() == title.lower():
            print("Book found. Enter new details:")
            book.title = input("Enter new title: ")
            book.author = input("Enter new author: ")
            book.publish_date = input("Enter new publish date: ")
            book.pages = int(input("Enter new number of pages: "))
            book.summary = input("Enter new summary: ")
            book.genre = input("Enter new genre: ")
            book.tags = input("Enter new tags: ").split(',')
            print("Book details updated.")
            save_books(books)
            found = True
            break
        if not found:
            print("Book not found.")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    for i, book in enumerate(books):
        if book.title.lower() == title.lower():
            del books[i]
            print("Book deleted.")
            save_books(books)
            break
    else:
        print("Book not found.")            

while True:
    print("Welcome to the library!")
    choice = input("Choose an option: [1] Add a book, [2] Display books, [3] Find a book, [4] Sort books, [5] Edit a book, [6] Delete a book, [7] Quit: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        find_book()
    elif choice == '4':
        sort_books()
    elif choice == '5':
        edit_book()
    elif choice == '6':
        delete_book()
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")        