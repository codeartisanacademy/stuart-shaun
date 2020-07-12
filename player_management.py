import DB
import Player

connection = DB.DB("playerdb.db")

jordan = Player.Player("Michael Jordan", "Point Guard", 23, "Chicago Bulls")
jordan.save(connection)

jordan.club = "Wizard"
jordan.update()