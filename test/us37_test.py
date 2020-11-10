import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us37 import us37

class us37_test(unittest.TestCase):
    def test1(self):
      result = ['Lucia Johnson', 'Michelle Jones', 'Lucia Johnson', 'Michelle Jones']
      self.assertEqual(result, us37("seeds/us37/test1.ged"))

    def test2(self):
      result = []
      self.assertEqual(result, us37("seeds/us37/test2.ged"))

    def test3(self):
      result = []
      self.assertEqual(result, us37("seeds/us37/test3.ged"))

    def test4(self):
       result = ['Maria Hamilton', 'Joseph Jones']
       self.assertEqual(result, us37("seeds/us37/test4.ged"))

    def test5(self):
       result = []
       self.assertEqual(result, us37("seeds/us37/test5.ged"))

if __name__ == '__main__':
    unittest.main()
