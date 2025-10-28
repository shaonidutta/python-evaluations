# Abstract class

from abc import abstractmethod, ABC


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self) -> str:
        return f"Employee [{self.name}] (ID:{self.employee_id})"

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary) :
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
    
class Freelancer(Employee):
    def __init__(self, name, employee_id, project_count, payment_per_project):
        super().__init__(name, employee_id)
        self.project_count = project_count
        self.payment_per_project = payment_per_project

    def calculate_salary(self):
        return self.project_count * self.payment_per_project
    
#payroll system
class PayrollSystem:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def generate_payroll(self):
        total_payroll=0
        for employee in self.employees:
            print(employee)
            salary = employee.calculate_salary()
            print(f"Salary: {salary}")
        
        total_payroll += salary


if __name__ == "__main__":
    fte = FullTimeEmployee("Shaoni", 100, 60000)
    pte = PartTimeEmployee("employee2", 101, 80, 500)
    frl = Freelancer("employee3", 102, 4, 15000)
    payroll = PayrollSystem()
    payroll.add_employee(fte)
    payroll.add_employee(pte)
    payroll.add_employee(frl)

    payroll.generate_payroll()
