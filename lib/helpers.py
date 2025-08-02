# lib/helpers.py
from models.book import Book
from models.genre import Genre

def exit_program():
    print("Goodbye!")
    exit()

def select_from_list(items, item_display_func=str, prompt="\nSelect an option (or 0 to go back):"):
    """
    Displays a numbered list of items and prompt user to select one within a loop, validates user input, and returns the selected item.
    """
    if not items:
        return None
    
    for i, item in enumerate(items, start=1):
        print(f"    {i}. {item_display_func(item)}")
    
    print(prompt)

    choice = ""
    while choice != 0:
        try:
            choice = int(input("> "))
            if choice == 0:
                return None
            if 1 <= choice <= len(items):
                return items[choice - 1]
            print(f"Please enter a number between 0 and {len(items)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def select_book_status():
    """Displays book statuses to be selected in the CLI."""
    statuses = Book.statuses
    def status_display(status):
        return f"{status}"
    
    status = select_from_list(statuses, status_display, "Select the status of the book: \n")

    return status

def select_genre(prompt="Select a genre, or 0 to go back:"):
    """Displays existing genres and count of their books, or option to add new genre, and calls select_from_list to display in CLI."""
    genres = Genre.get_all()
    genres.append("Add new genre")

    def genre_display(item):
        if isinstance(item, Genre):
            return f"{item.name} ({len(item.books())} books)"
        else:
            return f"{item}"
    
    genre = select_from_list(genres, genre_display, prompt)
    return genre

def select_book(genre: Genre, status):
    """Displays existing books within a genre, and calls select_from_list to display in CLI."""
    books = genre.books()
    book_list = [book for book in books if book.status == status]

    if not book_list:
        print(f"    No books in '{status}' status!")
        return None

    def book_display(book: Book):
        return f"'{book.title}' by {book.author}, {book.page_count} pages"
    
    book = select_from_list(book_list, book_display, "\nSelect a book, or 0 to go back:")

    return book

def create_book(genre: Genre):
    """Creates a new book within a genre."""
    print(f"\nAdding a new {genre.name} book...")
    title = input("Enter the book's title: ")
    author = input("Enter the author's name: ")
    page_count = int(input("Enter the number of pages: "))
    print("Book statuses: ")
    status = select_book_status()

    try:
        book = Book.create(title, author, page_count, status, genre.id)
        print(f"\nSuccessfully created new {genre.name} book: '{book.title}' by {book.author}, {page_count} pages")
        return book
    except Exception as exc:
        print(f"Error creating the book: {exc}\n")

def update_book_details(book: Book):
    """Updates a book's title, author, and/or page count."""
    try:
        print(f"\nCurrent title: '{book.title}'")
        title = input("Enter the updated title, or press 'enter' to keep current title: ")
        print(f"\nCurrent author: {book.author}")
        author = input("Enter the updated author's name, or press 'enter' to keep current author: ")
        print(f"\nCurrent page count: {book.page_count}")
        page_count = input("Enter the updated page count, or press 'enter' to keep current page count: ")
        
        if title.strip() != "":
            book.title = title
        if author.strip() != "":
            book.author = author
        if page_count.strip() != "":
            book.page_count = int(page_count)
        
        book.update()
        print(f"\nSuccessfully updated book: '{book.title}' by {book.author}, {book.page_count} pages.")

    except Exception as exc:
        print(f"Error updating book: {exc}")

def update_book_reading_status(book: Book):
    """Updates a book's reading status."""
    print(f"\n'{book.title}' current status: {book.status}")
    print("\nSelect a new status: ")
    new_status = select_book_status()
    book.status = new_status
    
    book.update()
    print(f"Successfully updated '{book.title}' status: {book.status}")

def get_genre_total_pages_read(genre: Genre):
    """Gets the count of total pages read for finished books in a genre."""
    books = genre.books()
    pages_read = sum(book.page_count for book in books if book.status == "Finished")
    return pages_read

def get_genre_total_books_read(genre: Genre):
    """Gets the count of total finished books in a genre."""
    books = genre.books()
    books_read = len([book for book in books if book.status == "Finished"])
    return books_read

def get_book_status_counts(genre: Genre):
    """Gets a count of all current book statuses within a genre to display in CLI."""
    status_counts = {status: 0 for status in Book.statuses}

    for book in genre.books():
        if book.status in status_counts:
            status_counts[book.status] += 1

    return status_counts

def delete_book(book: Book):
    print(f"\nDeleting '{book.title}' by {book.author}...")
    try:
        book.delete()
        print(f"Successfully deleted '{book.title}'!")
        print("Returning to genre menu...")
    except Exception as exc:
        print(f"\nError deleting book: {exc}")

def create_genre():
    print(f"\nAdding a new genre...")
    name = input("Enter the genre's name: ")
    description = input("Enter a short description for the genre: ")

    try:
        genre = Genre.create(name, description)
        print(f"\nSuccessfully created {genre.name} genre.")
        return genre
    except Exception as exc:
        print(f"\nError creating genre: {exc}")

def update_genre(genre: Genre):
    print("\nUpdating genre...")
    try:
        print(f"Genre's current name: {genre.name}")
        name = input("Enter a new name, or press 'enter' to keep current name: ")
        print(f"\nGenre's current description: {genre.description}")
        description = input("Enter a new description, or press 'enter' to keep current description: ")

        if name.strip() != "":
            genre.name = name
        if description.strip() != "":
            genre.description = description
        
        genre.update()
        print(f"\nSuccessfully updated genre: {genre.name}")
        print(f"Description: '{genre.description}")
    except Exception as exc:
        print(f"\nError updating genre: {exc}")


    




