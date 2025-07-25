from models.__init__ import CURSOR, CONN
from datetime import datetime, date

class Book:

    all = {}
    statuses = ["To Read", "Reading", "Finished", "Did Not Finish"]

    def __init__(self, author, page_count, status, genre_id, started_date=None, finished_date=None):
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

    
        

    



    


