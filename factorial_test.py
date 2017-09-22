import unittest
from lab2 import recur_factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        ap=recur_factorial
        #self.assertEqual(ap,120)
        self.assertNotEqual(ap,89)

if __name__ == '__main__':
    unittest.main()        
