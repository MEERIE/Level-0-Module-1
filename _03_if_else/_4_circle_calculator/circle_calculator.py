from tkinter import messagebox, simpledialog, Tk
import math

window = Tk()
window.withdraw()
# Write a Python program that asks the user for the radius of a circle.
radius = simpledialog.askinteger(title='None', prompt='Input A Radius For Your Circle')
# Next, ask the user if they would like to calculate the area or circumference of a circle.
radorcirc = simpledialog.askstring(title='None', prompt='Would you like to calculate Area or Circumference')
# If they choose area, display the area of the circle using the radius.
area = math.pi*(radius**2)
if radorcirc == 'area' or radorcirc == 'Area':
    messagebox.showinfo(title='None', message='Your area is going to be ' + str(area))

# Otherwise, display the circumference of the circle using the radius.
