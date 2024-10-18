# Book and User Collection
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Available"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "status": "Available"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "status": "Checked Out"},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic", "status": "Available"}
]

users = [
    {"id": 1, "name": "Ali", "borrowed_books": []},
    {"id": 2, "name": "Ahmad", "borrowed_books": []}
]

# Helper Functions
def find_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def find_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# 1. Borrow a Book
def borrow_book(user_id, book_id):
    user = find_user_by_id(user_id)
    book = find_book_by_id(book_id)
    if user and book and book["status"] == "Available":
        book["status"] = "Checked Out"
        user["borrowed_books"].append(book)
        print(f"{user['name']} successfully borrowed '{book['title']}'")
    else:
        print(f"Book is not available or user not found.")

# 2. Return a Book
def return_book(user_id, book_id):
    user = find_user_by_id(user_id)
    book = find_book_by_id(book_id)
    if user and book and book in user["borrowed_books"]:
        book["status"] = "Available"
        user["borrowed_books"].remove(book)
        print(f"{user['name']} successfully returned '{book['title']}'")
    else:
        print(f"Book not found in user's borrowed list.")

# 3. Search Books
def search_books(keyword):
    results = [book for book in books if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower() or keyword.lower() in book["genre"].lower()]
    if results:
        for book in results:
            print(f"{book['id']}: {book['title']} by {book['author']} ({book['genre']}) - {book['status']}")
    else:
        print("No books found.")

# 4. View Books by Status
def view_all_books():
    print("\nAll Books:")
    for book in books:
        print(f"{book['id']}: {book['title']} by {book['author']} ({book['genre']}) - {book['status']}")

def view_available_books():
    print("\nAvailable Books:")
    available_books = [book for book in books if book["status"] == "Available"]
    for book in available_books:
        print(f"{book['id']}: {book['title']} by {book['author']} ({book['genre']})")

def view_checked_out_books():
    print("\nChecked Out Books:")
    checked_out_books = [book for book in books if book["status"] == "Checked Out"]
    for book in checked_out_books:
        print(f"{book['id']}: {book['title']} by {book['author']} ({book['genre']})")

# 5. User Input and Menu-Driven Interface
def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. Search Books")
        print("4. View All Books")
        print("5. View Available Books")
        print("6. View Checked Out Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_book(user_id, book_id)
        
        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            return_book(user_id, book_id)
        
        elif choice == '3':
            keyword = input("Enter title, author, or genre to search: ")
            search_books(keyword)
        
        elif choice == '4':
            view_all_books()
        
        elif choice == '5':
            view_available_books()
        
        elif choice == '6':
            view_checked_out_books()
        
        elif choice == '7':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()
