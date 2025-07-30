# lib/cli.py

from helpers import (
    exit_program,
    create_book,
    select_genre,
    select_from_list,
    select_book,
    update_book_details
)


def main():
    print("\nWelcome to Libro Tracker!\n")
    genre = ""
    while genre is not None:
        print("\n*** GENRES ***")
        genre = select_genre("\nSelect a genre number, or 0 to exit the program:")
        if genre == None or genre == "0":
            exit_program()
        elif genre:
            genre_menu(genre)
        else:
            print("Invalid choice, please try again.")
        

def menu():
    print("\nWelcome to Libro Tracker!\n")

def genre_menu(genre):
    choice = ""
    while choice is not None:
        print(f"\n *** {genre.name.upper()} ***")
        print(f"    {genre.description}\n")
        print("What would you like to do in this genre?: ")
        print("     1. Add New Book To Genre")
        print("     2. See Currently Reading Books")
        print("     3. See 'To Read' Books")
        print("     4. See 'Finished' Books")
        print("     5. See 'Did Not Finish' Books")
        print("     6. Edit Genre")
        print("Select an option number, or 0 to go back:")
        choice = input("> ")
        if choice == "0":
            choice = None
            break

        book = None
        if choice == "1":
            book = create_book(genre)
        elif choice == "2":
            print("Books you're currently reading: ")
            book = select_book(genre, "Reading")
        elif choice == "3":
            print("Books you haven't read yet: ")
            book = select_book(genre, "To Read")
        elif choice == "4":
            print("Books you've finished reading: ")
            book = select_book(genre, "Finished")
        elif choice == "5":
            print("Books you did not finish:")
            book = select_book(genre, "Did Not Finish")
        else:
            print("Invalid choice, please try again.")
            continue

        if not book:
            continue

        book_menu(book)
            
def book_menu(book):
    choice = ""
    while choice is not None:
        print(f"\n*** Selected {book.title} by {book.author}. Current status: {book.status} *** ")
        print("What would you like to do?")
        print("     1. Update Book Title, Author, or Page Count")
        print("     2. Update Reading Status")
        print("Select an option, or 0 to go back:")
        choice = input("> ")
        if choice == "0":
            choice = None
        elif choice == "1":
            update_book_details(book)
        elif choice == "2":
            print("Start reading...")
            pass

            




if __name__ == "__main__":
    main()
