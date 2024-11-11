#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Allocate given arguments as variable to be easier to be understood
    username = sys.argv(1)
    password = sys.argv(2)
    database_name = sys.argv(3)

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
    usedatabase.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Get the result, a list of tuple with states.id and states.names, of the query above (SELECT * etc)
    states_list = usedatabase.fetchall()

    # Print each line of the list 
    for line in states_list:
        print(line)

    # Closing cursor and connexion to database
    usedatabase.close()
    db.close()