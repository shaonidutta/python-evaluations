Q: 1
Implement a payroll system for a company with different types of employees.
Requirements:

Create an abstract base class Employee:

Attributes: name, employee_id

Abstract method: calculate_salary()

Method: __str__() → prints “Employee [name] (ID: employee_id)”

Create the following subclasses:

FullTimeEmployee(Employee)

Attributes: monthly_salary

calculate_salary() → returns monthly_salary

PartTimeEmployee(Employee)

Attributes: hours_worked, hourly_rate

calculate_salary() → returns hours_worked * hourly_rate

Freelancer(Employee)

Attributes: project_count, payment_per_project

calculate_salary() → returns project_count * payment_per_project

Create a class PayrollSystem:

Maintains a list of employees

Method add_employee(employee: Employee)

Method generate_payroll() → prints each employee’s details and salary using polymorphism

Total company payroll at the end.

Demonstrate:

Creating different employee types

Adding them to PayrollSystem

Calling generate_payroll() to show polymorphic behavior.

Submit the GitHub repository link to the code file


Q: 2
Product Inventory
Design a small Product Inventory System:

Class Product

Attributes: name, price, quantity

Dunder methods:

__str__ – readable info

__add__ – merge two products of same name (combine quantity, average price)

__lt__ – compare based on price

Class Inventory

Maintains a private list of products

Methods:

add_product()

__len__() → returns total number of items

__getitem__() → allows indexing

search_by_name() (case-insensitive match)

Demonstrate:

Adding multiple products

Sorting them using Python’s built-in sorted()

Printing total inventory value.

Submit the GitHub repository link to the code file


Q: 3
Design a small Library Management System using Object-Oriented Programming.
Requirements:

Create a base class Book with:

Attributes: title, author, isbn, copies

Methods:

__str__() → returns a user-friendly string

borrow() → decreases available copies

return_book() → increases available copies

Raise an exception if borrow() is called when no copies are available.

Create a subclass EBook(Book) with:

Extra attribute: file_size (in MB)

Override __str__() to include file size

Override borrow() so that it does not change copies (since ebooks are unlimited)

Create a class Library that:

Maintains a private list of all books (__books)

Methods:

add_book(book: Book)

find_books_by_author(author: str) → returns a list of books by that author

__len__() → total number of book titles

__getitem__() → allow indexing through the library (e.g., library[0])

Demonstrate:

Adding both Book and EBook instances

Borrowing/returning logic

Searching by author

Using len(library) and indexing syntax

Submit the GitHub repository link to the code file


Q: 5
Create a file sales.json which contains:

[
  {"id": 1, "item": "Pen", "price": 20, "qty": 5},
  {"id": 2, "item": "Notebook", "price": 100, "qty": 2},
  {"id": 3, "item": "Bag", "price": 500, "qty": 1}
]
Read this file, compute total revenue per item, and write results into report.txt as formatted strings:
Pen → ₹100
Notebook → ₹200
Bag → ₹500
Implement it safely using context managers and handle file errors gracefully.
Submit the GitHub repository link to the code file

Q: 7
Write a one-line Python expression (no loops) that generates a list of all integers between 1 and 1000 that are:
divisible by 7 or 9, but not both

and are palindromic numbers (e.g., 121)

Submit the GitHub repository link to the code file


Q: 9
Write a generator prime_generator(n) that yields the first n prime numbers efficiently.

Write a decorator measure_time that prints how long it takes to generate those primes.

Submit the GitHub repository link to the code file