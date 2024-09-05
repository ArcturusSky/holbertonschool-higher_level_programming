# Python - Programming for Begginers (Refreshing memories)

This repository will hold all the directories, projects and task about **Python**. In this README.md you will find some reminders like "what is a variable" "how to assign values" etc, to get back memmories from the "C" learnt previously. However its quality of reminder, it also add some concepts and syntax unique to Python.

## Summary

- [Python - Programming for Begginers (Refreshing memories)](#python---programming-for-begginers-refreshing-memories)
	- [Summary](#summary)
	- [Glossary](#glossary)
	- [Forewords: What is Python and why is indentation important](#forewords-what-is-python-and-why-is-indentation-important)
	- [Variables and How to assign values](#variables-and-how-to-assign-values)
	- [Using comments to document code](#using-comments-to-document-code)
	- [`if`, `else`, and `Elif` statements](#if-else-and-elif-statements)
	- [Loops: `While` and `For`](#loops-while-and-for)
		- [`while` Loop](#while-loop)
		- [`for` loop](#for-loop)
	- [The `range()` function](#the-range-function)
	- [`break`, `continue`, and `else` clauses in Loops](#break-continue-and-else-clauses-in-loops)
		- [`Break`](#break)
		- [`continue`](#continue)
		- [`else` clause in loops](#else-clause-in-loops)
	- [Functions in Python](#functions-in-python)
	- [`return` statements in functions](#return-statements-in-functions)
	- [Variable scope (Local vs Global)](#variable-scope-local-vs-global)
	- [`pass` statement](#pass-statement)
	- [Arithmetic operators](#arithmetic-operators)
	- [Tracesbacks and handling Errors](#tracesbacks-and-handling-errors)
	- [Conclusion](#conclusion)
	- [Author](#author)

## Glossary

**A**
- **Arithmetic Operators:** Symbols that represent basic mathematical operations like addition and multiplication.

**B**
- **`break`:** A statement used to exit a loop prematurely.

**C**
- **Comments:** Lines in the code that are ignored by Python, used for documentation.
- **`continue`:** A statement used to skip the rest of a loop iteration and proceed to the next one.

**F**
- **Function:** A block of reusable code that performs a specific task.

**I**
- **`if` Statement:** A conditional statement that runs a block of code only if the condition is true.
- **Indentation:** The use of spaces or tabs to define code blocks in Python.

**L**
- **Loops:** Constructs that repeat a block of code until a condition is met (`while`, `for`).

**P**
- **`pass`:** A statement used as a placeholder when no code is needed.

**R**
- **`range()`:** A function that generates a sequence of numbers.

**S**
- **Scope:** The region of the program where a variable is accessible.

**T**
- **Traceback:** An error message showing where and why a program crashed.
 

## Forewords: What is Python and why is indentation important

Python is a **high-level programming language** known for its readability and ease of use. One thing that makes Python unique is its **use of indentation** to define the structure of the code.

In Python, blocks of code are not defines by braces `{}` as in languages like C or Java. Instead, indentation (a number of spaces or tabs) is used to groupe code. Incorrect indentation will result in a syntax error.

*Example:*

```python

if x > 0:
	print("Positive number")
else:
	print("Non-positive number")
```

**Key Points:**

  - Indentation is mandatory in Python and must be consistent.
  - Incorrect indentation leads to errors.

## Variables and How to assign values

A **variable** is used to store a value that can be used later in your program. To assign a value to a variable, use the `=` operator. They also don't need to specified their type, Python automatically knows regarding the value given to it.

*Example:*

```python

number = 10
name = "Alice"
```

**Key Points:**

  - Variable names should be descriptive.
  - Variable names cannot start with a number or contain spaces
  - Variable types isn't necessary and it's automatically understood.

## Using comments to document code

Comments help to explain what your code does. They are ignored by ÿthon and are useful for documentation. In Python, comments start with the `#` symbol

*Example:*

```python

# This is a comment
x = 10 # This assigns 10 to x
``` 
**Key Points:**

  - Use comments to make your code easier to understand.
  - Comments do not affect the program's output.

## `if`, `else`, and `Elif` statements

The `if` statement allows you to run a block of code only if a certain condition is true. The `else` statement specifies what happens if the condition is false, and `elif` allows for multiple conditions. 

:warning: Contrary to the C language in which `{}` where needed after each of these statements. In Python a **`:`** is **mandatory** after the condition or the statement it self.

*Example:*

```python

x = 5
if x > 10:
	print("Large number")
elif x == 5:
	print("Medium number")
else:
	print("Small number")
```

**Key Points:**

  - `if` checks a condition.
  - `elif` is used for multiple conditions
  - `else` is executed if non 

## Loops: `While` and `For`

### `while` Loop

The `while` loop repeats a bloc of code as long as a condition is true.

*Example:*

```python
i = 0
while i < 5:
	print(i)
	i += 1
```

### `for` loop 

The `for` loop iterates over a sequence (like a list, string or range)

*Example:*

```python
for i in range(5):
	print(i)
```

**Key Points:**

  - Use `while` when the number of iterations is not known in advance.
  - Use `for` when you need to iterate over a sequence of items.

## The `range()` function

The `range()` function generates a sequence of nnumbers, which is often used in loops. By default, it starts at 0 and increments by 1.

*Example:*

```python

for i in range(3, 10, 2): # Start at 3, end at 9, step by 2
	print(i)

```

## `break`, `continue`, and `else` clauses in Loops

### `Break`

The `break` statement is used to exit a loop prematurely.

*Example:*

```python

for i in range(10):
	if i == 5:
		break
	print(i)

```

### `continue`

The `continue` statement skips the rest of the current loop iteration and moves to the next one.

*Example:*

```python

for i in range(10):
	if i == 5:
		continue
	print(i)

```

### `else` clause in loops

The `else` block after a loop is executed if the loop completes without a `break`.

*Example*

```python

for i in range(5):
	print(i)
else:
	print("loop completed")

```


## Functions in Python

A function is a reusable block of code that performs a specific task. You define a function using the `def` keyword.

*Example*

```python

def greet(name):
	return "Hello" + name

print(greet("Alice")) #Outputs: Hello, Alice)
```

**Key points:**

  - Functions make code reusable.
  - Functions can take inputs (parameters) and return outputs.

## `return` statements in functions

The `return` statement ends a function and retuns a value. If a function doesn't have a `return` statement, it returns `None`.

*Example:*

```python

def add(a, b):
	return a + b

result = add(3, 4) #result will be 7

```

## Variable scope (Local vs Global)

The **scope** of a variable refers to where it can be accessed in your program.

  - **Local variables** are declared inside a function and cannot be accessed outside.
  - **Global variables** are declared outside any function and can be accessed anywhere in the program.

*Example*

```python

x = 10 # Global variable

def my_function():
	y = 5 # Local variable
	print(x) # Accessing global variable

my_function()
print(y) # Error: y us not defined  outside the function

```


## `pass` statement

The `pass` statement is used as a placeholder when a statement is required syntactically, but you don't want to write any code yet.

*Example:*

```python

def unfinished_function():
	pass

```

## Arithmetic operators

Python supports standard arithmetic operations:

  - `+` Addition
  - `-` Substraction
  - `*` Multiplication
  - `/` Division
  - `//` Integer Division
  - `%` Modulo
  - `**` Exponentiation

*Example:*

```python

x = 10
y = 3
print(x + y) # 13
print (x ** y) # 1000

```

## Tracesbacks and handling Errors

A **traceback** is the error message that Python displays when an exception occurs. It shows where the error happened and what caused it.

*Example of a simple error and its traceback:*

```python
print(1 / 0) # Output: "ZeroDivisionError: division by zero"
```


## Conclusion


## Author

Anne-Cécile Besse (Arc)