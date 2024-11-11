# Introduction to Python ORM

## Summary

- [Introduction to Python ORM\*\*](#introduction-to-python-orm)
  - [Summary](#summary)
  - [Introduction to Python ORM with MySQLdb](#introduction-to-python-orm-with-mysqldb)
    - [What is ORM (Object-Relational Mapping)?](#what-is-orm-object-relational-mapping)
      - [Why Use ORM?](#why-use-orm)
    - [Steps to Install `MySQLdb`](#steps-to-install-mysqldb)
    - [Connecting to the Database](#connecting-to-the-database)
    - [Simple ORM Example: Using `MySQLdb`](#simple-orm-example-using-mysqldb)
    - [1. Define a Python Class](#1-define-a-python-class)
    - [2. Insert Data into the Database](#2-insert-data-into-the-database)
    - [3. Query Data from the Database](#3-query-data-from-the-database)
    - [4. Closing the Connection](#4-closing-the-connection)
    - [Full Example: Putting It All Together](#full-example-putting-it-all-together)
    - [Breaking Down the Code:](#breaking-down-the-code)
    - [Why This Is ORM-like:](#why-this-is-orm-like)
    - [Conclusion:](#conclusion)


## Introduction to Python ORM with MySQLdb

### What is ORM (Object-Relational Mapping)?

ORM is a technique that lets you interact with a database using **objects** (like Python classes and instances), instead of writing raw SQL queries. The idea is to "map" the database tables to Python classes. This way, instead of working with SQL directly, you can work with Python objects and attributes.

#### Why Use ORM?

1. **Abstraction**: You don't need to write SQL queries directly. You interact with the database using Python code.
2. **Portability**: You can switch databases easily, since your Python code is abstracted from the SQL syntax.
3. **Simplified Code**: Your code looks more like regular Python and can be easier to manage, especially as your project grows.

---

### Steps to Install `MySQLdb`

If you haven't already installed the `MySQLdb` library, you can install it by running:

```bash
pip install mysqlclient
```

---

### Connecting to the Database

Before using ORM, we need to understand how to connect to a MySQL database using Python:

```python
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user="root", passwd="your_password", db="your_db")

# Create a cursor object to interact with the database
cursor = db.cursor()
```

- `MySQLdb.connect`: This function connects Python to your MySQL database. You need to specify the host (server), user, password, and database name.
- `cursor()`: This is used to create a cursor object which allows you to execute SQL queries.

---

### Simple ORM Example: Using `MySQLdb`

We will simulate a simple ORM-like behavior by using classes in Python. Let’s create a `User` class that represents the data in a table and use it to interact with the database.

---

### 1. Define a Python Class

Let’s create a Python class to represent a table (e.g., `User`) in the database:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

This class doesn't interact with the database yet; it's just a regular Python class with attributes (`name`, `age`). In ORM, this would typically be mapped to a database table.

---

### 2. Insert Data into the Database

Now let's insert data into the database using the class. In a real ORM system, this would be handled automatically, but here we’ll show how to do it manually using `MySQLdb`:

```python
# Create a new User object
new_user = User("Alice", 25)

# Insert the user into the database
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (new_user.name, new_user.age))

# Commit the changes
db.commit()
```

- We created a `User` object (`new_user`) with the attributes `name` and `age`.
- The `cursor.execute()` function executes an SQL statement. We use placeholders (`%s`) to safely insert the values into the query to avoid SQL injection.
- `db.commit()` commits the transaction, saving the data to the database.

---

### 3. Query Data from the Database

Let’s retrieve the data from the `users` table:

```python
# Fetch all users from the database
cursor.execute("SELECT * FROM users")

# Get all rows from the query result
users = cursor.fetchall()

# Print the result
for user in users:
    print(f"User: {user[1]}, Age: {user[2]}")
```

- `cursor.execute("SELECT * FROM users")` executes the SQL query to get all users.
- `cursor.fetchall()` fetches all the rows returned by the query.
- We loop through the rows and print the results.

---

### 4. Closing the Connection

Once we’re done with the database operations, it’s important to close the connection:

```python
# Close the cursor and database connection
cursor.close()
db.close()
```

---

### Full Example: Putting It All Together

```python
import MySQLdb

# Step 1: Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="your_password", db="your_db")
cursor = db.cursor()

# Step 2: Define a simple User class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Step 3: Insert a new user into the database
new_user = User("Alice", 25)
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (new_user.name, new_user.age))
db.commit()

# Step 4: Fetch and print all users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
for user in users:
    print(f"User: {user[1]}, Age: {user[2]}")

# Step 5: Close the connection
cursor.close()
db.close()
```

---

### Breaking Down the Code:

1. **Connect to the Database**: 
   - We establish a connection to the MySQL database using `MySQLdb.connect()`.
   
2. **Define the `User` Class**: 
   - The `User` class defines the attributes (e.g., `name`, `age`) that represent a user in the database.
   
3. **Insert Data**:
   - We create a `User` object (`new_user`) and insert it into the `users` table using `cursor.execute()`.

4. **Fetch Data**:
   - We retrieve all rows from the `users` table and print the results.

5. **Close Connection**:
   - Finally, we close the cursor and the database connection.

---

### Why This Is ORM-like:

In this example, we're manually handling the database interaction. However, the `User` class in Python is intended to represent a record in the `users` table. Ideally, an ORM would manage this process more automatically by linking the class to the table and handling the data persistence without us needing to write the SQL queries directly.

This is just a simple simulation of how an ORM works. A more advanced ORM (like SQLAlchemy) would automate a lot of this for you, allowing you to work with Python objects rather than writing SQL queries.

---

### Conclusion:

1. **ORM** helps you work with your database using Python objects instead of SQL queries.
2. **MySQLdb** is a way to connect Python to MySQL databases and execute queries.
3. In the example, you see how you can simulate ORM-like behavior using Python classes and manual SQL queries.

This is a very basic example, and real-world ORMs would involve more features, like relationships between tables (e.g., foreign keys), validations, and much more abstraction.