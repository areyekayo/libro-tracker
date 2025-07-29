# lib/cli.py

from helpers import (
    exit_program,
    create_book,
    select_genre,
    select_from_list,
    select_book
)


def main():
    print("\nWelcome to Libro Tracker!\n")
    genre = ""
    while genre != None:
        print("*** GENRES ***")
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
    in_genre_menu = True
    print(f"\n *** {genre.name.upper()} ***")
    print(f"    {genre.description}\n")
    while in_genre_menu:
        print("Options: ")
        print("     1. Add New Book To Genre")
        print("     2. See Currently Reading Books")
        print("     3. See 'To Read' Books")
        print("     4. See 'Finished' Books")
        print("     5. See 'Did Not Finish' Books")
        print("     6. Edit Genre")
        book = None
        print("Select an option number, or 0 to go back:")
        choice = input("> ")
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
        elif choice == "0":
            in_genre_menu = False
        else:
            print("Invalid choice, please try again.")
            
        if not book:
            continue
        if book:
            pass


if __name__ == "__main__":
    main()
