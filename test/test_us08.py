import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us08 import us08

class us08_test(unittest.TestCase):
    def test1(self):
      result = []
      self.assertEqual(result, us08("seeds/us08/test1.ged"))

    def test2(self):
      result = ['I4']
      self.assertEqual(result, us08("seeds/us08/test2.ged"))

    def test3(self):
      result = ['I6']
      self.assertEqual(result, us08("seeds/us08/test3.ged"))

    def test4(self):
      result = ['I6', 'I3']
      self.assertEqual(result, us08("seeds/us08/test4.ged"))

    def test5(self):
      result = ['I1', 'I4']
      self.assertEqual(result, us08("seeds/us08/test5.ged"))

if __name__ == '__main__':
    unittest.main()
