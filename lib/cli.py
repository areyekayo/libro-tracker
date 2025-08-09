# lib/cli.py

from helpers import (
    exit_program,
    create_book,
    select_genre,
    update_book_details,
    update_book_reading_status,
    delete_book,
    create_genre,
    update_genre,
    delete_genre,
    genre_menu_prompt
)

def main():
    print("\nWelcome to Libro Tracker!")
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
    action = ""
    while action != "0":
        action, book = genre_menu_prompt(genre)

        if action is None and book is None:
            # If both are none, user entered invalid input
            continue
        elif action == "add_book":
            book = create_book(genre)
        elif action == "edit_genre":
            update_genre(genre)
        elif action == "show_desc":
            print(f"Genre Description: {genre.description}")
        elif action == "delete_genre":
            delete_genre(genre)
            break

        if not book:
            continue

        book_menu(book)
            
def book_menu(book):
    """Displays options for a book."""
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
