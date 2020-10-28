import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us36 import us36

class us36_test(unittest.TestCase):
    def test1(self):
      result = ['Lucia Johnson','Evan Smith']
      self.assertEqual(result, us36("seeds/us36/test1.ged"))

    def test2(self):
      result = []
      self.assertEqual(result, us36("seeds/us36/test2.ged"))

    def test3(self):
      result = ['Dylan Smith', 'Bernard Smith']
      self.assertEqual(result, us36("seeds/us36/test3.ged"))

    # def test4(self):
    #   result = []
    #   self.assertEqual(result, us36("seeds/us36/test4.ged"))

    # def test5(self):
    #   result = []
    #   self.assertEqual(result, us36("seeds/us36/test5.ged"))

if __name__ == '__main__':
    unittest.main()
