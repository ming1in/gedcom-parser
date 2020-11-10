'''
Author: Grace Miguel
I pledge my honor that I've abided by the Stevens Honor Code. 
'''
import sys
import os 
import unittest
sys.path.append(os.path.abspath('src'))
#os.chdir(os.path.abspath('src'))
import us11
class us11_test(unittest.TestCase):
    def test1(self):
        x = "There is a polyamorous relationship"
        self.assertEqual(x,us11.us11('test011.ged'))
    
    def test2(self):
        x= None 
        self.assertEqual(x, us11.us11("test1.ged"))

if __name__ == '__main__':
    unittest.main()

