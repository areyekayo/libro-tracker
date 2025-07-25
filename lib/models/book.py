from models.__init__ import CURSOR, CONN
from datetime import datetime, date

class Book:

    all = {}
    statuses = ["To Read", "Reading", "Finished", "Did Not Finish"]

    def __init__(self, author, page_count, status, genre_id, started_date=None, finished_date=None, id=None):
        self.id = id
        self.author = author
        self.page_count = page_count
        self.status = status
        self.genre_id = genre_id
        self.started_date = started_date
        self.finished_date = finished_date
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, str) and author:
            self._author = author
        else: raise ValueError("Author must be a non-empty string.")
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int) and page_count:
            self._page_count = page_count
        else: raise ValueError("Page count must be a whole number.")

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        if status not in Book.statuses:
            raise Exception("Status not recognized. Possible statuses: 'To Read', 'Reading', 'Finished', or 'Did Not Finish'.")
        else: 
            self._status = status

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            author TEXT,
            page_count INTEGER,
            status TEXT,
            started_date TEXT,
            finished_date TEXT,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO books (author, page_count, status, genre_id, started_date, finished_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.author, self.page_count, self.status, self.genre_id, self.started_date, self.finished_date))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE books
            SET author = ?, page_count = ?, status = ?, genre_id = ?, 
            started_date = ?, finished_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.author, self.page_count, self.status, 
                             self.   genre_id, self.started_date, self.finished_date, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE from books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, author, page_count, status, genre_id, started_date, finished_date):
        book = cls(author, page_count, status, genre_id, started_date, finished_date)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.author = row[1]
            book.page_count = row[2]
            book.status = row[3]
            book.genre_id = row[4]
            book.started_date = row[5]
            book.finished_date = row[6]
        else:
            book = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def genre(self):
        pass