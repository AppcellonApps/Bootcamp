import unittest
from code.numerals import roman_converter

class NumeralTests(unittest.TestCase):
    def test_I(self):
        roman_I = roman_converter(1)
        roman_II = roman_converter(2)

        self.assertEqual(roman_I, 'I') 
        self.assertEqual(roman_II, 'II') 

if __name__ == '__main__':
    unittest.main()