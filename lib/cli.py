# lib/cli.py

from helpers import (
    exit_program,
    create_book,
    select_genre,
    select_from_list
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            genre_menu()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Genres")

def genre_menu():
    print("*** GENRE MENU ***")
    print("-------------------")
    genre = ""
    while genre != None:
        print("Select a genre, or press 0 to go back:\n>")
        genre = select_genre()
        if genre:
            choice = ""
            print(f"Selected {genre.name}. Please select an option, or 0 to go back:\n")
            print("     1. Add Book")
            choice = input(">")
            while choice != "0":
                if choice == "1":
                     book = create_book(genre)
                     return book

            





if __name__ == "__main__":
    main()
