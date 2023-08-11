from tkinter import *
from tkinter import ttk
from calculator import *
#from functions import * 


A = 0
B = 0
COUNT = 0
Operator = ""
STORED = False
CALCULATED = False

def input(k):
    global CALCULATED, A, COUNT
    print("CALCULATED", CALCULATED)
    print("COUNT", COUNT)
    if COUNT > 0:
        return
    elif CALCULATED:
        A = display_number.get()
        dspl_entry.delete(0, END)
        dspl_entry.insert(0, str(k))
        CALCULATED = False
    elif not CALCULATED:
        val = display_number.get()
        dspl_entry.delete(0, END)
        dspl_entry.insert(0, int(str(val) + str(k)))

def store_value(op):
    global A, Operator, STORED, CALCULATED
    print("CALCULATED", CALCULATED)
    print("STORED", STORED)
    print("Operator", Operator)
    if not STORED:
        Operator = op
        A = display_number.get()
        dspl_entry.delete(0, END)
        STORED = True
    elif CALCULATED:
        dspl_entry.delete(0, END)
        get_result()
    else:
        get_result()

def parse_operation():
    global A, B, Operator
    match Operator:
        case "*":
            return multiply(A, B)
        case "/":
            return divide(A, B)
        case "+":
            return add(A, B)
        case "-":
            return subtract(A, B)

def get_result():
    global Operator, CALCULATED, STORED,COUNT, A, B
    B = display_number.get()
    print(A,B)
    if A == 0: 
        return
    elif B == 0:
        return
    COUNT = 0
    CALCULATED = True
    STORED = False
    result = parse_operation()
    print(result)
    dspl_entry.delete(0, END)
    dspl_entry.insert(0, int(result))
    A = display_number.get()

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

display_number = StringVar()
feet = StringVar()
dspl_entry = ttk.Entry(mainframe, width=20, textvariable=display_number)
dspl_entry.grid(column=1, row=1, sticky=(W))

debug_A = ttk.Label(mainframe, text="x")
debug_A.grid(column=5, row=1, sticky=(W))
debug_A.bind('<ButtonPress-1>', lambda e: debug_A.configure(text='A = %s, B = %s' % (A, B)))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

select_button = ttk.Frame(root, padding="3 3 12 12")
select_button.grid(column=0, row=3, sticky=(N, W, E, S))

button_labels = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
row = 6
col = 1
for label in button_labels:
    ttk.Button(select_button, text=label, command=lambda l=label: input(l)).grid(column=col, row=row, sticky=W)
    col += 1
    if col > 3:
        col = 1
        row += 1

ttk.Button(select_button, text=0, command=lambda l=0: input(l)).grid(column=2, row=9, sticky=W)

ttk.Button(select_button, text="*", command=lambda x="*": store_value(x)).grid(column=4, row=6, sticky=W)
ttk.Button(select_button, text="-", command=lambda x="-": store_value(x)).grid(column=4, row=7, sticky=W)
ttk.Button(select_button, text="+", command=lambda x="+": store_value(x)).grid(column=4, row=8, sticky=W)
ttk.Button(select_button, text="=", command=lambda x="=": get_result()).grid(column=4, row=9, sticky=W)



ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

dspl_entry.focus()
root.bind("<Return>", get_result)

root.mainloop()