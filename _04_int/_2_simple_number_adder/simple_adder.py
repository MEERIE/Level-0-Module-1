"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
window=Tk()
window.withdraw()
num1 = simpledialog.askinteger(title=None, prompt="Provide a number")
num2 = simpledialog.askinteger(title=None, prompt="Provide another number")
num3 = num1 + num2
messagebox.showinfo(message=str(num3))
