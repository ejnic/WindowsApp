import tkinter as tk
import random as rd


window = tk.Tk()

def RandomNumber():
    mynumber = rd.randint(1,6)
    dice_thrown.configure(text = 'Dice thrown: ' + str(mynumber))


mytitle = tk.Label(window, text = 'Random number generator', font = 'Helvetica 16 bold')
mytitle.pack()

mybutton = tk.Button(window, text = 'OK', command = RandomNumber)
mybutton.pack()

dice_thrown = tk.Label(window, text = 'OK', font = 'Helvetica 16 bold')
dice_thrown.pack()

window.mainloop()





