import sqlite3

connection = sqlite3.connect('citydb.db')

cursor = connection.cursor()

sql_select = 'SELECT * FROM cities'

cursor.execute(sql_select)

cities = cursor.fetchall()

print(cities)
for city in cities:
    print("{city} - {population}".format(city=city[1], population=city[2]))

id = input('Enter the id: ')

sql_select_one= 'SELECT * FROM cities WHERE id={0}'.format(id)

cursor.execute(sql_select_one)

city = cursor.fetchone()

print(city)

connection.close()