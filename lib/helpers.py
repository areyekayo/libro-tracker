# lib/helpers.py
from models.book import Book
from models.genre import Genre

def exit_program():
    print("Goodbye! Go read some books!")
    exit()

def select_from_list(items, item_display_func, prompt="\nSelect an option (or 0 to go back):"):
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

    status_display = lambda status: f"{status}"
    
    status = select_from_list(statuses, status_display, "Select the status of the book: \n")

    return status

def select_genre(prompt="Select a genre, or 0 to go back:", genre_options=None):
    """Displays existing genres and count of their books, or option to add new genre, and calls select_from_list to display in CLI. A list of genres may be passed from delete_genre function when books need to be reassigned to another genre."""
    if not genre_options:  
        # If genre_options are not passed, this is being called by main in CLI, and option to add new genre should be displayed along with all genre objects
        genre_options = Genre.get_all()
        genre_options.append("Add new genre")

    def genre_display(item):
        if isinstance(item, Genre):
            return f"{item.name} ({len(item.books())} books)"
        else:
            return f"{item}"
    
    genre = select_from_list(genre_options, genre_display, prompt)
    return genre

def select_book(genre: Genre, status):
    """Displays existing books by status within a genre, and calls select_from_list to display in CLI."""
    books = genre.books()
    book_list = [book for book in books if book.status == status]

    book_display = lambda book: f"'{book.title}' by {book.author}, {book.page_count} pages"
    
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
    """Updates a book's title, author, page count, and/or genre."""
    try:
        print(f"\nCurrent title: '{book.title}'")
        title = input("Enter the updated title, or press 'enter' to keep current title: ")

        print(f"\nCurrent author: {book.author}")
        author = input("Enter the updated author's name, or press 'enter' to keep current author: ")

        print(f"\nCurrent page count: {book.page_count}")
        page_count = input("Enter the updated page count, or press 'enter' to keep current page count: ")

        genre = Genre.find_by_id(book.genre_id)
        print(f"\nCurrent genre: {genre.name}")
        new_genre = select_genre("Select a new genre, or 0 to keep current genre: ", [g for g in Genre.get_all() if g.id != book.genre_id])
        
        if title.strip() != "": book.title = title
        if author.strip() != "": book.author = author
        if page_count.strip() != "": book.page_count = int(page_count)
        if new_genre is not None: book.genre_id = new_genre.id
        
        book.update()
        print(f"\nSuccessfully updated book: '{book.title}' by {book.author}, genre: {Genre.find_by_id(book.genre_id).name}, {book.page_count} pages")

    except Exception as exc:
        print(f"Error updating book: {exc}")

def update_book_reading_status(book: Book):
    """Updates a book's reading status."""
    print(f"\nUpdating '{book.title}' current status: {book.status}")
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

def book_status_counts(genre: Genre):
    """Gets a count of all current book statuses within a genre to display in CLI."""
    status_counts = {status: 0 for status in Book.statuses}

    for book in genre.books():
        if book.status in status_counts:
            status_counts[book.status] += 1

    return status_counts

def delete_book(book: Book):
    """Deletes a book."""
    print(f"\nDeleting '{book.title}' by {book.author}...")
    try:
        book.delete()
        print(f"Successfully deleted '{book.title}'!")
        print("Returning to genre menu...")
    except Exception as exc:
        print(f"\nError deleting book: {exc}")

def create_genre():
    """Creates a new genre."""
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
    """Updates a genre's name and description."""
    print("\nUpdating genre...")
    try:
        print(f"Genre's current name: {genre.name}")
        name = input("Enter a new name, or press 'enter' to keep current name: ")
        print(f"\nGenre's current description: '{genre.description}'")
        description = input("Enter a new description, or press 'enter' to keep current description: ")

        if name.strip() != "":
            genre.name = name
        if description.strip() != "":
            genre.description = description
        
        genre.update()
        print(f"\nSuccessfully updated genre: {genre.name}")
        print(f"Description: '{genre.description}'")
    except Exception as exc:
        print(f"\nError updating genre: {exc}")
    
def delete_genre(genre: Genre):
    """Deletes a genre. If there are books assigned to the genre, user will be prompted to reassign the books to another genre."""
    print("\nDeleting genre...")
    books = genre.books()
    try:
        if books:
            print(f"\nThis genre has {len(books)} books that need to be assigned a new genre: ")
            genres = [g for g in Genre.get_all() if g.id != genre.id]
            print(*(f"   '{book.title}' by {book.author}" for book in books), sep="\n")
            print("\nAvailable genres: ")
            new_genre = select_genre("Select a new genre for these books: ", genres)
            if new_genre == "Add new genre":
                new_genre = create_genre()
                
            print(f"\nAssigning books to '{new_genre.name}' genre...")
            for book in books:
                book.genre_id = new_genre.id
                book.update()
        
        genre.delete()
        print(f"\nSuccessfully deleted {genre.name} genre.")
        
    except Exception as exc:
        print(f"\nError deleting genre: {exc}")


def genre_stats(genre: Genre):
    """Gets counts of the total number of books and pages (book status = "Finished") that have been read in a genre."""
    pages_read = get_genre_total_pages_read(genre)
    books_read = get_genre_total_books_read(genre)
    print(f"  Books read: {books_read}")
    print(f"  Total pages read: {pages_read}")


def genre_menu_prompt(genre: Genre):
    """
    Displays dynamic options for a genre, returns a tuple (selected option, book) based on user choice.
    """
    print(f"\n *** {genre.name.upper()} GENRE MENU ***")
    genre_stats(genre)  # show number of books and pages read
    status_counts = book_status_counts(genre)  # get counts of books in each status

    # Start empty option array and option number to list dynamic options if a genre has no books in some statuses
    print(f"\nOptions for {genre.name} genre: ")
    options = []
    number = 1

    # Each option item will have a number to select, an option name, and descrition to display. 
    # "Add New Book To Genre" will always be option 1.
    options.append((str(number), "add_book", "Add New Book To Genre"))
    number += 1

     # Book options to show only if book status count is > 0 for the genre
    status_options = [
        ("Reading", "Currently Reading"),
        ("To Read", "To Read"),
        ("Finished", "Finished"),
        ("Did Not Finish", "Did Not Finish")
    ]
    # Append book status to options list if status count > 0
    for status_key, label in status_options:
        count = status_counts.get(status_key, 0)
        if count > 0:
            options.append((str(number), status_key, f"See '{label}' Books ({count} books)"))
            number += 1

    # Add other fixed options for the genre
    options.extend([
        (str(number), "edit_genre", "Edit Genre"),
        (str(number + 1), "show_desc", "Show Genre Description"),
        (str(number + 2), "delete_genre", "Delete Genre"),
    ])

    for opt_num, _, description in options:
        print(f"     {opt_num}. {description}")

    print("Select an option number, or 0 to go back:")
    
    # Map choice input to actions, to be used to CLI genre menu flow
    choice_map = {opt_num: option for opt_num, option, _ in options}
    choice = ""
    while choice != "0":
        choice = input("> ")

        if choice == "0":
            return "0", None 
            # "0" must be returned here to exit the CLI genre menu loop that called this function
        
        if choice not in choice_map:
            print("Invalid choice, please try again.")
            continue

        option = choice_map[choice]
        book = None

        if option in ("Reading", "To Read", "Finished", "Did Not Finish"):
            print(f"\n{genre.name} books with status '{option}':")
            book = select_book(genre, option)

        return option, book