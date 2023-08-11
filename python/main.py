from tkinter import *
from tkinter import ttk
from operations import *
#from functions import * 

A = 0
B = 0
COUNT = 0
OPERATION = ""
FIRST_OPERATION = True
RESULTADO_NA_TELA = False


# typing number
def input(k):
    global RESULTADO_NA_TELA, A, COUNT
    if COUNT > 0:
        return
    elif RESULTADO_NA_TELA:
        A = display_num.get()
        dspl_entry.delete(0, END)
        dspl_entry.insert(0, str(k))
        RESULTADO_NA_TELA = False
    elif not RESULTADO_NA_TELA:
        val = display_num.get()
        dspl_entry.delete(0, END)
        dspl_entry.insert(0, int(str(val) + str(k)))

# called when "+ - / *"
def store_value(op):
    global A, OPERATION, FIRST_OPERATION, RESULTADO_NA_TELA
    OPERATION = op
    if FIRST_OPERATION:
        A = display_num.get()   
        dspl_entry.delete(0, END)
        FIRST_OPERATION = False
    elif RESULTADO_NA_TELA:
        get_result(True)
    else:
        print("ELSE!!!", RESULTADO_NA_TELA)
        get_result(True)

def parse_operation():
    global A, B, OPERATION
    match OPERATION:
        case "*":
            return multiply(A, B)
        case "/":
            return divide(A, B)
        case "+":
            return add(A, B)
        case "-":
            return subtract(A, B)

def get_result(flag):
    global OPERATION, RESULTADO_NA_TELA, FIRST_OPERATION,COUNT, A, B
    B = display_num.get()
    print(A,B)
    if A == 0 or B == 0: 
        return
    COUNT = 0
    if not RESULTADO_NA_TELA:
        FIRST_OPERATION = True
    RESULTADO_NA_TELA = True
    result = parse_operation()
    print(result)
    A = result
    dspl_entry.delete(0, END)
    dspl_entry.insert(0, int(result))

def traceee(*args):
    global A,B
    print(A,B) 

def clear_all():
    global A, B, OPERATION
    OPERATION = ""
    A = B = 0
    dspl_entry.delete(0, END) 

def clear_last():
    global B
    B = 0
    dspl_entry.delete(0, END) 

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

display_num = StringVar()
feet = StringVar()
display_num.trace('w', traceee)
dspl_entry = ttk.Entry(mainframe, width=20, textvariable=display_num)
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


ttk.Button(select_button, text="/", command=lambda x="/": store_value(x)).grid(column=4, row=5, sticky=W)
ttk.Button(select_button, text="*", command=lambda x="*": store_value(x)).grid(column=4, row=6, sticky=W)
ttk.Button(select_button, text="-", command=lambda x="-": store_value(x)).grid(column=4, row=7, sticky=W)
ttk.Button(select_button, text="+", command=lambda x="+": store_value(x)).grid(column=4, row=8, sticky=W)
ttk.Button(select_button, text="=", command=lambda x="=": get_result(False)).grid(column=4, row=9, sticky=W)

ttk.Button(select_button, text="C", command=clear_all).grid(column=4, row=3, sticky=W)
ttk.Button(select_button, text="CE", command=clear_last).grid(column=3, row=3, sticky=W)



ttk.Label(mainframe, text="YAC").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

dspl_entry.focus()
root.bind("<Return>", get_result)

root.mainloop()