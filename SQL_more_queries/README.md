# MySQL more queries

- [MySQL more queries](#mysql-more-queries)
  - [Creating MySQL Users](#creating-mysql-users)
  - [Granting Privileges in MySQL](#granting-privileges-in-mysql)
    - [Granting Privileges](#granting-privileges)
    - [Displaying User Privileges](#displaying-user-privileges)
    - [Revoking Privileges](#revoking-privileges)
  - [Primary Keys](#primary-keys)
  - [Foreign Keys](#foreign-keys)
  - [Constraints (NOT NULL and UNIQUE)](#constraints-not-null-and-unique)
    - [NOT NULL Constraint](#not-null-constraint)
    - [UNIQUE Constraint](#unique-constraint)
  - [Retrieving Data from Multiple Tables](#retrieving-data-from-multiple-tables)
  - [Subqueries](#subqueries)
  - [Joins](#joins)
    - [INNER JOIN](#inner-join)
    - [LEFT JOIN](#left-join)
    - [RIGHT JOIN](#right-join)
  - [Key Differences between the various JOIN commands:](#key-differences-between-the-various-join-commands)
  - [Union](#union)


## Creating MySQL Users

**Short Description/Explanation:**

Creating a new user in MySQL is essential for managing database access and permissions. It allows you to control who can access your databases and what they can do with them.

**Command Explanation:**

The `CREATE USER` command is used to create a new MySQL account. This is necessary when you want to:
- Set up different users for different applications
- Control access to your databases
- Implement security best practices by not using the root user
- Create users with specific permissions for specific tasks

**Basic Syntax:**

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

The `'host'` part specifies where the user can connect from:
- `'localhost'`: only from the same machine
- `'%'`: from any host
- Specific IP: from a specific address

**Concrete Example:**

```sql
-- Create a new user named 'john_doe' with the password 'SecurePassword123!'
CREATE USER 'john_doe'@'localhost' IDENTIFIED BY 'SecurePassword123!';
```

**Breakdown of the Example:**
- **`'john_doe'`**: The username for the new user
- **`'localhost'`**: The host from which the user can connect
- **`'SecurePassword123!'`**: The password for the user

## Granting Privileges in MySQL

**Privileges**
Privileges determine what a user can do with data in a database. They can include permissions to access, modify, delete, or execute specific operations.

**Types of Privileges**

* `SELECT`: Read data
* `INSERT`: Add new data
* `UPDATE`: Modify existing data
* `DELETE`: Delete data
* `CREATE`: Create new databases and tables
* `DROP`: Delete existing databases and tables
* `ALTER`: Modify the structure of existing tables
* `EXECUTE`: Execute stored procedures
* `GRANT OPTION`: Transfer privileges to other users
* `REFERENCES`: Create foreign keys
* `USAGE`: Connect to a database without additional privileges
* `ALL PRIVILEGES`: Have all available privileges on a database or table

### Granting Privileges

```sql
GRANT privilege_type ON database_name.table_name TO 'username'@'host';
```

**Concrete Example:**

```sql
-- Grant SELECT privilege on the 'mydatabase' database to the user 'john_doe'
GRANT SELECT ON mydatabase.* TO 'john_doe'@'localhost';

-- Grant ALL privileges on the 'mydatabase' database to the user 'john_doe'
GRANT ALL PRIVILEGES ON mydatabase.* TO 'john_doe'@'localhost';
```

**Breakdown of the Example:**
- **`SELECT`**: The privilege type being granted
- **`mydatabase`**: The database on which the privilege is being granted
- **`john_doe`**: The user to whom the privilege is being granted
- **`ALL PRIVILEGES`**: Grants all privileges on the database

### Displaying User Privileges

```sql
SHOW GRANTS FOR 'username'@'host';
```

**Example:**

```sql
SHOW GRANTS FOR 'john_doe'@'localhost';
```

This will display the privileges of the user `'john_doe'@'localhost'`.

### Revoking Privileges

```sql
REVOKE privilege_type ON database_name.table_name FROM 'username'@'host';
```

**Example:**

```sql
REVOKE SELECT ON mydatabase.* FROM 'john_doe'@'localhost';
```

This will revoke the `SELECT` privilege on the mydatabase database from the user `'john_doe'@'localhost'`.

## Primary Keys

[Course dedicated to Keys and their relationships](https://github.com/ArcturusSky/holbertonschool-higher_level_programming/blob/main/SQL-more-queries/PRIMARY_AND_FOREIGN_KEYS.md)

**Short Description/Explanation:**

A primary key is a column or a combination of columns that uniquely identifies each row in a table. It ensures data integrity by preventing duplicate values.

**Command Explanation:**

The `PRIMARY KEY` constraint is used to define which column(s) will serve as the primary key. This is essential for maintaining unique identifiers for each row.

**Basic Syntax:**

```sql
CREATE TABLE table_name (
    column1 data_type PRIMARY KEY,
    column2 data_type
);
```

**Concrete Example:**

```sql
-- Create a table named 'users' with a primary key on the 'user_id' column
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);
```


**Breakdown of the Example:**
- **`user_id`**: The column that will serve as the primary key
- **`INT'`**: The data type of the primary key column
- **`username`** and **`email`**: Additional columns in the table

## Foreign Keys

**Short Description/Explanation:**

A foreign key creates a relationship between two tables by referencing the primary key of another table. This ensures referential integrity and prevents actions that would destroy links between tables.

**Command Explanation:**

The `FOREIGN KEY` constraint is used to establish relationships between tables. This is crucial for maintaining data consistency across related tables.

**Basic Syntax:**

```sql
CREATE TABLE table_name (
    column1 data_type,
    column2 data_type,
    FOREIGN KEY (column1) REFERENCES other_table(other_column)
);
```

**Concrete Example:**

```sql
-- Create a table named 'orders' with a foreign key referencing the 'users' table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

**Breakdown of the Example:**
- **`user_id`**: The foreign key column in the `orders` table
- **`INT`**: The data type of the foreign key column
- **`REFERENCES users(user_id)`**: Establishes the relationship with the 'users' table

## Constraints (NOT NULL and UNIQUE)

### NOT NULL Constraint

**Short Description/Explanation:**

The `NOT NULL` constraint ensures that a column cannot contain `NULL` values. This is useful for ensuring that critical data fields are always populated.

**Command Explanation:**

The `NOT NULL` constraint is applied to columns that must always have a value. This prevents `NULL` values from being inserted into these columns.

**Basic Syntax:**

```sql
CREATE TABLE table_name (
    column1 data_type NOT NULL,
    column2 data_type
);
```

**Concrete Example:**

```sql
-- Create a table named 'employees' with a NOT NULL constraint on the 'first_name' column
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100)
);
```

**Breakdown of the Example:**
- **`first_name`**: The column with the NOT NULL constraint
- **`VARCHAR(50)`**: The data type of the column
- **`NOT NULL`**: Ensures the column always has a value

### UNIQUE Constraint

**Short Description/Explanation:**

The `UNIQUE` constraint ensures that all values in a column are different. This is useful for preventing duplicate entries in columns where uniqueness is required.

**Command Explanation:**
The `UNIQUE` constraint is applied to columns where each value must be unique. This prevents duplicate values from being inserted into these columns.

**Basic Syntax:**

```sql
CREATE TABLE table_name (
    column1 data_type UNIQUE,
    column2 data_type
);
```

**Concrete Example:**

```sql
-- Create a table named 'users' with a UNIQUE constraint on the 'username' column
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100)
);
```

**Breakdown of the Example:**
- **`username`**: The column with the UNIQUE constraint
- **`VARCHAR(50)`**: The data type of the column
- **`UNIQUE`**: Ensures all values in the column are different

## Retrieving Data from Multiple Tables

**Short Description/Explanation:**

Retrieving data from multiple tables involves **joining** tables based on related columns. This is essential for combining data from different tables to get a more comprehensive view.

**Command Explanation:**

The `JOIN` clause is used to **combine** rows from two or more tables based on a related column. This allows you to retrieve data that spans multiple tables.

**Basic Syntax:**

```sql
SELECT table1.column1, table2.column2
FROM table1
JOIN table2 ON table1.common_column = table2.common_column;
```

**Concrete Example:**

```sql
-- Retrieve usernames and order dates from 'users' and 'orders' tables
SELECT users.username, orders.order_date
FROM users
JOIN orders ON users.user_id = orders.user_id;
```

**Expected Output:**
A result set containing usernames and corresponding order dates.

**Breakdown of the Example:**
- **`users`** and **`orders`**: The tables being joined
- **`username`** and **`order_date`**: The columns being selected
- **`user_id`**: The common column used for the join

## Subqueries

**Short Description/Explanation:**

A **subquery** is a query nested inside another query. Subqueries are used to find data that depends on the result of another query.

**Command Explanation:**

**Subqueries** can be used in various contexts such as in the `WHERE` clause or as a derived table. They help in filtering or transforming data based on the results of another query.

**Basic Syntax:**

```sql
SELECT column1, column2
FROM table1
WHERE column3 = (SELECT column4 FROM table2 WHERE condition);
```

**Concrete Example:**

```sql
-- Retrieve users with an order date later than the average order date
SELECT users.username, orders.order_date
FROM users
JOIN orders ON users.user_id = orders.user_id
WHERE orders.order_date > (SELECT AVG(order_date) FROM orders);
```

**Expected Output:**
A result set containing usernames and order dates that are later than the average order date.

**Breakdown of the Example:**
- **`users`** and **`orders`**: The tables being joined
- **`username`** and **`order_date`**: The columns being selected
- **`(SELECT AVG(order_date) FROM orders)`**: The subquery calculating the average order date

## Joins

### INNER JOIN

**Short Description/Explanation:**

An `INNER JOIN` returns records that have matching values in both tables. It is used to combine rows from two tables where there is a match.

**Command Explanation:**

The `INNER JOIN` clause is used to return records that have matching values in both tables. This is useful for retrieving data that exists in both tables.

**Basic Syntax:**

```sql
SELECT table1.column1, table2.column2
FROM table1
INNER JOIN table2 ON table1.common_column = table2.common_column;
```

**Concrete Example:**

```sql
-- Retrieve usernames and order dates from 'users' and 'orders' tables
SELECT users.username, orders.order_date
FROM users
INNER JOIN orders ON users.user_id = orders.user_id;
```

**Expected Output:**
A result set containing usernames and corresponding order dates.

**Breakdown of the Example:**
- **`users`** and **`orders`**: The tables being joined
- **`username`** and **`order_date`**: The columns being selected
- **`user_id`**: The common column used for the join

### LEFT JOIN

**Short Description/Explanation:**
A `LEFT JOIN` returns all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.

**Command Explanation:**
The `LEFT JOIN` clause is used to return all records from the left table and the matched records from the right table. This is useful when you need all records from one table and corresponding records from another, if available.

**Basic Syntax:**

```sql
SELECT table1.column1, table2.column2
FROM table1
LEFT JOIN table2 ON table1.common_column = table2.common_column;
```

**Concrete Example:**

```sql
-- Retrieve usernames and order dates from 'users' and 'orders' tables
SELECT users.username, orders.order_date
FROM users
LEFT JOIN orders ON users.user_id = orders.user_id;
```

**Expected Output:**
A result set containing all usernames from the 'users' table and corresponding order dates if available.

**Breakdown of the Example:**
- **`users`** and **`orders`**: The tables being joined
- **`username`** and **`order_date`**: The columns being selected
- **`user_id`**: The common column used for the join

### RIGHT JOIN

**Short Description/Explanation:**
A `RIGHT JOIN` returns all records from the right table and the matched records from the left table. If there is no match, the result is NULL on the left side.

**Command Explanation:**
The `RIGHT JOIN` clause is used to return all records from the right table and the matched records from the left table. This is useful when you need all records from one table and corresponding records from another, if available.

**Basic Syntax:**

```sql
SELECT table1.column1, table2.column2
FROM table1
RIGHT JOIN table2 ON table1.common_column = table2.common_column;
```

**Concrete Example:**

```sql
-- Retrieve usernames and order dates from 'users' and 'orders' tables
SELECT users.username, orders.order_date
FROM users
RIGHT JOIN orders ON users.user_id = orders.user_id;
```

**Expected Output:**
A result set containing all order dates from the 'orders' table and corresponding usernames if available.

**Breakdown of the Example:**
- **`users'`** and **`orders`**: The tables being joined
- **`username`** and **`order_date`**: The columns being selected
- **`user_id`**: The common column used for the join


## Key Differences between the various JOIN commands:

1. **INNER JOIN**
   - Only returns matched records
   - Excludes all unmatched records
   - Best for: Finding records that exist in both tables

2. **LEFT JOIN**
   - Returns all records from the left table
   - Returns matched records from the right table
   - Fills unmatched right table records with NULL
   - Best for: Getting all records from one table with optional matching records from another

3. **RIGHT JOIN**
   - Returns all records from the right table
   - Returns matched records from the left table
   - Fills unmatched left table records with NULL
   - Best for: Getting all records from one table with optional matching records from another (opposite direction of LEFT JOIN)

4. **FULL OUTER JOIN**
   - Returns all records from both tables
   - Fills unmatched records with NULL
   - Best for: Getting everything from both tables regardless of matches

## Union

**Short Description/Explanation:**
The `UNION` operator is used to combine the result sets of two or more `SELECT` statements. It removes duplicate rows by default.

**Command Explanation:**
The `UNION` operator combines two or more `SELECT` statements into a single result set. This is useful for merging data from different queries into one result set.

**Basic Syntax:**

```sql
SELECT column1, column2
FROM table1
UNION
SELECT column1, column2
FROM table2;
```

**Concrete Example:**

```sql
-- Combine usernames from 'active_users' and 'inactive_users' tables
SELECT username FROM active_users
UNION
SELECT username FROM inactive_users;
```

**Expected Output:**
A result set containing all unique usernames from both `active_users` and `inactive_users` tables.

**Breakdown of the Example:**
- **`active_users`** and **`inactive_users`**: The tables being combined
- **`username`**: The column being selected
- **`UNION`**: Combines the result sets of the two SELECT statements