# Refresh about Python Objets and going a bit further

- [Refresh about Python Objets and going a bit further](#refresh-about-python-objets-and-going-a-bit-further)
  - [What Are Objects and References?](#what-are-objects-and-references)
    - [Mutable vs Immutable Types](#mutable-vs-immutable-types)
  - [Working with References](#working-with-references)
    - [Aliasing](#aliasing)
    - [Cloning](#cloning)
  - [Collections in Python](#collections-in-python)
    - [Dictionaries and Keys](#dictionaries-and-keys)
    - [Lists vs Dictionaries](#lists-vs-dictionaries)
  - [Managing State in Python (Necessary here?)](#managing-state-in-python-necessary-here)
    - [Nonlocal Statements](#nonlocal-statements)
  - [Memory Management](#memory-management)
    - [Garbage Collection (Necessary here?)](#garbage-collection-necessary-here)
    - [Circular References and Solutions](#circular-references-and-solutions)
  - [Best Practices](#best-practices)
  - [Questions asked in the project:](#questions-asked-in-the-project)
    - [1. What is an object?](#1-what-is-an-object)
    - [2. What is the difference between a class and an object or instance?](#2-what-is-the-difference-between-a-class-and-an-object-or-instance)
    - [3. What is the difference between immutable object and mutable object?](#3-what-is-the-difference-between-immutable-object-and-mutable-object)
    - [4. What is a reference?](#4-what-is-a-reference)
    - [5. What is an assignment?](#5-what-is-an-assignment)
    - [6. What is an alias?](#6-what-is-an-alias)
    - [7. How to know if two variables are identical?](#7-how-to-know-if-two-variables-are-identical)
    - [8. How to know if two variables are linked to the same object?](#8-how-to-know-if-two-variables-are-linked-to-the-same-object)
    - [9. How to display the variable identifier (memory address in CPython)?](#9-how-to-display-the-variable-identifier-memory-address-in-cpython)
    - [10. What is mutable and immutable?](#10-what-is-mutable-and-immutable)
    - [11. Built-in mutable types:](#11-built-in-mutable-types)
    - [12. Built-in immutable types:](#12-built-in-immutable-types)
    - [13. How does Python pass variables to functions?](#13-how-does-python-pass-variables-to-functions)

## What Are Objects and References?

**Definition and role of objects and references in Python**

:warning: In Python, **objects** are entities that contains **both data and code**. **Variables** are **references** to these **objects**, acting as **labels** that point to the objects in memory. Understanding how variables reference objects is crucial for efficient data management and manipulation in Python.

### Mutable vs Immutable Types

**The fundamental difference between mutable and immutable types**

Mutable types can be modified after creation, while immutable types cannot be altered once created. This distinction is crucial for understanding how Python handles data and memory.

**Examples of immutable types:**
- Integers
- Floats
- Strings
- Tuples

**Examples of mutable types:**
- Lists
- Dictionaries
- Sets

```python
# Example to show the difference between mutable and immutable types

# Immutable type: string
immutable_string = "hello"  # A string is immutable
immutable_string += " world"  # A new string is created

# Displaying the result
print(immutable_string)  # This will print: hello world

# Mutable type: list
mutable_list = [1, 2, 3]  # A list is mutable
mutable_list.append(4)  # Adding an element to the list

# Displaying the result
print(mutable_list)  # This will print: [1, 2, 3, 4]
```

**Explanations, breakdown of the example:**

- **Immutable Types (here strings):** When modifying a **string**, Python creates a **new** string object instead of modifying the original one. The **variable** is then **reassigned** to this new object.
- **Mutable Types (here lists):** **Lists** can be modified directly, allowing you to change their contents **without creating a new object**. The same object is modified in place.

**Implications of mutability:**
1. **Memory usage:** Immutable objects can be more memory-efficient in certain scenarios as Python can reuse identical immutable objects.
2. **Performance:** Operations on mutable objects can be faster as they don't require creating new objects.
3. **Function arguments:** Understanding mutability is crucial when passing objects to functions, as it affects **whether the original object can be modified within the function.**

## Working with References

### Aliasing

**What happens when creating aliases**

Aliasing occurs when multiple variables refer to the same object in memory. This can lead to unexpected behavior if not properly understood and managed.

```python
# Example of aliasing

# Creating a list
original_list = [1, 2, 3]  # original_list is a list with elements 1, 2, 3

# Aliasing: alias_list is another name for original_list
alias_list = original_list   # Both variables point to the same object

# Modifying alias_list
alias_list[0] = 5            # Modifying the element at index 0

# Displaying the results
print(original_list)         # This will print: [5, 2, 3]
print(alias_list)            # This will print: [5, 2, 3]
```

**Risks related to aliasing:**

1. **Unintended side effects**: Modifications made through **one** alias **affect all other aliases**, which can lead to bugs if not anticipated.
2. **Difficulty in tracking changes**: In large programs, it can be challenging to keep track of all aliases and their potential modifications.
3. **Concurrency issues**: In multi-threaded programs, aliasing can lead to race conditions if multiple threads modify the same object simultaneously.

### Cloning

**Creating an independent copy to avoid conflicts**

**Cloning** allows you to create an **independent copy** of an object, preventing modifications to the copy from affecting the original object.

```python
# Example of cloning

# Creating a list
original_list = [1, 2, 3]  # original_list is a list with elements 1, 2, 3

# Cloning: creating a new list with the same values
cloned_list = original_list[:]  # cloned_list is a new list with the same elements

# Modifying the cloned list
cloned_list[0] = 5             # Modifying the element at index 0 of cloned_list

# Displaying the results
print(original_list)           # This will print: [1, 2, 3]
print(cloned_list)             # This will print: [5, 2, 3]
```

**Cloning techniques with concrete examples:**

1. **Slice notation (`[:]`)**: Works for **lists** and other **sequence types**.
2. **`list()` constructor**: Creates a shallow copy of **a list**.
3. **`copy.copy()`**: Creates a shallow copy of **any object**.
4. **`copy.deepcopy()`**: Creates a deep copy, **also copying nested objects**.

**Shallow vs Deep Copy:**
- **Shallow copy:** Creates a new object but **references the same nested objects**.
- **Deep copy:** Creates a new object and **recursively copies all nested objects**.

## Collections in Python

### Dictionaries and Keys

**Definition and use of dictionaries**

Dictionaries are unordered collections of key-value pairs. They provide fast lookup of values based on their associated keys.

```python
# Example of using a dictionary

# Creating a dictionary with Roman numerals
roman_numerals = {'I': 1, 'V': 5, 'X': 10}  # Key-value pairs are stored in curly braces

# Adding a new key-value pair
roman_numerals['L'] = 50  # Adding 'L' for 50

# Accessing values
print(roman_numerals['V'])  # This will print: 5

# Modifying values
roman_numerals['X'] = 11  # Changing the value associated with 'X'

# Displaying the dictionary
print(roman_numerals)  # This will print: {'I': 1, 'V': 5, 'X': 11, 'L': 50}
```

**Key features of dictionaries:**

1. **Fast lookup:** Dictionaries use **hash tables** for **O(1)** average-case lookup time.
2. **Mutable:** Keys and values can be **added**, **modified**, or **removed**.
3. **Flexible keys:** Any **immutable object** can be used as a **key** (**strings, numbers, tuples**).
4. **Unordered:** **Above** Python 3.7, dictionaries maintain insertion order, but this should not be relied upon for functionality.

**Common dictionary methods:**

- **`dict.get(key, default)`**: Returns the value **for key** if it exists, else **defaul**t.
- **`dict.keys()`**: Returns a view of **all keys** in the dictionary.
- **`dict.values()`**: Returns a view of **all values** in the dictionary.
- **`dict.items()`**: Returns a view of **all key-value pairs as tuples**.

### Lists vs Dictionaries

**Comparing the two structures to choose the best one**

| Feature | Lists | Dictionaries |
|---------|-------|--------------|
| Order | Ordered sequence | Unordered (as of Python 3.7, insertion order is preserved) |
| Access | By index (integer) | By key (any immutable type) |
| Lookup speed | O(n) for unsorted, O(log n) for sorted | O(1) average case |
| Use case | When order matters, homogeneous data | When fast lookup by key is needed, heterogeneous data |
| Mutability | Mutable | Mutable |
| Duplicates | Allowed | Keys must be unique |

**When to use lists:**
1. When you need to maintain a specific order of elements.
2. When you frequently need to add or remove elements from the end (or beginning with deque).
3. When your data is homogeneous and you want to perform operations on all elements.

**When to use dictionaries:**
1. When you need fast lookup based on a unique identifier.
2. When your data consists of key-value pairs.
3. When you need to count occurrences of items.
4. When you want to quickly check if an item exists in the collection.

## Managing State in Python (Necessary here?)

### Nonlocal Statements

**Managing variables in nested functions**

The `nonlocal` keyword allows nested functions to modify variables defined in an outer function, providing a way to manage state in closures.

```python
# Example of using nonlocal

def create_counter():
    count = 0  # This variable holds the state

    def increment():
        nonlocal count  # Declare count as nonlocal
        count += 1
        return count

    return increment

# Creating a counter
counter = create_counter()
print(counter())  # This will print: 1
print(counter())  # This will print: 2
print(counter())  # This will print: 3
```

**When and why to use nonlocal:**

1. **Encapsulation:** To create functions with private state.
2. **Avoiding global variables:** To manage state without resorting to global variables.
3. **Creating stateful closures:** To create functions that remember their state between calls.

**Limitations and considerations:**
- `nonlocal` cannot be used to modify variables in the global scope; use `global` for that purpose.
- Overuse of `nonlocal` can lead to complex and hard-to-understand code.
- Consider using classes for more complex stateful behavior.

## Memory Management

### Garbage Collection (Necessary here?)

**How Python manages memory automatically**

Python uses automatic memory management and garbage collection to handle memory allocation and deallocation, freeing developers from manual memory management.

```python
import gc  # Importing the garbage collection module

class Example:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"Object {self.name} is being deleted")

# Creating objects
obj1 = Example("Object 1")
obj2 = Example("Object 2")

# Creating a circular reference
obj1.ref = obj2
obj2.ref = obj1

# Removing references
del obj1
del obj2

# Forcing garbage collection
gc.collect()  # This will trigger the __del__ methods
```

**Key aspects of Python's memory management:**

1. **Reference counting:** Python keeps track of how many references point to an object.
2. **Generational garbage collection:** Objects are divided into generations based on their age.
3. **Cycle detection:** Python can detect and collect objects with circular references.

**Benefits of automatic garbage collection:**
- Prevents memory leaks
- Reduces the likelihood of bugs related to memory management
- Simplifies code by removing the need for manual memory allocation and deallocation

### Circular References and Solutions

**Risks and how Python solves them**

Circular references occur when two or more objects reference each other, creating a cycle that cannot be broken by reference counting alone.

**How Python handles circular references:**
1. **Cycle detector:** Periodically checks for and breaks reference cycles.
2. **Generational GC:** Focuses on younger objects first, as they are more likely to become garbage.

**Best practices to avoid issues with circular references:**
1. Use weak references when appropriate (weakref module).
2. Implement proper `__del__` methods that break circular references.
3. Use context managers (`with` statement) for resource management.
4. Explicitly break circular references when objects are no longer needed.

## Best Practices

1. **Choose the right data structure:** Use lists for ordered collections and dictionaries for key-value pairs.

2. **Avoid unnecessary copying:** Use references when possible, but be aware of aliasing effects.

3. **Use list comprehensions judiciously:** They're concise and efficient, but can be hard to read if too complex.

4. **Leverage immutability:** Use immutable types (tuples, frozensets) when data shouldn't change.

5. **Be cautious with global state:** Minimize the use of global variables; use function parameters or class attributes instead.

6. **Understand mutability consequences:** Be aware of how mutability affects function arguments and return values.

7. **Use context managers:** Employ `with` statements for proper resource management (file handling, locks, etc.).

8. **Optimize memory usage:** Use generators for large datasets to save memory.

9. **Employ defensive programming:** Check types and validate input, especially when working with mutable objects.

10. **Document your code:** Clearly explain the behavior of functions, especially regarding mutability and side effects.

## Questions asked in the project:

### 1. What is an object?
An object in Python is a fundamental unit that combines data (attributes) and behavior (methods). Everything in Python is an object, including numbers, strings, functions, and custom-defined types. Objects have:
- A type
- A value
- An identity (memory address)

### 2. What is the difference between a class and an object or instance?
- A class is a blueprint or template that defines the structure and behavior of objects
- An object (instance) is a concrete realization of a class, with its own unique data

**Example:**
```python
class Car:  # Class (blueprint)
    def __init__(self, color):
        self.color = color

my_car = Car("red")  # Object/Instance
```

### 3. What is the difference between immutable object and mutable object?
- Immutable objects cannot be changed after creation
- Mutable objects can be modified after creation

```python
# Immutable (string)
x = "hello"
x = x + " world"  # Creates a new string

# Mutable (list)
y = [1, 2, 3]
y.append(4)  # Modifies the existing list
```

### 4. What is a reference?
A reference is a name that points to an object in memory. It's how variables "refer to" or "point to" objects.

### 5. What is an assignment?
An assignment creates a reference to an object, binding a name to that object.

```python
x = [1, 2, 3]  # Assigns the list to x
y = x  # Creates another reference to the same list
```

### 6. What is an alias?
An alias is when multiple variables refer to the same object in memory.

```python
x = [1, 2, 3]
y = x  # y is an alias of x
```

### 7. How to know if two variables are identical?
Use the `==` operator to check if two variables has the same value:

```python
x = [1, 2, 3]
z = [1, 2, 3]

print(x == z)  # True
print(x is z)  # False
```

### 8. How to know if two variables are linked to the same object?
Use the `is` operator or `id()` function:

```python
x = [1, 2, 3]
y = x
print(x is y)  # True
print(id(x) == id(y))  # True
```

### 9. How to display the variable identifier (memory address in CPython)?
Use the `id()` function:

```python
x = [1, 2, 3]
print(id(x))  # Prints the memory address
```

### 10. What is mutable and immutable?
- Mutable: Can be changed after creation
- Immutable: Cannot be changed after creation

### 11. Built-in mutable types:
- Lists
- Dictionaries
- Sets

### 12. Built-in immutable types:
- Integers
- Floats
- Strings
- Tuples
- Frozensets

### 13. How does Python pass variables to functions?
Python uses "pass by object reference":
- For immutable objects, it behaves like pass-by-value
- For mutable objects, the function can modify the original object

```python
def modify_list(lst):
    lst.append(4)  # Modifies the original list

def modify_int(x):
    x += 1  # Creates a new object, doesn't modify original

my_list = [1, 2, 3]
modify_list(my_list)  # my_list is now [1, 2, 3, 4]

my_int = 5
modify_int(my_int)  # my_int remains 5
```