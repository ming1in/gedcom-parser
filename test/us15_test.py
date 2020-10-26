import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us15 import us15

class us15_test(unittest.TestCase):
    def test1(self):
      self.assertEqual([], us15("seeds/test1.ged"))

    def test2(self):
      self.assertEqual([], us15("seeds/test2.ged"))

    def test3(self):
      self.assertEqual([], us15("seeds/test3.ged"))

    def test4(self):
      self.assertEqual([], us15("seeds/test5.ged"))

    def test5(self):
      self.assertEqual([], us15("seeds/test6.ged"))

if __name__ == '__main__':
    unittest.main()