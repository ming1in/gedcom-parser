import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us24 import us24

class us24_test(unittest.TestCase):
    def test1(self):
      result = ['F6']
      self.assertEqual(result, us24("seeds/us24/test1.ged"))

    def test2(self):
      result = []
      self.assertEqual(result, us24("seeds/us24/test2.ged"))

    def test3(self):
      result = ['F7', 'F8']
      self.assertEqual(result, us24("seeds/us24/test3.ged"))

    def test4(self):
      result = []
      self.assertEqual(result, us24("seeds/us24/test4.ged"))

    def test5(self):
      result = []
      self.assertEqual(result, us24("seeds/us24/test5.ged"))

if __name__ == '__main__':
    unittest.main()
