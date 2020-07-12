import sqlite3

class DB:

    def __init__(self, database):
        self.database = database
    
    def connect(self):
        connection = sqlite3.connect(self.database)
        if connection:
            return connection
        else:
            return None
        