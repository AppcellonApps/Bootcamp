import unittest
from code.calculator import add

class Calc(unittest.TestCase):

    def test_add(self):
        sum = add(3, 1) 
        sum2 = add(45, 7)
        sum3 = add(106, 79)

        self.assertEquals(sum, 4)
        self.assertEqual(sum2, 52, msg='not correct sum')
        self.assertEqual(sum3, 185, msg='not correct sum')
    
    def test_is_correct_type(self):
        result = add('5', 7)
        result2 = add(5, '7')

        self.assertEqual(result, 'not a valid integer')
        self.assertEqual(result2, 'not a valid integer')

    def test_correct_return_type(self):
        result = add (9, 5)
        self.assertIsInstance(result, int)

if __name__ == '__main__':
    unittest.main()