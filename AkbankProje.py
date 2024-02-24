class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books available.")
        else:
            for book in books:
                title, author, year, pages = book.split(",")
                print(f"Title: {title}, Author: {author}, Year: {year}, Pages: {pages}")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the first release year of the book: ")
        pages = input("Enter the number of pages of the book: ")
        book_info = f"{title},{author},{year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        updated_books = []
        removed = False
        for book in books:
            if title_to_remove not in book:
                updated_books.append(book)
            else:
                removed = True
        if removed:
            self.file.seek(0)
            self.file.truncate()
            for book in updated_books:
                self.file.write(book + "\n")
            print(f"Book '{title_to_remove}' removed successfully.")
        else:
            print(f"Book '{title_to_remove}' not found.")

lib = Library()

while True:
    print("\n  MENU ")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        del lib  
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
