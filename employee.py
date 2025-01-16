"""Question2:
Create a Python module named employee that contains a class Employee with attributes name, salary and methods get_name() and get_salary().
Write a program to use this module to create an object of the Employee class and display its name and salary."""

name="ajay"
salary=10000
class Employee:
    def _init_(self):
        pass
    def get_name(self,name):
        print(f"Employee Name:{name}")

    def get_salary(self,salary):
        print(f"Employee Salary:{salary}")
employee_details = Employee()
employee_details.get_name("ajay")
employee_details.get_salary(60000)





