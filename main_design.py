#POS System by jackjrz
from tkinter import *
from tkinter import font
from tkinter.ttk import *


FONT_STYLE = ("", 12)
FONT_STYLE_ENTRY = ("", 14)

class main:
    def __init__(self):
        root = Tk()
        self.configure()
        self.column0(root)
        self.column1(root)
        self.column2(root)
        root.mainloop()

    def configure(self):
        style = Style()
        style.configure('MyRB.TRadiobutton', font=FONT_STYLE)
        style.configure('MyCH.TCheckbutton', font=FONT_STYLE)
        style.configure('MyCB.TCombobox', font=FONT_STYLE)
        style.configure('MyBTN.TButton', font=FONT_STYLE, background='#00FF22')

    def column0(self,root):
        frame_column0 = Frame(root)
        frame_column0.grid(row=0, column=0)

        div = Frame(frame_column0)
        div.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        lbl_paper_type = Label(div,text="Paper Type", font=FONT_STYLE)
        lbl_paper_type.grid(sticky=W)

        def paper_selection(event):
            print(f"Selected: {cmb_paper_type.get()}")

        paper_type_var = StringVar()
        cmb_paper_type = Combobox(div, textvariable=paper_type_var, style='MyCB.TCombobox')
        cmb_paper_type['values'] = ('Short', 'Long', 'A4')
        cmb_paper_type.state(['readonly'])
        cmb_paper_type.bind('<<ComboboxSelected>>', paper_selection)
        cmb_paper_type.grid(pady=5)

        def rb_selection():
            print(f"Selected: {print_type_var.get()}")
        
        div = Frame(frame_column0)
        div.grid(row=2, column=0, sticky=W, padx=10)
        print_type_var = IntVar()

        rb_print_colored = Radiobutton(div, text="Colored", variable=print_type_var, value=1, command=rb_selection, style='MyRB.TRadiobutton')
        rb_print_bw = Radiobutton(div, text="Black and White", variable=print_type_var, value=2, command=rb_selection, style='MyRB.TRadiobutton')
        rb_print_colored.grid(sticky=W)
        rb_print_bw.grid(sticky=W)

        div = Frame(frame_column0)
        div.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        lbl_pages_printed = Label(div, text="Pages Printed", font=FONT_STYLE)
        lbl_pages_printed.grid(sticky=W)

        tb_pages_printed = Entry(div, font=FONT_STYLE_ENTRY, width=9)
        tb_pages_printed.grid(sticky=W, pady=10)


    def column1(self, root):
        frame_column1 = Frame(root)
        frame_column1.grid(row=0, column=1, rowspan=3, sticky=NW, padx=10, pady=10)

        lbl_available = Label(frame_column1, text="Available Paper", font=FONT_STYLE)
        lbl_available_no = Label(frame_column1, text="0", font=FONT_STYLE)
        lbl_price = Label(frame_column1, text="Price", font=FONT_STYLE)
        lbl_price_no = Label(frame_column1, text="Php 0.00 per pages", font=FONT_STYLE)
        lbl_available.pack(anchor=W)
        lbl_available_no.pack(anchor=E)
        lbl_price.pack(anchor=W)
        lbl_price_no.pack(anchor=W)

    
    def column2(self, root):
        frame_column2 = Frame(root)
        frame_column2.grid(row=0, column=2, padx=10, pady=10, sticky=NSEW)

        div = Frame(frame_column2)
        div.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        lbl_amount = Label(div, text="Amount", font=FONT_STYLE)
        lbl_amount.grid(row=0, column=0, sticky=W)

        lbl_amount_value = Label(div, text="0.00", font=("",30), anchor=E, width=8, background='#FFFFFF', relief=SOLID)
        lbl_php = Label(div, text="PHP", font=("",30))
        lbl_amount_value.grid(row=1, column=0, ipadx=5, ipady=5, sticky=E)
        lbl_php.grid(row=1, column=1, sticky=E)

        div = Frame(frame_column2)
        div.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        lbl_payment = Label(div, text="Payment", font=FONT_STYLE)
        lbl_payment.grid(row=0, column=0, sticky=W)

        exact_cash_var = IntVar()
        chk_exact_cash = Checkbutton(div, variable=exact_cash_var, text="Exact Cash", style='MyCH.TCheckbutton')
        tb_cash_value = Entry(div, font=FONT_STYLE_ENTRY, width=8, justify=RIGHT)
        lbl_php = Label(div, text="PHP", font=FONT_STYLE_ENTRY)
        chk_exact_cash.grid(row=1, column=0)
        tb_cash_value.grid(row=1, column=1, sticky=E)
        lbl_php.grid(row=1, column=2, sticky=E)

        lbl_change = Label(div, text="Change", font=FONT_STYLE)
        lbl_change_value = Label(div, text="0.00",font=FONT_STYLE)
        lbl_php = Label(div, text="PHP", font=FONT_STYLE)
        lbl_change.grid(row=2, column=0)
        lbl_change_value.grid(row=2, column=1, sticky=E, ipadx=5, ipady=5)
        lbl_php.grid(row=2, column=2)

        btn_save_transaction = Button(div, text="Save Transaction", style='MyBTN.TButton')
        btn_save_transaction.grid(row=3, columnspan=3, sticky=NSEW)


pos = main()