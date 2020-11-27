import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us19 import us19

class us14_test(unittest.TestCase):
    def test1(self):
      result = []
      self.assertEqual(result, us19("seeds/test1.ged"))

    def test2(self):
      result = []
      self.assertEqual(result, us19("seeds/test2.ged"))

    def test3(self):
      result = []
      self.assertEqual(result, us19("seeds/test3.ged"))

    def test4(self):
      result = []
      self.assertEqual(result, us19("seeds/test5.ged"))

    def test5(self):
      result = []
      self.assertEqual(result, us19("seeds/test6.ged"))

if __name__ == '__main__':
    unittest.main()