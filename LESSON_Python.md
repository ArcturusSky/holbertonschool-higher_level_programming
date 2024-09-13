# Python - Programming for Begginers

This document will hold information I didn't know where to put in other files/repositories. Some key concepts or not. In anycase it is useful.

## Summary

- [Python - Programming for Begginers](#python---programming-for-begginers)
  - [Summary](#summary)
  - [Classes and Subclasses](#classes-and-subclasses)
    - [Class (or Superclass)](#class-or-superclass)
    - [Subclass (or Derived Class)](#subclass-or-derived-class)
    - [Instance](#instance)
    - [To sum up](#to-sum-up)
  - [:mag: TESTING :wrench:](#mag-testing-wrench)
    - [`doctest` in Python](#doctest-in-python)
      - [What is `doctest`?](#what-is-doctest)
      - [Why Use `doctest`?](#why-use-doctest)
    - [How to Write a `doctest`](#how-to-write-a-doctest)
    - [How to Use doctest](#how-to-use-doctest)
    - [What to Expect from doctest](#what-to-expect-from-doctest)
    - [What is `unittest`?](#what-is-unittest)
      - [Why Use `unittest`?](#why-use-unittest)
      - [How to Write a `unittest`](#how-to-write-a-unittest)
      - [How to use `unittest`](#how-to-use-unittest)
      - [What to expect from `unittest`](#what-to-expect-from-unittest)
      - [To resume](#to-resume)
    - [`unittest` vs. `doctest`](#unittest-vs-doctest)
      - [`unittest`](#unittest)
      - [`doctest`](#doctest)
      - [When to Use Each](#when-to-use-each)
      - [Combining Both](#combining-both)
  
## Classes and Subclasses

### Class (or Superclass)

- **Definition:** A general blueprint.
- **Purpose:** Defines common attributes and methods.

### Subclass (or Derived Class)

- **Definition:** A specialized version of the class.
- **Inheritance:** Inherits methods and attributes from the superclass without rewriting them.
- **Capabilities:**
  - **Modify:** Use `super().method()` to call the superclass's method and extend or modify it.
  - **Add:** Introduce new methods or attributes unique to the subclass.
  - **Override:** Redefine existing methods to change their behavior in the subclass.

### Instance

- **Definition:** A concrete copy of the class blueprint.
- **Purpose:** Created with specific values for its attributes.
- **Functionality:** Uses the class's methods but operates with the values provided during instantiation.

---

### To sum up

- **Class/Superclass:** General template.
- **Subclass:** Specialized version with inherited and/or new features.
- **Instance:** A specific object created from the class blueprint with its own data.

## :mag: TESTING :wrench:

### `doctest` in Python

#### What is `doctest`?

`doctest` is a built-in Python module that allows you to embed tests directly into the docstrings of your functions, methods, or classes. These tests are then run to check if the examples in the documentation work as expected.

#### Why Use `doctest`?

- **Simple Verification:** Great for ensuring that the examples in your documentation are correct.
- **Readable Tests:** Embedding tests in docstrings makes your code easier to understand.
- **Quick Feedback:** It's useful for small, self-contained tests that don’t need a full test framework like `unittest`.

### How to Write a `doctest`

- Include an example of how to use the function in its docstring.
- Start the test with the Python prompt `>>>`, and follow it with expected output.

- **Example:**

```python
def add(a, b):
    """
    Adds two numbers together.

    Example:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

### How to Use doctest

1. **Manually run** the `doctest` by adding this at the bottom of your script:

```python

if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

2. **Run the script:** When you run the script, `doctest` will check if the output matches the expected result in the docstring examples.

3. **Command-line usage:** Alternatively, you can run the tests from the command line:

```bash

python -m doctest -v your_script.py

```

:large_blue_circle: The `-v` option enables verbose mode, which prints the test results even if they pass. This is useful for seeing a detailed output of all tests being run, including their results.


### What to Expect from doctest

- Without the `-v`, if all tests pass, doctest will run silently.
- With the `-v`, you'll see a full breakdown of all tests, whether they pass or fail.
- If a test fails, doctest will show you the expected output and the actual output, so you can identify and fix errors.

- *Example of a failure:*

```python

**********************************************************************
File "your_script.py", line 5, in your_script.add
Failed example:
    add(2, 3)
Expected:
    6
Got:
    5
**********************************************************************
1 items had failures:
   1 of   2 in your_script.add
***Test Failed*** 1 failures.


```

### What is `unittest`?

`unittest` is Python's built-in testing framework. It allows you to write and run tests for your code in a structured way. `unittest` supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of tests from the reporting framework.

#### Why Use `unittest`?

- **Comprehensive Testing:** Good for testing complex logic with multiple conditions.
- **Test Discovery:** Automatically finds and runs tests.
- **Modular and Reusable:** Offers setup and teardown methods for initializing tests.
- **Detailed Reporting:** Provides detailed test results and failure reporting.

#### How to Write a `unittest`

- Define a class that inherits from `unittest.TestCase`
- Inside the class, write methods where each one starts with `test_.`
- Use `assert` methods like `assertEqual()`, `assertTrue()`, `assertRaises()`, etc., to check expected outcomes.

```python

import unittest

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()

```

#### How to use `unittest`

1. **Run the Tests:** Once you’ve written your tests, you can run them using the command:

```bash

python -m unittest your_test_file.py

```

2. **Test Discovery:** `unittest` can automatically discover tests in files starting with test_. Use this command in your project directory:

```bash

python -m unittest discover

```

3. **Command-line usage with verbosity:** To see detailed output, use the -v option:

```bash

python -m unittest -v your_test_file.py

```

This will show the detailed results of each test.

#### What to expect from `unittest`

- **Success**: If all tests pass, you’ll get a summary like `OK`.
- **Failure**: If a test fails, you’ll get detailed information about what went wrong, including the failing test, the expected result, and the actual result.

- *Example of output with a failing test:*

```markdown

F
======================================================================
FAIL: test_add (your_test_file.TestMathFunctions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "your_test_file.py", line 5, in test_add
    self.assertEqual(add(2, 3), 6)
AssertionError: 5 != 6

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=1)

```

#### To resume

`unittest` is a robust testing framework suitable for larger projects and complex test scenarios. It offers structured test writing with setup and teardown options, making it ideal for comprehensive testing. Use the `-v` option for verbose output, showing detailed test results and debugging information.

### `unittest` vs. `doctest`

#### `unittest`

- **Purpose:** Provides a framework for writing and running tests.
- **Features:**
  - Allows you to create test cases and suites.
  - Supports test discovery, setup and teardown, and assertions.
  - Suitable for complex testing scenarios with multiple tests and test cases.

```python
import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
```

#### `doctest`

- **Purpose:** Tests embedded in docstrings.
- **Features:**
  - Allows you to write tests within your docstrings, which can then be automatically tested.
  - Useful for simple examples and ensuring that code snippets in documentation are correct.

```python

def add(a, b):
    """
    Adds two numbers together.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

#### When to Use Each

- **Use `unittest`** when you need a structured approach for testing with:
  - Complex test scenarios.
  - A large number of tests.
  - Advanced features like test discovery and setup/teardown procedures.

- **Use `doctest`** for:
  - Simple checks of code snippets in documentation.
  - Ensuring that examples in docstrings are correct.

#### Combining Both

You can use both `unittest` and `doctest` in the same project. `doctest` can ensure your examples in docstrings work as expected, while `unittest` can handle more comprehensive testing.

```python
import unittest
import doctest

def add(a, b):
    """
    Adds two numbers together.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 1), 2)

if __name__ == "__main__":
    doctest.testmod()
    unittest.main()
```

This way, you can leverage the strengths of both tools to ensure your code is well-tested and documented.