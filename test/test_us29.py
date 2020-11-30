import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us29 import us29

class us29_test(unittest.TestCase):
    def test1(self):
        result = ['I12']
        self.assertEqual(result, us29("seeds/us29/test1.ged"))

    def test2(self):
        result = ['I10', 'I11', 'I7', 'I8']
        self.assertEqual(result, us29("seeds/us29/test2.ged"))

    def test3(self):
        result = ['I4', 'I6']
        self.assertEqual(result, us29("seeds/us29/test3.ged"))

    def test4(self):
        result = ['I12', 'I14']
        self.assertEqual(result, us29("seeds/us29/test4.ged"))

    def test5(self):
        result = []
        self.assertEqual(result, us29("seeds/us29/test5.ged"))


if __name__ == '__main__':
    unittest.main()
