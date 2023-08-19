from tkinter import *
from tkinter import ttk
from calculator import *


class GuiCalculator(CalculatorLogic):

    def __init__(self):
        super().__init__()
        self.math_operators = ["/", "*", "-", "+"]

    def gui_input(self, k):
        self.input(k)
        vod.delete(0, END)
        vod.insert(0, self.visor)

    def gui_get_result(self, origin):
        self.get_result(origin)
        vod.delete(0, END)
        vod.insert(0, self.visor)

    def gui_store_value(self, op):
        self.store_value(op)
        vod.delete(0, END)
        vod.insert(0, self.visor)

    def gui_clear_all(self):
        vod.delete(0, END)
        self.clear_all()

    def gui_clear_last(self):
        vod.delete(0, END)
        self.clear_last()

    def on_key_press(self, e):
        key = e.char
        print(key)
        if key.isdigit():
            self.gui_input(key)
        elif key in self.math_operators:
            self.gui_store_value(key)
        # elif key == "Enter":
        #    self.gui_get_result


calc = GuiCalculator()

# tkinter
root = Tk()
root.title("Calculator")

root.bind("<KeyPress>", calc.on_key_press)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# display
display_val = StringVar()
vod = ttk.Entry(
    mainframe, width=40, justify="right", cursor="man", textvariable=display_val)
vod.grid(column=1, row=1, sticky=W)
# vod.configure(family="Helvetica", size=36, weight="bold")

# input field
input_field = ttk.Frame(root, padding="3 3 12 12")
input_field.grid(column=0, row=3, sticky=(N, W, E, S))

button_labels = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
ROW = 6
COL = 1
# number field
for label in button_labels:
    ttk.Button(input_field, text=label, command=lambda l=label: calc.gui_input(l)).grid(
        column=COL, row=ROW, sticky=W)
    COL += 1
    if COL > 3:
        COL = 1
        ROW += 1
# 0
ttk.Button(input_field, text=0, command=lambda l=0: calc.gui_input(l)
           ).grid(column=2, row=9, sticky=W)


math_operations = calc.math_operators
# basic operations
for row, op in enumerate(math_operations, start=5):
    ttk.Button(input_field, text=op, command=lambda x=op: calc.gui_store_value(x)
               ).grid(column=4, row=row, sticky=W)

# get result
ttk.Button(input_field, text="=", command=lambda x="=": calc.gui_get_result(
    "FROM_BUTTON")).grid(column=4, row=9, sticky=W)


# reset
ttk.Button(input_field, text="C", command=calc.gui_clear_all).grid(
    column=4, row=3, sticky=W)
ttk.Button(input_field, text="CE", command=calc.gui_clear_last).grid(
    column=3, row=3, sticky=W)


# whatever
ttk.Label(mainframe, text="label").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

vod.focus()
root.bind("<Return>", calc.gui_get_result)

root.mainloop()
