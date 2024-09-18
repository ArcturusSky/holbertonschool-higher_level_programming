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
    - [Private and Protected Attributes in Python](#private-and-protected-attributes-in-python)
      - [What Are Private and Protected Attributes?](#what-are-private-and-protected-attributes)
      - [Using Getters and Setters with Private and Protected Attributes](#using-getters-and-setters-with-private-and-protected-attributes)
  - [Example: Private and Protected Attributes with Getters and Setters](#example-private-and-protected-attributes-with-getters-and-setters)
    - [Original Case: A Class with Public Attributes (Initial State)](#original-case-a-class-with-public-attributes-initial-state)
    - [Step 1: Making an attribute protected (or private) without getter and setter](#step-1-making-an-attribute-protected-or-private-without-getter-and-setter)
    - [Step 2.5: Making an Attribute Protected Using Getters and Setters](#step-25-making-an-attribute-protected-using-getters-and-setters)
    - [Step 3: Making an Attribute Private with Getters and Setters](#step-3-making-an-attribute-private-with-getters-and-setters)
  - [Key Points:](#key-points)
  - [Recap:](#recap)
  
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

### Private and Protected Attributes in Python

#### What Are Private and Protected Attributes?

In Python, attributes aren't strictly private, but there are conventions to indicate whether an attribute is public, protected, or private.

- **Public Attributes**: Can be accessed and modified freely from outside the class.
  - Example: `self.name`
- **Protected Attributes**: Indicated by a single underscore (`_attribute`). This signals that the attribute is intended for internal use, but it can still be accessed directly (though it's discouraged).
  - Example: `self._age`
- **Private Attributes**: Indicated by double underscores (`__attribute`). This is intended to make the attribute private, meaning it can't be accessed directly from outside the class. This triggers name mangling, which makes it harder (but not impossible) to access the attribute.
  - Example: `self.__salary`

#### Using Getters and Setters with Private and Protected Attributes

You can use **getters** and **setters** to control access to private and protected attributes. This allows you to make an attribute effectively private by controlling how it's accessed and modified.

---

## Example: Private and Protected Attributes with Getters and Setters

### Original Case: A Class with Public Attributes (Initial State)

Here’s an example with public attributes:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self.salary = salary  # Public attribute

employee = Employee("Alice", 50000)

# Accessing and modifying public attributes directly
print(employee.name)  # Output: Alice
employee.salary = 60000
print(employee.salary)  # Output: 60000
```

---

### Step 1: Making an attribute protected (or private) without getter and setter

Here’s an example how you can making an attribute privte or protected (it just change the number of `_` as we seen above).

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self._salary = salary  #Protected attribute

employee = Employee("Alice", 50000)
```

As it is now, the attribute is protected or private and so can't be changed. It can be useful for variables you won't change at all once they are created.


But what if we want to modify it? We will use another technique to make the attribute private AND change it in a specific way!

### Step 2.5: Making an Attribute Protected Using Getters and Setters

To make `salary` protected, we won't name it `_salary` directly in the __init__ because if we do that then all the getter and setter will be skipped.

So we introduce a getter and setter for controlled access.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Attribute we want to protect

    @property
    def salary(self):
        return self._salary  # Getter for the protected attribute

    @salary.setter
    def salary(self, value):
        if value >= 0:  # Ensure salary is a non-negative value
            self._salary = value
        else:
            raise ValueError("Salary must be a positive number")

employee = Employee("Alice", 50000)

# Accessing salary using the getter
print(employee.salary)  # Output: 50000

# Modifying salary using the setter
employee.salary = 60000
print(employee.salary)  # Output: 60000

# Trying to set an invalid salary
try:
    employee.salary = -100  # Raises ValueError: Salary must be a positive number
except ValueError as e:
    print(e)
```

**Explanation**:
- Public attribute `salary` in the `__init__` received the characteristic protected" in the through the getter and setter (`_salary`), and can only be accessed through the `@property` getter and setter.
- The setter ensures that the salary cannot be negative.

---

### Step 3: Making an Attribute Private with Getters and Setters

To make `salary` private, change `_salary` to `__salary` and use getters and setters to manage access.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Private attribute

    @property
    def salary(self):
        return self.__salary  # Getter for the private attribute

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be a positive number")

employee = Employee("Alice", 50000)

# Accessing salary using the getter
print(employee.salary)  # Output: 50000

# Modifying salary using the setter
employee.salary = 60000
print(employee.salary)  # Output: 60000

# Trying to set an invalid salary
try:
    employee.salary = -100  # Raises ValueError: Salary must be a positive number
except ValueError as e:
    print(e)

# Trying to access the private attribute directly (not possible)
try:
    print(employee.__salary)  # Raises AttributeError
except AttributeError:
    print("Cannot access private attribute directly")
```

**Explanation**:
- The attribute `__salary` is private and cannot be accessed directly outside of the class.
- **Name mangling** internally changes `__salary` to `_Employee__salary`, making it difficult to modify the attribute from outside the class.

---

## Key Points:

- **Public attributes** can be accessed and modified freely.
- **Protected attributes** (e.g., `_attribute`) signal internal use, though they can still be accessed outside if needed.
- **Private attributes** (e.g., `__attribute`) are intended to be fully private and should be accessed only through methods like getters and setters.
- **Using `@property`** with getters and setters allows controlled access and modification while keeping the syntax clean and Pythonic (`object.attribute`).

---

## Recap:

- **Protected Attributes**: Use a single underscore (`_attribute`) to indicate the attribute is for internal use.
- **Private Attributes**: Use double underscores (`__attribute`) to prevent external access or modification.
- **Getters and Setters**: Use `@property` and `@attribute.setter` to manage access to private or protected attributes.
- **`@property` Decorator**: Provides a simple, readable way to use getters and setters while maintaining control over access.

This lesson demonstrates how to manage attribute visibility and encapsulation using getters, setters, and Python’s private/protected naming conventions.
