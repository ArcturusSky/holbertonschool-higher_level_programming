# Python - Classes

This document will hold information I didn't know where to put in other files/repositories. Some key concepts or not. In anycase it is useful.

## Summary

- [Python - Classes](#python---classes)
  - [Summary](#summary)
  - [Glossary](#glossary)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
    - [Classes and Subclasses hierarchy](#classes-and-subclasses-hierarchy)
      - [Class (or Superclass)](#class-or-superclass)
      - [Subclass (or Derived Class)](#subclass-or-derived-class)
      - [Instance](#instance)
      - [To sum up](#to-sum-up)
      - [Full hierarchy](#full-hierarchy)
    - [First-class Everything](#first-class-everything)
    - [A Minimal Class in Python](#a-minimal-class-in-python)
    - [Attributes](#attributes)
    - [Methods](#methods)
    - [The `__init__` Method](#the-__init__-method)
    - [The `self` parameter in Python OOP](#the-self-parameter-in-python-oop)
      - [How to use the `self` parameter in Python](#how-to-use-the-self-parameter-in-python)
    - [Example Defining a Simple Class](#example-defining-a-simple-class)
      - [Defining a Simple class](#defining-a-simple-class)
      - [Adding Methods to a Class](#adding-methods-to-a-class)
      - [Adding the `__init__` Method](#adding-the-__init__-method)
    - [Private and Protected Attributes in Python](#private-and-protected-attributes-in-python)
      - [What Are Private and Protected Attributes?](#what-are-private-and-protected-attributes)
    - [Private and Protected Attributes with Getters and Setters](#private-and-protected-attributes-with-getters-and-setters)
      - [Original Case: A Class with Public Attributes (Initial State)](#original-case-a-class-with-public-attributes-initial-state)
      - [Option 1: Making an attribute protected (or private) without getter and setter](#option-1-making-an-attribute-protected-or-private-without-getter-and-setter)
      - [Option 2: Making an Attribute Protected Using Getters and Setters](#option-2-making-an-attribute-protected-using-getters-and-setters)
    - [Key Points:](#key-points)
    - [Data Abstraction, Data Encapsulation, and Information Hiding](#data-abstraction-data-encapsulation-and-information-hiding)
    - [`__str__` and `__repr__` Methods](#__str__-and-__repr__-methods)
    - [Destructor](#destructor)
    - [Static Methods in Python](#static-methods-in-python)
  - [Inheritance](#inheritance)
    - [Basic syntax of inheritance](#basic-syntax-of-inheritance)
    - [The `super()` function](#the-super-function)
    - [Types of inheritance](#types-of-inheritance)
      - [Single inheritance](#single-inheritance)
      - [Multiple inheritance](#multiple-inheritance)
      - [Multilevel inheritance](#multilevel-inheritance)
      - [Hierarchical inheritance](#hierarchical-inheritance)
      - [Method Overriding](#method-overriding)
    - [Odd and Ends](#odd-and-ends)
      - [Abstract classes](#abstract-classes)

## Glossary

**A**
- **Abstraction:** Hiding complex implementation details and displaying only necessary features of an object.
- **Attribute:** A variable that stores data within a class or instance.

**C**
- **Class:** A blueprint or template for creating objects that encapsulate data and behavior.
- **Class Variable:** A variable shared by all instances of a class.

**D**
- **Data Abstraction:** The process of hiding complex implementation details and showing only the necessary features of an object.
- **Data Encapsulation:** The bundling of data and methods that operate on that data within a single unit (class).
- **Destructor:** A method called when an object is destroyed or deleted.

**F**
- **First-class Everything:** A concept in Python where everything, including functions and classes, is treated as objects.

**G**
- **Getter:** A method that retrieves the value of a private or protected attribute.

**I**
- **Information Hiding:** The practice of restricting access to certain details of an object.
- **Inheritance:** A mechanism where a subclass inherits methods and attributes from a superclass.
- **Instance:** A concrete copy of the class blueprint, created with specific values for its attributes.

**M**
- **Method:** A function defined within a class that describes the behaviors of the class instances.

**O**
- **Object:** An instance of a class in object-oriented programming.
- **Object-Oriented Programming (OOP):** A programming paradigm that organizes code into objects, combining data and functionality.

**P**
- **Private Attribute:** An attribute indicated by double underscores, intended to be accessed only within the class.
- **Protected Attribute:** An attribute indicated by a single underscore, intended for internal use but can be accessed outside the class.
- **Public Attribute:** An attribute that can be accessed and modified freely from outside the class.

**S**
- **Self:** A parameter in Python class methods referring to the current instance of the class.
- **Setter:** A method that sets or updates the value of a private or protected attribute while enforcing rules (e.g., validation).
- **Static Method:** A method that belongs to a class rather than an instance of the class.
- **Subclass:** A specialized version of a class that inherits from a superclass.
- **Superclass:** A general blueprint class from which other classes can inherit.

**Special Symbols**
- **`__init__`:** A special method in Python classes used for initializing new objects.
- **`__str__`:** A special method that returns a string representation of an object.
- **`__repr__`:** A special method that returns a detailed string representation of an object, typically used for debugging.

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

### Classes and Subclasses hierarchy

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

### First-class Everything

In Python, everything is treated as an object, including functions and classes. This concept is known as "**first-class everything**."

**Example:**

```python
def greet(name):
    return f"Hello, {name}!"

# Assigning a function to a variable
greeting = greet
print(greeting("Alice"))

# Expected output: Hello, Alice!
```

**Explanation:**

In this example, we define a function `greet` and assign it to a variable `greeting`. We can then call the function using the variable name, demonstrating that functions are first-class objects in Python.

### A Minimal Class in Python

**Definition**: A class is a blueprint for creating objects that **encapsulate** data and behavior.

**Syntax:**

```python
class ClassName:
    pass
```

**Example:**

```python
class Dog:
    pass

my_dog = Dog()
print(my_dog)

# Expected output:
# <__main__.Dog object at 0x...>
```

**Explanation:**

We define a minimal class `Dog` using the `class` keyword. The `pass` statement is used as a placeholder. We create an instance of the `Dog` class and assign it to `my_dog`. When we print `my_dog`, Python displays the object's type and memory address.

### Attributes

**Definition**: Attributes are variables that store data within a class or instance.

**Example:**

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

my_dog = Dog("Buddy", 5)
print("Name: {}, Age: {}, Species: {}".format(my_dog.name, my_dog.age, my_dog.species))

# Expected output:
# Name: Buddy, Age: 5, Species: Canis familiaris
```

**Explanation:**
We define a `Dog` class with a class attribute `species` and two instance attributes `name` and `age`. The `__init__` method initializes the instance attributes. We create a `Dog` instance and access its attributes using dot notation.

### Methods

**Definition**: Methods are functions defined within a class that describe the behaviors of the class instances.

**Example:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = Dog("Rex", 3)
print("{} says: {}".format(my_dog.name, my_dog.bark()))

# Expected output:
# Rex says: Woof!
```

**Explanation:**
We define a `Dog` class with an `__init__` method to initialize attributes and a `bark` method to define a behavior. We create a `Dog` instance and call its `bark` method.

### The `__init__` Method

**Definition**: The `__init__` method is a special method in Python classes used for initializing new objects.

**Syntax:**

```python
class ClassName:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2
```

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print("Name: {}, Age: {}".format(person.name, person.age))

# Expected output:
# Name: Alice, Age: 30
```

**Explanation:**
The `__init__` method is called when creating a new instance of the class. It initializes the object's attributes (`name` and `age`) with the values passed as arguments.

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

#### Adding the `__init__` Method

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

### Private and Protected Attributes with Getters and Setters

#### Original Case: A Class with Public Attributes (Initial State)

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

#### Option 1: Making an attribute protected (or private) without getter and setter

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

#### Option 2: Making an Attribute Protected Using Getters and Setters

To make `salary` protected, we won't name it `_salary` directly in the `__init__` because if we do that then all the getter and setter will be **skipped**.

So we introduce a **getter** and **setter** for controlled access.

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

### Key Points:

- **Public attributes** can be accessed and modified freely.
- **Protected attributes** Use a single underscore (`_attribute`) to indicate the attribute is for internal use, though they can still be accessed outside if needed.
- **Private attributes** (e.g., `__attribute`) are intended to be fully private and should be accessed only through methods like **getters** and **setters**.
- **Getters and Setters**: Use `@property` and `@attribute.setter` to manage access to private or protected attributes.
- **`@property` Decorator**: Provides a simple, readable way to use getters and setters while maintaining control over access.

### Data Abstraction, Data Encapsulation, and Information Hiding

**Definition**:

- **Data Abstraction:** Hiding complex implementation details and showing only the necessary features of an object.
- **Data Encapsulation:** Bundling data and methods that operate on that data within a single unit (class).
- **Information Hiding:** Restricting access to certain details of an object.

**Example:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Balance: ${:.2f}".format(account.get_balance()))

# Expected output:
# Balance: $1300.00
```

**Explanation:**

The `BankAccount` class **encapsulates** the balance and operations on it. The balance is a private attribute (**`__balance`**), implementing information hiding. The class provides methods for interacting with the balance, abstracting the internal implementation.

### `__str__` and `__repr__` Methods

**Definition**:

- `__str__`: Returns a **string representation** of an object for **end-users**.
- `__repr__`: Returns a **detailed string representation** of an object for **developers**.

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} ({} years old)".format(self.name, self.age)

    def __repr__(self):
        return "Person(name='{}', age={})".format(self.name, self.age)

person = Person("Bob", 25)
print(str(person))  # Calls __str__
print(repr(person))  # Calls __repr__

# Expected output:
# Bob (25 years old)
# Person(name='Bob', age=25)
```

**Explanation:**

The `__str__` method provides a human-readable string representation of the object. The `__repr__` method provides a more detailed representation, typically used for debugging or development purposes.

### Destructor

**Definition**: A destructor is a special method called when an object is about to be destroyed.

**Syntax:**

```python
class ClassName:
    def __del__(self):
        # cleanup code
```

**Example:**

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')
        print("File {} opened.".format(self.filename))

    def __del__(self):
        self.file.close()
        print("File {} closed.".format(self.filename))

handler = FileHandler("example.txt")
del handler

# Expected output:
# File example.txt opened.
# File example.txt closed.
```

**Explanation:**
The `__del__` method is called when the `FileHandler` object is about to be destroyed. It ensures that the file is properly closed before the object is removed from memory. However, it's generally recommended to use context managers (`with` statement) for resource management instead of relying on destructors.

### Static Methods in Python

**Definition**: A static method is a method that belongs to a class rather than an instance of the class. It doesn't require access to instance-specific data and doesn't modify the class state.

**Syntax:**

```python
class ClassName:
    @staticmethod
    def method_name(parameters):
        # method body
```

**Example:**

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Using static methods
print("Sum: {}".format(MathOperations.add(5, 3)))
print("Product: {}".format(MathOperations.multiply(4, 2)))

# Expected output:
# Sum: 8
# Product: 8
```

**Explanation:**
- Static methods are defined using the `@staticmethod` decorator.
- They don't require the `self` parameter because they don't access instance-specific data.
- Static methods can be called on the class itself, without creating an instance.
- They are useful for utility functions that are related to the class but don't need to access instance or class data.

**Use Cases:**
1. Utility functions related to the class's purpose.
2. Factory methods that create instances of the class.
3. Methods that operate on class attributes rather than instance attributes.

**Comparison with Instance Methods:**

```python
class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def add(self, x):
        self.value += x
        return self.value
    
    @staticmethod
    def add_numbers(x, y):
        return x + y

# Using instance method
calc = Calculator(5)
print("Instance method result: {}".format(calc.add(3)))

# Using static method
print("Static method result: {}".format(Calculator.add_numbers(5, 3)))

# Expected output:
# Instance method result: 8
# Static method result: 8
```

**Key Points:**
- Static methods don't have access to `self` or `cls` parameters.
- They can be called on the class without creating an instance.
- Use static methods when you don't need to access or modify instance or class state.
- Static methods improve code organization by grouping related functions within a class.

## Inheritance


**Inheritance** allows a class (called the ***child***, ***subclass*** or ***derived*** class) to inherit the properties and methods from another class (called the ***parent***, ***superclass*** or ***baseclass***). This enables code reuse, making your code more organized and modular. Additionally, it allows you to add or modify features of a child class without rewriting the parent class entierely.

### Basic syntax of inheritance

To create a child class that inherits from a parent class, you simply specify the parent class in parentheses when defining the child class.

*Example:*

```python

# Define the Parent class

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("{} makes a sound.".format(self.name))

# Define the Child class that inherits from Animal

class Dog(Animal):
    def speak(self):
    print("{} barks.".format(self.name))

# Creating an instance of Dog

dog_instance = Dog("Buddy")
dog_instance.speak() 
# Output: Buddy barks.

```

**Explanations:**

  - **Parent Class (Animal):** This class contains an `__init__` method to initialize the name of the animal and a `speak()` method to display a sound.
  - **Child Class (Dog):** This class inherits from `Animal`, meaning it automatically gets all its properties and methods. However, it overrides the `speak()` method with its own specific implementation.

You can also access attribute this way, the same way as in any other class.

```python

# Example of accessing attribute from the parent class within the current class
print(dog_instance.name) # Output: Buddy

```

### The `super()` function

The `super()` function is used to call a method from the parent class inside the child class. This is useful when the child class needs to use the parent's logic but also extend or modify it.

*Example:*

```python

# Parent class

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("{} makes a sound.".format(self.name))

# Child class that inherits from Animal

class Dog(Animal):
    def __init__(self, name, breed):
        # Use super() to call the parent class's __init_method
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Use the parent class's speak method
        super().speak()
        print("{}, the {}, barks.".format(self.name, self.breed))

# Creating an instance of Dog

dog_instance = Dog("Max", "Labrador")
dog_instance.speak() 
# Output:   Max, makes a sound.         # Inherit from the parent class
#           Max, the Labrador, barks.   # Added in the child class

```

**Explanation:**

  - In the `Dog` class, we use `super().__init__(name)` to initialize the `name` attribute using the `Animal` class `__init__` method.
  - We also **EXTEND** the `speak()` method of the `Animal` class. To do this we first call `super().speak()` to use the parent method and then we **ADD** an additional behaviour for the `Dog` class. Leading to have **BOTH** of output.

To sum it up in one sentence:

*`super().` allows you to retrieve the method from its parent then ADD things to it, or else.*

**Importance of `super()`:** It helps avoid explicit naming of the parent class, making your code more flexible and easier to maintain.

### Types of inheritance

In python, you can use different types of inheritance depending on your needs.

#### Single inheritance

This is when a child class inherits from only one parent class.

```python

class Parent:
    def __init__(self):
        print("Parent class initialized")
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class initialized")

c = Child()
c()
# Output:   Parent class initialized
#           Child class initialized

```

#### Multiple inheritance

In Python, a class can inherit from multiple parent classes. This is called **multiple inheritance**.

```python

class Mother:
    def show_mother(self):
        print("Mother's class")

class Father:
    def show_father(self):
        print("Father's class")

class Child(Mother, Father):
    def show_child(self):
        print("Child's class")

c = Child()
c.show_mother()
c.show_father()

# Output:   Mother's class
#           Father's class
```

**Explanation:**

Here we could call each `parent`'s methods through the `Child` class since the `Child` class has both `mother` and `father` as `parent` class.

:thought_balloon: **Reminder:** "`Parent`" class is also known as "`super`" class. (Which explain why the `super().` method to get method from super/parent class.)

:page_facing_up: **Note:** In cases of multiple inheritance, Python uses a **method resolution order** to determine the order in which base classes are seached when looking for a method. You can view the **MRO** of a class using the `__mro__` attribute:

```python

print(Child.__mro__) # Show the method resolution order for the Child class

```

#### Multilevel inheritance

In this type of inheritance, a class inherits from a child class, creating a **chain of inheritance.**

```python

class Grandparent:
    def __init__(self):
        print("Grandparent's constructor called")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent's constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child's constructor called")

c = Child()
c()     # Calling the child in the end

# Output:   Grandparent's constructor called
#           Parent's constructor called
#           Child's constructor called

```

**Explanation:**

Here, it's simple it's like Russian dolls. Each layer of doll will obviously hold the one inside. Here it's the same:

Grandparent has 1 method = 1 method  
Parent inherit 1 method from Grandparent and add 1 = 2 methods  
Child inherit the 2 methods from Parent (since we already seen that parent has 2.) and add 1 = 3 methods.

#### Hierarchical inheritance

This occurs when multiple child class inherit from the same parent class.

```python

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()

# Output:   Dog barks.
#           Cat meows.

```

**Explanation:**

Kinda the same as before, here it has been override but with the `super.` all the childs would have kept the *"Animal makes a sound"*.

#### Method Overriding

As seen earlier, a **subclass** (aka **Child** class) can override a method of its **superclass** (aka **parent**/**base** class) to provide its own version of the method. This is useful when the child class needs to implement its own version of the method. 

For example in the previous subsection both `Dog` and `Cat` override the `speak()` method from the `Animal` class.

### Odd and Ends

#### Abstract classes

**Definition:** An **abstract class** is a class that cannot be instantiated and is designed to be a **baseclass** for the other classes. It may contain **abstract methods** that must be implemented by **derived** (**subclass**) classes.

So this is the definition given by ChatGPT. But here is what **I** understood:

An **abstract class** is a class that **MUST** be a **baseclasse** (also known as **parent class**, **superclass**). In it there will be **abstract methods**. And an **abstract method** is a method that won't be used like this, called or whatever directly in the class BUT that all its child **MUST** have. So both of them are kinda like a blueprints for their childs. A Requiered blueprint that CAN'T be removed. 

*Example without code:* in factories, a "**car**" is the blueprint (**abstract class**) and "**wheels**" is a requirement (**abstract methods**) in that blueprint for each car factored in the factories. You can't make car without wheels can you? So that's the idea.