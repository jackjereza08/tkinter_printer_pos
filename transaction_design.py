from tkinter import *
# from tkinter import font
from tkinter.ttk import *
# from tkinter import messagebox as mgb

HEADER_FONT = ("", 14, "bold")
FONT_STYLE = ("", 12)


class Transaction:
    def __init__(self):
        self.root = Tk()
        self.configure()
        self.header()
        self.root.mainloop()

    def configure(self):

        window_width = 920
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

    def header(self):
        frame = Frame(self.root)
        frame.grid()

        lbl_price = Label(frame, text="Price", font=HEADER_FONT)
        lbl_pages_printed = Label(frame, text="Pages Printed", font=HEADER_FONT)
        lbl_price.grid(row=0, column=2, columnspan=2, sticky=W, padx =5)
        lbl_pages_printed.grid(row=0, column=4, columnspan=2, sticky=W, padx =5)

        labels = ("Paper Type", "Cost", "BW", "Colored", "BW", "Colored", "Full Sales", "Less Shared", "Total Sales", "Net Profit")

        x = 0
        for label in labels:
            l = Label(frame, text=label, font=HEADER_FONT)
            l.grid(row=1, column=x, padx=5)
            x+=1

        data = ("Short","0.75", "3.00", "5.00")

        x=0
        for datum in data:
            l = Label(frame, text=datum, font = FONT_STYLE)
            l.grid(row=2, column=x)
            x+=1

Transaction()