
# Campus Library Management System

## Project Overview

This project is a Python-based Library Management System
that manages three types of library items:

- Books
- Magazines
- DVDs

Members can borrow and return items. The system checks
availability, enforces borrowing limits and calculates
late fees based on the item type.

## Project Structure

library_manager/
|
|-- main.py
|-- models.py
|-- README.md

## Features

1. Uses an abstract parent class LibraryItem.
2. Implements Book, Magazine and DVD using inheritance.
3. Calculates different late fees:
   - Book: Rs 2 per day
   - Magazine: Rs 1 per day
   - DVD: Rs 5 per day
4. Maintains item availability.
5. Maintains private borrowed-item lists for members.
6. Enforces member borrowing limits.
7. Handles invalid operations using ValueError.
8. Demonstrates polymorphism.
9. Maintains a shared total item counter.

## How to Run

Make sure Python 3 is installed.

Open the terminal inside the library_manager folder.

Execute:

python3 main.py

On Windows:

python main.py

## Reflection

### 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is an abstract class because it provides common properties and methods for all library items while requiring every child class to implement its own `late_fee()` method. If DVD forgets to implement `late_fee()`, Python raises a `TypeError` when we try to create a DVD object because it has not implemented the required abstract method.

### 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

When we try to access `item.__available` directly from outside the class, Python raises an `AttributeError` because the double underscore triggers name mangling. We use `is_available()` instead because it provides a controlled way to check the item's availability without directly accessing its private attribute.

### 3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a class attribute shared by all objects of the LibraryItem class and its child classes, so it keeps track of the total number of library items created. In contrast, `self.title` is an instance attribute that stores the individual title of each library item, meaning every object can have a different title.

## Conclusion

This project demonstrates the practical use of Python
Object-Oriented Programming concepts, including classes,
objects, constructors, inheritance, abstraction,
encapsulation, polymorphism and exception handling.
