
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

### 1. Why did I use an abstract parent class?

I used LibraryItem as an abstract parent class to define
common properties and behaviours for all library items.

The abstract method late_fee() ensures that every child
class implements its own late fee calculation.

This avoids code duplication and provides a common
structure for all item types.

### 2. How did I implement encapsulation?

I used double underscore attributes to protect the
availability status and the member's borrowed-item list.

The availability can be checked using is_available(),
and the borrowed item titles can be retrieved using
borrowed_titles().

This ensures that the internal data is managed through
methods rather than directly accessed or modified.

### 3. How did I implement polymorphism?

I implemented polymorphism by overriding late_fee()
in Book, Magazine and DVD.

Each class calculates its fee using a different daily rate.

In main.py, I created a mixed list containing all three
item types and called late_fee() inside one loop.

Python automatically executes the correct method
depending on the object's class, without requiring
conditional type checks.

## Conclusion

This project demonstrates the practical use of Python
Object-Oriented Programming concepts, including classes,
objects, constructors, inheritance, abstraction,
encapsulation, polymorphism and exception handling.
