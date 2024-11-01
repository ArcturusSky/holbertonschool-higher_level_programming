# MySQL - Introduction

This repository will holds all the projects and tasks about **MySQL**.

## Summary

- [MySQL - Introduction](#mysql---introduction)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [Introduction to MySQL](#introduction-to-mysql)
    - [Basic Syntax](#basic-syntax)
  - [Creating (CREATE DATABASE) a Database](#creating-create-database-a-database)
  - [Deleting (DROP DATABASE) a database](#deleting-drop-database-a-database)
  - [Inserting Data](#inserting-data)
    - [Basic Syntax](#basic-syntax-1)
  - [Querying Data](#querying-data)
    - [Basic Syntax](#basic-syntax-2)
  - [Updating Data](#updating-data)
    - [Basic Syntax](#basic-syntax-3)
  - [Deleting Data](#deleting-data)
    - [Basic Syntax](#basic-syntax-4)
  - [Joins](#joins)
    - [Basic Syntax](#basic-syntax-5)
  - [Aggregate Functions](#aggregate-functions)
    - [Basic Syntax](#basic-syntax-6)
  - [Indexes](#indexes)
    - [Basic Syntax](#basic-syntax-7)
  - [Conclusion](#conclusion)
  - [Author](#author)
  - [P.S about Author](#ps-about-author)

## Glossary


## Introduction to MySQL

**Definition**
MySQL is an open-source relational database management system (RDBMS) that uses Structured Query Language (SQL) for managing and manipulating data.

### Basic Syntax

To interact with MySQL, we use SQL commands. Let's start with a simple example:

*Example:*

```sql
SELECT first_name, last_name FROM customers WHERE age > 18;
```

**Explanations, breakdown of the example:**

- **SELECT**: This keyword specifies which columns we want to retrieve.
- **first_name, last_name**: These are the specific columns we're selecting.
- **FROM**: This keyword indicates which table we're querying.
- **customers**: This is the name of the table we're querying.
- **WHERE**: This keyword allows us to filter the results based on a condition.
- **age > 18**: This is the condition; we're only selecting customers over 18.

## Creating (CREATE DATABASE) a Database

**Definition**
A database in MySQL is a collection of tables that store related data.

*Example:*

```sql
CREATE DATABASE my_first_database;
```

## Deleting (DROP DATABASE) a database

**Definition:**
A database can be deleted of course by "dropping" it.

*Example:*

```sql
DROP DATABASE databasename;

**Explanations:**

- **CREATE DATABASE**: This command creates a new database.
- **my_first_database**: This is the name we're giving to our new database.
- **USE**: This command tells MySQL which database we want to work with.

## Creating Tables

**Definition**
Tables are structures within a database that store specific sets of data.

### Basic Syntax

*Example:*

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade FLOAT
);
```

**Explanations:**

- **CREATE TABLE**: This command creates a new table.
- **students**: This is the name we're giving to our new table.
- **id INT PRIMARY KEY AUTO_INCREMENT**: This creates a unique identifier for each row.
- **VARCHAR(50)**: This data type is for strings up to 50 characters long.
- **INT**: This data type is for whole numbers.
- **FLOAT**: This data type is for decimal numbers.

## Inserting Data

**Definition**
Inserting data means adding new rows of information to a table.

### Basic Syntax

*Example:*

```sql
INSERT INTO students (first_name, last_name, age, grade)
VALUES ('John', 'Doe', 18, 85.5);
```

**Explanations:**

- **INSERT INTO**: This command is used to add new data to a table.
- **students**: This is the name of the table we're inserting data into.
- **VALUES**: This keyword precedes the actual data we're inserting.

## Querying Data

**Definition**
Querying data means retrieving information from the database based on specific criteria.

### Basic Syntax

*Example:*

```sql
SELECT * FROM students WHERE grade > 80 ORDER BY last_name ASC;
```

**Explanations:**

- **SELECT ***: This selects all columns from the table.
- **FROM students**: This specifies which table we're querying.
- **WHERE grade > 80**: This filters for students with grades above 80.
- **ORDER BY last_name ASC**: This sorts the results by last name in ascending order.

## Updating Data

**Definition**
Updating data means modifying existing records in a table.

### Basic Syntax

*Example:*

```sql
UPDATE students
SET grade = 90.0
WHERE first_name = 'John' AND last_name = 'Doe';
```

**Explanations:**

- **UPDATE**: This keyword specifies that we're modifying existing data.
- **SET**: This keyword precedes the column and new value we're setting.
- **WHERE**: This clause determines which records will be updated.

## Deleting Data

**Definition**
Deleting data means removing specific records from a table.

### Basic Syntax

*Example:*

```sql
DELETE FROM students
WHERE grade < 60;
```

**Explanations:**

- **DELETE FROM**: This command is used to remove data from a table.
- **WHERE**: This clause specifies which records to delete.

## Joins

**Definition**
Joins allow us to combine rows from two or more tables based on a related column between them.

### Basic Syntax

*Example:*

```sql
SELECT students.first_name, students.last_name, courses.course_name
FROM students
INNER JOIN enrollments ON students.id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.id;
```

**Explanations:**

- **INNER JOIN**: This type of join returns records that have matching values in both tables.
- **ON**: This keyword is used to specify the condition for the join.

## Aggregate Functions

**Definition**
Aggregate functions perform a calculation on a set of values and return a single result.

### Basic Syntax

*Example:*

```sql
SELECT AVG(grade) as average_grade, MAX(grade) as highest_grade
FROM students;
```

**Explanations:**

- **AVG()**: This function calculates the average of a set of values.
- **MAX()**: This function returns the maximum value in a set.
- **as**: This keyword is used to give an alias to the result column.

## Indexes

**Definition**
An index is a data structure that improves the speed of data retrieval operations on a database table.

### Basic Syntax

*Example:*

```sql
CREATE INDEX idx_last_name
ON students (last_name);
```

**Explanations:**

- **CREATE INDEX**: This command creates a new index.
- **idx_last_name**: This is the name we're giving to our new index.
- **ON students (last_name)**: This specifies the table and column to index.


## Conclusion


## Author

Anne-Cécile Besse (Arc) and A.I (NotDiamond)

## P.S about Author

Due to lack of time with projects, I don't have time anymore to write myself the course about the documentation so now I'm using A.I to helps me provide a simple and concise course about the necessary notions.