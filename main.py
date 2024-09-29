# Library Management System in Python

library = {}

def add_book(book_id, title, author):
    library[book_id] = {'Title': title, 'Author': author, 'Available': True}
    print(f"Book '{title}' added successfully!")

def display_books():
    if library:
        print("\nList of Books in the Library:")
        for book_id, details in library.items():
            availability = 'Available' if details['Available'] else 'Not Available'
            print(f"ID: {book_id}, Title: {details['Title']}, Author: {details['Author']}, Status: {availability}")
    else:
        print("No books in the library.")

def update_book(book_id, title=None, author=None):
    if book_id in library:
        if title:
            library[book_id]['Title'] = title
        if author:
            library[book_id]['Author'] = author
        print(f"Book ID {book_id} updated successfully!")
    else:
        print("Book not found.")

def delete_book(book_id):
    if book_id in library:
        del library[book_id]
        print(f"Book ID {book_id} deleted successfully!")
    else:
        print("Book not found.")

def borrow_book(book_id):
    if book_id in library:
        if library[book_id]['Available']:
            library[book_id]['Available'] = False
            print(f"You have borrowed '{library[book_id]['Title']}'.")
        else:
            print("Book is not available.")
    else:
        print("Book not found.")

def return_book(book_id):
    if book_id in library:
        library[book_id]['Available'] = True
        print(f"Thank you for returning '{library[book_id]['Title']}'.")
    else:
        print("Book not found.")

def menu():
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            add_book(book_id, title, author)
        elif choice == '2':
            display_books()
        elif choice == '3':
            book_id = input("Enter Book ID: ")
            title = input("Enter new Title (leave blank to skip): ")
            author = input("Enter new Author (leave blank to skip): ")
            update_book(book_id, title or None, author or None)
        elif choice == '4':
            book_id = input("Enter Book ID: ")
            delete_book(book_id)
        elif choice == '5':
            book_id = input("Enter Book ID: ")
            borrow_book(book_id)
        elif choice == '6':
            book_id = input("Enter Book ID: ")
            return_book(book_id)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
