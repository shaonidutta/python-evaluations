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