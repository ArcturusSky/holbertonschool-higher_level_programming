# MySQL - Introduction

This repository will holds all the projects and tasks about **MySQL**.

## Summary

- [MySQL - Introduction](#mysql---introduction)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [Introduction to MySQL](#introduction-to-mysql)
  - [CREATE DATABASE](#create-database)
    - [Create a simple database](#create-a-simple-database)
    - [Create a database with conditions](#create-a-database-with-conditions)
  - [CREATE TABLE](#create-table)
    - [Create a simple table](#create-a-simple-table)
    - [Create a table with constraints](#create-a-table-with-constraints)
  - [INSERT](#insert)
    - [Insert a single record](#insert-a-single-record)
    - [Insert multiple records](#insert-multiple-records)
  - [SELECT](#select)
    - [Select all columns](#select-all-columns)
    - [Select specific columns](#select-specific-columns)
    - [Select with conditions](#select-with-conditions)
  - [UPDATE](#update)
    - [Update a single record](#update-a-single-record)
    - [Update multiple records](#update-multiple-records)
  - [DELETE](#delete)
    - [Delete a single record](#delete-a-single-record)
    - [Delete multiple records](#delete-multiple-records)
  - [JOIN](#join)
    - [Inner join](#inner-join)
    - [Left join](#left-join)
  - [AGGREGATE FUNCTIONS](#aggregate-functions)
    - [Calculate average](#calculate-average)
    - [Calculate maximum](#calculate-maximum)
    - [Calculate minimum](#calculate-minimum)
  - [INDEXES](#indexes)
    - [Create an index](#create-an-index)
    - [Drop an index](#drop-an-index)
  - [Conclusion](#conclusion)
  - [Author](#author)
  - [P.S about Author](#ps-about-author)

## Glossary


## Introduction to MySQL

**Definition**
MySQL is an open-source relational database management system (RDBMS) that uses Structured Query Language (SQL) for managing and manipulating data.

## CREATE DATABASE

### Create a simple database

The `CREATE DATABASE` command is used to create a new database in MySQL.

```sql
CREATE DATABASE example_database;
```

### Create a database with conditions

Creating a database can have different conditions like:

- Creating if it doesn't exist:

```sql
CREATE DATABASE IF NOT EXISTS example_database;
```

## CREATE TABLE

### Create a simple table

The `CREATE TABLE` command is used to create a new table in the database.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade FLOAT
);
```

### Create a table with constraints

You can add constraints like NOT NULL and UNIQUE to ensure data integrity.

- Adding constraints:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    grade FLOAT,
    UNIQUE (first_name, last_name)
);
```

## INSERT

### Insert a single record

The `INSERT` command is used to add new rows of data to a table.

```sql
INSERT INTO students (first_name, last_name, age, grade)
VALUES ('John', 'Doe', 18, 85.5);
```

### Insert multiple records

You can insert multiple records at once by listing them in the VALUES clause.

```sql
INSERT INTO students (first_name, last_name, age, grade)
VALUES
    ('Jane', 'Smith', 20, 90.0),
    ('Alice', 'Johnson', 19, 88.5);
```

## SELECT

### Select all columns

The `SELECT` command is used to retrieve data from the database.

```sql
SELECT * FROM students;
```

### Select specific columns

You can specify which columns you want to retrieve.

```sql
SELECT first_name, last_name FROM students;
```

### Select with conditions

Use the `WHERE` clause to filter the results.

```sql
SELECT first_name, last_name FROM students WHERE age > 18;
```

## UPDATE

### Update a single record

The `UPDATE` command is used to modify existing records in a table.

```sql
UPDATE students
SET grade = 90.0
WHERE first_name = 'John' AND last_name = 'Doe';
```

### Update multiple records

You can update multiple records by using conditional statements.

```sql
UPDATE students
SET grade = grade + 5
WHERE grade < 80;
```

## DELETE

### Delete a single record

The `DELETE` command is used to remove records from a table.

```sql
DELETE FROM students
WHERE first_name = 'John' AND last_name = 'Doe';
```

### Delete multiple records

You can delete multiple records by using conditional statements.

```sql
DELETE FROM students
WHERE grade < 60;
```

## JOIN

### Inner join

The `INNER JOIN` command is used to combine rows from two or more tables based on a related column between them.

```sql
SELECT students.first_name, students.last_name, courses.course_name
FROM students
INNER JOIN enrollments ON students.id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.id;
```

### Left join

The `LEFT JOIN` command returns all records from the left table (students), and the matched records from the right table (enrollments). If there is no match, the result is NULL.

```sql
SELECT students.first_name, students.last_name, courses.course_name
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id
LEFT JOIN courses ON enrollments.course_id = courses.id;
```

## AGGREGATE FUNCTIONS

### Calculate average

The `AVG()` function calculates the average of a set of values.

```sql
SELECT AVG(grade) as average_grade
FROM students;
```

### Calculate maximum

The `MAX()` function returns the maximum value in a set.

```sql
SELECT MAX(grade) as highest_grade
FROM students;
```

### Calculate minimum

The `MIN()` function returns the minimum value in a set.

```sql
SELECT MIN(grade) as lowest_grade
FROM students;
```

## INDEXES

### Create an index

An index is a data structure that improves the speed of data retrieval operations.

```sql
CREATE INDEX idx_last_name
ON students (last_name);
```

### Drop an index

You can drop an index if it's no longer needed.

```sql
DROP INDEX idx_last_name
ON students;
```

## Conclusion


## Author

Anne-Cécile Besse (Arc) and A.I (NotDiamond)

## P.S about Author

Due to lack of time with projects, I don't have time anymore to write myself the course about the documentation so now I'm using A.I to helps me provide a simple and concise course about the necessary notions.