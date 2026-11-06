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
