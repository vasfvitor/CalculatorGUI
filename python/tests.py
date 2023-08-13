import unittest
from main import *

class TestCalculatorFunctions(unittest.TestCase):

    def test_sequence(self):
        print("3 * 5")
        input(3)
        store_value("*")
        input(5)
        r = get_result(True)
        self.assertEqual(r, 15.0)
        

# Add other test cases if needed

if __name__ == '__main__':
    unittest.main()
    close_app()
    
    