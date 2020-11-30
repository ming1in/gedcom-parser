import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us32 import us32

class us32_test(unittest.TestCase):
    def test1(self):
        result = ['I4']
        self.assertEqual(result, us32("seeds/us32/test1.ged"))

    def test2(self):
        result = ['I2', 'I7', 'I5']
        self.assertEqual(result, us32("seeds/us32/test2.ged"))

if __name__ == '__main__':
    unittest.main()
