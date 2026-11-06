import matplotlib.pyplot as plt

categories = ["Food", "Travel", "Hotel", "Shopping"]
expenses = [3000, 2000, 4000, 1000]

plt.pie(expenses, labels=categories, autopct="%1.1f%%")
plt.title("Trip Expense Distribution")
plt.show()
