# Python-Assignment-6--OOPS
This  Assignment explains about the OOPS concept in Python
# Asssignment6.py
"""Question 1:
Build a program to manage a university's course catalog. You want to define a base class Course that has the following properties:
course_code: a string representing the course code (e.g., "CS101")
course_name: a string representing the course name (e.g., "Introduction to Computer Science")
credit_hours: an integer representing the credit hours for the course (e.g., 3)
You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for a particular major.
ElectiveCourse (e.g., "general", "technical", "liberal arts")."""

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_course_info(self):
        return f"Course Code: {self.course_code}, Name: {self.course_name}, Credit Hours: {self.credit_hours}"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_course_info(self):
        base_info = super().display_course_info()
        return f"{base_info}, Required for Major: {self.required_for_major}"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_course_info(self):
        base_info = super().display_course_info()
        return f"{base_info}, Elective Type: {self.elective_type}"

# Example usage
core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("LA202", "Artificial intelligence", 2, "Information technology")

print(core_course.display_course_info())
print(elective_course.display_course_info())


import employee
employee.Employee()
print(employee.name)



# employee.py
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






