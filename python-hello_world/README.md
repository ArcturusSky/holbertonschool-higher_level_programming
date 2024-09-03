# Introduction to Python "Python - Hello, World"

This directory is part of the `higher_level_programming` parent repository focused on Python programming. Here, I'm starting to learn and work with Python basics

Note : I will also update that README.md regarding new concepts I have to learn during these projects.

## Summary

- [Introduction to Python "Python - Hello, World"](#introduction-to-python-python---hello-world)
	- [Summary](#summary)
	- [Glossary (in alphabetical order)](#glossary-in-alphabetical-order)
	- [Forewords](#forewords)
	- [Python Basics](#python-basics)
		- [Definition Python Interpreter](#definition-python-interpreter)
			- [How to Use the Python Interpreter](#how-to-use-the-python-interpreter)
		- [How to Print Text and Variables using `print`](#how-to-print-text-and-variables-using-print)
		- [How to use strings](#how-to-use-strings)
		- [What are Indexing and Slicing in Python ?](#what-are-indexing-and-slicing-in-python-)
		- [PEP 8 Style Guide Summary](#pep-8-style-guide-summary)
			- [Key Points of PEP 8](#key-points-of-pep-8)
				- [1. Indentation](#1-indentation)
				- [2. Line Length](#2-line-length)
				- [3. Blank Lines](#3-blank-lines)
				- [4. Imports](#4-imports)
				- [5. Whitespace](#5-whitespace)
				- [6. Comments](#6-comments)
				- [7. Naming Conventions](#7-naming-conventions)
				- [8. String Quotes](#8-string-quotes)
				- [9. Avoid Complicated Expressions](#9-avoid-complicated-expressions)
				- [10. Programming Recommendations](#10-programming-recommendations)
	- [Differences between C and Python](#differences-between-c-and-python)
		- [1. Variable Declaration](#1-variable-declaration)
		- [2. Semicolons and Blocks](#2-semicolons-and-blocks)
		- [3. **Function Definition**](#3-function-definition)
		- [4. Control Structures](#4-control-structures)
		- [5. Input/Output](#5-inputoutput)
		- [6. Memory Management](#6-memory-management)
		- [7. String Handling](#7-string-handling)
		- [8. Error Handling](#8-error-handling)
		- [9. Comments](#9-comments)
		- [10. Array vs. List](#10-array-vs-list)
		- [11. Type Casting](#11-type-casting)
		- [12. Pointers](#12-pointers)
	- [Conclusion](#conclusion)
	- [Author](#author)

## Glossary (in alphabetical order)

**A**
  - **Name:** 

**B**

  - **Name:** 

**C**

  - **Name:** 

**D**

  - **Name:** 

**E**

  - **Name:** 

**F**  

  - **Name:** 

**G**  

  - **Name:** 

**H**  

  - **Name:** 

**I**  

  - **Name:** 

**J**

  - **Name:** 

**K**

  - **Name:** 

**L**

  - **Name:** 

**M**

  - **Name:** 

**N**

  - **Name:** 

**O**  

  - **Name:** 

**P**  

  - **Name:** 

**Q**  

  - **Name:** 

**R**  

  - **Name:**

**S**

  - **Name:** 

**T**

  - **Name:** 

**U**

  - **Name:** 

**V**

  - **Name:** 

**W**

  - **Name:** 

**X**  

  - **Name:** 

**Y**  

  - **Name:** 

**Z**  

  - **Name:**  

## Forewords

This directory is a little bit different from any other I've done before because it's the turnaway between the C language and Python. Considering that it can't be divided in concept as before (maybe for later projects, but not this one). And so, to avoid having an empty README.md I will compile some information about Python basics.

## Python Basics

### Definition Python Interpreter
The Python interpreter is a program that read and executes Python code.

#### How to Use the Python Interpreter

- **Running Python Code Interactively:**
  
  - You can open a terminal or command prompt and type `python` or `python3` (depending on your installation) to start the Pythin interpreter.
  
  - In the interactive shell, you can type Python commands, and they will be executed immediately.

- **Running Python scripts:**
  
  - You can save your Python code in a file with a `.py` extension and run it by typing `pythin filename.py` in the terminal.   

### How to Print Text and Variables using `print`

In Python, the `print()` function is used to ourput data to the consol. You can print strings and variables like this:

```python
# Printing text
print("Hello, World!")

# Printing a variable
name = "Alice"
print(name)

# Printing text and variables together
age = 30
print("Name:", name, "Age:", age)

# Using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")
```

### How to use strings

You can use single, double, or triple quotes to define strings in Python.

  - **Defining strings:**

```python
single_quote_string = 'Hello'
double_quote_string = "World"
triple_quote_string = '''This is a 
multiline string'''

```

  - **Common string operations:**

```python
# Concatenation
greeting = "Hello" + " " + "World"

# Repetition
repeated = "Hi! " * 3

# Accessing characters (indexing)
first_char = greeting[0]  # 'H'

# Length of the string
length = len(greeting)

# Methods like lower(), upper(), replace(), etc.
lower_greeting = greeting.lower()
replaced_greeting = greeting.replace("World", "Python")

```

### What are Indexing and Slicing in Python ?

  - **Indexion:**
    
	- Indexing allows you to access individual characters in a string using their position (index).
	- Python uses zero-based indexing, so the first character has an index of **`0`**.

```python 
text = "Python"
first_letter = text[0]  # 'P'
last_letter = text[-1]  # 'n'
``` 

  - **Slicing:**
    
	- Slicing allows you to access a subset of a string by specifying a start and end index.
	- The syntax is **`string[start:end]`**, where **`start`** is inclusive and **`end`** is exclusive.

```python
text = "Python"
first_three = text[0:3]  # 'Pyt'
last_three = text[-3:]   # 'hon'
middle = text[1:4]       # 'yth'
``` 

### PEP 8 Style Guide Summary

PEP 8 is the official Python style guide that provides conventions for writing clean, readable, and consistent Python code. It is widely adopted by the Python community and serves as a standard for Python coding practices.

#### Key Points of PEP 8

##### 1. Indentation
- Use **4 spaces** per indentation level. Avoid using tabs.
- Continuation lines should align with the opening delimiter or be indented by 4 spaces from the previous line.

##### 2. Line Length
- Limit all lines to a maximum of **79 characters**.
- For long blocks of text (e.g., comments or docstrings), limit to **72 characters**.

##### 3. Blank Lines
- Use blank lines to separate functions, classes, and blocks of code inside functions.
- Use **two blank lines** before top-level functions and classes, and **one blank line** between methods inside a class.

##### 4. Imports
- Place all imports at the top of the file, after any module comments and docstrings.
- Group imports into three categories:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library-specific imports
- Each group should be separated by a blank line.

##### 5. Whitespace
- Avoid extraneous whitespace in the following situations:
  - Inside parentheses, brackets, or braces: `foo(1)`
  - Before a comma, semicolon, or colon: `if x == 42:`
  - Immediately before an opening parenthesis in a function call: `func(42)`
- Always use a **single space** around operators and after commas.

##### 6. Comments
- Comments should be complete sentences and should be used to explain **why** something is done, not **what** is done.
- Use inline comments sparingly and place them at least two spaces away from the code they explain.
- Use block comments to describe more complex code sections and **docstrings** to describe modules, classes, and functions.

##### 7. Naming Conventions
- Variable and function names should be in `lower_case_with_underscores`.
- Class names should follow the `CapWords` convention (e.g., `MyClass`).
- Constants should be in `ALL_CAPS_WITH_UNDERSCORES`.
- Avoid using single-character variable names except for counters in loops.

##### 8. String Quotes
- Consistently use **single (`'`) or double (`"`) quotes** for strings, but be consistent within a file.

##### 9. Avoid Complicated Expressions
- Break down complex expressions into simpler, more readable ones.

##### 10. Programming Recommendations
- Use `is` and `is not` when comparing to `None`.
- Avoid using wildcard imports (`from module import *`).
- Use `if x is not None:` instead of `if not x:` when checking for `None`.

## Differences between C and Python

Here’s a comparison of the main differences in coding between C and Python, focusing on syntax, structure, and common programming practices:

### 1. Variable Declaration

C: Variables must be explicitly declared with a type before use.

```c
int x = 10;
float y = 5.5;
char z = 'A';
```

Python: Variables are dynamically typed, so you don't need to declare the type explicitly.

```python
x = 10
y = 5.5
z = 'A'
```
### 2. Semicolons and Blocks

C: Statements end with a semicolon (;), and blocks of code are defined using braces ({}).

```c

int main() {
    int x = 10;
    if (x > 5) {
        printf("x is greater than 5");
    }
    return 0;
}
```

Python: No semicolons needed, and blocks of code are defined by indentation.

```python

x = 10
if x > 5:
    print("x is greater than 5")
```


### 3. **Function Definition**

- **C**: Functions must be declared with a return type, and parameters also need their types specified.
 
```c
  int add(int a, int b) {
      return a + b;
  }
```

Python: Functions are defined using def, and you don’t specify the return type or parameter types.

```python

def add(a, b):
    return a + b
```

### 4. Control Structures

C: Uses for, while, and do-while loops, with traditional for loop syntax requiring initialization, condition, and increment/decrement in a single line.

```c

for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}
```

Python: Also uses for and while loops, but for loops iterate directly over sequences (like lists).

```python

for i in range(10):
    print(i)
```

### 5. Input/Output

C: Uses printf and scanf for output and input, respectively.

```c

int age;
printf("Enter your age: ");
scanf("%d", &age);
```

Python: Uses print for output and input for input.

```python

age = int(input("Enter your age: "))
```

### 6. Memory Management

C: Manual memory management using malloc, calloc, and free.

```c

int *ptr = (int*) malloc(sizeof(int) * 5);
free(ptr);
```

Python: Automatic memory management with garbage collection. No need for manual memory allocation or deallocation.

```python

lst = [0] * 5
```

### 7. String Handling

C: Strings are arrays of characters and require null terminators (\0). You manipulate strings using functions like strcpy, strcat, etc.

```c

char name[20];
strcpy(name, "Alice");
```

Python: Strings are objects with built-in methods for manipulation.

```python

name = "Alice"
```

### 8. Error Handling

C: Uses return codes or errno for error handling. More complex error handling might use setjmp and longjmp.

```c

FILE *file = fopen("data.txt", "r");
if (file == NULL) {
    printf("Error opening file");
    return 1;
}
```

Python: Uses exceptions with try, except, and finally blocks.

```python

try:
    file = open("data.txt", "r")
except IOError:
    print("Error opening file")
```

### 9. Comments

C: Single-line comments start with `/*`, and multi-line comments are enclosed in /* */.

```c

/* This is a single-line comment /*

/** 
 * This isa multi-line
 * comment */
```

Python: Single-line comments start with #. Multi-line comments are often created using triple quotes ("""), though these are technically multi-line strings.

```python

# This is a single-line comment
"""
This is
a multi-line
comment
"""
```

### 10. Array vs. List

C: Arrays are fixed-size and require explicit type declarations.

```c

int arr[5] = {1, 2, 3, 4, 5};
```

Python: Lists are dynamic, can hold elements of different types, and are more flexible.

```python

arr = [1, 2, 3, 4, 5]
```

### 11. Type Casting

C: Type casting is explicit and required for certain operations.

```c

float a = 10.5;
int b = (int) a;
```

Python: Type casting is also explicit, but it's often done using built-in functions.

```python

a = 10.5
b = int(a)
```

### 12. Pointers

C: Pointers are used for direct memory access and manipulation.

```c

int x = 5;
int *p = &x;
```

Python: No direct equivalent of pointers. Variables are references to objects, and memory management is abstracted away.

```python

x = 5
p = x  # p is just another reference to the object
```

These differences highlight how C is more low-level and requires explicit management of many aspects of programming (e.g., memory, data types), whereas Python is higher-level, focusing on simplicity and readability.

## Conclusion

To conclude, Python has the same essence as the C language but with simpler ways for some part, and harder for others.

## Author

Anne-Cécile Besse (Arc)