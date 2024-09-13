# Python - Errors and Exceptions

This directory is part of the parent repository `holbertonschool-higher_level_programming` and will focus on **Handling Errors and Exceptions**

## Summary

- [Python - Errors and Exceptions](#python---errors-and-exceptions)
  - [Summary](#summary)
  - [Errors Types](#errors-types)
    - [Syntax Errors](#syntax-errors)
    - [Exceptions](#exceptions)
  - [Handling Exceptions](#handling-exceptions)
    - [Formatted string printing](#formatted-string-printing)
    - [Basic Exception Handling](#basic-exception-handling)
    - [Exception Handling Best Practices](#exception-handling-best-practices)
    - [List Indexing and Out of Range errors](#list-indexing-and-out-of-range-errors)
      - [Accessing list elements safely without `len()`](#accessing-list-elements-safely-without-len)
    - [Multiple Except Clauses](#multiple-except-clauses)
    - [Returning Values from Functions](#returning-values-from-functions)
    - [Catching Multiple Exceptions](#catching-multiple-exceptions)
    - [Exception Hierarchy](#exception-hierarchy)
    - [Exception Arguments](#exception-arguments)
  - [Raising Exceptions](#raising-exceptions)
    - [Using `raise`](#using-raise)
    - [Re-raising exceptions](#re-raising-exceptions)
  - [Exception Chaining](#exception-chaining)
    - [Chaining Exceptions](#chaining-exceptions)
    - [Supressing Chained Exceptions](#supressing-chained-exceptions)
    - [Working with lists containing mixed types](#working-with-lists-containing-mixed-types)
  - [User-Defined exceptions](#user-defined-exceptions)
    - [Creating custom exceptions](#creating-custom-exceptions)
  - [Cleanup Actions](#cleanup-actions)
    - [Using `finally`](#using-finally)
    - [Context Managers](#context-managers)
  - [Handling Multiple Exceptions](#handling-multiple-exceptions)
  - [Conclusion](#conclusion)
  - [Author](#author)

**A**

- **Argument**: Data passed to a function or method, used in raising exceptions or processing user input.

**B**

- **BaseException**: The base class for all built-in exceptions in Python. All exceptions inherit from it, but not typically used for exception handling.

**C**

- **Class**: A blueprint for creating objects. In exception handling, custom exceptions are often derived from the `Exception` class.
- **Chaining (Exception Chaining)**: Linking one exception to another by raising a new exception while handling a previous one.

**D**

- **DivisionByZeroError**: Exception raised when attempting to divide by zero.
- **Detail**: The specific message or information provided when an exception is raised, explaining the cause of the error.

**E**

- **Exception**: The base class for all non-fatal errors in Python. Exceptions indicate conditions that a program should handle.
- **Except clause**: A block of code that catches and handles exceptions when they occur in the corresponding `try` block.
- **Error**: A problem that occurs during program execution. Can be categorized into syntax errors and exceptions.
- **Else clause**: An optional clause in a `try` block that executes only if no exceptions occur.
  
**F**

- **FileNotFoundError**: Exception raised when trying to open a file that doesn’t exist.

**H**

- **Handler (Exception Handler)**: A block of code within an `except` clause that defines how to respond to an exception.

**I**

- **ImportError**: Raised when an import statement fails to find the module definition or when an imported module is not found.

**K**

- **KeyboardInterrupt**: Exception raised when the user interrupts program execution, typically with `Ctrl+C`.

**N**

- **NameError**: Raised when a local or global name is not found in the namespace.

**O**

- **OSError**: Exception related to system errors like file system operations, including file not found, permissions errors, etc.

**R**

- **Raise statement**: Forces a specified exception to be thrown.
- **RuntimeError**: A generic error that doesn't fall into other categories, indicating a problem during program execution.

**S**

- **SyntaxError**: Raised when Python encounters invalid syntax in the code.
- **Stack traceback**: A report showing the sequence of function calls leading to the exception, useful for debugging.

**T**

- **Try statement**: Defines a block of code to be tested for errors, followed by an `except` block to handle any exceptions that occur.
- **TypeError**: Raised when an operation or function is applied to an object of inappropriate type (e.g., adding a string and an integer).

**V**

- **ValueError**: Raised when a function receives an argument of the correct type but an inappropriate value (e.g., converting a string to an integer where the string isn’t a valid number).

**Z**

- **ZeroDivisionError**: Raised when a division or modulo operation is performed with zero as the divisor.



## Errors Types

### Syntax Errors

Syntax errors occur when the Python parser detects incorrect syntax in the code. These errors are usually due to typos or missing elements.

- *Example:*

```Python

while True print('Hello world')
# Error: SyntaxError: invalid syntax

```

The error message includes a pointer to the exact location of the syntac issue and describes the problem.

### Exceptions

Exceptions are runtime errors that occur when the code is syntactically correct but fails during execution. Examples include:

- **ZeroDivisionError:** Division by zero.
- **NameError:** Using a variable that hasn't been defined.
- **TypeError:** Incorrect data type operations.

- *Example:*

```Python

10 * (1/0) # ZeroDivisionError
'2' + 2    # Type Error

``` 

Exception messages include a traceback that shows where the error occurred and what type of error it was.

## Handling Exceptions

### Formatted string printing

```python

# Using f-strings for cleaner output:
try:
    result = 10 / 0
except ZeroDivisionError:
    print(f"Error: Division by zero")


```

### Basic Exception Handling

Use the `try` and `except` blocs to handle exceptions. The `try` block contains code that may cause an exception, and the `except` bloc contains code to handle the exception if it occurs.

**Syntax**

```python

try:
    # Code tha tmight cause an exception
except ExceptionType:
    # Code that runs if an exception
finally:
    # Code that runs no matter what (example, cleanup actions)

```

- *Example:*

```Python

while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

```

### Exception Handling Best Practices

This example describe when and how to handle specific exceptions and best practices for keeping exception handling clean and clear.

```python

# Best practice: Catch spepcific exceptions, not just a generic "except:"

try:
    x = int("abc")
except ValueError:
    print("ValueError: Could not convert string to integer")

```

### List Indexing and Out of Range errors

```python

# Example of handling IndexError

my_list = [1, 2, 3]
try:
    print(my_list[10]) # Out of range access
except IndexError:
    print("Index out of range")

```

#### Accessing list elements safely without `len()`

```python
# Safely accessing list elements without len()
try:
    element = my_list[10]
except IndexError:
    print("Tried to access an element outside the list")
```



### Multiple Except Clauses

You can handle different types of exceptions separately by specifying multiple `except` clauses.

- *Example:*

```Python

try:
    result = 10 / 0
except: ZeroDivisionError:
    print("Cannot divide by zero.")
except: TypeError:
    print("Type error occured.")

```

### Returning Values from Functions

```python

def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_division(10, 0))  # Output: None

```

### Catching Multiple Exceptions

You can catch multiple exceptions in a single `except` clause using a tuple.

- *Example:*

```Python

try:
    x = int("string")
except (ValueError, TypeError) as e:
    print("Error:", e)

```

### Exception Hierarchy

You can catch exceptions based on their class hierarchy. The first matching `except` clause will handle the exception.

- *Example:*

```Python

classe BaseError(Exception): pass
class DerivedError(BaseError): pass

try:
    raise DerivedError("An error")
except DerivedError:
    print("Handled DerivedError")
except BaseError:
    print("Handled BaseError")

```

### Exception Arguments

Exceptions can have arguments, which are accessible via the `args` attribute.

- *Example:*

```Python

try:
    raise Exception('error message')
except Exception as e:
    print("Exception:", e)

```

## Raising Exceptions

### Using `raise`

You can raise exceptions manually using the `raise` statement.

- *Example:*

```Python
# Raising a custom error

raise ValueError("This is a custom error message")

```

### Re-raising exceptions

You can re-raise the same exception within an `except` block

- *Example:*

```Python

try:
    raise ValueError("Initial error")
except ValueError:
    print("Handling erro")
    raise

```

## Exception Chaining

### Chaining Exceptions

You can chain exceptions to indicate that one exception caused another.

- *Example:*

```Python

try:
    open('nonexistent_file')
except OSError as e:
    raise RuntimeError("Error handling file") from e

```

### Supressing Chained Exceptions

You can suppress the original exception with `from None`.

- *Example:*

```Python

try:
    open("nonexistent_file")
except OSError:
    raise RuntimeError"File error" from None

```

### Working with lists containing mixed types

```python

mixed_list = [1, 'two', 3, None]

for item in mixed_list:
    try:
        print(item * 2)
    except TypeError:
        print(f"Cannot multiply {item} (not a number)")

```

## User-Defined exceptions

### Creating custom exceptions

Create custom exceptions by defining classes that inherit from `Exception`.

- *Example:*

```Python

class CustomError(Exception):
    pass # I guess the condition or the error?

raise CustomError("A custom error occured")

```

## Cleanup Actions

### Using `finally`

The `finally` block is executed regardless of whether an exception occured, and is often used for cleanup actions.

**Syntax**

```python

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("This will always execute")


```

- *Example:*

```Python

try:
    file = open("file.txt")
finally:
    file.close()

```

### Context Managers

Use the `with` statement to ensure resources are properly cleaned up.

- *Example:*

```Python

with open("file.txt") as file:
    content = file.read()

```

## Handling Multiple Exceptions

In some cases, you might need to handle multiple exceptions that occur simultaneously.

- *Example:*

```Python

try:
    # some code
except ExceptionGroup as e:
    for exc in e.exceptions:
        print("Handled:", exc)

```

## Conclusion

By understand and applying these concepts, it's possible to write Python code that is both robust and resilient to errors and exceptions.

## Author

Anne-Cécile Besse (Arc)