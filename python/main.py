from tkinter import *
from tkinter import ttk
from operations import *

STEP = 0
COUNT = 0
EQUAL = 0

def parse_math_operation():
    x = A.get()
    y = B.get()
    if last_result.get() != 0:
        y = last_result.get()
    match math_operation.get():
        case "*":
            return multiply(x, y)
        case "/":
            return divide(x, y)
        case "+":
            return add(x, y)
        case "-":
            return subtract(x, y)

def clear_operator():
    A.set(0)
    B.set(0)
    last_result.set(0)
    math_operation.set("")

def clear_all():
    global STEP
    STEP = 0
    A.set(0)
    B.set(0)
    last_result.set(0)
    math_operation.set("")
    current_display.set("")
    value_on_display.delete(0, END)

def clear_last():
    global STEP
    if STEP == 1:
        STEP = 0
    B.set(0)
    value_on_display.delete(0, END)

def input(k):
    global COUNT
    COUNT+=1
    #print(last_result.get())
    if last_result.get() != 0:
        value_on_display.delete(0, END)
        value_on_display.insert(0, str(k))
    else:
        val = current_display.get()
        value_on_display.delete(0, END)
        value_on_display.insert(0, (str(val) + str(k)))

def store_value(op):
    global STEP
    math_operation.set(op)
    if STEP == 0:
        A.set(current_display.get())
        STEP+=1
        value_on_display.delete(0, END)
    else:
        #STEP = 0
        B.set(current_display.get())
        get_result("FROM_FUNCTION")
    print("A ", A.get(),"  B ", B.get())
    

def get_result(origin):
    global COUNT, EQUAL
   
    if COUNT == 1:
        print("COUNT",COUNT)
        B.set(A.get())
        result = handle_result()
        return result
    print("A ", A.get(),"  B ", B.get())
    if origin == "FROM_FUNCTION":
        print("FROM_FUNCTION")
        B.set(current_display.get())
        return handle_result()
    #
    if origin == "FROM_BUTTON":
        print("FROM_BUTTON")
       
        EQUAL+=1
        B.set(current_display.get())
        result = handle_result()
        clear_operator()
    return result

def handle_result():
    result = parse_math_operation()
    last_result.set(result)
    print("result ", result)
    value_on_display.delete(0, END)
    value_on_display.insert(0, result)
    return result

def close_app():
    root.destroy()

## tkinter
root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# values
A = DoubleVar() # first value  - x
B = DoubleVar() # second value - y
last_result = DoubleVar()
math_operation = StringVar()

# display
current_display = StringVar()
value_on_display = ttk.Entry(mainframe, width=20, textvariable=current_display)
value_on_display.grid(column=1, row=1, sticky=W)

## input field
input_field = ttk.Frame(root, padding="3 3 12 12")
input_field.grid(column=0, row=3, sticky=(N, W, E, S))

button_labels = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
ROW = 6
COL = 1
# number field
for label in button_labels:
    ttk.Button(input_field, text=label, command=lambda l=label: input(l)).grid(
        column=COL, row=ROW, sticky=W)
    COL += 1
    if COL > 3:
        COL = 1
        ROW += 1
# 0
ttk.Button(input_field, text=0, command=lambda l=0: input(l)
           ).grid(column=2, row=9, sticky=W)


math_operations = ["/", "*", "-", "+"]
# basic operations
for row, op in enumerate(math_operations, start=5):
    ttk.Button(input_field, text=op, command=lambda x=op: store_value(x)
               ).grid(column=4, row=row, sticky=W)

# get result
ttk.Button(input_field, text="=", command=lambda x="=": get_result(
    "FROM_BUTTON")).grid(column=4, row=9, sticky=W)


# reset
ttk.Button(input_field, text="C", command=clear_all).grid(
    column=4, row=3, sticky=W)
ttk.Button(input_field, text="CE", command=clear_last).grid(
    column=3, row=3, sticky=W)


# whatever
ttk.Label(mainframe, text="YAC").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

value_on_display.focus()
root.bind("<Return>", get_result)

root.mainloop()


