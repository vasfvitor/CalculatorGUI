def add(x, y):
    return float(int(x) + int(y))

def subtract(x, y):
    return float(int(x) - int(y))

def multiply(x, y):
    return float(int(x) * int(y))

def divide(x, y):
    if int(y) == 0:
        print("Can't be")
    return float(int(x) / int(y))