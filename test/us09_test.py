import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us09 import us09


class us09_test(unittest.TestCase):
    def test1(self):
      result = ['I13']
      self.assertEqual(result, us09("seeds/us09/test1.ged"))

    # def test2(self):
    #   result = ['I2']
    #   self.assertEqual(result, us09("seeds/us09/test2.ged"))

    # def test3(self):
    #     result = ['I6']
    #     self.assertEqual(result, us09("seeds/us09/test3.ged"))


if __name__ == '__main__':
    unittest.main()
