from tkinter import *
# from tkinter import font
from tkinter.ttk import *
from scripts.transaction_script import TransactionSum
# from tkinter import messagebox as mgb

HEADER_FONT = ("", 14, "bold")
FONT_STYLE = ("", 12)


class Transaction:
    def __init__(self):
        self.root = Tk()
        self.configure()
        self.frame = Frame(self.root)
        self.frame.grid()
        self.header()
        self.content()
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
        lbl_price = Label(self.frame, text="Price", font=HEADER_FONT)
        lbl_pages_printed = Label(self.frame, text="Pages Printed", font=HEADER_FONT)
        lbl_price.grid(row=0, column=2, columnspan=2, sticky=W, padx =5)
        lbl_pages_printed.grid(row=0, column=4, columnspan=2, sticky=W, padx =5)

        labels = ("Paper Type", "Cost", "Colored", "BW", "Colored", "BW", "Full Sales", "Less Shared", "Total Sales", "Net Profit")

        x = 0
        for label in labels:
            l = Label(self.frame, text=label, font=HEADER_FONT)
            l.grid(row=1, column=x, padx=5)
            x+=1

    def content(self):
        tran_sum = TransactionSum()

        paper_type_list = tran_sum.display_paper_type_all()
        id_paper_list = tran_sum.get_paper_id()
        cost_list = tran_sum.display_cost_all()

        # Display Paper Type
        x=2
        for paper_type in paper_type_list:
            l = Label(self.frame, text=paper_type, font = FONT_STYLE)
            l.grid(row=x, column=0, padx=5, sticky=NSEW)
            x+=1
        # Display Cost
        x=2
        for cost in cost_list:
            l = Label(self.frame, text=cost, font = FONT_STYLE)
            l.grid(row=x, column=1, padx=5, sticky=NSEW)
            x+=1
        # Diplay Price
        x=2
        index = 2
        for id in id_paper_list:
            price = tran_sum.display_price_all(id)
            for p in price:
                l = Label(self.frame, text=p, borderwidth=1, relief=SOLID, font = FONT_STYLE)
                l.grid(row=x, column=index, padx=5, sticky=NSEW)
                index+=1
            x+=1


Transaction()