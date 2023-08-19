from operations import *


class CalculatorLogic:
    def __init__(self):
        self.A = None
        self.B = None
        self.step = 0
        self.count = None
        self.visor = None
        self.result = None
        self.track = None
        self.math_operator = None
        self.mode = "INTEGER"

    def input(self, x):
        match self.mode:
            case "INTEGER":
                if self.step == 0:
                    if self.A is None:
                        self.A = x
                    else:
                        self.A = int(str(self.A) + str(x))
                    self.visor = self.A
                elif self.step == 1:
                    if self.B is None:
                        self.B = x
                    else:
                        self.B = int(str(self.B) + str(x))
                    self.visor = self.B
            case "FLOAT":
                return
        self.track = "INPUT"

    def store_value(self, operator):
        if self.track == "INPUT" and self.step == 1:
            self.get_result("NONE")
        elif self.track == "RESULT":
            self.math_operator = operator
        elif self.track == "OPERATOR":
            self.math_operator = operator
            return
        self.math_operator = operator
        self.track = "OPERATOR"
        self.step = 1

    def get_result(self, source="CALL"):
        if self.track == "OPERATOR":
            self.B = self.result
        if self.B is None:
            self.B = self.A
        if source != "NONE":
            self.track = "RESULT"
        self.step = 0
        self.result = self.parse_math_operation()
        self.A = self.result
        self.visor = self.result

    def parse_math_operation(self):
        match self.math_operator:
            case "*":
                return multiply(self.A, self.B)
            case "/":
                return divide(self.A, self.B)
            case "+":
                return add(self.A, self.B)
            case "-":
                return subtract(self.A, self.B)

    def clear_all(self):
        self.A = None
        self.B = None
        self.step = 0
        self.count = None
        self.visor = None
        self.result = None
        self.math_operator = None

    def input_float(self):
        self.mode = "FLOAT"
        """
    def clear_last():
        if STEP == 1:
            STEP = 0
        B.set(0)
        #clear display
        """