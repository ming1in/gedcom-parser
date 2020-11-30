import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us47 import us47

class us47_test(unittest.TestCase):
    def test1(self):
        result = ['I5', 'I7', 'I15']
        self.assertEqual(result, us47("seeds/us47/test1.ged"))

    def test2(self):
        result = []
        self.assertEqual(result, us47("seeds/us47/test2.ged"))

if __name__ == '__main__':
    unittest.main()
