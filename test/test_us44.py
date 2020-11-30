import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us44 import us44

class us44_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/us44/seed.ged" 
        ret = 'I11'
        self.assertEqual(us44(filename),ret)

    def test2(self):
        filename = "seeds/us44/test3.ged" 
        ret = 'I4'
        self.assertEqual(us44(filename),ret)


if __name__ == '__main__':
        unittest.main() 
