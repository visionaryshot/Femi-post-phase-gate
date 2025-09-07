books = [
    {"book_title": "Harry Potter", "Report": "available"},
    {"book_title": "The Hobbit", "Report": "available"},
    {"book_title": "To Kill a Mockingbird", "Report": "available"},
    {"book_title": "1984", "Report": "available"},
    {"book_title": "Pride and Prejudice", "Report": "available"}
]

def view_all_books():
    print("\nALL BOOKS")
    for count in range(len(books)):
        print(f"{count+1}. {books[count]['book_title']} - {books[count]['Report']}")

def borrow_book():
    print("\nBORROW A BOOK ")
    print("Available books:")
    
    available_books = []
    for count in range(len(books)):
        if books[count]['Report'] == "available":
            print(f"{count+1}. {books[count]['book_title']}")
            available_books.append(count + 1)
    
    if not available_books:
        print("No books available to borrow.")
        return
    
    book_choice = input("Enter the book number to borrow: ")
    
    if book_choice.isdigit():
        book_num = int(book_choice)
        if book_num in available_books:
            books[book_num - 1]['Report'] = "borrowed"
            print(f"You have borrowed '{books[book_num - 1]['title']}'")
        else:
            print("Invalid book number or book not available.")
    else:
        print("Please enter a valid number.")

def return_book():
    print("\nRETURN A BOOK")
    print("Borrowed books:")
    
    borrowed_books = []
    for count in range(len(books)):
        if books[count]['Report'] == "borrowed":
            print(f"{count+1}. {books[count]['book_title']}")
            borrowed_books.append(count + 1)
    
    if not borrowed_books:
        print("No books are currently borrowed.")
        return
    
    book_choice= input("Enter the book number to return: ")
    
    if book_choice.isdigit():
        book_number = int(book_choice)
        if book_number in borrowed_books:
            books[book_number - 1]['Report'] = "available"
            print(f"You have returned '{books[book_number - 1]['title']}'")
        else:
            print("Invalid book number")
    else:
        print("Enter a valid number.")

def show_menu():
    print("\nDASHBOARD")	
    print("1. View all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")


def intro():
    while True:
        show_menu()
        user_input = input("Enter your between (1-4): ")
        
        if  user_input == "1":
            view_all_books()
        elif  user_input == "2":
            borrow_book()
        elif  user_input == "3":
            return_book()
        elif  user_input == "4":
            print("Have a nice day buddy!")
            break
        else:
            print("Wrong input. click between 1-4.")

intro()
