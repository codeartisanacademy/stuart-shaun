import sqlite3

def create_connection(db):
    connection = None
    try:
        connection = sqlite3.connect(db)
    except Exception as error:
        print('There is an error: ' + error )

    return connection

def insert_city(connection, name, population, country_id):
    if connection:
        insert_sql = "INSERT INTO cities(name, population, country) VALUES('{0}', {1}, {2})".format(name, population, country_id)

        cursor = connection.cursor()
        cursor.execute(insert_sql)
        connection.commit()
        # print(cursor.lastrowid)
        city = select_city(connection, cursor.lastrowid)
        return city
    else:
        print("No connection")

def select_city(connection, id):
    if connection:
        select_sql = "SELECT * FROM cities WHERE id={0}".format(id)
        cursor = connection.cursor()
        cursor.execute(select_sql)
        city = cursor.fetchone()
        return city
    else:
        print("No connection")

connection = create_connection('citydb.db')

with connection:
    new_city_name = input("Enter the city name: ")
    new_city_population = input("Enter the population for {0}: ".format(new_city_name))
    new_city_country = input("Enter the country id (1-3): ")

    city = insert_city(connection, new_city_name, int(new_city_population), int(new_city_country))

    print(city)

