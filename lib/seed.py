from models.__init__ import CONN, CURSOR
from models.book import Book
from models.genre import Genre

def seed_database():
    Book.drop_table()
    Genre.drop_table()

    Book.create_table()
    Genre.create_table()

    sci_fi_fantasy = Genre.create("Sci-Fi and Fantasy", "Science fiction or fantasy features speculative world-building based around hard/soft science or fantasy as part of the plot and impacts on characters, culture, or society.")
    mindfulness = Genre.create("Mindfulness", "Mindfulness includes books exploring mindful practices such as meditation, Buddhism, yoga, and therapy/self-help.")
    non_fiction = Genre.create("Non-Fiction", "Non-fiction includes science, creative non-fiction, biographies, or history.")
    fiction = Genre.create("Fiction", "Fiction is any creative or narrative work featuring imaginary characters in a realistic setting and a plot.")
    poetry = Genre.create("Poetry", "Poetry is a literary art that uses aesthetic and rhythmic qualities of language to evoke meanings.")

    book1 = Book.create("House of Suns", "Alastair Reynolds", 473, "Finished", sci_fi_fantasy.id, "2025-05-13", "2025-06-05")
    book2 = Book.create("Children of Time", "Adrian Tchaikovsky", 600, "Finished",sci_fi_fantasy.id, "2025-07-01", "2025-07-24")
    book3 = Book.create("Unwinding Anxiety", "Judson Brewer", 304, "Finished", mindfulness.id, "2025-03-04", "2025-03-27")
    book4 = Book.create("The Information: A History, A Theory, A Flood", "James Gleick", 544, "Finished",non_fiction.id, "2025-02-01", "2025-02-24")
    book5 = Book.create("Children of Ruin", "Adrian Tchaikovsky", 576, "Reading", sci_fi_fantasy.id, "2025-07-24", None)
    book6 = Book.create("Emperor of Gladness", "Ocean Vuong",409,"To Read", fiction.id, None, None)
    book7 = Book.create("Autobiography of Red: A Novel In Verse", "Anne Carson", 149, "Finished", fiction.id, "2025-01-03", "2025-01-18")
    book8 = Book.create("Plainwater: Essays and Poetry", "Anne Carson", 260, "Finished", poetry.id, "2025-02-15", "2025-03-01")
    book9 = Book.create("Perdido Street Station", "China Mieville", 867, "Did Not Finish", sci_fi_fantasy.id, "2025-06-13", None)
    book10 = Book.create("The Sirens' Call", "Chris Hayes", 336, "To Read", non_fiction.id, None, None)

seed_database()



