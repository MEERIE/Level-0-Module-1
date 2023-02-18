"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
window=Tk()
window.withdraw()
num1 = simpledialog.askinteger(title=None, prompt="Provide a number")
num2 = simpledialog.askinteger(title=None, prompt="Provide another number")
math = simpledialog.askstring(title=None, prompt="Would you like to add, subtract, multiply, or divide?")

if math == "add":
    messagebox.showinfo(message=int(num1)+int(num2))
elif math == "multiply":
    messagebox.showinfo(message=int(num1)*int(num2))
elif math == "divide":
    messagebox.showinfo(message=int(num1)/int(num2))
elif math == "subtract":
    messagebox.showinfo(message=int(num1)-int(num2))
