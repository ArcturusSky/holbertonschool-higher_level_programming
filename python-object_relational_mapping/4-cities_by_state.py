#!/usr/bin/python3
"""
Script that lists all cities from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Allocate given arguments as variable to be easier to be understood
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connecting to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name)

    # Create a cursor object to interact with the database
    usedatabase = db.cursor()

    # Fetching all states from the database ordered by ID
    # starting only with "N"
    usedatabase.execute("""
                        SELECT cities.id, cities.name, states.name
                        FROM cities
                        LEFT JOIN states
                        ON cities.state_id = states.id
                        ORDER BY cities.id ASC
                        """,)

    # Get the result, a list of tuple with "cities.id"
    # and "cities.name", from the query above (SELECT * etc)
    cities_list = usedatabase.fetchall()

    # Print each line of the list
    for line in cities_list:
        print(line)

    # Closing cursor and connexion to database
    usedatabase.close()
    db.close()
