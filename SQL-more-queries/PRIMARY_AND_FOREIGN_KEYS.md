# Primary Keys and Foreign Keys

This example demonstrates how to create a small school database system where we track students and their course enrollments.

**What are we going to do here:**

We'll create three interconnected tables:
1. Students table (to store student information)
2. Courses table (to store available courses)
3. Enrollments table (to track which students are enrolled in which courses)

**Concrete Code:**
```sql
-- Create the students table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- Create the courses table
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL
);

-- Create the enrollments table that connects students with courses
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- Insert sample data
INSERT INTO students (first_name, last_name, email) VALUES
('John', 'Doe', 'john.doe@email.com'),
('Jane', 'Smith', 'jane.smith@email.com');

INSERT INTO courses (course_name) VALUES
('Mathematics 101'),
('Computer Science 101');

INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2023-09-01'),  -- John enrolls in Mathematics
(1, 2, '2023-09-01'),  -- John enrolls in CS
(2, 1, '2023-09-02');  -- Jane enrolls in Mathematics
```

**Breakdown of the Code:**

1. **What we created:**
   - A students table where each student has a unique ID
   - A courses table where each course has a unique ID
   - An enrollments table that connects students to their courses

2. **How the keys work together:**
   - In the students table:
     * `student_id` is the primary key
     * It automatically increments (John gets ID 1, Jane gets ID 2)
     * Email must be unique (prevents duplicate student registrations)

   - In the courses table:
     * `course_id` is the primary key
     * Mathematics 101 gets ID 1
     * Computer Science 101 gets ID 2

   - In the enrollments table:
     * `enrollment_id` is its own primary key
     * `student_id` and `course_id` are foreign keys
     * Together they create a **many-to-many relationship**

3. **What the example achieves:**
   - John (`student_id` = 1) is enrolled in both:
     * Mathematics 101 (`course_id` = 1)
     * Computer Science 101 (`course_id` = 2)
   - Jane (`student_id` = 2) is enrolled in:
     * Mathematics 101 (`course_id` = 1) only

4. **Key behaviors demonstrated:**
   - If we delete John's student record:
     * `ON DELETE CASCADE` means his enrollment records are automatically deleted
     * This prevents orphaned enrollment records
   
   - If we try to delete Mathematics 101:
     * `ON DELETE RESTRICT` prevents deletion because students are enrolled
     * This protects against accidental data loss

5. **Practical use:**
   - We can easily find:
     * All courses a student is enrolled in
     * All students in a particular course
     * When each enrollment occurred
   
   Example query to see John's courses:
   ```sql
   SELECT courses.course_name, enrollments.enrollment_date
   FROM students
   JOIN enrollments ON students.student_id = enrollments.student_id
   JOIN courses ON enrollments.course_id = courses.course_id
   WHERE students.first_name = 'John';
   ```

# Relationship Tables and Keys

## Database Relationship Patterns

### 1. One-to-One Relationship
**Description:**
- One record in Table A relates to exactly one record in Table B
- Least common relationship type

**Example:**
```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50)
);

CREATE TABLE user_profiles (
    profile_id INT PRIMARY KEY,
    user_id INT UNIQUE,  -- Key to enforce one-to-one
    full_name VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

**Use Cases:**
- User and extended profile information
- Employee and employee details
- Passport and person information

### 2. One-to-Many Relationship
**Description:**
- One record in Table A can relate to multiple records in Table B
- Most common relationship type

**Example:**
```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    department_id INT,
    employee_name VARCHAR(100),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
```

**Use Cases:**
- One department, multiple employees
- One customer, multiple orders
- One author, multiple books

### 3. Many-to-Many Relationship
**Description:**
- Multiple records in Table A can relate to multiple records in Table B
- Requires a junction/relationship table

**Example:**
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

**Use Cases:**
- Students enrolled in multiple courses
- Actors in multiple movies
- Products in multiple categories

### 4. Self-Referencing Relationship
**Description:**
- A table has a relationship with itself
- Useful for hierarchical or tree-like structures

**Example:**
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
```

**Use Cases:**
- Organizational hierarchy
- Comment threads
- Category and subcategories
- Family tree relationships

### 5. Polymorphic Relationship (Advanced)
**Description:**
- A record can belong to multiple types of related records
- More complex, typically implemented in application logic

**Example Concept:**
```sql
CREATE TABLE comments (
    comment_id INT PRIMARY KEY,
    content TEXT,
    resource_type VARCHAR(50),  -- 'post', 'photo', 'video'
    resource_id INT
);
```

**Use Cases:**
- Commenting system across different entity types
- Tagging system
- Generic attachment mechanisms

### Relationship Pattern Cheat Sheet

| Pattern         | Table A | Table B | Junction Table | Key Characteristics |
|----------------|---------|---------|---------------|---------------------|
| One-to-One     | 1       | 1       | No            | UNIQUE Foreign Key  |
| One-to-Many    | 1       | Many    | No            | Foreign Key in Many |
| Many-to-Many   | Many    | Many    | Yes           | Composite Keys      |
| Self-Reference | Same    | Same    | No            | Self Foreign Key    |

**Choosing the Right Pattern:**
1. Understand your data relationships
2. Consider future scalability
3. Optimize for query performance
4. Maintain data integrity
5. Keep design as simple as possible

## The Three-Table Pattern (for Many to Many Relationships)

**Typical Structure:**
1. **First Table (Main Entity)**: 
   - Contains data about one type of entity (e.g., students)
   - Has a primary key (`student_id`)

2. **Second Table (Related Entity)**: 
   - Contains data about another type of entity (e.g., courses)
   - Has its own primary key (`course_id`)

3. **Relationship Table (Junction Table)**:
   - Contains foreign keys referencing both other tables
   - Captures the relationships between entities
   - Allows many-to-many relationships

**Concrete Example:**

```sql
-- Students Table (First Table)
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- Courses Table (Second Table)
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    department VARCHAR(50)
);

-- Enrollments Table (Relationship/Junction Table)
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

**Why This Pattern?**

1. **Many-to-Many Relationships**:
   - A student can enroll in multiple courses
   - A course can have multiple students
   - The relationship table tracks these connections

2. **Flexibility**:
   - Can add extra information about the relationship
   - In this case, we added an enrollment_date
   - Could also add things like grade, semester, etc.

3. **Data Integrity**:
   - Prevents duplicate or invalid relationships
   - Ensures referential integrity

**Real-World Analogies:**

- **Library System**:
  - Books Table
  - Members Table
  - Borrowing Table (tracks who borrowed which book)

- **E-commerce**:
  - Products Table
  - Customers Table
  - Orders Table (links products and customers)

**Common Relationship Types:**

1. **One-to-Many**:
   - One student can have many enrollments
   - One course can have many enrollments

2. **Many-to-Many**:
   - Many students can be in many courses
   - Resolved using the relationship table

3. **One-to-One**:
   - Less common, but possible
   - Use UNIQUE constraint on foreign key

**Best Practices:**
- Always use primary keys
- Use foreign keys to establish relationships
- Consider performance and indexing
- Keep relationship tables focused and clean