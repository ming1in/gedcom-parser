from us25 import us25
import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))


class us25_test(unittest.TestCase):
    def test1(self):
        result = ['I15']
        self.assertEqual(result, us25("seeds/us25/test1.ged"))

    def test2(self):
        result = []
        self.assertEqual(result, us25("seeds/us25/test2.ged"))

    def test3(self):
        result = ['I15', 'I16']
        self.assertEqual(result, us25("seeds/us25/test3.ged"))

    def test4(self):
        result = ['I6']
        self.assertEqual(result, us25("seeds/us25/test4.ged"))

    def test5(self):
        result = ['I15', 'I16', 'I17']
        self.assertEqual(result, us25("seeds/us25/test5.ged"))


if __name__ == '__main__':
    unittest.main()
