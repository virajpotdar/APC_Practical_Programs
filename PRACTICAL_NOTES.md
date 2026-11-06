# APC Practical Notes

Simple problem statements, sample outputs, explanations and important concepts for all 29 experiments.

## Experiment 1: 01_read_file.py

**Problem Statement:** Write a Python program to read the contents of a text file and display them on the console.

**Program:**

```python
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
```

**Sample Output / Result:**
```text
Displays the lines stored in sample.txt.
```

**Explanation:** Reads the complete contents of sample.txt and prints them on the console.

**Important Concepts:** open(), read(), print(), close()

## Experiment 2: 02_copy_file.py

**Problem Statement:** Write a Python program to read the contents of one file and write them into another file.

**Program:**

```python
source = open("sample.txt", "r")
content = source.read()
source.close()

destination = open("copy.txt", "w")
destination.write(content)
destination.close()

print("File copied successfully")
```

**Sample Output / Result:**
```text
File copied successfully
```

**Explanation:** Opens the source file in read mode, reads its contents, and writes the same contents into copy.txt.

**Important Concepts:** open(), read(), write(), close()

## Experiment 3: 03_directory_functions.py

**Problem Statement:** Write a Python program to demonstrate 10 directory and path handling functions using the os module.

**Program:**

```python
import os

folder = "demo_folder"
file_name = "demo_folder/sample.txt"

print("Current directory:", os.getcwd())
os.mkdir(folder)
print("Directory created:", os.path.exists(folder))
print("Is directory:", os.path.isdir(folder))
print("Joined path:", os.path.join(folder, "sample.txt"))

file = open(file_name, "w")
file.write("Directory handling example")
file.close()

print("Is file:", os.path.isfile(file_name))
print("Directory contents:", os.listdir(folder))
os.rename(file_name, "demo_folder/new_sample.txt")
print("Renamed file exists:", os.path.exists("demo_folder/new_sample.txt"))
os.remove("demo_folder/new_sample.txt")
os.rmdir(folder)
print("Directory removed:", not os.path.exists(folder))
```

**Sample Output / Result:**
```text
Displays the current directory, directory checks, joined path, directory contents and confirmation that the directory was removed. The current directory path depends on the computer.
```

**Explanation:** Uses os and os.path functions to create a directory, check paths, list its contents, rename and remove a file, and remove the directory.

**Important Concepts:** os.getcwd(), os.mkdir(), os.path.exists(), os.path.isdir(), os.path.join(), os.path.isfile(), os.listdir(), os.rename(), os.remove(), os.rmdir()

## Experiment 4: 04_horizontal_bar_chart.py

**Problem Statement:** Write a Python program to display a horizontal bar chart showing the popularity of programming languages.

**Program:**

```python
import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.barh(languages, popularity)
plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.title("Popularity of Programming Languages")
plt.show()
```

**Sample Output / Result:**
```text
Opens a horizontal bar chart for Java, Python, PHP, JavaScript, C# and C++.
```

**Explanation:** Stores language names and popularity values in two lists. Matplotlib barh() displays them as horizontal bars.

**Important Concepts:** Matplotlib, barh(), xlabel(), ylabel(), title(), show()

## Experiment 5: 05_pie_chart.py

**Problem Statement:** Write a Python program to create a pie chart showing the distribution of trip expenses by category.

**Program:**

```python
import matplotlib.pyplot as plt

categories = ["Food", "Travel", "Hotel", "Shopping"]
expenses = [3000, 2000, 4000, 1000]

plt.pie(expenses, labels=categories, autopct="%1.1f%%")
plt.title("Trip Expense Distribution")
plt.show()
```

**Sample Output / Result:**
```text
Opens a pie chart showing Food, Travel, Hotel and Shopping expense percentages.
```

**Explanation:** The pie() function creates a chart from expense values and displays each category as a labelled slice with its percentage.

**Important Concepts:** Matplotlib, pie(), title(), show()

## Experiment 6: 06_tkinter_gui.py

**Problem Statement:** Write a Python program to design a simple GUI using Tkinter with a label, entry box and button.

**Program:**

```python
from tkinter import *

window = Tk()
window.title("Simple GUI")
window.geometry("300x200")

def show_name():
    label_result.config(text="Hello " + entry_name.get())

label_name = Label(window, text="Enter your name:")
label_name.pack(pady=5)

entry_name = Entry(window)
entry_name.pack(pady=5)

button = Button(window, text="Submit", command=show_name)
button.pack(pady=5)

label_result = Label(window, text="")
label_result.pack(pady=5)

window.mainloop()
```

**Sample Output / Result:**
```text
Opens a GUI window with a name entry box and Submit button. Submitting Viraj displays Hello Viraj.
```

**Explanation:** Creates a Tkinter window. The user enters a name and clicks Submit; the button calls show_name() and updates the result label.

**Important Concepts:** Tk(), title(), geometry(), Label(), Entry(), Button(), pack(), mainloop()

## Experiment 7: 07_class_object_constructor.py

**Problem Statement:** Write a Python program to demonstrate a class, object and constructor using student information.

**Program:**

```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

student1 = Student("Viraj", 101)
student1.display()
```

**Sample Output / Result:**
```text
Name: Viraj
Roll Number: 101
```

**Explanation:** Student is a class. The constructor __init__() stores the name and roll number when an object is created. display() prints the details.

**Important Concepts:** class, object, __init__(), self, instance method

## Experiment 8: 08_method_overloading.py

**Problem Statement:** Write a Python program to demonstrate method overloading using default arguments.

**Program:**

```python
class Addition:
    def add(self, a, b=0, c=0):
        print("Sum:", a + b + c)

obj = Addition()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)
```

**Sample Output / Result:**
```text
Sum: 10
Sum: 30
Sum: 60
```

**Explanation:** Python does not provide traditional method overloading by defining the same method many times. Default arguments allow add() to work with one, two or three values.

**Important Concepts:** class, method, default arguments

## Experiment 9: 09_method_overriding.py

**Problem Statement:** Write a Python program to demonstrate method overriding using parent and child classes.

**Program:**

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()
```

**Sample Output / Result:**
```text
Dog barks
```

**Explanation:** Dog inherits from Animal and defines its own sound() method. The child class version is called for a Dog object.

**Important Concepts:** inheritance, method overriding

## Experiment 10: 10_single_inheritance.py

**Problem Statement:** Write a Python program to demonstrate single inheritance.

**Program:**

```python
class Person:
    def show_name(self):
        print("Name: Viraj")

class Student(Person):
    def show_roll_no(self):
        print("Roll Number: 101")

obj = Student()
obj.show_name()
obj.show_roll_no()
```

**Sample Output / Result:**
```text
Name: Viraj
Roll Number: 101
```

**Explanation:** Student inherits from one parent class, Person. Its object can use methods from both classes.

**Important Concepts:** single inheritance, parent class, child class

## Experiment 11: 11_multilevel_inheritance.py

**Problem Statement:** Write a Python program to demonstrate multilevel inheritance.

**Program:**

```python
class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class")

class Child(Parent):
    def show_child(self):
        print("Child class")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()
```

**Sample Output / Result:**
```text
Grandparent class
Parent class
Child class
```

**Explanation:** Inheritance takes place in a chain: Child inherits Parent, and Parent inherits Grandparent. The Child object can access all three methods.

**Important Concepts:** multilevel inheritance

## Experiment 12: 12_multiple_inheritance.py

**Problem Statement:** Write a Python program to demonstrate multiple inheritance.

**Program:**

```python
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
```

**Sample Output / Result:**
```text
Father: gardening
Mother: cooking
Child: painting
```

**Explanation:** Child inherits from two parent classes, Father and Mother, so its object can use methods from both parents.

**Important Concepts:** multiple inheritance

## Experiment 13: 13_hybrid_inheritance.py

**Problem Statement:** Write a Python program to demonstrate hybrid inheritance.

**Program:**

```python
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
```

**Sample Output / Result:**
```text
Person details
Student details
Employee details
Intern details
```

**Explanation:** This example combines hierarchical inheritance (Student and Employee inherit Person) with multiple inheritance (Intern inherits both).

**Important Concepts:** hybrid inheritance, multiple inheritance, hierarchical inheritance

## Experiment 14: 14_hierarchical_inheritance.py

**Problem Statement:** Write a Python program to demonstrate hierarchical inheritance.

**Program:**

```python
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
```

**Sample Output / Result:**
```text
This is a shape
Area of circle = 3.14 * r * r
This is a shape
Area of rectangle = length * breadth
```

**Explanation:** Circle and Rectangle are two child classes of the same parent class Shape. Both inherit display().

**Important Concepts:** hierarchical inheritance

## Experiment 15: 15_array_functions.py

**Problem Statement:** Write a Python program to demonstrate 10 functions or operations of the array module.

**Program:**

```python
from array import array

numbers = array("i", [10, 20, 30])
print("Original:", numbers.tolist())
numbers.append(40)
print("append:", numbers.tolist())
numbers.extend([50, 60])
print("extend:", numbers.tolist())
numbers.insert(1, 15)
print("insert:", numbers.tolist())
print("count:", numbers.count(20))
print("index:", numbers.index(30))
numbers.remove(15)
print("remove:", numbers.tolist())
print("pop:", numbers.pop())
numbers.reverse()
print("reverse:", numbers.tolist())
print("itemsize:", numbers.itemsize)
print("typecode:", numbers.typecode)
```

**Sample Output / Result:**
```text
Shows the integer array after append, extend, insert, remove, pop and reverse, plus count, index, itemsize and typecode values.
```

**Explanation:** Creates an integer array and demonstrates adding, searching, removing, reversing and checking array information.

**Important Concepts:** array(), append(), extend(), insert(), count(), index(), remove(), pop(), reverse(), itemsize, typecode

## Experiment 16: 16_list_functions.py

**Problem Statement:** Write a Python program to demonstrate 10 list methods and functions.

**Program:**

```python
numbers = [30, 10, 20]
print("Original:", numbers)
numbers.append(40)
print("append:", numbers)
numbers.extend([50, 60])
print("extend:", numbers)
numbers.insert(1, 15)
print("insert:", numbers)
numbers.remove(15)
print("remove:", numbers)
print("pop:", numbers.pop())
print("count:", numbers.count(20))
print("index:", numbers.index(20))
numbers.sort()
print("sort:", numbers)
numbers.reverse()
print("reverse:", numbers)
print("length:", len(numbers))
```

**Sample Output / Result:**
```text
Shows the list after each operation, including append, extend, insert, remove, pop, sort and reverse.
```

**Explanation:** Demonstrates common operations for adding, deleting, searching and arranging list elements.

**Important Concepts:** append(), extend(), insert(), remove(), pop(), count(), index(), sort(), reverse(), len()

## Experiment 17: 17_dictionary_functions.py

**Problem Statement:** Write a Python program to demonstrate 10 dictionary methods and functions.

**Program:**

```python
student = {"name": "Viraj", "roll_no": 101, "marks": 85}
print("Original:", student)
print("get:", student.get("name"))
print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))
student.update({"marks": 90})
print("update:", student)
student.setdefault("city", "Kolhapur")
print("setdefault:", student)
print("pop:", student.pop("city"))
copy_student = student.copy()
print("copy:", copy_student)
print("length:", len(student))
student.clear()
print("clear:", student)
```

**Sample Output / Result:**
```text
Displays dictionary keys, values, items and the results of updating, setting a default, popping, copying and clearing entries.
```

**Explanation:** Creates a student dictionary and demonstrates accessing, updating, copying and removing key-value pairs.

**Important Concepts:** get(), keys(), values(), items(), update(), setdefault(), pop(), copy(), len(), clear()

## Experiment 18: 18_string_functions.py

**Problem Statement:** Write a Python program to demonstrate 10 string methods and functions.

**Program:**

```python
text = "  python programming  "
print("Original:", text)
print("upper:", text.upper())
print("lower:", text.lower())
print("title:", text.title())
print("capitalize:", text.capitalize())
print("strip:", text.strip())
print("replace:", text.replace("python", "Java"))
print("find:", text.find("programming"))
print("count:", text.count("m"))
print("startswith:", text.strip().startswith("python"))
print("split:", text.split())
```

**Sample Output / Result:**
```text
Displays the original string and the results of upper, lower, title, capitalize, strip, replace, find, count, startswith and split.
```

**Explanation:** Uses common string methods to change letter case, remove spaces, replace text and search within a string.

**Important Concepts:** upper(), lower(), title(), capitalize(), strip(), replace(), find(), count(), startswith(), split()

## Experiment 19: 19_tuple_functions.py

**Problem Statement:** Write a Python program to demonstrate 10 useful tuple operations and built-in functions.

**Program:**

```python
numbers = (10, 20, 30, 20, 40)
print("Tuple:", numbers)
print("count:", numbers.count(20))
print("index:", numbers.index(30))
print("length:", len(numbers))
print("maximum:", max(numbers))
print("minimum:", min(numbers))
print("sum:", sum(numbers))
print("sorted:", sorted(numbers))
print("first element:", numbers[0])
print("slice:", numbers[1:4])
print("concatenation:", numbers + (50, 60))
```

**Sample Output / Result:**
```text
Tuple: (10, 20, 30, 20, 40)
count: 2
index: 2
length: 5
maximum: 40
minimum: 10
sum: 120
sorted: [10, 20, 20, 30, 40]
first element: 10
slice: (20, 30, 20)
concatenation: (10, 20, 30, 20, 40, 50, 60)
```

**Explanation:** Demonstrates the two tuple methods, count() and index(), along with common built-in functions and tuple operations.

**Important Concepts:** count(), index(), len(), max(), min(), sum(), sorted(), indexing, slicing, concatenation

## Experiment 20: 20_set_functions.py

**Problem Statement:** Write a Python program to demonstrate 10 set methods and operations.

**Program:**

```python
a = {10, 20, 30, 40}
b = {30, 40, 50}

a.add(60)
print("add:", a)
a.update([70, 80])
print("update:", a)
a.remove(80)
print("remove:", a)
a.discard(100)
print("discard:", a)
print("union:", a.union(b))
print("intersection:", a.intersection(b))
print("difference:", a.difference(b))
print("symmetric difference:", a.symmetric_difference(b))
print("issubset:", {30, 40}.issubset(b))
print("issuperset:", b.issuperset({30, 40}))
print("isdisjoint:", a.isdisjoint({100, 200}))
```

**Sample Output / Result:**
```text
Displays the set after adding and removing values and the results of union, intersection, difference and set relationship operations. Set element display order may vary.
```

**Explanation:** Demonstrates adding and removing elements and performing common mathematical set operations.

**Important Concepts:** add(), update(), remove(), discard(), union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset(), isdisjoint()

## Experiment 21: 21_function_lambda.py

**Problem Statement:** Write a Python program to create and call a normal function and a lambda function.

**Program:**

```python
def square(number):
    return number * number

result = square(5)
print("Square using function:", result)

cube = lambda number: number * number * number
print("Cube using lambda:", cube(3))
```

**Sample Output / Result:**
```text
Square using function: 25
Cube using lambda: 27
```

**Explanation:** The square() function uses def, while lambda creates a small anonymous function to calculate a cube.

**Important Concepts:** def, return, function call, lambda

## Experiment 22: 22_package/main.py

**Problem Statement:** Create a Python package for addition and multiplication and use it in another program.

**Program:**

```python
from my_package.operations import add, multiply

print("Addition:", add(10, 5))
print("Multiplication:", multiply(10, 5))
```

**Sample Output / Result:**
```text
Addition: 15
Multiplication: 50
```

**Explanation:** Imports add() and multiply() from the operations module inside my_package and calls them.

**Important Concepts:** package, module, import, __init__.py

## Experiment 23: 23_nltk_stemming.py

**Problem Statement:** Write a Python program to apply stemming using NLTK PorterStemmer.

**Program:**

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["playing", "played", "plays", "happiness", "studies"]

for word in words:
    print(word, "->", stemmer.stem(word))
```

**Sample Output / Result:**
```text
Prints each word and its Porter stem, for example: playing -> play, played -> play, plays -> play.
```

**Explanation:** PorterStemmer reduces related words to their stem. It does not require downloading a text corpus.

**Important Concepts:** NLTK, PorterStemmer, stem()

## Experiment 24: 24_nltk_tokenization.py

**Problem Statement:** Write a Python program to demonstrate word tokenization using NLTK.

**Program:**

```python
from nltk.tokenize import wordpunct_tokenize

sentence = "Python is easy to learn and use."
words = wordpunct_tokenize(sentence)

print("Original sentence:", sentence)
print("Tokens:", words)
```

**Sample Output / Result:**
```text
Original sentence: Python is easy to learn and use.
Tokens: ['Python', 'is', 'easy', 'to', 'learn', 'and', 'use', '.']
```

**Explanation:** wordpunct_tokenize() splits a sentence into individual word and punctuation tokens. It uses NLTK without needing a separate language-data download.

**Important Concepts:** NLTK, wordpunct_tokenize(), tokenization

## Experiment 25: 25_numpy_library.py

**Problem Statement:** Write a Python program to demonstrate NumPy array creation, properties and operations.

**Program:**

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])
print("Array:", numbers)
print("Shape:", numbers.shape)
print("Dimensions:", numbers.ndim)
print("Size:", numbers.size)
print("Data type:", numbers.dtype)
print("Addition:", numbers + 5)
print("Multiplication:", numbers * 2)
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
```

**Sample Output / Result:**
```text
Array: [10 20 30 40]
Shape: (4,)
Dimensions: 1
Size: 4
Data type: int...
Addition: [15 25 35 45]
Multiplication: [20 40 60 80]
Sum: 100
Mean: 25.0
```

**Explanation:** Creates a NumPy array, displays its properties and performs simple mathematical operations.

**Important Concepts:** NumPy, array(), shape, ndim, size, dtype, sum(), mean()

## Experiment 26: 26_pandas_csv.py

**Problem Statement:** Write a Python program using Pandas to read student records from a CSV file and display them in tabular format.

**Program:**

```python
import pandas as pd

students = pd.read_csv("student_records.csv")
print(students)
```

**Sample Output / Result:**
```text
Displays a table with columns Roll Number, Name and Marks for Viraj, Rahul and Amit.
```

**Explanation:** Pandas read_csv() reads the student_records.csv file into a DataFrame. print() displays the records in tabular form.

**Important Concepts:** Pandas, read_csv(), DataFrame

## Experiment 27: 27_abstract_class.py

**Problem Statement:** Write a Python program to demonstrate an abstract class and abstract method.

**Program:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

obj = Rectangle(10, 5)
print("Area of rectangle:", obj.area())
```

**Sample Output / Result:**
```text
Area of rectangle: 50
```

**Explanation:** Shape is an abstract class with an abstract area() method. Rectangle implements area(), so an object of Rectangle can be created.

**Important Concepts:** ABC, abstractmethod, abstract class, method overriding

## Experiment 28: 28_user_defined_exception.py

**Problem Statement:** Write a Python program to create and demonstrate a user-defined exception.

**Program:**

```python
class InvalidMarksError(Exception):
    pass

marks = 120

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    print("Valid marks:", marks)
except InvalidMarksError as error:
    print("Error:", error)
```

**Sample Output / Result:**
```text
Error: Marks must be between 0 and 100
```

**Explanation:** Defines InvalidMarksError by inheriting from Exception. raise creates the exception when marks are outside the valid range.

**Important Concepts:** user-defined exception, class, raise, try, except

## Experiment 29: 29_exception_handling.py

**Problem Statement:** Write a Python program to demonstrate exception handling using try, except, else and finally.

**Program:**

```python
try:
    number1 = 10
    number2 = 0
    result = number1 / number2
except ZeroDivisionError:
    print("A number cannot be divided by zero")
else:
    print("Result:", result)
finally:
    print("Program completed")
```

**Sample Output / Result:**
```text
A number cannot be divided by zero
Program completed
```

**Explanation:** The try block contains code that may cause an error. except handles division by zero, else runs when there is no error, and finally always runs.

**Important Concepts:** try, except, else, finally, ZeroDivisionError
