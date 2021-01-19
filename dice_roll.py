from dice import dice_list, numerical_association
from tkinter import *
import random


class Dice_Roll:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.label = Label(master, font=(200), anchor=(CENTER))
        button = Button(master, text=("Roll Dice!"), command=self.roll)
        button.place(x=200, y=0)
    
    def roll(self):
        dice1 = random.randint(0, len(dice_list))
        dice2 = random.randint(0, len(dice_list))
        self.label.config(text="\u2680")
        self.label.pack()
    

if __name__ == '__main__':
    root = Tk()
    root.title("Dice Roller")
    root.geometry("500x300")
    Dice_Roll(root)
    root.mainloop()

    