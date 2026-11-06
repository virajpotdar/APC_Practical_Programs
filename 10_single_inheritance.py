class Person:
    def show_name(self):
        print("Name: Viraj")

class Student(Person):
    def show_roll_no(self):
        print("Roll Number: 101")

obj = Student()
obj.show_name()
obj.show_roll_no()
