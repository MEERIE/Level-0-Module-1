from tkinter import messagebox, simpledialog, Tk

"""
* Write a python program that asks the user a minimum of 3 riddles.
 
* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
window = Tk()
window.withdraw()
riddle1 = simpledialog.askstring(title="Respond with 1 word", prompt="What gets more wet the more it dries?")
count = 0
if riddle1 == "towel":
    count += 1
    print(count)
riddle2 = simpledialog.askstring(title="Respond with 1 word", prompt="Who makes you food but is not your cook?")
