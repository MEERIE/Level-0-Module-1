"""
 * Write a python program that prints the word 'banana' one thousand (1,000) times
"""
import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    green = turtle.Turtle()
    green.penup()
    x = -475
    y = 380
    green.goto(x, y)
    green.pendown()
    for i in range(1000):
        print(green.xcor())
        green.write(arg="banana ", move=True, align='left', font=('Arial', 18, 'normal'))
        if green.xcor() > 475:
            y -= 25
            x = -475
            green.penup()
            green.goto(x, y)

