
class Player:

    def __init__(self, name, position, number, club ):
        self.name = name
        self.position = position
        self.number = number
        self.club = club

    def __str__(self):
        return self.name + " - " + self.club

    def save(self, connection):
        cursor = connection.cursor()
        insert = "INSERT INTO players (name, position, number, club) VALUES {0}, {1}, {2}, {3}".format(self.name, self.position, self.number, self.club)

        cursor.execute(insert)
        connection.commit()

        return cursor.lastrowid
    
    def select(self, connection, id):
        pass

    def select_all(self, connection):
        pass

    def update(self, connection):
        pass