# lib/cli.py

from helpers import (
    exit_program,
    create_book,
    select_genre,
    select_book,
    update_book_details,
    update_book_reading_status,
    get_book_status_counts,
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
        print("\n*** GENRES ***")
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
        genre_stats(genre)
        status_counts = get_book_status_counts(genre)
        print(f"\nOptions for {genre.name} genre: ")
        print("     1. Add New Book To Genre")
        print(f"     2. See 'Currently Reading' Books ({status_counts.get('Reading')} books)")
        print(f"     3. See 'To Read' Books ({status_counts.get('To Read')} books)")
        print(f"     4. See 'Finished' Books ({status_counts.get('Finished')} books)")
        print(f"     5. See 'Did Not Finish' Books ({status_counts.get('Did Not Finish')} books)")
        print("     6. Edit Genre")
        print("     7. Show Description")
        print("     8. Delete Genre")
        print("Select an option number, or 0 to go back:")
        choice = input("> ")
        book = None
        if choice == "1":
            book = create_book(genre)
        elif choice == "2":
            print(f"\n{genre.name} books you're currently reading: ")
            book = select_book(genre, "Reading")
        elif choice == "3":
            print(f"\n{genre.name} books you haven't read yet: ")
            book = select_book(genre, "To Read")
        elif choice == "4":
            print(f"\n{genre.name} books you've finished reading: ")
            book = select_book(genre, "Finished")
        elif choice == "5":
            print(f"\n{genre.name} books you did not finish:")
            book = select_book(genre, "Did Not Finish")
        elif choice == "6":
            update_genre(genre)
        elif choice == "7":
            print(f"Genre Description: {genre.description}")
        elif choice == "8":
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
        print(f"\n*** Selected '{book.title}' by {book.author}, {book.page_count} pages. Current status: {book.status} *** ")
        print("\nWhat would you like to do?")
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
