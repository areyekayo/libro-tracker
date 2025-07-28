# lib/helpers.py
from models.book import Book
from models.genre import Genre

def exit_program():
    print("Goodbye!")
    exit()

def select_from_list(items, item_display_func=str, prompt="Select an option (or 0 to go back):\n>"):
    """
    Displays a numbered list of items and prompt user to select one within a loop, validates user input, and returns the selected item.
    """
    if not items:
        return None
    
    print(prompt)
    for i, item in enumerate(items, start=1):
        print(f"    {i}. {item_display_func(item)}")
    
    while True:
        try:
            choice = int(input(">"))
            if choice == 0:
                return None
            if 1 <= choice <= len(items):
                return items[choice - 1]
            print(f"Please enter a number between 0 and {len(items)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def select_new_book_status():
    statuses = Book.statuses
    def status_display(status):
        return f"{status}"
    
    status = select_from_list(statuses, status_display, "Select the status of the new book: \n")

    return status

def select_genre():
    genres = Genre.get_all()

    def genre_display(genre):
        return f"{genre.name}—{len(genre.books())} books"
    
    genre = select_from_list(genres, genre_display, "Select a genre, or 0 to go back: ")
    return genre

def create_book(genre):
    """Creates a new book."""
    title = input("Enter the book's title: ")
    author = input("Enter the author's name: ")
    page_count = int(input("Enter the number of pages: "))
    status = select_new_book_status()

    if status == "Did Not Finish" or status == "Reading":
        started_date = input(f"What date did you start reading {title}? Enter date in YYYY-MM-DD format:\n>")

    elif status == "Finished":
        started_date = input(f"What date did you start reading {title}? Enter date in YYYY-MM-DD format:\n>")
        finished_date = input(f"What date did you finish reading {title}? Enter date in YYYY-MM-DD format:\n>")

    else:
        started_date = None
        finished_date = None

    try:
        book = Book.create(title, author, page_count, status, genre.id, started_date, finished_date)
        print(f"Successfully created new {genre.name} book: {book.title} by {book.author}, {page_count} pages")
    except Exception as exc:
        print(f"Error creating the book: {exc}\n")

