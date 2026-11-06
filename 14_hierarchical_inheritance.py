class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def circle_area(self):
        print("Area of circle = 3.14 * r * r")

class Rectangle(Shape):
    def rectangle_area(self):
        print("Area of rectangle = length * breadth")

circle = Circle()
rectangle = Rectangle()
circle.display()
circle.circle_area()
rectangle.display()
rectangle.rectangle_area()
