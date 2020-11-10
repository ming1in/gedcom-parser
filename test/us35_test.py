import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us35 import us35


class us35_test(unittest.TestCase):
    def test1(self):
        result = []
        self.assertEqual(result, us35("seeds/us35/test1.ged"))

    def test2(self):
        result = ['I12']
        self.assertEqual(result, us35("seeds/us35/test2.ged"))

    #def test3(self):
    #    result = ['I4']
    #    self.assertEqual(result, us35("seeds/us35/test3.ged"))

    def test4(self):
        result = ['I12', 'I3']
        self.assertEqual(result, us35("seeds/us35/test4.ged"))

    def test5(self):
        result = ['I12', 'I3', 'I4']
        self.assertEqual(result, us35("seeds/us35/test5.ged"))


if __name__ == '__main__':
    unittest.main()
