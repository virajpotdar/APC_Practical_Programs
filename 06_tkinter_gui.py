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
