def square(number):
    return number * number

result = square(5)
print("Square using function:", result)

cube = lambda number: number * number * number
print("Cube using lambda:", cube(3))
