import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us52 import us52
from Gedcom import Gedcom, Family

class us52_test(unittest.TestCase):
    def test1(self):
      result = ['Sam Smith', 'Alexa Smith', 'Rick Smith', 'Hannah Smith']
      self.assertEqual(result, us52("seeds/test1.ged"))

    def test2(self):
      result = ['Rick Smith', 'Hannah Smith Smith']
      self.assertEqual(result, us52("seeds/test11.ged"))

if __name__ == '__main__':
    unittest.main()