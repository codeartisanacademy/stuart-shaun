import sqlite3

connection = sqlite3.connect('citydb.db')

cursor = connection.cursor()

sql_select = 'SELECT * FROM cities'

cursor.execute(sql_select)

cities = cursor.fetchall()

print(cities)
 
