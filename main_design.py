#POS System by jackjrz
from tkinter import *
from tkinter.ttk import *

class main:
    def __init__(self):
        root = Tk()
        self.column0(root)
        self.column1(root)
        self.column2(root)
        root.mainloop()

    def column0(self,root):
        frame_column0 = Frame(root)
        frame_column0.grid(row=0, column=0)

        lbl_paper_type = Label(frame_column0,text="Paper Type")
        lbl_paper_type.pack()

        def paper_selection(event):
            print(f"Selected: {cmb_paper_type.get()}")

        paper_type_var = StringVar()
        cmb_paper_type = Combobox(frame_column0, textvariable=paper_type_var)
        cmb_paper_type['values'] = ('Short', 'Long', 'A4')
        cmb_paper_type.state(['readonly'])
        cmb_paper_type.bind('<<ComboboxSelected>>', paper_selection)
        cmb_paper_type.pack()

        def rb_selection():
            print(f"Selected: {print_type_var.get()}")
        
        print_type_var = IntVar()
        rb_print_colored = Radiobutton(frame_column0, text="Colored", variable=print_type_var, value=1, command=rb_selection)
        rb_print_bw = Radiobutton(frame_column0, text="Black and White", variable=print_type_var, value=2, command=rb_selection)
        rb_print_colored.pack()
        rb_print_bw.pack()

        lbl_pages_printed = Label(frame_column0, text="Pages Printed")
        lbl_pages_printed.pack()

        tb_pages_printed = Entry(frame_column0)
        tb_pages_printed.pack(padx=10, pady=10)


    def column1(self, root):
        frame_column1 = Frame(root)
        frame_column1.grid(row=0, column=1)

        lbl_available = Label(frame_column1, text="Available Paper")
        lbl_available_no = Label(frame_column1, text="0")
        lbl_price = Label(frame_column1, text="Price")
        lbl_price_no = Label(frame_column1, text="Php 0.00 per pages")
        lbl_available.pack()
        lbl_available_no.pack()
        lbl_price.pack()
        lbl_price_no.pack()

    
    def column2(self, root):
        frame_column2 = Frame(root)
        frame_column2.grid(row=0, column=2)

        lbl_amount = Label(frame_column2, text="Amount")
        lbl_amount.pack()
        frame_div = Frame(frame_column2)
        frame_div.pack()

        lbl_amount_value = Label(frame_div, text="0.00")
        lbl_php = Label(frame_div, text="PHP")
        lbl_amount_value.grid(row=0, column=0, ipady=5)
        lbl_php.grid(row=0, column=1)

        lbl_payment = Label(frame_div, text="Payment")
        lbl_payment.grid(row=1, columnspan=2)

        exact_cash_var = IntVar()
        chk_exact_cash = Checkbutton(frame_div, variable=exact_cash_var, text="Exact Cash")
        tb_cash_value = Entry(frame_div)
        lbl_php = Label(frame_div, text="PHP")
        chk_exact_cash.grid(row=2, column=0)
        tb_cash_value.grid(row=2, column=1)
        lbl_php.grid(row=2, column=2)

        lbl_change = Label(frame_div, text="Change")
        lbl_change_value = Label(frame_div, text="0.00")
        lbl_php = Label(frame_div, text="PHP")
        lbl_change.grid(row=3, column=0)
        lbl_change_value.grid(row=3, column=1)
        lbl_php.grid(row=3, column=2)

        btn_save_transaction = Button(frame_div, text="Save Transaction")
        btn_save_transaction.grid(row=4, columnspan=3)


pos = main()