from tkinter import *

window_width = 800
window_height = 800
root = Tk()

canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()

# This code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # Draws a dark blue background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="#000050")

    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    

    
    # 1. Add details to your rocket to make it look better. You can look at
    #    rocket.png for inspiration.
    canvas.create_oval(x+25, y+300, x-25, y+50, fill='red')
    canvas.create_oval(x+20, y+200, x-20, y+50, fill='yellow')
    # 2. Modify the locations of the shapes above so the rocket will be drawn
    #    where the mouse is clicked
    # This defines the x and y coordinated of all three points
    # of a triangle
    points = [x, y, x - 50, y + 100, x + 50, y + 100]
    canvas.create_polygon(points, fill='gray', width=2) # draws triangle

# ====================== DO NOT MODIFY THE CODE BELOW ========================

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()
