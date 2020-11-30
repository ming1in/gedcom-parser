'''
Author: Grace Miguel
Date: 11/28/20
I pledge my honor that I've abided by the Stevens Honor Code
'''

import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
import us50

class us50_test(unittest.TestCase):
    def test1(self):
        filename = "seeds/test011.ged"
        s = ["F3 Richard Jablowksi Brittany Hinker"]
        self.assertEqual(s, us50.us50(filename))

if __name__ == '__main__':
    unittest.main()