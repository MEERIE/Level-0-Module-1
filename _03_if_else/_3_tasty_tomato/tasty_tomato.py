from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
tomato = simpledialog.askstring(title=None, prompt="What color Tomato Would you Like? Red, Blue or Green?")
print(tomato)
# 2. Use if-else statements to draw the tomato in the color that they chose
if tomato == "Red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
elif tomato == "Blue":
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
elif tomato == "Green":
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
else:
    messagebox.dialog(Title=None, message="SORRY this color is not available!")
root.mainloop()
