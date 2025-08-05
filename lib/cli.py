# lib/cli.py

from helpers import (
    exit_program,
    create_book,
    select_genre,
    select_book,
    update_book_details,
    update_book_reading_status,
    book_status_counts,
    delete_book,
    create_genre,
    update_genre,
    genre_stats,
    delete_genre
)

def main():
    print("\nWelcome to Libro Tracker!\n")
    genre = ""
    while genre is not None:
        print("\n*** MAIN MENU ***")
        genre = select_genre("\nSelect a genre number, or 0 to exit the program:")

        if genre == "Add new genre":
            genre = create_genre()
        elif genre:
            genre_menu(genre)
        else:
            exit_program()

def genre_menu(genre):
    choice = ""
    while choice != "0":
        print(f"\n *** {genre.name.upper()} GENRE MENU ***")
        genre_stats(genre) # Show number of books and pages read in the genre
        status_counts = book_status_counts(genre) # get counts of books in each status
        print(f"\nOptions for {genre.name} genre: ")
        # Start empty option array and option number to list dynamic options if a genre has no books in some statuses
        options = []
        number = 1

        # Each option item will have a number to select, an action key, and descrition to display. 
        # Always add "Add New Book To Genre" as option 1. 
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
            (str(number+1), "show_desc", "Show Genre Description"),
            (str(number+2), "delete_genre", "Delete Genre"),
        ])

        # Print options
        for opt_num, _, description in options:
            print(f"     {opt_num}. {description}")

        print("Select an option number, or 0 to go back:")
        choice = input("> ")

        book = None

        # Map choice input to actions, to be used to control menu flow
        choice_map = {opt_num: action for opt_num, action, _ in options}
        
        if choice in choice_map:
            # Get the action that maps to the user's choice
            action = choice_map[choice]
            if action == "add_book":
                book = create_book(genre)
            elif action in ("Reading", "To Read", "Finished", "Did Not Finish"):
                print(f"\n{genre.name} books with status '{action}':")
                book = select_book(genre, action)
            elif action == "edit_genre":
                update_genre(genre)
            elif action == "show_desc":
                print(f"Genre Description: {genre.description}")
            elif action == "delete_genre":
                delete_genre(genre)
                break
        elif choice != "0":
            print("Invalid choice, please try again.")

        if not book:
            continue

        book_menu(book)
            
def book_menu(book):
    choice = ""
    while choice != "0":
        print(f"\n*** '{book.title}' by {book.author}, {book.page_count} pages. Current status: {book.status} *** ")
        print("\nWhat would you like to do with this book?")
        print("     1. Update Title, Author, or Page Count")
        print("     2. Update Reading Status")
        print("     3. Delete Book")
        print("Select an option, or 0 to go back:")
        choice = input("> ")
        if choice == "1":
            update_book_details(book)
        elif choice == "2":
            update_book_reading_status(book)
        elif choice == "3":
            delete_book(book)
            break
        elif choice != "0":
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
