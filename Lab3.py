
class Book_class:
    def __init__(self, book_id, book_title, author_id, publisher, year_of_publication):
        self.book_id = book_id
        self.book_title = book_title
        self.author_id = author_id
        self.publisher = publisher
        self.year_of_publication = year_of_publication


class Author_class:
    def __init__(self, author_id, author_name, affiliation, country, phone, email_id):
        self.author_id = author_id
        self.author_name = author_name
        self.affiliation = affiliation
        self.country = country
        self.phone = phone
        self.email_id = email_id



class User_class:
    def __init__(self, user_id, name, password, address, phone, emailid, booksborrowed = None):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.address = address
        self.phone = phone
        self.email_id = emailid
        self.booksborrowed = [] if booksborrowed is None else booksborrowed



books = []

def add_book():
    book_id = input("Enter Book ID: ")
    book_title = input("Enter Book Title: ")
    author_id = input("Enter Author ID: ")
    publisher = input("Enter Publisher: ")
    year_of_publication = input("Enter Year of Publication: ")

    book = Book_class(book_id, book_title, author_id, publisher, year_of_publication)

    books.append(book)

    print("Book added successfully!")


authors = []

def add_author():
    author_id = input("Enter Author ID: ")
    author_name = input("Enter Author Name: ")
    affiliation = input("Enter Affiliation: ")
    country = input("Enter Country: ")
    phone = input("Enter Phone: ")
    email_id = input("Enter Email: ")

    author = Author_class(author_id, author_name, affiliation, country, phone, email_id)

    authors.append(author)

    print("Author added successfully!")


users = []

def add_user():
    user_id = input("Enter User ID: ")
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone: ")
    email_id = input("Enter Email: ")

    user = User_class(user_id, name, password, address, phone, email_id)

    users.append(user)

    print("User added successfully!")


def display_books():
    for book in books:
        print("Book ID:", book.book_id)
        print("Book Title:", book.book_title)
        print("Author ID:", book.author_id)
        print("Publisher:", book.publisher)
        print("Year of Publication:", book.year_of_publication)


def display_authors():
    for author in authors:
        print("Author ID:", author.author_id)
        print("Author Name:", author.author_name)
        print("Affiliation:", author.affiliation)
        print("Country:", author.country)
        print("Phone:", author.phone)
        print("Email:", author.email_id)


def display_users():
    for user in users:
        print("User ID:", user.user_id)
        print("Name:", user.name)
        print("Password:", user.password)
        print("Address:", user.address)
        print("Phone:", user.phone)
        print("Email:", user.email_id)
        print("Books Borrowed:", user.booksborrowed)



while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. Add Author")
    print("3. Add User")
    print("4. Display Books")
    print("5. Display Authors")
    print("6. Display Users")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        add_author()
    elif choice == "3":
        add_user()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_authors()
    elif choice == "6":
        display_users()
    elif choice == "7":
        print("Exit")
        break
    else:
        print("Invalid choice")



