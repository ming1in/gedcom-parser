import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
import us49

'''
Author: Grace Miguel
Date: 11/27/20
I pledge my honor that I've abided by the Stevens Honor Code
'''

class us49_test(unittest.TestCase):
    def test1(self):
        filename = 'seeds/test011.ged'
        s = 'F2 Richard Jablowksi Monica Jablowski'
        self.assertEquals(s, us49.us49(filename))

    def test2(self):
        filename = 'seeds/test1.ged'
        s = 'F1 Sam Smith Alexa Smith'
        self.assertEquals(s, us49.us49(filename))

if __name__ == '__main__':
    unittest.main() 