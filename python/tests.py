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
        self.assertEqual(calc.visor, 8.0)
    
    def test_carry_via_result(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.get_result()
        calc.get_result()
        calc.get_result()
        self.assertEqual(calc.visor, 81.0)

    def test_carry_via_operator(self):
        calc = CalculatorLogic()
        calc.input(1)
        calc.input(1)
        calc.store_value("+")
        calc.input(9)
        calc.store_value("+")
        self.assertEqual(calc.visor, 20.0)
        calc.input(2)
        calc.input(2)
        calc.store_value("-")
        self.assertEqual(calc.visor, 42.0)
        calc.input(5)
        calc.store_value("+")
        self.assertEqual(calc.visor, 37.0)
    
    def test_carry_operation_change_operator(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("+")
        calc.get_result()
        calc.store_value("-")
        calc.get_result()
        self.assertEqual(calc.visor, 0.0)

    def test_output_int(self):
        calc = CalculatorLogic()
        calc.input(16)
        calc.store_value("/")
        calc.input(2)
        calc.get_result()
        self.assertEqual(calc.visor, 8)
    
    def test_output_float(self):
        calc = CalculatorLogic()
        calc.input(5)
        calc.store_value("/")
        calc.input(2)
        calc.get_result()
        self.assertEqual(calc.visor, 2.5)

    def test_two_operations(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.visor, 15.0)

    def test_clear_all(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        calc.clear_all()
        calc.input(3)
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.get_result()
        self.assertEqual(calc.visor, 165.0)
    
    def test_clear_last(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.store_value("*")
        calc.input(5)
        calc.clear_last()
        calc.input(3)
        calc.get_result()
        self.assertEqual(calc.visor, 9)

    def test_negate(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.negate()
        self.assertEqual(calc.visor, -3)
    
    def test_negate_and_sum(self):
        calc = CalculatorLogic()
        calc.input(3)
        calc.negate()
        calc.store_value("+")
        calc.input(3)
        calc.get_result()
        self.assertEqual(calc.visor, 0)


if __name__ == '__main__':
    unittest.main()
    
    