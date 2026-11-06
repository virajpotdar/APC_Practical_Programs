class Father:
    def father_skill(self):
        print("Father: gardening")

class Mother:
    def mother_skill(self):
        print("Mother: cooking")

class Child(Father, Mother):
    def child_skill(self):
        print("Child: painting")

obj = Child()
obj.father_skill()
obj.mother_skill()
obj.child_skill()
