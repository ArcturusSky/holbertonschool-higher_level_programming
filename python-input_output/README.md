# Python - Input/Output

Welcome to this comprehensive course on Python input/output operations and related concepts. This course is designed to help you understand the fundamentals of reading and writing files, working with JSON data, and handling command-line arguments in Python. It is structured to be easy to follow, with clear examples and explanations, making it perfect for beginners and those looking to refresh their memories.


## Summary

- [Python - Input/Output](#python---inputoutput)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [Why Python Programming is Awesome](#why-python-programming-is-awesome)
    - [Reasons Python is Awesome](#reasons-python-is-awesome)
  - [Working with Files in Python](#working-with-files-in-python)
    - [Opening Files](#opening-files)
    - [Reading Files](#reading-files)
    - [Writing to Files](#writing-to-files)
    - [Closing Files Automatically](#closing-files-automatically)
  - [Serializing and Deserializing Data with JSON](#serializing-and-deserializing-data-with-json)
    - [Serialization](#serialization)
    - [Deserialization](#deserialization)
  - [Accessing Command Line Arguments in Python](#accessing-command-line-arguments-in-python)
    - [Accessing Command Line Arguments](#accessing-command-line-arguments)
    - [Handling Command Line Arguments](#handling-command-line-arguments)
  - [Author](#author)

## Glossary

**A**
- **Append Mode:** A file mode that allows adding data to the end of an existing file without overwriting its contents.

**B**
- **Binary Files:** Files containing raw bytes rather than text, used for non-text data like images, audio, and video.

**C**
- **Command-Line Arguments:** Parameters passed to a script when executed from the command line, accessible via `sys.argv`.

**D**
- **Deserialization:** The process of converting a JSON string back into a Python object.

**E**
- **Encoding:** The character encoding used when reading or writing text files, such as UTF-8.

**F**
- **File Object:** An object returned by the `open()` function, representing a file on the system.

**J**
- **JSON:** A lightweight data interchange format easy for humans to read/write and machines to parse/generate.

**O**
- **Open() Function:** A built-in Python function used to open files, taking filename, mode, and optional encoding.

**P**
- **Print() Function:** A built-in Python function used to display output to the console or other output streams.

**R**
- **Read Mode:** A file mode that allows reading from a file without modifying its contents.

**S**
- **Serialization:** The process of converting a Python object into a JSON string.
- **Standard Input:** The input stream that is the source of data for the program, typically the keyboard.
- **Standard Output:** The output stream where program results are displayed, typically the console.
- **Standard Error:** The output stream where error messages are displayed, typically the console.
- **Sys Module:** A Python module providing access to interpreter variables and functions.

**W**
- **With Statement:** A statement ensuring resources like files are properly closed after use, even if exceptions occur.
- **Write Mode:** A file mode that allows writing to a file, overwriting any existing contents.

## Why Python Programming is Awesome

**Definition**

Python is a high-level, general-purpose programming language that is widely praised for its simplicity, readability, and versatility. Python's clean syntax, extensive libraries, and large community make it an excellent choice for a wide range of applications, from web development and data analysis to automation and machine learning.

### Reasons Python is Awesome

1. **Simplicity**: Python has a very clean and readable syntax, making it easy to learn and understand, even for beginners.
2. **Versatility**: Python can be used for a wide variety of tasks, from web development and data analysis to automation and machine learning.
3. **Extensive Libraries**: Python has a vast ecosystem of libraries and frameworks that provide pre-built functionality, saving developers time and effort.
4. **Cross-Platform**: Python code can run on multiple operating systems, including Windows, macOS, and Linux, making it a portable language.
5. **Large Community**: Python has a large and active community of developers who contribute to the language, create new libraries, and provide support and resources.
6. **Interpreted**: Python is an interpreted language, which means it can execute code directly without the need for compilation, making it easier to test and debug.
7. **Dynamic Typing**: Python is dynamically typed, which allows for more flexible and expressive code, without the need for explicit type declarations.
8. **Productivity**: Python's simplicity and extensive libraries allow developers to write more code in less time, increasing overall productivity.

**Memory Aid**: Think of Python as the "Swiss Army Knife" of programming languages - it's versatile, easy to use, and has a tool for just about any task you can imagine.

**Real-Life Analogy**: Python is like a trusty companion that makes your programming life easier, just like a Swiss Army Knife makes your everyday tasks more manageable.

## Working with Files in Python

**Definition**

Files are a fundamental way to store and retrieve data in Python. The built-in `open()` function is used to open files, and various methods are available to read from and write to these files.

### Opening Files

To open a file, use the `open()` function with the file name and mode:

*Example:*

```python
file = open('example.txt', 'r')
```

**Explanations, breakdown of the example:**

- **Modes**: `'r'` (read), `'w'` (write), `'a'` (append), `'r+'` (read and write)

### Reading Files

To read the contents of a file, use the `read()` or `readlines()` methods:

*Example:*

```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

**Explanations, breakdown of the example:**

- **`file.read()`**: Reads the entire contents of the file as a single string.
- **`file.readlines()`**: Reads the file line by line and returns a list of strings.

**Note:** To read file with special encoding, adding `encoding=''` with the special encoding between the `''`.

*Example:*

```python
file = open('example.txt', encoding='utf-8')
```

### Writing to Files

To write to a file, open it in write or append mode and use the `write()` method:

*Example:*

```python
file = open('example.txt', 'w')
file.write('Hello, world!')
file.close()
```

**Explanations, breakdown of the example:**

- **`'w'`**: Opens the file in write mode, overwriting the existing contents.
- **`file.write()`**: Writes the specified string to the file.

### Closing Files Automatically

The `with` statement ensures that a file is properly closed, even if an exception occurs:

*Example:*

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

**Explanations, breakdown of the example:**

- The `with` statement automatically calls `file.close()` when the block is exited, ensuring the file is properly closed.

**Memory Aid**: Think of opening a file like opening a book - you need to open it, read or write, and then close it when you're done.

**Real-Life Analogy**: Working with files in Python is like using a physical file cabinet - you need to open the drawer, retrieve or store the document, and then close the drawer when you're finished.

## Serializing and Deserializing Data with JSON

**Definition**

JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. Python's `json` module provides tools to serialize Python objects into JSON strings and deserialize JSON strings back into Python objects.

### Serialization

Serialization is the process of converting a Python object into a JSON string:

*Example:*

```python
import json

python_data = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(python_data)
print(json_data)
```

**Explanations, breakdown of the example:**

- **`json.dumps()`**: Converts a Python object (dictionary in this case) into a JSON string.

### Deserialization

Deserialization is the process of converting a JSON string back into a Python object:

*Example:*

```python
import json

json_string = '{"name": "John", "age": 30}'
python_object = json.loads(json_string)

```

**NOTE:** if it's the whole json file you want to use and not a JSON **string** then:

```python
import json

with open('my_file.json', 'r') as file:
    python_object = json.load(file)

```

**Explanations, breakdown of the example:**

- **`json.loads()`**: Converts a JSON **string** into a Python object (dictionary in this case).

**Memory Aid**:

- **Serialization**: Think of it as "packing" your Python data into a JSON "suitcase" for easier transport.
- **Deserialization**: Think of it as "unpacking" the JSON "suitcase" to get your Python data back.



## Accessing Command Line Arguments in Python

**Definition**

In Python, you can access the command line arguments passed to your script using the `sys` module.

### Accessing Command Line Arguments

To access command line arguments, import the `sys` module and use the `sys.argv` list:

*Example:*

```python
import sys

print(sys.argv)
```

**Explanations, breakdown of the example:**

- **`sys.argv`**: A list containing all the command line arguments passed to the script.
- `sys.argv[0]` is the name of the script itself, and the remaining elements are the actual arguments.

### Handling Command Line Arguments

You can use a loop or indexing to access the individual command line arguments:

*Example:*

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py [arguments]")
else:
    for arg in sys.argv[1:]:
        print(arg)
```

**Explanations, breakdown of the example:**

- **`len(sys.argv)`**: Checks the number of command line arguments.
- **`sys.argv[1:]`**: Slices the `sys.argv` list to exclude the script name and only include the actual arguments.

**Memory Aid**: Think of `sys.argv` as a list of all the words you typed when you ran your Python script, with the first word being the script name itself.

**Real-Life Analogy**: Accessing command line arguments is like asking someone to give you a list of all the items they brought with them to a meeting - the first item is the meeting agenda, and the rest are the actual items they brought.

## Author

Anne-Cécile Besse (Arc)