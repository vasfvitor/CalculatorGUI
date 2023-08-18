import unittest
from calculator import *



class TestCalculatorFunctions(unittest.TestCase):

    def test_input_A(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.input(1)
        calc.input(4)
        calc.input(0)
        calc.input(5)
        self.assertEqual(calc.visor, 31405.0)
    
    def test_input_B(self):
        calc = CalculatorLogic()
        calc.input(1)
        calc.store_value("*")
        calc.input(3)
        calc.input(1)
        calc.input(4)
        calc.input(0)
        calc.input(5)
        self.assertEqual(calc.visor, 31405.0)
        
    def test_single_input_operation(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.visor, 15.0)
    
    def test_double_input_A(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.input(0)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.visor, 150.0)
    
    def test_double_input_B(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.input(0)
        calc.get_result()
        self.assertEqual(calc.visor, 150.0)
    
    def test_double_input_AB(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.input(0)
        calc.store_value("*")
        calc.input(5)
        calc.input(0)
        calc.get_result()
        self.assertEqual(calc.visor, 1500.0)
    
    def test_change_operation(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.store_value("+")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.result, 8.0)
    
    def test_carry_via_result(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.get_result()
        calc.get_result()
        calc.get_result()
        self.assertEqual(calc.result, 81.0)

    def test_carry_via_operator(self):
        calc = CalculatorLogic()
        calc.input(1)
        calc.store_value("+")
        calc.input(9)
        calc.store_value("+")
        self.assertEqual(calc.result, 10.0)
        calc.input(2)
        calc.store_value("+")
        self.assertEqual(calc.result, 12.0)
        calc.input(5)
        calc.store_value("+")
        self.assertEqual(calc.result, 15.0)
    
    def test_carry_operation_change_operator(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("+")
        calc.get_result()
        calc.store_value("-")
        calc.get_result()
        self.assertEqual(calc.result, 0.0)

    def test_output_int(self):
        calc = CalculatorLogic()
        calc.input(16)
        calc.store_value("/")
        calc.input(2)
        calc.get_result()
        self.assertEqual(calc.result, 8)
    
    def test_output_float(self):
        calc = CalculatorLogic()
        calc.input(5)
        calc.store_value("/")
        calc.input(2)
        calc.get_result()
        self.assertEqual(calc.result, 2.5)

if __name__ == '__main__':
    unittest.main()
    
    