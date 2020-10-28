import unittest
import os
import sys
sys.path.append(os.path.abspath('../src'))
import us06





class us06_test(unittest.TestCase):
    def test1(self):
        filename = "us06/test1.ged"
        s = "The following people have divorces after their death date['DANIEL SOLLER']"
        self.assertEqual(s, us06.us06(filename))
    
    def test2(self):
        filename = "us06/test2.ged"
        s = None
        self.assertEqual(s, us06.us06(filename))


if __name__ == '__main__':
    unittest.main()