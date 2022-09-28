#POS System by jackjrz
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from scripts.main_script import MainScript
from tkinter import messagebox as mgb


FONT_STYLE = ("", 12)
FONT_STYLE_ENTRY = ("", 14)

class Main:
    def __init__(self):
        self.script = MainScript()
        self.root = Tk()
        self.init_variables()
        self.configure()
        self.menu()
        self.column0()
        self.column1()
        self.column2()
        self.root.mainloop()

    def init_variables(self):
        self.paper_type_index_var = IntVar()
        self.paper_available_var = StringVar()
        self.print_type_var = StringVar()
        self.price_no_var = IntVar()
        self.no_pages_printed_var = IntVar()
        self.amount_var = IntVar()
        self.exact_cash_var = IntVar()
        self.cash_value_var = IntVar()
        self.change_value_var = IntVar()

    def configure(self):
        style = Style()
        style.configure('MyRB.TRadiobutton', font=FONT_STYLE)
        style.configure('MyCH.TCheckbutton', font=FONT_STYLE)
        style.configure('MyCB.TCombobox', font=FONT_STYLE)
        style.configure('MyBTN.TButton', font=FONT_STYLE, background='#00FF22')

        window_width = 590
        window_height = 220

        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.resizable(False,False)
        self.root.title("Print POS")

    def menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Transaction")
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

    def column0(self):
        frame_column0 = Frame(self.root)
        frame_column0.grid(row=0, column=0)
        
        div = Frame(frame_column0)
        lbl_paper_type = Label(div,text="Paper Type", font=FONT_STYLE)
        cmb_paper_type = Combobox(div, style='MyCB.TCombobox')
        cmb_paper_type['values'] = self.script.display_paper_type()
        cmb_paper_type.state(['readonly'])
        cmb_paper_type.bind('<<ComboboxSelected>>', lambda e:self.paper_selection(cmb_paper_type.current()))

        div.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        lbl_paper_type.grid(sticky=W)
        cmb_paper_type.grid(pady=5)
        
        div = Frame(frame_column0)
        rb_print_colored = Radiobutton(div, text="Colored", variable=self.print_type_var, value="Colored", command=lambda: self.select_print_type(cmb_paper_type.current()), style='MyRB.TRadiobutton')
        rb_print_bw = Radiobutton(div, text="Black and White", variable=self.print_type_var, value="BW", command=lambda: self.select_print_type(cmb_paper_type.current()), style='MyRB.TRadiobutton')
        
        div.grid(row=2, column=0, sticky=W, padx=10)
        rb_print_colored.grid(sticky=W)
        rb_print_bw.grid(sticky=W)

        div = Frame(frame_column0)
        lbl_pages_printed = Label(div, text="Pages Printed", font=FONT_STYLE)
        tb_pages_printed = Entry(div, font=FONT_STYLE_ENTRY, width=9)
        tb_pages_printed['textvariable'] = self.no_pages_printed_var
        self.no_pages_printed_var.set("")

        div.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        lbl_pages_printed.grid(sticky=W)
        tb_pages_printed.grid(sticky=W, pady=10)
        tb_pages_printed.bind('<Return>', lambda e:self.calculate_amount())

    def column1(self):
        frame_column1 = Frame(self.root)
        frame_column1.grid(row=0, column=1, rowspan=3, sticky=NW, padx=10, pady=10)

        lbl_available = Label(frame_column1, text="Available Paper", font=FONT_STYLE)
        lbl_available_no = Label(frame_column1, text="0", font=FONT_STYLE)
        lbl_available_no['textvariable'] = self.paper_available_var
        self.paper_available_var.set("0")
        lbl_price = Label(frame_column1, text="Price", font=FONT_STYLE)
        lbl_price_no = Label(frame_column1, text="0.00", font=FONT_STYLE)
        lbl_price_no['textvariable'] = self.price_no_var
        self.price_no_var.set("0.00")
        
        lbl_available.pack(anchor=W)
        lbl_available_no.pack(anchor=E)
        lbl_price.pack(anchor=W)
        lbl_price_no.pack(anchor=E)
    
    def column2(self):
        frame_column2 = Frame(self.root)
        frame_column2.grid(row=0, column=2, padx=10, pady=10, sticky=NSEW)

        div = Frame(frame_column2)

        lbl_amount = Label(div, text="Amount", font=FONT_STYLE)
        lbl_amount_value = Label(div, text="0.00", font=("",30), anchor=E, width=8, background='#FFFFFF', relief=SOLID)
        lbl_amount_value['textvariable'] = self.amount_var
        lbl_amount_value['text'] = "0.00"
        lbl_php = Label(div, text="PHP", font=("",30))
        
        div.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        lbl_amount.grid(row=0, column=0, sticky=W)
        lbl_amount_value.grid(row=1, column=0, ipadx=5, ipady=5, sticky=E)
        lbl_php.grid(row=1, column=1, sticky=E)

        div = Frame(frame_column2)
        div.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        lbl_payment = Label(div, text="Payment", font=FONT_STYLE)
        chk_exact_cash = Checkbutton(div, variable=self.exact_cash_var, text="Exact Cash", style='MyCH.TCheckbutton')
        chk_exact_cash.bind('<Button-1>', lambda e:self.check_exact_cash())
        tb_cash_value = Entry(div, font=FONT_STYLE_ENTRY, width=8, justify=RIGHT)
        lbl_php = Label(div, text="PHP", font=FONT_STYLE_ENTRY)

        lbl_payment.grid(row=0, column=0, sticky=W)
        chk_exact_cash.grid(row=1, column=0)
        tb_cash_value.grid(row=1, column=1, sticky=E)
        lbl_php.grid(row=1, column=2, sticky=E)
        tb_cash_value['textvariable'] = self.cash_value_var
        tb_cash_value.bind('<Return>', lambda e:self.set_change())

        lbl_change = Label(div, text="Change", font=FONT_STYLE)
        lbl_change_value = Label(div, text="0.00",font=FONT_STYLE)
        lbl_php = Label(div, text="PHP", font=FONT_STYLE)
        
        lbl_change.grid(row=2, column=0)
        lbl_change_value.grid(row=2, column=1, sticky=E, ipadx=5, ipady=5)
        lbl_php.grid(row=2, column=2)
        lbl_change_value['textvariable'] = self.change_value_var

        btn_save_transaction = Button(div, text="Save Transaction", style='MyBTN.TButton', command=lambda: self.save_transaction())
        btn_save_transaction.grid(row=3, columnspan=3, sticky=NSEW)

    # Methods to call scripts
    def paper_selection(self, index):
        result = self.script.show_available_no_paper(index)
        self.paper_available_var.set(str(result[0]))
        self.paper_type_index_var.set(index)

    def select_print_type(self, index):
        result = self.script.show_print_price(index, self.print_type_var.get())
        self.price_no_var.set(f"{result[0]}")

    def calculate_amount(self):
        result = self.script.calculate(self.price_no_var.get(), self.no_pages_printed_var.get())
        self.amount_var.set(f"{str(result)}.00")

    def check_exact_cash(self):
        is_exact = self.exact_cash_var.get()
        if is_exact == 0:
            self.cash_value_var.set(self.amount_var.get())
        else:
            self.cash_value_var.set(0)

    def set_change(self):
        self.change_value_var.set(self.cash_value_var.get() - self.amount_var.get())

    def save_transaction(self):
            result = self.script.save_transaction(
                    id_paper=self.paper_type_index_var.get()+1,
                    print_type=self.print_type_var.get(),
                    print_price=self.price_no_var.get(),
                    print_no_page=self.no_pages_printed_var.get()
                )
        
            if result == 1:
                mgb.showinfo(title="Save Transaction", message="Saved Transaction Successfully!")
            else:
                mgb.showerror(title="Save Transaction", message="Saved Transaction Failed!")
        

Main()