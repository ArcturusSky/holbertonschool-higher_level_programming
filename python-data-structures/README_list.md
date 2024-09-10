# Python Data Structures: Lists, Tuples, Sets and Dictionaries

This repository will hold all the projects and tasks in Python about **Lists** and **Data Structure**.

## Summary

- [Python Data Structures: Lists, Tuples, Sets and Dictionaries](#python-data-structures-lists-tuples-sets-and-dictionaries)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [TL;DR](#tldr)
  - [Lists](#lists)
    - [Introduction to Lists](#introduction-to-lists)
      - [What is a List?](#what-is-a-list)
      - [List indexing and slicing](#list-indexing-and-slicing)
      - [List concatenation](#list-concatenation)
    - [Modifying lists](#modifying-lists)
      - [Lists are mutables](#lists-are-mutables)
      - [Appending elements](#appending-elements)
    - [List operations](#list-operations)
      - [Assignment and references](#assignment-and-references)
      - [Slicing and copying](#slicing-and-copying)
      - [Assigning to slices](#assigning-to-slices)
      - [The `len()` function](#the-len-function)
      - [Nesting lists](#nesting-lists)
    - [Advanced list methods:](#advanced-list-methods)
      - [List methods](#list-methods)
      - [Examples using list methods](#examples-using-list-methods)
    - [Using list as Stacks and Queues](#using-list-as-stacks-and-queues)
      - [List as Stacks (LIFO)](#list-as-stacks-lifo)
      - [List as Queues (FIFO)](#list-as-queues-fifo)
        - [What is a `deque` in Python?](#what-is-a-deque-in-python)
        - [Key Operations of `deque`:](#key-operations-of-deque)
        - [Examples of each key operation](#examples-of-each-key-operation)
    - [List comprehensions](#list-comprehensions)
      - [Introduction to List Comprehensions](#introduction-to-list-comprehensions)
      - [Filtering with list comprehensions](#filtering-with-list-comprehensions)
      - [Benefits of list comprehensions](#benefits-of-list-comprehensions)
  - [Tuples](#tuples)
    - [Definition](#definition)
    - [Key Characteristics of Tuples](#key-characteristics-of-tuples)
    - [Basic Syntax](#basic-syntax)
    - [Key operation of tuples:](#key-operation-of-tuples)
  - [Sets](#sets)
    - [Definition:](#definition-1)
    - [Key characteristics of sets](#key-characteristics-of-sets)
    - [Creating a set](#creating-a-set)
    - [Key features of Sets](#key-features-of-sets)
    - [Set Operations](#set-operations)
    - [Common Set Methods](#common-set-methods)
    - [Set comprehension](#set-comprehension)
    - [Use cases of Sets](#use-cases-of-sets)
  - [Dictionaries](#dictionaries)
    - [Definition](#definition-2)
    - [Creating a dictionary](#creating-a-dictionary)
    - [Key features of Dictionaries](#key-features-of-dictionaries)
    - [Accessing and Modifying values in a dictionary](#accessing-and-modifying-values-in-a-dictionary)
    - [Common Dictionnary Methods](#common-dictionnary-methods)
    - [Dictionary Operations](#dictionary-operations)
    - [Use cases of dictionaries](#use-cases-of-dictionaries)
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





## Lists

### Introduction to Lists

#### What is a List?

A list is a versatile compound data type in Python used to group multiple values together. List are written as a sequence of comma-separated values (called items) enclosed in square brackets.

- *Example:*

```python

squares = [1, 4, 9, 16, 25]
print(squares) # Output: [1, 4, 9, 16, 25]

```

#### List indexing and slicing

Like strings, lists can be indexed (accessd by position) and sliced (retrieving parts of the list).

*Example of indexing:*

```python

squares[0] # Output: 1
squares[-1] # Output: 25

```

*Example of slicing:*

```python

squares[-3] # Output: [9, 16, 25]

```

#### List concatenation

You can concatenate lists using the `+` operator.

- *Example:*

```python

squares + [36, 49, 64, 81, 100]
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

```

### Modifying lists

#### Lists are mutables

Unlike strings, lists are mutable, meaning their content can be changed.

- *Example:*

```python

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64 # Correct the wrong value
print(cubes) # Output: [1, 8, 27, 64, 125]

```

#### Appending elements

You can add new items to the end of a list using the `append()` method.

- *Example:*

```python

cubes.append(216) # Add 216 at the end, enlarging the list.
print cubes # Output: [1, 8, 27, 64, 125, 216]

```

### List operations

#### Assignment and references

Assigning a list to another variable doesn't copy the list; it simply creates a **reference**.

- *Example:*

```python

rgb = ["Red", "Green", "Blue"]
rgba = rgb
rgba.append("Alpha")
print(rgb) # Output: ["Red", "Green", "Blue", "Alpha"]

```

As we can see in the example above, even if "Alpha" has been appended to "rgba", the "rgb" list has changed too.

#### Slicing and copying

Slicing returns a **shallow** copy of the list which means it creats a new independent list.

- *Example:*

```python

rgba = ["Red", "Green", "Blue", 0,5] # Original list
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba) # Output: ["Red", "Green", "Blue", "Alpha"]
print(rgba) # Output: ["Red", "Green", "Blue", "0,5"]

```

As we can see in the example above, on the contrary to **reference** here the new list `correct_rgba` has been modified without modifying the orignal one.

#### Assigning to slices

You can replace parts of a list by assigning to slices, which can change its size or even empty it.

- *Example:*

```python

letters = ["a", "b", "c", "d", "e", "f", "g"]
letters[2:5] = ["C", "D", "E",]
print(letters) # Output: ["a", "b", "C", "D", "E", "f", "g"]

```

#### The `len()` function

You can use the `len()` function to get the lenghts of a list.

- *Example:*

```python

len(letters) # Output: 7

```

#### Nesting lists

Lists can contain others lists, allowing for complex data structures.

- *Example:*

```python

a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]

print(x) # Output: [["a", "b", "c"], [1, 2, 3]]

```

### Advanced list methods:

#### List methods

Pythons lists have several useful methods:

  - `append(x)` – Add `x` to the end.
  - `extend(iterable)` – Extend the list by appending items from another iterable.
  - `insert(i, x)` – Insert `x` at index `i`.
  - `remove(x)` – Remove the first item whose value is `x`.
  - `pop([i])` – Remove the item at index `i`(or the last item if `i` is not provided) and return it.
  - `clear()` – Remove all items from the list.
  - `index(x[, start[, end]])` – Return the index of the first occurence of `x`
  - `count(x)` – Return the number of times `x` appears.
  - `sort()` – Sort the list in place.
  - `reverse()` – Reverse the list in place.
  - `copy()` – Return a shallow copy of the list.

#### Examples using list methods

```python

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
# Given list that will be alterate through the examples

# 1. append(x) – Add "grape" to the end
fruits.append("grape")
print(fruits)
# Output:  ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana", "grape"]

# 2. extend(iterable) – Extend the list by adding ["mango", "pineapple"]
fruits.extend(["mango", "pineapple"])
print(fruits)
# Output: ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana", "grape", "mango", "pineapple"]

# 3. insert(i, x) – Insert "cherry" at index 2
fruits.insert(2, "cherry")
print(fruits)
# Output: ["orange", "apple", "cherry", "pear", "banana", "kiwi", "apple", "banana", "grape", "mango", "pineapple"]

# 4. remove(x) – Remove the first occurence of "apple"
fruits.remove("apple")
print(fruits)
# Output: ["orange", "cherry", "pear", "banana", "kiwi", "apple", "banana", "grape", "mango", "pineapple"]

# 5. pop([i]) – Remove the item at index 3 (which is "banana") and return it
removed_item = fruits.pop(3)
print(removed_item)
# Output: "banana"
print(fruits)
# Output: ["orange", "cherry", "pear", "kiwi", "apple", "banana", "grape", "mango", "pineapple"]

# 6. clear() – Remove all items from the list
fruits.clear()
print(fruits)
# Ouput: []

# Resetting fruits list for the remaining examples
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

# 7. index(x[, start[, end]]) – Return the index of the first occurence of "banana"
index_banana = fruits.index("banana")
print(index_banana)
# Output: 3

# 8. count(x) – Return the number of times "apple" appears
apple_count = fruits.count("apple")
print(apple_count)
# Output: 2

# 9. sort() – sort the list in place
fruits.sort()
print(fruits)
# Output: ["apple", "apple", "banana", "banana", "kiwi", "orange", "pear"]

# 10. reverse() – Reverse the list in place
fruits.reverse()
# Output: ["pear", "orange", "kiwi", "banana", "banana", "apple", "apple"]

# 11. copy() – Return a shallow copy of the list
fruits_copy = fruits.copy()
print(fruits_copy)
# Output: ["pear", "orange", "kiwi", "banana", "banana", "apple", "apple"]

```

### Using list as Stacks and Queues

#### List as Stacks (LIFO)

You can use a list as a stack, where the last element added is the first one retrieved

- *Example:*

```python

stack = [3, 4, 5]
stack.append(6)
stack.pop() # Output: 6
# pop() removed the last item so it removed 6

```

#### List as Queues (FIFO)

List can also be used as queues, but it's inefficient. Instead, use `collections.deque`.

##### What is a `deque` in Python?

`deque` stands for `double-ended queue` and is part of the `collections` module in Python. It is a generalization of a stack and queue that allows fast and efficient additions and removals of elements **from both ends**

  - A **list** in Pythin is optimized for operations that add or remove elements from the end (like `append()` and `pop()`), but operations on the front (like `insert(0, x)` or `pop(0)`) are slower because they require shifting all the elements.
  
  - A **deque**, on the other hand, provides **O(1)** [time complexity](https://github.com/ArcturusSky/holbertonschool-sorting_algorithms/blob/main/README.md#time-complexity) for adding and removing itemmps from **both** ends (front and back), making it faster for such operations 

##### Key Operations of `deque`:

- `append(x)` – Add `x` to the right end of the deque
- `appendleft(x)` – Add `x` to the left end od the deque
- `pop()` – Remove and return the rightmost element (the last)
- `popleft()` – Remove and return the leftmost element (the first)
- `extend(iterable)` – Extend the deque by appending itemps from another iterable to the right.
- `extendleft(iterable)` – Extend the deque by appending items from another iterable to the left (in reverse order).
- `rotate(n)` – Rotate the deque `n` steps to the right. If `n` is negative, rotate to the left.
- `clear()` – Remove all items from the deque.
- `maxlen` – Set a maximum size for the deque; when the deque is full, new items remove items from the opposite end.

##### Examples of each key operation

```python

from collections import deque

# Initialize a deque with the list
queue = deque(["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"])

# 1. append(x) -- Add "grape" to the right end
queue.append("grape")
print(queue)
# Output: deque(["orange", "apple", "pear", "banana", "kiwi", "apple", "banana", "grape"])

# 2. appendleft(x) -- Add "mango" to the left end
queue.appendleft("mango")
print(queue)
# Output: deque(["mango", "orange", "apple", "pear", "banana", "kiwi", "apple", "banana", "grape"])

# 3. pop() -- Remove and return the rightmost element ("grape")
print(queue.pop())  # Output: "grape"
print(queue)
# Output: deque(["mango", "orange", "apple", "pear", "banana", "kiwi", "apple", "banana"])

# 4. popleft() -- Remove and return the leftmost element ("mango")
print(queue.popleft())  # Output: "mango"
print(queue)
# Output: deque(["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"])

# 5. extend(iterable) -- Extend the deque by adding ["peach", "plum"]
queue.extend(["peach", "plum"])
print(queue)
# Output: deque(["orange", "apple", "pear", "banana", "kiwi", "apple", "banana", "peach", "plum"])

# 6. extendleft(iterable) -- Extend the deque by adding ["strawberry", "blueberry"] to the left
queue.extendleft(["strawberry", "blueberry"])
print(queue)
# Output: deque(["blueberry", "strawberry", "orange", "apple", "pear", "banana", "kiwi", "apple", "banana", "peach", "plum"])

# 7. rotate(n) -- Rotate the deque 3 steps to the right
queue.rotate(3)
print(queue)
# Output: deque(["banana", "peach", "plum", "blueberry", "strawberry", "orange", "apple", "pear", "banana", "kiwi", "apple"])

# 8. clear() -- Remove all items from the deque
queue.clear()
print(queue)
# Output: deque([])

# Resetting the deque for remaining examples
queue = deque(["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"])

# 9. maxlen -- Set a maximum size for the deque
queue = deque(queue, maxlen=5)
print(queue)
# Output: deque(["apple", "pear", "banana", "kiwi", "apple"])

# Adding more items to see the effect of maxlen
queue.append("grape")
print(queue)
# Output: deque(["pear", "banana", "kiwi", "apple", "grape"])


```

### List comprehensions

#### Introduction to List Comprehensions

List comprehensionss in Python are a powerful and concise way to create lists. They allow you to generate a new list by applying an expression to each item in an existing iterable (like a list or range), optionally including conditions to filter items.

**1. Basic syntax:**

```python

[expression for item in iterable]

```

- `expression`: This is the value or calculation to include in the new list. It can be a single value or a more complex expression.
- `for item in iterable`: This iterates over each item in the given iterable (such as a list, range, or string).

**2. Optional condition:**

```python

[expression for item in iterable if condition]

```

- `if condition`: This filters items based on a condition. Only items for which the condition is `True` are included in the resulting list. 


**Break-downed example:**
  
```python

squares = [x**2 for x in range(10)]
print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

- **Expression:** `x**2`
  - This calculates the square of each number `x`.
- **For clause:** `for x in range(10)`
  - This iterates over each number from `0` to `9` (since `range(10)` generates numbers from `0` up to, but not including `10`) 

**How it works:**

- The list comprehension iterates through each number in the range `0` to `9`.
- For each number `x`, it calculates `x**2` (which is `x` squared) and adds the result to the list.
- Finally, it creates a new list `squares` containing these squared values.

**Output:**

- The resultint list `squares` is `[0, 1, 4, 9, 16, 25, 36 , 49, 64, 81]`

#### Filtering with list comprehensions

You can also add conditions to filter items within a list comprehension.

- *Example:*
  
```python

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

```

In this example: 
  - The condition `if x % 2 == 0` ensures that only even numbers are squared
  - Thus, the list `even_squares` contains squares of even numbers only.

#### Benefits of list comprehensions

- **Conciseness:** They condense several lines of code into a single line, making the code easier to read.
- **Efficiency:** They can be more efficient than using a loop to generate the list
- **Readability:** When used properly, they make code more expressive and clear.

## Tuples

We have seen that lists and strings share several common properties, such as indexing and slicing. These are examples of **sequence data types**. Python offers several sequence data types, with **tuples** being another standard type.

### Definition

A **Tuple** is a built-in data type in Python that represents an immutable sequence of elements.
Unlik lists, tuples cannot be modified after creation, making them useful for **fixe collections of items**.

### Key Characteristics of Tuples

  1. **Immutable:** Once created, the elements of a tuple cannot be changed, added, or removed. This immutability makes tuples hashable and thus usable as keys in **dictionaries**, unlike lists.
  2. **Ordered:** Tuples maintain the order of elements as they were originally defined. This means you can access elements by their index.
  3. **Indexing and Slicing:** You can access tuple elements using indexing and slicing, similar to lists.
  4. **Iterable:** Tuples are iterable, meaning you can loop through their elements using a `for` loop.
  5. **Allow mixed types:** Tuples can contain elements of different data types (integers, strings, lists).

### Basic Syntax

Tuples are defined by enclosing elements in parenthesis `()` **BUT** :warning: what make a tuple, a tuple, is the **comma** `,`. That's why, if you don't add the comma for a single element tuple, it won't be tuple, even if it's betwen `()`, it will be simple a value.

```python

# Example tuple
my_tuple = (1, "apple", 3, "banana", 5, "cherry", 7)

```

:lens: **Note:** A tuple can be created and being empty or having only one single item.

```python

# Empty tuple
empty_tuple = ()
len(empty_tuple) # Output: 0

# Single-item Tuple:
single_item_tuple = "hello",
len(single_item_tuple) # Output: 1
print(single_item_tuple) # Output: ('hello',)
```

### Key operation of tuples:

Tuples have a more limited set of operations compated to lists, giver their immutable nature. 

- **Indexing:** Access the element at a specific position.

```python

my_tuple = (1, "apple", 3, "banana", 5, "cherry", 7)
print(my_tuple[1])  # Output: "apple"

``` 

- **Slicing:** Retrieve a slice of the tuple. 

```python

print(my_tuple[2:5])  # Output: (3, "banana", 5)

``` 

- **Concatenation:** Combine two tuples into a new tuple 

```python

another_tuple = (9, "kiwi")
combined = my_tuple + another_tuple
print(combined)  # Output: (1, "apple", 3, "banana", 5, "cherry", 7, 9, "kiwi")


``` 

- **Repetition:** Repeat the elements of the tuple

```python

repeated = my_tuple * 2
print(repeated)  # Output: (1, "apple", 3, "banana", 5, "cherry", 7, 1, "apple", 3, "banana", 5, "cherry", 7)


``` 

- **Length:** Get the number of elements in the tuple. 

```python

print(len(my_tuple))  # Output: 7

``` 

- **Membership:** Check if an item is in the tuple. 

```python

print("banana" in my_tuple)  # Output: True
print(10 in my_tuple)  # Output: False


``` 

- **Index method:** Find the index of the first occurence of a value.

```python

print(my_tuple.index("cherry"))  # Output: 5

``` 

- **Count method:** Count the number of occurences of a value.

```python

print(my_tuple.count("apple")) # Output: 1

``` 

- **Unpacking:** Assign tuple elements to multiple variables.

```python

a, b, c, d, e, f, g = my_tuple
print(a, b, c, d, e, f, g) # Output: 1 apple 3 banana 5 cherry 7

``` 

- **Nested tuples:** Access elements withing nested tuples.

```python

nested_tuple = (1, ("apple", 2), 3)
print(nested_tuple[1][0])  # Output: "apple"

``` 

## Sets

### Definition:

Sets are another built-in data type in Python. A **set** is an **unordered collection** of unique elements. Sets are used to store multiple items, but unlike lists or tuples, they do not allow **duplicate** values, and theur elements are not ordered, meaning they don't have a specific positions or index.

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

- **<span style="color:red">No</span> duplicate:** If you add the same element more than once, the set will only store it once.

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

```
- **Intersection:** Returns only the elements that are present in both sets. 

```python

print(set1 & set2) # Output {3}

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

### Set comprehension

Similar to [list comprehension](https://github.com/ArcturusSky/holbertonschool-higher_level_programming/blob/main/python-data-structures/README_list.md#list-comprehensions), set comprehensions allow for concise set creations.



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

## Conclusion

Choosing the right data structure is key to efficient programming. **Strings** are great for text manipulation, **lists** for dynamic collections, **tuples** for immutable groupings, **sets** for unique elements, and **dictionaries** for key-value mappings. Understanding their characteristics and appropriate use cases will enhance your ability to solve problems effectively and write clear maintainable code.

## Author

Anne-Cécile Besse (Arc)