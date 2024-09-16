# Python - Classes

This document will hold information I didn't know where to put in other files/repositories. Some key concepts or not. In anycase it is useful.

## Summary

- [Python - Classes](#python---classes)
  - [Summary](#summary)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
    - [Classes and Subclasses](#classes-and-subclasses)
      - [Class (or Superclass)](#class-or-superclass)
      - [Subclass (or Derived Class)](#subclass-or-derived-class)
      - [Instance](#instance)
      - [To sum up](#to-sum-up)
      - [Full hierarchy](#full-hierarchy)
    - [The `self` parameter in Python OOP](#the-self-parameter-in-python-oop)
      - [How to use the `self` parameter in Python](#how-to-use-the-self-parameter-in-python)
    - [Example Defining a Simple Class](#example-defining-a-simple-class)
      - [Defining a Simple class](#defining-a-simple-class)
      - [Adding Methods to a Class](#adding-methods-to-a-class)
      - [The `__init__` Method](#the-__init__-method)
  
## Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a way of structuring programs by combining data and functionality into entities calles **objects**, as opposed to the procedural approach which focuses on functions manipulation data.

- **Classes** and **objects** are core components:
  - A **class** is a blue print or template for creating objects
  - **Objects** are **instances** of **classes**.
- **Fields** (also called **attributes**) refer to variables withing a class:
  - **Instance variables** belong to individual objects
  - **Class variables** are shared by all instances of the class
- **Methods** are functions defined within a class, providing functionality to objects. This disintction is important fo understanding the relationshop between **data** (**fields** or **attributes**) and behavior (**methods**).

**Classes** are defined using the **`class`** keyword, and both **fields** (**attributes**) and **methods** are specified in an indented block under the class definition.

**OOP** is especially useful for larger or more complex programs that benefit from organizing code around objects rather than functions alone.

### Classes and Subclasses

#### Class (or Superclass)

- **Definition:** A general blueprint.
- **Purpose:** Defines common attributes and methods.

#### Subclass (or Derived Class)

- **Definition:** A specialized version of the class.
- **Inheritance:** Inherits methods and attributes from the superclass without rewriting them.
- **Capabilities:**
  - **Modify:** Use `super().method()` to call the superclass's method and extend or modify it.
  - **Add:** Introduce new methods or attributes unique to the subclass.
  - **Override:** Redefine existing methods to change their behavior in the subclass.

#### Instance

- **Definition:** A concrete copy of the class blueprint.
- **Purpose:** Created with specific values for its attributes.
- **Functionality:** Uses the class's methods but operates with the values provided during instantiation.

---

#### To sum up

- **Class/Superclass:** General template.
- **Subclass:** Specialized version with inherited and/or new features.
- **Instance:** A specific object created from the class blueprint with its own data.

#### Full hierarchy 

```plaintext
Class: Animal
│
├── Attributes
│   ├── name
│   └── age
│
├── Methods
│   ├── eat│   └ sleep()
│
├── Subclass: Mammal
│   │
│   ├── Attributes
│   │   ├── fur_color
│   │   └── is_warm_blooded
│   │
│   ├── Methods
│   │   ├── nurse()
│   │   └── run()
│   │
│   └── Subclass: Dog
│       │
│       ├── Attributes
│       │   └── breed
│       │
│       └── Methods
│           ├── bark()
│           └── fetch()
│
└── Subclass: Bird
    │
    ├── Attributes
    │   ├── wing_span
    │   └── can_fly
    │
    ├── Methods
        ├── fly()
        └── sing()
```

### The `self` parameter in Python OOP

In Python, **class methods** differ from ordinary functions because they include an extra first parameter, tipically named **`self`**. This parameter refers to the **current** **instance** (or object) calling the **methods**.

-   **`self`** allows access to the instance's **attributes** and **methods**.
-    You do not pass **`self`** when calling the **method**; Python automatically provides it.

-   *Example:*

```python

myobject.method(arg1, arg2)

```

is internally converted to:

```python

MyClass.method(myobject, arg1, arg2)

```

Even if a method takes no arguments, you still need to include **`self`**. Using the name **`self`** is a convention widely recognized by developers and tools.

#### How to use the `self` parameter in Python

Here's an example that demonstrates how the **`self`** parameter works:

```python

class Dog:
    # Constructor method to initialize the object's attributes
    def __init__(self, name, age):
        self.name = name    # "self.name" refers to the current instance's name attribute
        self.age = age      # "self.age" refers tp the current instance's age attribute 

    # Method to display dog information
    def info(self):
        # Accessing the instance's attributes using "self"
        print("My dog's name is {} and it is {} years old.".format(self.name, self.age))

# Create an instance (object) of the Dog class
my_dog = Dog("Buddy", 5)

# Call the info method (in which there is a "print()")
my_dog.info()
```

**What happens:**

-   When `my_dog.info()` is called, Python automatically converts this to `Dog.info(my_dog)`
-   The **`self`** parameter now refers to **`my_dog`**, allowing access to the instance's `name` and `age` attributes.

**Output:**

```python

# My dog's name is Buddy and it is 5 years old.

```

This shows how `self` connects methods to the specific **object** (**instance**) that calls them, making **object-oriented programming** possible.

### Example Defining a Simple Class

#### Defining a Simple class

Example: `oop_simplestclass.py`

```python

# Define a simple class named Person
class Person:
    pass # An empty block, meaning no attributes or methods

# Create an instance of the Person class
p = Person()
print(p) # Output will show the instance type and memory address
```

**Explanations:**

  - **Class Definition**: **`class Person:`** creates a new class named `Person`. The `pass` statement is used as a placeholder to indicate that the class body is currently empty.

  -  **Instance Creation**: **`p = Person()`** creates an instance (also called "an **object**") of the `Person` class.
  
  -  **Printing the Instance**: `print(p)` displays information about the instance, including its type and memory adress.

#### Adding Methods to a Class

```python

# Defin a class with a method
class Person:
    def say_hi(self):
        # Method to print a greeting
        print('Hello, how are you?')

# Create an instance of the Person class
p = Person()
p.say_hi # Call the say_hi method

```

Output

```bash
$ python oop_method.py
Hello, how are you?
```

**Explanations:**

  - **Method Definition:** `def say_hi(self):` defines a method `say_hi` that prints a greeting. The `self` parameter refers to the instance of the class.
  
  - **Method Call:** `p.say_hi()` calls the `say_hi` method on the instance `p`.

#### The `__init__` Method

```python

# Defin a class with an initializer method
class Person:
    def __init__(self, name):
        # Initialize the instance with a name
        self.name = name

    def say_hi(self):
        # Method to print a greeting with the person's name
        print("Hello, my name is", self.name)

# Create an instance of the Person class with a name
p = Person("Swaroop")
p.say_hi() # Call the say_hi method

```

Output

```bash
$ python oop_init.py
Hello, my name is Swaroop
```


