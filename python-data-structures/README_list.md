# Python Data Structures: Lists, Tuples, Sets and Dictionaries

This repository will hold all the projects and tasks in Python about **Lists** and **Data Structure**.

## Summary

- [Python Data Structures: Lists, Tuples, Sets and Dictionaries](#python-data-structures-lists-tuples-sets-and-dictionaries)
  - [Summary](#summary)
  - [Glossary](#glossary)
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
  - [Conclusion](#conclusion)
  - [Author](#author)

## Glossary

**A**
- **Append:** The `append()` method adds an item to the end of a list.

**C**
- **Concatenation:** Combining two lists into one using the `+` operator.

**D**
- **Deque:** A double-ended queue from the `collections` module that allows for fast appends and pops from both ends.

**E**
- **Extend:** The `extend()` method adds each element of an iterable (e.g., another list) to the end of a list.

**F**
- **Filtering:** The process of creating a new list by including only elements that meet certain criteria, often done using list comprehensions.

**I**
- **Index:** A position in a list, starting from 0, used to access elements.

**L**
- **List:** An ordered, mutable collection of items enclosed in square brackets (`[]`).

**M**
- **Mutable:** A data type that allows modification after creation, such as lists in Python.

**N**
- **Nesting:** The practice of placing one list inside another, allowing for complex data structures.

**P**
- **Pop:** The `pop()` method removes and returns the item at a specified index, or the last item if no index is provided.

**R**
- **Reference:** A variable that points to the same object in memory, such as when assigning one list to another.

**S**
- **Slice:** A subset of a list obtained by specifying a start and end index, creating a new list with the selected elements.

**S**
- **Stack:** A data structure that follows Last In, First Out (LIFO) order, where the most recently added item is the first to be removed.

**Q**
- **Queue:** A data structure that follows First In, First Out (FIFO) order, where the first item added is the first to be removed.

**S**
- **Sort:** The `sort()` method arranges the items of a list in ascending or descending order.

**T**
- **Tuple:** An immutable sequence type in Python, often used to group related items together. (Not covered in the course but related to lists.)

**U**
- **Unpacking:** The process of extracting values from a list (or other iterable) into separate variables.

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
  - `remove(x)` – Remove the first item whose vamue is `x`.
  - `pop([i])` – Remove the item at index `i`(or the last item if `i` is not provided) and return it.
  - `clear()` – Remove all items from the list.
  - `index(x[, start[, end]])` – Return the index of the first occurence of `x`
  - `count(x)` – Return the number of times `x` appears.
  - `sort()` – Sort the list in place.
  - `reverse()` – Reverse the list in place.
  - `copy()` – Return a shallox copy of the list.

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

## Conclusion

This course structure covers Python lists, their operations, methods, and advanced techniques such as stacks, queues, and list comprehensions. Each section provides examples and explanations, making it easy to grasp list manipulation in Python.



## Author

Anne-Cécile Besse (Arc)