from models.__init__ import CURSOR, CONN


class Genre:
    all = {}

    def __init__(self, name, description, id=None):
        self.name = name
        self.description = description
        self.id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else: raise ValueError("Genre name must be a non-empty string.")

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str) and description:
            self._description = description
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS genres
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO genres (name, description)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.description))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, description):
        genre = cls(name, description)
        genre.save()
        return genre
    
    @classmethod
    def instance_from_db(cls, row):
        genre = cls.all.get(row[0])
        if genre:
            genre.name = row[1]
            genre.description = row[2]
        else:
            genre = cls(row[1], row[2])
            genre.id = row[0]
            cls.all[genre.id] = genre
        return genre
    
    

    