# Introduction to Python ORM

## Summary

- [Introduction to Python ORM](#introduction-to-python-orm)
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
  - [Parameterized Queries in Python with MySQLdb](#parameterized-queries-in-python-with-mysqldb)
    - [Introduction](#introduction)
    - [What Are Parameterized Queries?](#what-are-parameterized-queries)
    - [Why Use Parameterized Queries?](#why-use-parameterized-queries)
    - [Using Parameterized Queries with MySQLdb](#using-parameterized-queries-with-mysqldb)
      - [Basic Syntax](#basic-syntax)
        - [Example 1: Using Parameterized Queries with a Single Parameter](#example-1-using-parameterized-queries-with-a-single-parameter)
        - [Example 2: Using Multiple Parameters](#example-2-using-multiple-parameters)
    - [Why Use a Tuple or List?](#why-use-a-tuple-or-list)
    - [Key Points:](#key-points)
    - [Benefits of Parameterized Queries](#benefits-of-parameterized-queries)
    - [To sum up](#to-sum-up)
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

#### 1. Define a Python Class

Let’s create a Python class to represent a table (e.g., `User`) in the database:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

This class doesn't interact with the database yet; it's just a regular Python class with attributes (`name`, `age`). In ORM, this would typically be mapped to a database table.

---

#### 2. Insert Data into the Database

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

#### 3. Query Data from the Database

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

#### 4. Closing the Connection

Once we’re done with the database operations, it’s important to close the connection:

```python
# Close the cursor and database connection
cursor.close()
db.close()
```

---

#### Full Example: Putting It All Together

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

#### Breaking Down the Code:

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

## Parameterized Queries in Python with MySQLdb

### Introduction

When working with databases, it's crucial to ensure that your queries are safe and not vulnerable to **SQL injection attacks**. One of the best practices to avoid such attacks is to use **parameterized queries**. In this course, we will explore how to use parameterized queries with Python's MySQLdb module.

### What Are Parameterized Queries?

A parameterized query is a type of query where placeholders are used for values that are passed into the query at runtime. These placeholders are then replaced by actual values when the query is executed. This helps protect against SQL injection and ensures proper handling of input data.

In MySQLdb, parameterized queries are executed using placeholders like `%s` for all types of values (e.g., strings, integers). The actual values are passed as parameters.

### Why Use Parameterized Queries?

1. **Prevents SQL Injection**: 
   - If user inputs are directly inserted into SQL queries, attackers can manipulate the query by injecting malicious code. Parameterized queries ensure that user input is treated as data, not executable code.

2. **Improves Code Readability**: 
   - By using placeholders for parameters, your code is easier to read and maintain.

3. **Automatically Escapes Input**: 
   - Parameterized queries automatically escape special characters, ensuring that the input is safely passed to the database.

### Using Parameterized Queries with MySQLdb

In MySQLdb, you use the `cursor.execute()` method to execute SQL queries. To use parameters in a query, you need to use placeholders (`%s`) in the query string and pass the actual values as a tuple or list in the second argument to `execute()`.

#### Basic Syntax

The general syntax for a parameterized query in MySQLdb is:

```python
cursor.execute("""
    SELECT * 
    FROM table_name
    WHERE column_name = %s
""", (parameter_value,))
```

**Explanation:**
- `"%s"` is a placeholder for a parameter in the query.
- `(parameter_value,)` is a tuple containing the actual value that will replace the placeholder.

##### Example 1: Using Parameterized Queries with a Single Parameter

Let's start with a simple query that fetches a state by its name. The name will be passed as a parameter.

```python
import MySQLdb
import sys

if __name__ == "__main__":
    # Connecting to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user="username",
        passwd="password",
        db="database_name"
    )

    cursor = db.cursor()

    # Fetching a state by name using a parameterized query
    cursor.execute("""
        SELECT * 
        FROM states
        WHERE states.name = %s
    """, (sys.argv[1],))

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
```

**Explanation:**
- We connect to the MySQL database using `MySQLdb.connect()`.
- The query retrieves all rows from the `states` table where the state name matches the parameter passed (in this case, from `sys.argv[1]`).
- The parameter `sys.argv[1]` is passed as a tuple `(sys.argv[1],)` to ensure it is treated correctly.

##### Example 2: Using Multiple Parameters

You can use multiple placeholders (`%s`) if your query requires more than one parameter.

```python
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="username",
    passwd="password",
    db="database_name"
)

cursor = db.cursor()

# Fetching a state by name and ID using multiple parameters
cursor.execute("""
    SELECT * 
    FROM states
    WHERE states.name = %s AND states.id = %s
""", ("California", 5))

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
db.close()
```

**Explanation:**
- The query now has two placeholders: one for the state name and one for the state ID.
- We pass two values: `"California"` and `5`, as a tuple `("California", 5)`.

### Why Use a Tuple or List?

Even when you only have one parameter to pass, you should still use a tuple or list to ensure that the data is passed correctly. 

For example:
```python
cursor.execute("""
    SELECT * 
    FROM states
    WHERE states.name = %s
""", (sys.argv[1],))  # Passing a tuple with one item
```

Without the comma after `sys.argv[1]`, it would not be a tuple, and MySQLdb would not process it correctly.

### Key Points:
- A single parameter must still be passed as a tuple, e.g., `(value,)`.
- This allows MySQLdb to handle multiple parameters, even if there's only one.

### Benefits of Parameterized Queries

1. **Security**: 
   - Parameterized queries are secure and protect your application from SQL injection, as inputs are never directly concatenated into the SQL string.

2. **Data Integrity**: 
   - MySQLdb automatically handles data escaping and type conversion, ensuring that your input values are correctly interpreted by the database.

3. **Code Maintenance**: 
   - By using placeholders and passing values as parameters, your SQL queries remain clean and easier to modify later.

### To sum up

In this course, you learned how to use parameterized queries with Python's MySQLdb module. You learned that:
- Parameterized queries use placeholders (`%s`) for parameters.
- You must pass parameters as a tuple or list.
- Using parameterized queries prevents SQL injection and improves the security and readability of your code.

Always prefer parameterized queries over directly concatenating user inputs into SQL statements to ensure your database interactions are secure.

---

## Conclusion:

1. **ORM** helps you work with your database using Python objects instead of SQL queries.
2. **MySQLdb** is a way to connect Python to MySQL databases and execute queries.
3. In the example, you see how you can simulate ORM-like behavior using Python classes and manual SQL queries.

This is a very basic example, and real-world ORMs would involve more features, like relationships between tables (e.g., foreign keys), validations, and much more abstraction.