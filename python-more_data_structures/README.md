# Python - Data Structures: Sets and Dictionaries

This repository will hold all the projects and tasks in Python about **Sets** and **Dictionnaries** in **Data Structure**. For easier reading, this Readme.md has been cut in two parts ["Data Structures: Lists and Tuples"](https://github.com/ArcturusSky/holbertonschool-higher_level_programming/blob/main/README.md) and a second part directly following : "Data Structures: Sets and Dictionnaries"

## Summary

- [Python - Data Structures: Sets and Dictionaries](#python---data-structures-sets-and-dictionaries)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [TL;DR](#tldr)
  - [Sets](#sets)
    - [Definition:](#definition)
    - [Key characteristics of sets](#key-characteristics-of-sets)
    - [Creating a set](#creating-a-set)
    - [Key features of Sets](#key-features-of-sets)
    - [Set Operations](#set-operations)
    - [Common Set Methods](#common-set-methods)
    - [Frozen set](#frozen-set)
    - [Set comprehension](#set-comprehension)
    - [Use cases of Sets](#use-cases-of-sets)
  - [Dictionaries](#dictionaries)
    - [Definition](#definition-1)
    - [Creating a dictionary](#creating-a-dictionary)
    - [Key features of Dictionaries](#key-features-of-dictionaries)
    - [Accessing and Modifying values in a dictionary](#accessing-and-modifying-values-in-a-dictionary)
    - [Common Dictionnary Methods](#common-dictionnary-methods)
    - [Dictionary Operations](#dictionary-operations)
    - [Dictionary comprehension](#dictionary-comprehension)
    - [Nested Dictionaries:](#nested-dictionaries)
    - [Use cases of dictionaries](#use-cases-of-dictionaries)
  - [Lambda Functions, Filter, Reduce and Map](#lambda-functions-filter-reduce-and-map)
    - [Lambda Functions](#lambda-functions)
      - [Definition](#definition-2)
    - [Map Function](#map-function)
      - [Definition](#definition-3)
    - [Filter Function](#filter-function)
      - [Definition](#definition-4)
    - [Reduce Function](#reduce-function)
      - [Definition](#definition-5)
    - [Comparing Map, Filter, and Reduce](#comparing-map-filter-and-reduce)
    - [Practical Examples](#practical-examples)
      - [Using `map()` for transforming data](#using-map-for-transforming-data)
      - [Using `filter()` for data selection](#using-filter-for-data-selection)
    - [Using `reduce()` for aggregations](#using-reduce-for-aggregations)
    - [Lambda, Map, Filter and Reduce together](#lambda-map-filter-and-reduce-together)
  - [When to use each](#when-to-use-each)
  - [Conclusion](#conclusion)
  - [Author](#author)

## Glossary

**A**
- **Append:** The `append()` method adds an item to the end of a list.

**C**
- **Concatenation:** Combining two lists into one using the `+` operator.
- **Clear:** The `clear()` method removes all elements from a list, set, or dictionary, leaving it empty.

**D**
- **Deque:** A double-ended queue from the `collections` module that allows for fast appends and pops from both ends.
- **Dictionary:** An unordered collection of key-value pairs, where each key must be unique and hashable, and values can be of any type, enclosed in curly braces (`{}`).

**E**
- **Extend:** The `extend()` method adds each element of an iterable (e.g., another list) to the end of a list.

**F**
- **Filtering:** The process of creating a new list by including only elements that meet certain criteria, often done using list comprehensions.
- **Frozenset:** An immutable version of a set, which cannot be modified after creation.

**I**
- **Index:** A position in a list, tuple, or string, starting from 0, used to access elements.

**K**
- **Key:** A unique identifier in a dictionary that is associated with a value. Keys must be hashable (e.g., strings, numbers, or tuples).

**L**
- **List:** An ordered, mutable collection of items enclosed in square brackets (`[]`).

**M**
- **Mutable:** A data type that allows modification after creation, such as lists and dictionaries in Python.

**N**
- **Nesting:** The practice of placing one list, tuple, set, or dictionary inside another, allowing for complex data structures.

**P**
- **Pop:** The `pop()` method removes and returns the item at a specified index in a list or set, or the value associated with a key in a dictionary. For sets, it removes an arbitrary element.

**R**
- **Reference:** A variable that points to the same object in memory, such as when assigning one list to another.
- **Remove:** The `remove()` method removes the first occurrence of a value from a list or set.

**S**
- **Set:** An unordered collection of unique items, enclosed in curly braces (`{}`). Sets do not allow duplicates.
- **Slice:** A subset of a list, tuple, or string obtained by specifying a start and end index, creating a new sequence with the selected elements.
- **Sort:** The `sort()` method arranges the items of a list in ascending or descending order.
- **Stack:** A data structure that follows Last In, First Out (LIFO) order, where the most recently added item is the first to be removed.

**Q**
- **Queue:** A data structure that follows First In, First Out (FIFO) order, where the first item added is the first to be removed.

**T**
- **Tuple:** An immutable sequence type in Python, often used to group related items together. Tuples are enclosed in parentheses (`()`).

**U**
- **Unpacking:** The process of extracting values from a list, tuple, set, or dictionary into separate variables.
- **Update:** The `update()` method adds multiple elements to a set or updates the contents of a dictionary by adding key-value pairs from another dictionary or iterable.


## TL;DR

| **Feature**            | **String**                               | **List**                                  | **Tuple**                                 | **Set**                                    | **Dictionary**                              |
|------------------------|------------------------------------------|-------------------------------------------|-------------------------------------------|--------------------------------------------|---------------------------------------------|
| **Mutable**            | <span style="color:red">No</span>                                       | <span style="color:green">Yes</span>                                       | <span style="color:red">No</span>                                        | <span style="color:green">Yes</span>                                        | <span style="color:green">Yes</span>                                         |
| **Indexed**            | <span style="color:green">Yes</span> (by character index)                 | <span style="color:green">Yes</span> (by element index)                    | <span style="color:green">Yes</span> (by element index)                    | <span style="color:red">No</span> (unordered)                             | <span style="color:red">No</span> (key-value pairs)                        |
| **Ordered**            | <span style="color:green">Yes</span>                                      | <span style="color:green">Yes</span>                                       | <span style="color:green">Yes</span>                                       | <span style="color:red">No</span>                                         | <span style="color:green">Yes</span> (as of Python 3.7, before: <span style="color:red">No</span>)          |
| **Allows duplicates**  | <span style="color:green">Yes</span>                                      | <span style="color:green">Yes</span>                                       | <span style="color:green">Yes</span>                                       | <span style="color:red">No</span>                                         | Keys: <span style="color:red">No</span>, Values: <span style="color:green">Yes</span>                       |
| **Heterogeneous**      | <span style="color:red">No</span> (all elements are characters)         | <span style="color:green">Yes</span> (can hold different data types)       | <span style="color:green">Yes</span> (can hold different data types)       | <span style="color:green">Yes</span> (can hold different data types)        | <span style="color:green">Yes</span> (keys must be hashable)                 |
| **Syntax**             | `"hello"` or `'hello'`                   | `[1, 2, 3]` or `list()`                   | `(1, 2, 3)` or `tuple()`                  | `{1, 2, 3}` or `set()`                    | `{"key": "value"}` or `dict()`              |
| **Access Elements**    | `s[0]`                                  | `lst[0]`                                 | `tup[0]`                                 | Not applicable (unordered)                 | `dict[key]`                                 |
| **Add Elements**       | Not possible (immutable)                 | `append()`, `insert()`, `extend()`        | Not possible (immutable)                  | `add()`, `update()`                        | `dict[key] = value`, `update()`             |
| **Remove Elements**    | Not possible                             | `remove()`, `pop()`, `clear()`, `del`     | Not possible                             | `remove()`, `discard()`, `pop()`, `clear()`| `del dict[key]`, `pop()`, `clear()`         |
| **Concatenation**      | `+`                                      | `+`, `extend()`                          | `+` (creates a new tuple)                | Not applicable                            | Not applicable                              |
| **Iteration**          | `for char in string`                     | `for item in list`                       | `for item in tuple`                      | `for item in set`                          | `for key, value in dict.items()`            |
| **Conversion** (already built-in conversion from one data structure to another)         | `list("abc")` -> `['a', 'b', 'c']`       | `tuple([1, 2])` -> `(1, 2)`              | `list((1, 2))` -> `[1, 2]`               | `set([1, 2, 2])` -> `{1, 2}`               | `dict([("key", "value")])` -> `{'key': 'value'}` |
| **Example**            | A word or sentence, like `"hello world"` | A grocery list: `["milk", "eggs", "bread"]`| Coordinates: `(latitude, longitude)`     | A collection of unique email IDs: `{1, 2, 3}`| Contacts: `{"John": "123-4567", "Alice": "987-6543"}`|
| **When to use** (Best Situations)        | Use when working with text, sentences, or character data that won't change. | Use when you need a sequence of items where order matters, and modifications are common. | Use when you need a fixed set of data, such as coordinates, or constant settings. | Use when uniqueness is important (no duplicates), or when you need fast lookups. | Use when you need to map unique keys to specific values, like a database or configurations. |
| **Programming Example**| Storing a user's name in an app. `name = "John"`| Tracking tasks in a to-do list app. `tasks = ['send email', 'buy groceries']` | Storing fixed settings like screen resolution. `screen_resolution = (1920, 1080)` | Storing unique tags in a social media app. `tags = {'python', 'coding', 'development'}` | Storing user data or app settings. `user_data = {'name': 'Alice', 'age': 30}` |

## Sets

### Definition:

Sets are another built-in data type in Python. A **set** is an **unordered collection** of unique elements. Sets are used to store multiple items, but unlike lists or tuples, they do not allow **duplicate** values, and their elements are not ordered, meaning they don't have a specific positions or index.

### Key characteristics of sets

1. **Unique elements:** A set automatically removes any duplicates. Every element in a set must be unique
2. **Unordered:** The elements in a set are not stored in any specific order, so you cannot access items by index.
3. **Mutable:** Sets themselves can be changed (you can add or remove elements), but the elements inside the set must be ummutables (like numbers, strings, tuples)

### Creating a set

You can create a set by placing items inside curly braces `{}`, or by using the `set()` function.

```python

# Creating a set using curly braces
my_set = {1, 2, 3, "apple", "banana"}
print(my_set) # Output: {1, 2, 3, 'apple', 'banana'}

# Creating an empty set
empty_set = set()
print(empty_set) # Output: set()

```
:warning: **NOTE:** `{}` is reserved for creating an empty dictionay, so always use `set()` to create an empty set

### Key features of Sets

- **No duplicate:** If you add the same element more than once, the set will only store it once.

```python

my_set = {1, 2, 2, 3, "apple", "apple"}
print(my_set) # Output: {1, 2, 3, 'apple'}

```

- **Unordered:** The order in which elements are printed might not be the same as the order they were inserted, since sets are unordered

```python

my_set = {"banana", 1, "apple", 3}
print(my_set) # Output: {1, 3, 'apple', 'banana'}

```

### Set Operations

Sets support common mathematical set operations like union, intersection, and difference.

- **Union:** Combines two sets, including all elements from both.

```python

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2) # Output: {1, 2, 3, 4, 5}

# Or without operator:

union_result = set1.union(set2)

```
- **Intersection:** Returns only the elements that are present in both sets. 

```python

print(set1 & set2) # Output {3}

# Or without operator:

intersection_result = set1.intersection(set2)

```

- **Difference:** Returns elements that are in the first set but not in the second 

```python

print(set1 - set2) # Output {1, 2}

```

- **Symmetric difference:** Returns elements that are in one of the sets, but not in both. 

```python

print(set1 ^ set2) # Output: {1, 2, 4, 5}

```

### Common Set Methods

- **`add(x)`:** Add element `x` to the set 

```python

my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # Output {1, 2, 3, 4}
```

- **`remove(x)`:** Removes element `x` from the set. If `x` is not in the set, it raises a `KeyError` 

```python

my_set.remove(2)
print(my_set) # Output: {1, 3, 4}

```

- **`discard(x)`:** Removes elements `x` if it is in the set. if not, nothing happens (no error raised). 

```python

my_set.discard(5) # No error even if 5 is not in the set

```

- **`pop()`:** Removes and returns an arbitrary element from the set. Since sets are **unordered**, you don't know which element will be removed. 

```python

my_set = {1, 2, 3}
removed_element = my_set.pop()
print(removed_element) # Output could be: 1, 2 or 3 (since sets are unordered)
```

- **clear():** Removes all elements from the set

```python

my_set.clear()
print(my_set) # Output: set()

```

- **copy():** Copy a set to avoid unintentional changes to the original set when modifications are requiered.

```python

# Copying a set
my_set = {1, 2, 3}
new_set = my_set.copy()

```

### Frozen set

A **frozen set** is a immutable version of set. This can be useful for cases where you need a set but don't want it to be changed (example: using a set a a dictionary key)

```python

# Creating a frozen set

frozen = frozenset([1, 2, 3, "apple"])
print(frozen) # Output: frozenset({1, 2, 3, 'apple'})

```

Frozen sets have similar methods to **sets**, except they cannot be modifiel after creation (so, no `add` or `remove`, etc)


### Set comprehension

Similar to [list comprehension](https://github.com/ArcturusSky/holbertonschool-higher_level_programming/blob/main/python-data-structures/README_list.md#list-comprehensions), set comprehensions allow for concise set creations.

```python

squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}

```


### Use cases of Sets

- **Membership testing:** Sets are optimized for membership tests, meaning checking if an element is part of a set is very fast. 

```python

my_set {1, 2, 3}
print(1 in my_set) # Output: True

```

- **Removing duplicates from lists:** Sets are often used to remove duplicates from a list since sets do not allow duplicate values. 

```python

my_list = [1, 2, 2, 3, 4, 4]
unique_items = set(my_list)
print(unique_items) # Output: {1, 2, 3, 4}
```

## Dictionaries

### Definition

A **dictionay** in Python is an **unordered** (until Python 3.7), **mutable collection** of key-value pairs. Each key in a dictionary must be unique and immutable (strings, numbers, or tuples), while the values can be of any data type and can be duplicated. Dictionaries are used to map a set of unique keys to values.

### Creating a dictionary

You can create a dictionary using curly braces `{}` with key-value paris, or by using the `dict()` constructor.

```python

# Creating a dictionary using curly braces
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict) # Output: {'name" : 'Alice', 'age': 25, 'city': 'New York'}

# Creating a dictionary using dict()
my_dict_2 = dict(name="Bob", age=30, city="Chicago")
print(my_dict_2) # Output: {'name': 'Bob', 'age': 30, 'city': 'Chicago'}
```

### Key features of Dictionaries

1. **Key-Value Pairs:** Each element in a dictionary consists of a key and a corresponding value. the key is used to access the value.
2. **Unique Keys:** All keys in a dictionary must be unique. If you add an existing key, its value will be updated.
3. **Unordered(before Python 3.7):** Dictionaries do not store elements in any particular order. However, starting from Python 3.7, dictionaries maintain the insertion order of keys 

### Accessing and Modifying values in a dictionary

- **Accessing values:** Use the key to get the associated value.

```python

print(my_dict["name"]) #Output: Alice

```

- **Adding/Modifying values:** You can add new key-value pairs or modify existing ones by assigning values to keys.

```python

my_dict["age"] = 26 # Modifying an existing key
my_dict["profession"] = "Engineer" # Adding a new key
print(my_dict) # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

```

- **Removing a key-value pair:** Use the `del` keyword or dictionary methods to remove a key and its value.

```python

del my_dict["city"]
print(my_dict) # Output: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}

```

### Common Dictionnary Methods

- **`get(key[, default])`:** Returns the value for the specified key. If the key is not found, it returns `None` or a specified default value.

```python

print(my_dict.get("name")) # Output: Alice
print(my_dict.get("city", "Not found")) # Output: Not found

```

- **`len(my_dict)`:** Return the number of keys in a dictionnary

```python

print(len(my_dict)) # Output: 3


```

- **`setdefault()`:** Similar to `get()` but also inserts a default value for the key if it doesn't exist.

```python

my_dict = {"name": "Alice", "age": 25}
age = my_dict.setdefault("age", 30) # Output: 25
city = my_dict.setdefault("city", "New York") # Output: 'New York'
print(my_dict) # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

```

- **`fromkeys()`:** Create a dictionary with specified keys and a default value for all keys.

```python

keys = ["name", "age", "city"]
default_dict = dic.fromkeys(keys, "Unknown")
print(dafault_dict) # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

```

- **`keys()`:** Returns a view object of all the keys in the dictionary.

```python

print(my_dict.keys()) # Output: dict_keys(['name', 'age'n 'profession'])

```

- **`values()`:** Returns a view object of all the values in the dictionary.

```python

print(my_dict.values()) # Output: dict_values(['Alice', 26, 'Engineer'])

```

- **`items()`:** Returns a view object of all key-value pairs (tuples).

```python

print(my_dict.items()) # Output: dict_items([('name', 'Alice'), ('age', 26), ('profession', 'Engineer')])

```

- **`pop(key[, default])`:** Removes the key and returns its value. If the key is not found, it returns `default` if provided, otherwise raises a `KeyError`.

```python

age = my_dict.pop("age")
print(age) # Output: 26
print(my_dict) # Output: {'name': 'Alice', 'profession': 'Engineer'}
```

- **`update([other])`:** Updates the dictionary with key_value pairs from another dictionary or iterabl of key-value pairs.

```python

my_dict.update({"age": 27, "city": "New York"})
print(my_dict) # Output: {'name': 'Alice', 'profession': 'Engineer', 'age': 27, 'city': 'New York'}
```

- **`clear()`:** Removes all elements from the dictionary.

```python

my_dict.clear()
print(my_dict) # Output: {}
```

### Dictionary Operations

- **Checking if a key exists:**

```python

my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict) # Output: True
print("city" in my_dict) # Output: False
```

- **Iterating through a dictionary:** You can loop through both keys and values in a dictionary.

```python

for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25

```

### Dictionary comprehension

Dictionary comprehension is a concise and efficient way to create dictionnaries, similar to list comprehensions.

```python

squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


```

### Nested Dictionaries:

Nested dictionaries are commonly used to store more complexe data structures.

```python

nested_dict = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "Chicago"}
}

print(nested_dict["Alice"]["age"]) # Output: 25

```

### Use cases of dictionaries

- **Storing key-value data:** Dictionaries are ideal for scenarios where you need to associate data with unique keys, such as a database of users and their information.

```python

user_data = {"username":"alice", "email": "alice@example.com", "age": 25}

```

- **Countint occurences:** Dictionaries are often used for counting the occurence of items in a list or dataset.

```python

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = {}
for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
print(fruit_count) # Output: {'apple': 3, 'banana': 2, 'orange': 1}
```

## Lambda Functions, Filter, Reduce and Map

### Lambda Functions

#### Definition

A **lambda function** in Pythin is a small anonymous function efined with the keyword `lambda`. Lambda functions can have any number of arguments but only one expression. They are iften used when a simple function is required for a short period of time, typically in functions lik `map()`, `filter()`, and `reduce()`.

**Syntax:**

```python

lambda arguments: expression

```

The lambda function evaluates the expression and returns the result.

- *Example:*

```python

# Regular function
def add_numbers(number1, number2):
    return number1 + number2

# Equivalent lambda function
add_lambda = lambda number1, number2: number1 + number2

print(add_lambda(2, 3))  # Output: 5


```

**Why Use `lambda` functions?**

- They allow for **concise code.**
- Useful when you need a small function for **one-time use.**
- Can be passed as arguments to higher-order functions like `map()`, `filter()` and `reduce()`.

### Map Function

#### Definition

`map()` applies a function to **each item** of an iterable (like a list) and returns a **map object** (an iterator) with the results. You can convert it back to a list if necessary.

**Syntax:**

```python

map(function, iterable)

```

- `function`: a function to apply to each element of the iterable.
- `iterable`: The iterable (example: list, tuple) to be processed.

- *Example:*

```python

number_list = [1, 2, 3, 4]

# Applying lambda to square each number
squared_numbers = list(map(lambda number: number**2, number_list))

print(squared_numbers)  # Output: [1, 4, 9, 16]


```

### Filter Function

#### Definition

`filter()` applies a function to each item of an iterable and **filters out** the items that don't satisfy a given condition (example: when the function returns `False`)

**Syntax:**

```python

filter(function, iterable)

```

- `function`: A function that returns `True` or `False`
- `iterable`: The iterable to be filtered

- *Example:*

```python

number_list = [1, 2, 3, 4, 5, 6]

# Filtering even numbers
even_numbers = list(filter(lambda number: number % 2 == 0, number_list))

print(even_numbers)  # Output: [2, 4, 6]


```

### Reduce Function

#### Definition

`reduce()` from the `functools` module is used to **accumulate** the results of applying a function cumulatively to the items of an iterable. It reduces the iterable to a single value.

**Syntax**

```python

from functools import reduce

reduce(dunction, iterable)

```

- `function`: A function that takes two arguments an returns a single result
- `iterable`: The iterable to be processed.

- *Example:*

```python
from functools import reduce

number_sequence = [1, 2, 3, 4]

# Multiply all elements together
total_product = reduce(lambda current_product, next_number: current_product * next_number, number_sequence)

print(total_product)  # Output: 24



```

### Comparing Map, Filter, and Reduce

1. `map()` applies a function to each elements of the iterable and returns a new iterable with the results.

2. `filter()` applies a function to each element of the iterable and returns only the elements that satisfy the function's condition

3. `reduce()` applies a function cumulatively to the elements and returns a single reduced result.

### Practical Examples

#### Using `map()` for transforming data

You can use `map()` when you want to transform each element of a collection.

```python

temperatures_in_celsius = [0, 10, 20, 30]

# Convert Celsius to Fahrenheit
temperatures_in_fahrenheit = list(map(lambda celsius: (celsius * 9/5) + 32, temperatures_in_celsius))

print(temperatures_in_fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]


```

#### Using `filter()` for data selection

You can use `filter()` to extract elements that meet specific criteria.

```python

# Filtering a list of people older than 18

people_ages = [15, 22, 17, 35, 10]

# Filter people who are 18 or older
adults = list(filter(lambda age: age >= 18, people_ages))

print(adults)  # Output: [22, 35]

```

### Using `reduce()` for aggregations

You can use `reduce()` for summing, multiplying, or finding the maximum or minimum of a list.

```python

# Finding the maximum value in a list

from functools import reduce

number_list = [5, 1, 8, 2, 10]

max_value = reduce(lambda current_max, next_number: current_max if current_max > next_number else next_number, number_list)

```

### Lambda, Map, Filter and Reduce together

You can combien these functions to create concise, functional-style code.

- *Example:*

Let's say we have a list of numbers and want to:

1. Square all even numbers using `filter()` and `map()`.
2. Find the sum of the squared numbers using `reduce()`

```python

from functools import reduce

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Step 1: Filter out even numbers
even_numbers = list(filter(lambda number: number % 2 == 0, numbers_list))

# Step 2: Square the even numbers
squared_even_numbers = list(map(lambda number: number**2, even_numbers))

# Step 3: Sum the squared numbers
sum_of_squared_numbers = reduce(lambda accumulated_sum, current_number: accumulated_sum + current_number, squared_even_numbers)

print(sum_of_squared_numbers)  # Output: 120


```

## When to use each

- `lambda`: Use when you need a simple, one-off function.
- `map()`: Ideal for applying a transformation to each item in an iterable.
- `filter()`: Use when you want to filter items in an iterable based on a condition
- `reduce()`: Use for aggregation tasks that combien all elements of an iterable into a single value.

## Conclusion

Choosing the right data structure is key to efficient programming. **Strings** are great for text manipulation, **lists** for dynamic collections, **tuples** for immutable groupings, **sets** for unique elements, and **dictionaries** for key-value mappings. Understanding their characteristics and appropriate use cases will enhance your ability to solve problems effectively and write clear maintainable code.

## Author

Anne-Cécile Besse (Arc)