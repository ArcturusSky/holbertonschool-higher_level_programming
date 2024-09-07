# Python - Modules

This directory hold all the task to get introduce to the concept of **import** and **modules** in Python. This README.md will contain a small course about them.

## Summary

- [Python - Modules](#python---modules)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [Introduction to modules](#introduction-to-modules)
  - [Creating and using modules](#creating-and-using-modules)
    - [Importing the whole module](#importing-the-whole-module)
    - [Importing specific attributes](#importing-specific-attributes)
    - [Importing all attributes (NOT RECOMMENDED)](#importing-all-attributes-not-recommended)
    - [Aliasing modules and attributes](#aliasing-modules-and-attributes)
  - [Advanced module usage](#advanced-module-usage)
    - [Executing modules as scripts](#executing-modules-as-scripts)
    - [The module search path](#the-module-search-path)
  - [Packages](#packages)
    - [Example package structure](#example-package-structure)
    - [Importing from packages](#importing-from-packages)
  - [Intra-package references](#intra-package-references)
    - [Absolute Imports](#absolute-imports)
    - [Relative Imports](#relative-imports)
  - [Package in multiple directories](#package-in-multiple-directories)
  - [Conclusion](#conclusion)
  - [Author](#author)

## Glossary

**A**
- **Alias:** A different name given to a module or its attributes using the `as` keyword.

**I**
- **Import:** A statement used to include a module or its attributes into another script.
- **Intra-package reference:** A way to refer to submodules or sibling modules within the same package.

**M**
- **Module:** A Python file containing definitions and statements that can be reused in other programs.

**P**
- **Package:** A collection of modules organized into a directory hierarchy, with an `__init__.py` file indicating that the directory is a Python package.
- **Path (sys.path):** A list of directories Python searches when importing modules.

**R**
- **Relative Import:** A method of importing modules within the same package using a relative path (`.` for the current package or `..` for the parent package).

**S**
- **Shebang:** A special line in Unix-like systems that indicates the interpreter path used to run the script.
- **Standalone Script:** A script that can be executed directly from the command line, often identified using `if __name__ == "__main__":`.

**T**
- **Top-level module:** A module that is not part of a package and can be imported directly.

**U**
- **__path__ attribute:** A list that can be modified to specify additional directories where Python will search for submodules.

 

## Introduction to modules

In Python, a **module** is a file containing Python definitions and statements. Modules help you organize and reuse code efficiently. The file name is the module name with the suffix `.py` appended.

**Key Point:**

  - **Modules** allow you to split your program into multiples files for easier maintenance.
  
  - They help avoiding code duplication by allowing the reuse of functions and variables across different programs.

*Example:*

*Let's create a file name `fibo.py` with the following content:*

```python
# Fibonacci numbers module

def fib(number):    # Write Fibonacci series up to number
    a, b = 0, 1
    while a < number:
        print(a, end=" ")
        a, b = b, a+b
    print()

def fib2(number):   # Return Fibonacci series up to number
    result = []
    a, b = 0, 1
    while a < number:
        result.append(a)
        a, b = b, a+b
    return result

```

You can then **import** this **module** and use it's functions:

```python

import fibo

fibo.fib(1000) # Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print(fibo.fib2(100)) # Output : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

```

## Creating and using modules

To use a module, you **import** it into your script. You can importe an entire module or specific attributes from it.

### Importing the whole module

```python

import fibo
fibo.fib(500)
```

### Importing specific attributes

```python

from fibo import fib
fib(500)
```

### Importing all attributes (NOT RECOMMENDED)

```python

from fibo import *
fib(500)
```

### Aliasing modules and attributes

You can give a module or its attributes a different name:

```python

import fibo as fb
fb.fib(500)

from fibo import fib as fibonacci
fibonacci(500)

```

## Advanced module usage

### Executing modules as scripts

Modules can be run as standalone scripts. Use the following code to check if a module is being run as the main program:

```python

if __name__ == "__main__":
    import sys
    fib(int(sys.arv[1]))

```

### The module search path

When importing modules, Python searches directories listed in `sys.path`. You can modify this path to include custom directories.

```python

import sys
sys.path.append('/your/custom/path')

```

## Packages

Packages are a way to organize modules into a directory hierarchy. A package is a directory containing an `__init__.py` file and submodules.

### Example package structure

```python

__init__.py
formats/
    __init__.py
    wavread.py
    wavwrite.py
effects/
    __init__.py
    echo.py
filters/
    __init__.py
    equalizer.py

```

### Importing from packages

```python

import sound.effects.echo
from sound.effects import echo
from sounds.effects.echo import echofilter
```

## Intra-package references

You can use absolute and relative imports withing packages to refer to submodules.

### Absolute Imports

```python

from sound.effects import echo

```

### Relative Imports

```python

from . import echo
from .. import formats
from ..filters import equalizer

```

## Package in multiple directories

Packages can be extended by modifying the __path__ attribute, which holds the directories where submodules are searched.

## Conclusion


## Author

Anne-Cécile Besse (Arc)