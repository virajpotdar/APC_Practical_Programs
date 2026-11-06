class Person:
    def show_person(self):
        print("Person details")

class Student(Person):
    def show_student(self):
        print("Student details")

class Employee(Person):
    def show_employee(self):
        print("Employee details")

class Intern(Student, Employee):
    def show_intern(self):
        print("Intern details")

obj = Intern()
obj.show_person()
obj.show_student()
obj.show_employee()
obj.show_intern()
