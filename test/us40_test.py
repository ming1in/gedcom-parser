'''
Author: Grace Miguel
I pledge my honor that I've abided by the Stevens Honor Code.
'''
import unittest
import sys
import os 
sys.path.append(os.path.abspath('src'))
import us40

class us40_test(unittest.TestCase):
    def test1(self):
        x ="0 = 0 HEAD"
        self.assertEqual(x,us40.us40('test1.ged'))
    

if __name__ == '__main__':
    unittest.main()

