from tkinter import *
# from tkinter import font
from tkinter.ttk import *
# from tkinter import messagebox as mgb

class Transaction:
    def __init__(self):
        self.root = Tk()
        self.configure()
        self.root.mainloop()

    def configure(self):

        window_width = 900
        window_height = 490

        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.resizable(False,False)
        self.root.title("Print POS - Transaction Summary")

    


Transaction()