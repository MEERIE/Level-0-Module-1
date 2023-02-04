import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    green = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title=None, prompt="Choose: triangle, square, circle")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "triangle":
        for i in range(3):
            green.forward(100)
            green.right(120)
    elif shape == "circle":
        green.circle(100)
    elif shape == "square":
        for i in range(4):
            green.forward(150)
            green.right(90)
    # Call the turtle .done() method
    green.done()
