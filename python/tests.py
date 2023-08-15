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
        self.assertEqual(calc.A, 31405.0)
    
    def test_input_B(self):
        calc = CalculatorLogic()
        calc.input(1)
        calc.store_value("*")
        calc.input(3)
        calc.input(1)
        calc.input(4)
        calc.input(0)
        calc.input(5)
        self.assertEqual(calc.B, 31405.0)
        
    def test_simple_input_operation(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.result, 15.0)
    
    def test_double_input_A(self):
       
        calc = CalculatorLogic()
        calc.input(3)
        calc.input(0)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.result, 150.0)
    
    def test_double_input_B(self):
    
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.input(0)
        calc.get_result()
        self.assertEqual(calc.result, 150.0)
    
    def test_double_input_AB(self):

        calc = CalculatorLogic()
        calc.input(3)
        calc.input(0)
        calc.store_value("*")
        calc.input(5)
        calc.input(0)
        calc.get_result()
        self.assertEqual(calc.result, 1500.0)
    
    def test_chance_operation(self):

        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.store_value("+")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.result, 8.0)
    
    def test_carry_operation_via_result(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.get_result()
        calc.get_result()
        calc.get_result()
        self.assertEqual(calc.result, 81.0)

    
    def test_carry_operation_via_operator(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("+")
        calc.input(3)
        calc.store_value("+")
        self.assertEqual(calc.result, 6.0)
        calc.input(3)
        calc.store_value("+")
        self.assertEqual(calc.result, 9.0)
        calc.input(3)
        calc.store_value("+")
        self.assertEqual(calc.result, 12.0)
    
    def test_carry_operation_change_operator(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("+")
        calc.get_result()
        calc.store_value("-")
        calc.get_result()
        self.assertEqual(calc.result, 0.0)


# Add other test cases if needed

if __name__ == '__main__':
    unittest.main()
    
    