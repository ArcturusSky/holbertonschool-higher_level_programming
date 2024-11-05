# MySQL - Main COMMANDS full list

This document will hold a full list of commands and their subqueries for easy finding with `ctrl+f`

## Summary

- [MySQL - Main COMMANDS full list](#mysql---main-commands-full-list)
  - [Summary](#summary)
  - [Introduction to MySQL](#introduction-to-mysql)
  - [CREATE](#create)
    - [CREATE DATABASE](#create-database)
    - [CREATE TABLE](#create-table)
      - [Basic table creation](#basic-table-creation)
      - [Table creation with constraints](#table-creation-with-constraints)
      - [Create table from another table](#create-table-from-another-table)
    - [CREATE INDEX](#create-index)
      - [Basic index](#basic-index)
      - [Unique index](#unique-index)
      - [Fulltext index](#fulltext-index)
    - [CREATE VIEW](#create-view)
    - [CREATE PROCEDURE](#create-procedure)
    - [CREATE FUNCTION](#create-function)
    - [CREATE TRIGGER](#create-trigger)
    - [CREATE USER](#create-user)
    - [CREATE ROLE](#create-role)
  - [SHOW](#show)
    - [SHOW databases](#show-databases)
    - [SHOW tables](#show-tables)
    - [SHOW columns](#show-columns)
    - [SHOW create table](#show-create-table)
    - [SHOW index](#show-index)
    - [SHOW table status](#show-table-status)
    - [SHOW processlist](#show-processlist)
    - [SHOW variables](#show-variables)
    - [SHOW status](#show-status)
    - [SHOW grants](#show-grants)
    - [SHOW engines](#show-engines)
    - [SHOW warnings](#show-warnings)
    - [SHOW errors](#show-errors)
    - [SHOW character set](#show-character-set)
    - [SHOW collation](#show-collation)
  - [INSERT](#insert)
    - [Basic INSERT](#basic-insert)
    - [INSERT Multiple Rows](#insert-multiple-rows)
    - [INSERT with SELECT](#insert-with-select)
    - [INSERT IGNORE](#insert-ignore)
    - [INSERT with ON DUPLICATE KEY UPDATE](#insert-with-on-duplicate-key-update)
    - [INSERT with SET](#insert-with-set)
    - [INSERT with Subquery](#insert-with-subquery)
    - [INSERT with DEFAULT VALUES](#insert-with-default-values)
    - [INSERT with RETURNING (MySQL 8.0.19+)](#insert-with-returning-mysql-8019)
    - [INSERT with JSON (MySQL 5.7+)](#insert-with-json-mysql-57)
    - [Batch INSERT](#batch-insert)
    - [INSERT with DELAYED (deprecated in MySQL 5.6)](#insert-with-delayed-deprecated-in-mysql-56)
  - [SELECT](#select)
    - [Basic SELECT](#basic-select)
    - [SELECT Specific Columns](#select-specific-columns)
    - [SELECT with WHERE Clause](#select-with-where-clause)
    - [SELECT with ORDER BY](#select-with-order-by)
    - [SELECT with LIMIT](#select-with-limit)
    - [SELECT with OFFSET](#select-with-offset)
    - [SELECT with DISTINCT](#select-with-distinct)
    - [SELECT with Aggregate Functions](#select-with-aggregate-functions)
    - [SELECT with GROUP BY](#select-with-group-by)
    - [SELECT with HAVING](#select-with-having)
    - [SELECT with JOIN](#select-with-join)
    - [SELECT with Subquery](#select-with-subquery)
    - [SELECT with UNION](#select-with-union)
    - [SELECT with CASE](#select-with-case)
    - [SELECT with Wildcard](#select-with-wildcard)
    - [SELECT with Regular Expressions](#select-with-regular-expressions)
    - [SELECT with EXISTS](#select-with-exists)
    - [SELECT with Window Functions (MySQL 8.0+)](#select-with-window-functions-mysql-80)
    - [SELECT with JSON Operations (MySQL 5.7+)](#select-with-json-operations-mysql-57)
  - [ALTER](#alter)
    - [ALTER TABLE ADD COLUMN](#alter-table-add-column)
    - [ALTER TABLE DROP COLUMN](#alter-table-drop-column)
    - [ALTER TABLE MODIFY COLUMN](#alter-table-modify-column)
    - [ALTER TABLE CHANGE COLUMN](#alter-table-change-column)
    - [ALTER TABLE ADD PRIMARY KEY](#alter-table-add-primary-key)
    - [ALTER TABLE DROP PRIMARY KEY](#alter-table-drop-primary-key)
    - [ALTER TABLE ADD FOREIGN KEY](#alter-table-add-foreign-key)
    - [ALTER TABLE DROP FOREIGN KEY](#alter-table-drop-foreign-key)
    - [ALTER TABLE RENAME](#alter-table-rename)
    - [ALTER TABLE ENGINE](#alter-table-engine)
    - [ALTER TABLE ADD INDEX](#alter-table-add-index)
    - [ALTER TABLE CHARACTER SET](#alter-table-character-set)
    - [ALTER DATABASE](#alter-database)
    - [ALTER VIEW](#alter-view)
    - [ALTER TABLE PARTITION](#alter-table-partition)
  - [UPDATE](#update)
    - [Basic UPDATE](#basic-update)
    - [UPDATE with Subquery](#update-with-subquery)
    - [UPDATE with JOIN](#update-with-join)
    - [UPDATE with Subquery in WHERE](#update-with-subquery-in-where)
    - [UPDATE with Multiple Tables](#update-with-multiple-tables)
    - [UPDATE with ORDER BY](#update-with-order-by)
    - [UPDATE with LIMIT](#update-with-limit)
    - [UPDATE with CASE](#update-with-case)
    - [UPDATE with Correlated Subquery](#update-with-correlated-subquery)
    - [UPDATE with EXISTS](#update-with-exists)
    - [UPDATE with JOIN and Subquery](#update-with-join-and-subquery)
    - [UPDATE with ON DUPLICATE KEY](#update-with-on-duplicate-key)
    - [UPDATE with JSON Operations (MySQL 5.7+)](#update-with-json-operations-mysql-57)
    - [UPDATE with Window Functions (MySQL 8.0+)](#update-with-window-functions-mysql-80)
    - [UPDATE with Table Alias](#update-with-table-alias)
  - [DELETE](#delete)
    - [Basic DELETE](#basic-delete)
    - [DELETE with WHERE Clause](#delete-with-where-clause)
    - [DELETE with ORDER BY and LIMIT](#delete-with-order-by-and-limit)
    - [DELETE with Subquery](#delete-with-subquery)
    - [DELETE with JOIN](#delete-with-join)
    - [DELETE with TRUNCATE](#delete-with-truncate)
    - [DELETE with Partitioning](#delete-with-partitioning)
    - [DELETE with RETURNING (MySQL 8.0.19+)](#delete-with-returning-mysql-8019)
    - [DELETE with Subsubquery](#delete-with-subsubquery)
    - [DELETE with Transaction](#delete-with-transaction)
  - [DROP](#drop)
    - [DROP TABLE](#drop-table)
    - [DROP DATABASE](#drop-database)
    - [DROP VIEW](#drop-view)
    - [DROP INDEX](#drop-index)
    - [DROP PROCEDURE](#drop-procedure)
    - [DROP FUNCTION](#drop-function)
    - [DROP TRIGGER](#drop-trigger)
    - [DROP USER](#drop-user)
    - [DROP ROLE](#drop-role)
    - [DROP TEMPORARY TABLE](#drop-temporary-table)
    - [DROP TABLE IF EXISTS](#drop-table-if-exists)
    - [DROP FOREIGN KEY](#drop-foreign-key)
    - [DROP PRIMARY KEY](#drop-primary-key)
    - [DROP COLUMN](#drop-column)
    - [DROP PARTITION](#drop-partition)
  - [JOIN](#join)
    - [Basic JOIN](#basic-join)
    - [LEFT JOIN](#left-join)
    - [RIGHT JOIN](#right-join)
    - [FULL JOIN](#full-join)
    - [JOIN with WHERE Clause](#join-with-where-clause)
    - [JOIN with Subquery](#join-with-subquery)
    - [JOIN with Multiple Tables](#join-with-multiple-tables)
    - [JOIN with USING Clause](#join-with-using-clause)
    - [JOIN with CROSS JOIN](#join-with-cross-join)
    - [JOIN with NATURAL JOIN](#join-with-natural-join)
    - [JOIN with OUTER JOIN](#join-with-outer-join)
    - [JOIN with LATERAL Subquery (MySQL 8.0+)](#join-with-lateral-subquery-mysql-80)
    - [JOIN with Window Functions (MySQL 8.0+)](#join-with-window-functions-mysql-80)
    - [JOIN with JSON Operations (MySQL 5.7+)](#join-with-json-operations-mysql-57)
  - [AGGREGATE FUNCTIONS](#aggregate-functions)
    - [COUNT()](#count)
    - [SUM()](#sum)
    - [AVG()](#avg)
    - [MAX()](#max)
    - [MIN()](#min)
    - [GROUP\_CONCAT()](#group_concat)
    - [DISTINCT with Aggregate Functions](#distinct-with-aggregate-functions)
    - [Aggregate Functions with GROUP BY](#aggregate-functions-with-group-by)
    - [Aggregate Functions with HAVING](#aggregate-functions-with-having)
    - [Aggregate Functions with JOIN](#aggregate-functions-with-join)
    - [Aggregate Functions with Subquery](#aggregate-functions-with-subquery)
    - [Multiple Aggregate Functions](#multiple-aggregate-functions)
    - [Aggregate Functions with CASE](#aggregate-functions-with-case)
    - [Aggregate Functions with Window Functions (MySQL 8.0+)](#aggregate-functions-with-window-functions-mysql-80)
    - [Aggregate Functions with JSON (MySQL 5.7+)](#aggregate-functions-with-json-mysql-57)
  - [INDEXES](#indexes)
    - [Create an index](#create-an-index)
    - [Drop an index](#drop-an-index)
  - [Author(s)](#authors)
  - [P.S about Author](#ps-about-author)

## Introduction to MySQL

**Definition**
MySQL is an open-source relational database management system (RDBMS) that uses Structured Query Language (SQL) for managing and manipulating data.

## CREATE

The `CREATE` statement in MySQL is used to create new databases, tables, indexes, views, and other database objects.

### CREATE DATABASE

Creates a new database.

```sql
CREATE DATABASE database_name;
```

With conditions:

```sql
CREATE DATABASE IF NOT EXISTS database_name;
```

### CREATE TABLE

Creates a new table in the database.

#### Basic table creation

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

#### Table creation with constraints

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT CHECK (age >= 18),
    email VARCHAR(100) UNIQUE,
    grade FLOAT DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Create table from another table

```sql
CREATE TABLE new_table AS
SELECT column1, column2
FROM existing_table
WHERE condition;
```

### CREATE INDEX

Creates an index on a table.

#### Basic index

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

#### Unique index

```sql
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);
```

#### Fulltext index

```sql
CREATE FULLTEXT INDEX index_name
ON table_name (column1, column2, ...);
```

### CREATE VIEW

Creates a virtual table based on the result of a SELECT statement.

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### CREATE PROCEDURE

Creates a stored procedure.

```sql
DELIMITER //

CREATE PROCEDURE procedure_name(IN parameter1 INT, OUT parameter2 VARCHAR(50))
BEGIN
    -- SQL statements
    SELECT column_name INTO parameter2 FROM table_name WHERE id = parameter1;
END //

DELIMITER ;
```

### CREATE FUNCTION

Creates a stored function.

```sql
DELIMITER //

CREATE FUNCTION function_name(param1 INT, param2 INT) 
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE result INT;
    -- SQL statements
    SET result = param1 + param2;
    RETURN result;
END //

DELIMITER ;
```

### CREATE TRIGGER

Creates a trigger that activates when a specified event occurs in a table.

```sql
DELIMITER //

CREATE TRIGGER trigger_name
BEFORE INSERT ON table_name
FOR EACH ROW
BEGIN
    -- SQL statements
    SET NEW.column1 = UPPER(NEW.column1);
END //

DELIMITER ;
```

### CREATE USER

Creates a new MySQL user account.

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

### CREATE ROLE

Creates a new role (available in MySQL 8.0 and later).

```sql
CREATE ROLE 'role_name';
```


## SHOW

The `SHOW` statement in MySQL is used to display information about databases, tables, columns, and server status information.

### SHOW databases

Lists all databases on the MySQL server.

```sql
SHOW DATABASES;
```

### SHOW tables

Lists all tables in the current database.

```sql
SHOW TABLES;
```

### SHOW columns

Displays information about the columns in a table.

```sql
SHOW COLUMNS FROM table_name;
```

Alternative syntax:

```sql
DESCRIBE table_name;
```

### SHOW create table

Shows the CREATE TABLE statement that created the table.

```sql
SHOW CREATE TABLE table_name;
```

### SHOW index

Displays information about indexes on a table.

```sql
SHOW INDEX FROM table_name;
```

### SHOW table status

Provides information about the table, including engine type, row format, and more.

```sql
SHOW TABLE STATUS WHERE Name = 'table_name';
```

### SHOW processlist

Shows you which threads are running.

```sql
SHOW PROCESSLIST;
```

### SHOW variables

Displays system variables and their values.

```sql
SHOW VARIABLES;
```

To SHOW a specific variable:

```sql
SHOW VARIABLES LIKE 'max_connections';
```

### SHOW status

Provides server status information.

```sql
SHOW STATUS;
```

To SHOW specific status variables:

```sql
SHOW STATUS LIKE 'Threads%';
```

### SHOW grants

Shows the privileges granted to a user.

```sql
SHOW GRANTS FOR 'username'@'localhost';
```

### SHOW engines

Lists all available storage engines.

```sql
SHOW ENGINES;
```

### SHOW warnings

Displays information about the conditions (errors, warnings, and notes) from the previous statement.

```sql
SHOW WARNINGS;
```

### SHOW errors

Similar to SHOW WARNINGS, but only displays errors.

```sql
SHOW ERRORS;
```

### SHOW character set

Shows all available character sets.

```sql
SHOW CHARACTER SET;
```

### SHOW collation

Displays all available collations.

```sql
SHOW COLLATION;
```


## INSERT

The `INSERT` statement in MySQL is used to add new records (rows) to a table.

### Basic INSERT

Inserts a single row into a table.

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

### INSERT Multiple Rows

Inserts multiple rows in a single query.

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES 
    (value1, value2, value3, ...),
    (value1, value2, value3, ...),
    (value1, value2, value3, ...);
```

### INSERT with SELECT

Inserts data selected from another table.

```sql
INSERT INTO table1 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table2
WHERE condition;
```

### INSERT IGNORE

Ignores errors if you try to insert duplicate rows.

```sql
INSERT IGNORE INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

### INSERT with ON DUPLICATE KEY UPDATE

Updates existing row if a duplicate key is found, otherwise inserts a new row.

```sql
INSERT INTO table_name (id, column1, column2)
VALUES (1, 'value1', 'value2')
ON DUPLICATE KEY UPDATE
column1 = VALUES(column1),
column2 = VALUES(column2);
```

### INSERT with SET

An alternative syntax for INSERT, useful when you have many columns.

```sql
INSERT INTO table_name
SET column1 = value1,
    column2 = value2,
    column3 = value3;
```

### INSERT with Subquery

Inserts values based on a subquery.

```sql
INSERT INTO table1 (column1, column2)
SELECT column1, column2
FROM table2
WHERE condition;
```

### INSERT with DEFAULT VALUES

Inserts a row using default values for all columns.

```sql
INSERT INTO table_name
VALUES ();
```

### INSERT with RETURNING (MySQL 8.0.19+)

Inserts a row and returns values from the inserted row.

```sql
INSERT INTO table_name (column1, column2)
VALUES ('value1', 'value2')
RETURNING id, column1, column2;
```

### INSERT with JSON (MySQL 5.7+)

Inserts JSON data into a JSON column.

```sql
INSERT INTO table_name (json_column)
VALUES ('{"key1": "value1", "key2": "value2"}');
```

### Batch INSERT

For better performance when inserting large amounts of data.

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES 
    (value1, value2, value3),
    (value4, value5, value6),
    (value7, value8, value9),
    ...
    (valueN-2, valueN-1, valueN);
```

### INSERT with DELAYED (deprecated in MySQL 5.6)

Used to insert rows in a non-blocking way (not supported for all storage engines).

```sql
INSERT DELAYED INTO table_name (column1, column2)
VALUES (value1, value2);
```


## SELECT

The `SELECT` statement in MySQL is used to retrieve data from one or more tables.

### Basic SELECT

Retrieves all columns from a table.

```sql
SELECT * FROM table_name;
```

### SELECT Specific Columns

Retrieves only specified columns.

```sql
SELECT column1, column2 FROM table_name;
```

### SELECT with WHERE Clause

Filters rows based on a condition.

```sql
SELECT column1, column2 FROM table_name
WHERE condition;
```

### SELECT with ORDER BY

Sorts the result set in ascending or descending order.

```sql
SELECT column1, column2 FROM table_name
ORDER BY column1 ASC, column2 DESC;
```

### SELECT with LIMIT

Limits the number of rows returned.

```sql
SELECT column1, column2 FROM table_name
LIMIT 10;
```

### SELECT with OFFSET

Skips a specified number of rows before starting to return rows.

```sql
SELECT column1, column2 FROM table_name
LIMIT 10 OFFSET 20;
```

### SELECT with DISTINCT

Removes duplicate rows from the result set.

```sql
SELECT DISTINCT column1 FROM table_name;
```

### SELECT with Aggregate Functions

Uses functions like COUNT, SUM, AVG, MAX, MIN.

```sql
SELECT COUNT(*), AVG(column1), MAX(column2) FROM table_name;
```

### SELECT with GROUP BY

Groups rows that have the same values in specified columns.

```sql
SELECT column1, COUNT(*) FROM table_name
GROUP BY column1;
```

### SELECT with HAVING

Specifies a search condition for a group or an aggregate.

```sql
SELECT column1, COUNT(*) FROM table_name
GROUP BY column1
HAVING COUNT(*) > 5;
```

### SELECT with JOIN

Combines rows from two or more tables based on a related column between them.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.id;
```

### SELECT with Subquery

Uses a query within another query.

```sql
SELECT column1 FROM table1
WHERE column2 IN (SELECT column2 FROM table2);
```

### SELECT with UNION

Combines the result set of two or more SELECT statements.

```sql
SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;
```

### SELECT with CASE

Performs if-then-else logic in a SELECT statement.

```sql
SELECT column1,
       CASE
           WHEN condition1 THEN result1
           WHEN condition2 THEN result2
           ELSE result3
       END AS new_column
FROM table_name;
```

### SELECT with Wildcard

Uses the LIKE operator for pattern matching.

```sql
SELECT * FROM table_name
WHERE column1 LIKE 'a%';
```

### SELECT with Regular Expressions

Uses REGEXP for more complex pattern matching.

```sql
SELECT * FROM table_name
WHERE column1 REGEXP '^[a-d]';
```

### SELECT with EXISTS

Tests for the existence of rows that satisfy a subquery.

```sql
SELECT column1 FROM table1
WHERE EXISTS (SELECT 1 FROM table2 WHERE table2.id = table1.id);
```

### SELECT with Window Functions (MySQL 8.0+)

Performs calculations across a set of rows that are related to the current row.

```sql
SELECT column1,
       ROW_NUMBER() OVER (ORDER BY column2) AS row_num
FROM table_name;
```

### SELECT with JSON Operations (MySQL 5.7+)

Extracts or manipulates JSON data.

```sql
SELECT JSON_EXTRACT(json_column, '$.key') AS extracted_value
FROM table_name;
```

## ALTER

The ALTER statement in MySQL is used to modify the structure of existing database objects.

### ALTER TABLE ADD COLUMN

Adds a new column to an existing table.

```sql
ALTER TABLE table_name
ADD COLUMN column_name datatype;
```

### ALTER TABLE DROP COLUMN

Removes a column from an existing table.

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

### ALTER TABLE MODIFY COLUMN

Changes the data type of an existing column.

```sql
ALTER TABLE table_name
MODIFY COLUMN column_name new_datatype;
```

### ALTER TABLE CHANGE COLUMN

Renames a column and changes its data type.

```sql
ALTER TABLE table_name
CHANGE COLUMN old_name new_name new_datatype;
```

### ALTER TABLE ADD PRIMARY KEY

Adds a primary key constraint to an existing table.

```sql
ALTER TABLE table_name
ADD PRIMARY KEY (column_name);
```

### ALTER TABLE DROP PRIMARY KEY

Removes the primary key constraint from a table.

```sql
ALTER TABLE table_name
DROP PRIMARY KEY;
```

### ALTER TABLE ADD FOREIGN KEY

Adds a foreign key constraint to an existing table.

```sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name
FOREIGN KEY (column_name) REFERENCES referenced_table(referenced_column);
```

### ALTER TABLE DROP FOREIGN KEY

Removes a foreign key constraint from a table.

```sql
ALTER TABLE table_name
DROP FOREIGN KEY constraint_name;
```

### ALTER TABLE RENAME

Renames an existing table.

```sql
ALTER TABLE old_table_name
RENAME TO new_table_name;
```

### ALTER TABLE ENGINE

Changes the storage engine of a table.

```sql
ALTER TABLE table_name
ENGINE = InnoDB;
```

### ALTER TABLE ADD INDEX

Adds an index to an existing table.

```sql
ALTER TABLE table_name
ADD INDEX index_name (column1, column2);
```

### ALTER TABLE CHARACTER SET

Changes the default character set of a table.

```sql
ALTER TABLE table_name
CHARACTER SET = utf8mb4;
```

### ALTER DATABASE

Modifies database properties.

```sql
ALTER DATABASE database_name
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;
```

### ALTER VIEW

Modifies the definition of an existing view.

```sql
ALTER VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

### ALTER TABLE PARTITION

Modifies table partitioning.

```sql
ALTER TABLE table_name
PARTITION BY RANGE (column_name) (
    PARTITION p0 VALUES LESS THAN (1000),
    PARTITION p1 VALUES LESS THAN (2000),
    PARTITION p2 VALUES LESS THAN MAXVALUE
);
```

## UPDATE

The `UPDATE` statement in MySQL is used to modify existing records in a table.

### Basic UPDATE

Updates one or more columns of existing records.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

### UPDATE with Subquery

Uses a subquery to update records.

```sql
UPDATE students
SET grade = (SELECT AVG(grade) FROM students WHERE age = 20)
WHERE age = 20;
```

### UPDATE with JOIN

Combines the update with a join between tables.

```sql
UPDATE students s
JOIN enrollments e ON s.id = e.student_id
SET s.grade = s.grade + 5
WHERE e.course_id = 101;
```

### UPDATE with Subquery in WHERE

Uses a subquery in the WHERE clause to filter records.

```sql
UPDATE students
SET grade = grade + 5
WHERE id IN (SELECT student_id FROM enrollments WHERE course_id = 101);
```

### UPDATE with Multiple Tables

Updates multiple tables in a single statement.

```sql
UPDATE table1 t1, table2 t2
SET t1.column1 = t2.column1
WHERE t1.id = t2.id;
```

### UPDATE with ORDER BY

Orders the records before applying the update.

```sql
UPDATE table_name
SET column1 = value1
WHERE condition
ORDER BY column2;
```

### UPDATE with LIMIT

Limits the number of rows to be updated.

```sql
UPDATE table_name
SET column1 = value1
WHERE condition
LIMIT 10;
```

### UPDATE with CASE

Uses a CASE statement to determine the update value.

```sql
UPDATE students
SET grade = 
    CASE 
        WHEN grade < 60 THEN grade + 5
        WHEN grade >= 60 AND grade < 90 THEN grade + 2
        ELSE grade
    END
WHERE course_id = 101;
```

### UPDATE with Correlated Subquery

Uses a correlated subquery to update records.

```sql
UPDATE students s
SET grade = (SELECT AVG(grade) 
             FROM students s2 
             WHERE s2.age = s.age)
WHERE age > 18;
```

### UPDATE with EXISTS

Uses EXISTS to update records based on the existence of related records.

```sql
UPDATE students
SET grade = grade + 5
WHERE EXISTS (SELECT 1 FROM honor_roll WHERE honor_roll.student_id = students.id);
```

### UPDATE with JOIN and Subquery

Combines JOIN and subquery in an UPDATE statement.

```sql
UPDATE students s
JOIN enrollments e ON s.id = e.student_id
SET s.grade = (SELECT AVG(grade) FROM grades WHERE course_id = e.course_id)
WHERE e.course_id = 101;
```

### UPDATE with ON DUPLICATE KEY

Updates existing rows or inserts a new row if no matching row exists.

```sql
INSERT INTO students (id, name, grade)
VALUES (1, 'John Doe', 85)
ON DUPLICATE KEY UPDATE grade = grade + 5;
```

### UPDATE with JSON Operations (MySQL 5.7+)

Updates JSON data in a column.

```sql
UPDATE table_name
SET json_column = JSON_SET(json_column, '$.key', 'new_value')
WHERE condition;
```

### UPDATE with Window Functions (MySQL 8.0+)

Uses window functions in the SET clause of an UPDATE statement.

```sql
UPDATE students s
JOIN (
    SELECT id, 
           ROW_NUMBER() OVER (ORDER BY grade DESC) AS rank
    FROM students
) r ON s.id = r.id
SET s.rank = r.rank;
```

### UPDATE with Table Alias

Uses table alias in an UPDATE statement for better readability.

```sql
UPDATE students AS s
SET s.grade = s.grade + 5
WHERE s.age > 18;
```

## DELETE

The `DELETE` statement in MySQL is used to remove records from a table.

### Basic DELETE

Deletes all rows from a table.

```sql
DELETE FROM table_name;
```

### DELETE with WHERE Clause

Deletes rows based on a specific condition.

```sql
DELETE FROM table_name
WHERE condition;
```

### DELETE with ORDER BY and LIMIT

Deletes a specified number of rows, ordered by a column.

```sql
DELETE FROM table_name
ORDER BY column1 DESC
LIMIT 10;
```

### DELETE with Subquery

Deletes rows based on the result of a subquery.

```sql
DELETE FROM table1
WHERE column1 IN (SELECT column1 FROM table2 WHERE condition);
```

### DELETE with JOIN

Deletes rows from one table based on a condition in another table.

```sql
DELETE t1
FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.id
WHERE t2.column = value;
```

### DELETE with TRUNCATE

Deletes all rows from a table, resetting the auto-increment value.

```sql
TRUNCATE TABLE table_name;
```

### DELETE with Partitioning

Deletes rows from a partitioned table.

```sql
ALTER TABLE table_name
PARTITION BY RANGE (column1) (
    PARTITION p0 VALUES LESS THAN (10),
    PARTITION p1 VALUES LESS THAN (20),
    PARTITION p2 VALUES LESS THAN MAXVALUE
);

DELETE FROM table_name
WHERE column1 >= 10 AND column1 < 20;
```

### DELETE with RETURNING (MySQL 8.0.19+)

Deletes rows and returns values from the deleted rows.

```sql
DELETE FROM table_name
WHERE condition
RETURNING column1, column2;
```

### DELETE with Subsubquery

Deletes rows based on a subquery within a subquery.

```sql
DELETE FROM table1
WHERE column1 IN (
    SELECT column1
    FROM (
        SELECT column1
        FROM table2
        WHERE condition1
    ) as subquery
    WHERE condition2
);
```

### DELETE with Transaction

Performs a DELETE operation within a transaction.

```sql
START TRANSACTION;
DELETE FROM table_name
WHERE condition;
COMMIT;
```

## DROP

The DROP statement in MySQL is used to remove database objects such as tables, databases, views, and more.

### DROP TABLE

Removes a table and all its data from the database.

```sql
DROP TABLE table_name;
```

### DROP DATABASE

Deletes an entire database and all its contents.

```sql
DROP DATABASE database_name;
```

### DROP VIEW

Removes a view from the database.

```sql
DROP VIEW view_name;
```

### DROP INDEX

Removes an index from a table.

```sql
DROP INDEX index_name ON table_name;
```

### DROP PROCEDURE

Removes a stored procedure from the database.

```sql
DROP PROCEDURE procedure_name;
```

### DROP FUNCTION

Removes a stored function from the database.

```sql
DROP FUNCTION function_name;
```

### DROP TRIGGER

Removes a trigger from the database.

```sql
DROP TRIGGER trigger_name;
```

### DROP USER

Removes a user account from the MySQL server.

```sql
DROP USER 'username'@'hostname';
```

### DROP ROLE

Removes a role from the database (MySQL 8.0+).

```sql
DROP ROLE role_name;
```

### DROP TEMPORARY TABLE

Removes a temporary table.

```sql
DROP TEMPORARY TABLE table_name;
```

### DROP TABLE IF EXISTS

Removes a table only if it exists, preventing errors if the table doesn't exist.

```sql
DROP TABLE IF EXISTS table_name;
```

### DROP FOREIGN KEY

Removes a foreign key constraint from a table.

```sql
ALTER TABLE table_name
DROP FOREIGN KEY constraint_name;
```

### DROP PRIMARY KEY

Removes the primary key constraint from a table.

```sql
ALTER TABLE table_name
DROP PRIMARY KEY;
```

### DROP COLUMN

Removes a column from a table.

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

### DROP PARTITION

Removes one or more partitions from a partitioned table.

```sql
ALTER TABLE table_name
DROP PARTITION partition_name;
```

## JOIN

The `JOIN` clause in MySQL is used to combine rows from two or more tables based on a related column between them.

### Basic JOIN

Performs an INNER JOIN between two tables.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
INNER JOIN table2 t2
ON t1.id = t2.id;
```

### LEFT JOIN

Returns all rows from the left table and the matched rows from the right table.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
LEFT JOIN table2 t2
ON t1.id = t2.id;
```

### RIGHT JOIN

Returns all rows from the right table and the matched rows from the left table.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
RIGHT JOIN table2 t2
ON t1.id = t2.id;
```

### FULL JOIN

Returns all rows from both tables.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
FULL JOIN table2 t2
ON t1.id = t2.id;
```

### JOIN with WHERE Clause

Combines a JOIN with a filtering condition.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
INNER JOIN table2 t2
ON t1.id = t2.id
WHERE t1.column3 > 10;
```

### JOIN with Subquery

Uses a subquery in the JOIN condition.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
INNER JOIN (
    SELECT * FROM table2 WHERE column3 > 0
) t2
ON t1.id = t2.id;
```

### JOIN with Multiple Tables

Joins more than two tables.

```sql
SELECT t1.column1, t2.column2, t3.column3
FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.id
INNER JOIN table3 t3 ON t2.id = t3.id;
```

### JOIN with USING Clause

Uses the USING clause instead of ON to specify the join condition.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
INNER JOIN table2 t2
USING (id);
```

### JOIN with CROSS JOIN

Performs a Cartesian product between two tables.

```sql
SELECT *
FROM table1
CROSS JOIN table2;
```

### JOIN with NATURAL JOIN

Performs an inner join based on all columns with the same name in the two tables.

```sql
SELECT *
FROM table1
NATURAL JOIN table2;
```

### JOIN with OUTER JOIN

Combines LEFT, RIGHT, and FULL OUTER JOIN.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
FULL OUTER JOIN table2 t2
ON t1.id = t2.id;
```

### JOIN with LATERAL Subquery (MySQL 8.0+)

Uses a LATERAL subquery to reference columns from the outer query.

```sql
SELECT t1.column1, t2.column2
FROM table1 t1
CROSS JOIN LATERAL (
    SELECT * FROM table2 t2 WHERE t2.id = t1.id
) t2;
```

### JOIN with Window Functions (MySQL 8.0+)

Combines JOIN with window functions.

```sql
SELECT t1.column1, 
       ROW_NUMBER() OVER (PARTITION BY t1.column2) AS row_num
FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.id;
```

### JOIN with JSON Operations (MySQL 5.7+)

Extracts or manipulates JSON data in JOIN conditions.

```sql
SELECT t1.column1, JSON_EXTRACT(t2.json_column, '$.key') AS json_value
FROM table1 t1
INNER JOIN table2 t2 ON JSON_CONTAINS(t2.json_column, '"value"');
```

## AGGREGATE FUNCTIONS

Aggregate functions in MySQL perform calculations on a set of values and return a single result.

### COUNT()

Counts the number of rows or non-NULL values.

```sql
SELECT COUNT(*) FROM table_name;
SELECT COUNT(column_name) FROM table_name;
```

### SUM()

Calculates the sum of a set of values.

```sql
SELECT SUM(column_name) FROM table_name;
```

### AVG()

Calculates the average value of a set of values.

```sql
SELECT AVG(column_name) FROM table_name;
```

### MAX()

Returns the maximum value in a set of values.

```sql
SELECT MAX(column_name) FROM table_name;
```

### MIN()

Returns the minimum value in a set of values.

```sql
SELECT MIN(column_name) FROM table_name;
```

### GROUP_CONCAT()

Concatenates a set of strings.

```sql
SELECT GROUP_CONCAT(column_name) FROM table_name;
```

### DISTINCT with Aggregate Functions

Uses DISTINCT with aggregate functions to eliminate duplicate values before calculation.

```sql
SELECT COUNT(DISTINCT column_name) FROM table_name;
```

### Aggregate Functions with GROUP BY

Groups the result set by one or more columns.

```sql
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1;
```

### Aggregate Functions with HAVING

Specifies a search condition for a group or an aggregate.

```sql
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1 
HAVING COUNT(*) > 5;
```

### Aggregate Functions with JOIN

Uses aggregate functions in a JOIN query.

```sql
SELECT t1.column1, AVG(t2.column2)
FROM table1 t1
JOIN table2 t2 ON t1.id = t2.id
GROUP BY t1.column1;
```

### Aggregate Functions with Subquery

Uses aggregate functions in a subquery.

```sql
SELECT column1
FROM table1
WHERE column2 > (SELECT AVG(column2) FROM table1);
```

### Multiple Aggregate Functions

Uses multiple aggregate functions in a single query.

```sql
SELECT COUNT(*), AVG(column1), MAX(column2), MIN(column3)
FROM table_name;
```

### Aggregate Functions with CASE

Combines aggregate functions with CASE statements.

```sql
SELECT 
    SUM(CASE WHEN condition THEN 1 ELSE 0 END) as count_if
FROM table_name;
```

### Aggregate Functions with Window Functions (MySQL 8.0+)

Combines aggregate functions with window functions.

```sql
SELECT 
    column1,
    AVG(column2) OVER (PARTITION BY column1) as avg_per_group
FROM table_name;
```

### Aggregate Functions with JSON (MySQL 5.7+)

Uses aggregate functions with JSON data.

```sql
SELECT 
    JSON_OBJECTAGG(column1, column2) as json_result
FROM table_name;
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

## Author(s)

Anne-Cécile Besse (Arc) and A.I (NotDiamond)

## P.S about Author

Due to lack of time with projects, I don't have time anymore to write myself my course so now I'm using A.I to helps me provide a simple and concise course about the necessary notions.