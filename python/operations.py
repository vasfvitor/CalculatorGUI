import math


def add(x, y):
    try:
        res = float(float(x) + float(y))
        out = int(res) if res.is_integer() else res
    except:
        print("ERROR: ADDITION")
    return out


def subtract(x, y):
    try:
        res = float(float(x) - float(y))
        out = int(res) if res.is_integer() else res
        return out
    except:
        print("ERROR: SUBTRACTION")


def multiply(x, y):
    try:
        res = float(float(x) * float(y))
        out = int(res) if res.is_integer() else res
        return out
    except:
        print("ERROR: MULTIPLY")


def divide(x, y):
    try:
        if float(y) == 0.0:
            print("Can't be")
            return "Can't divide by 0"
        res = float(float(x) / float(y))
        out = int(res) if res.is_integer() else res
        return out
    except:
        print("ERROR: DIVISION")
