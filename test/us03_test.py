import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
os.chdir(os.path.abspath('../test/seeds'))
import us03

class Us03_test(unittest.TestCase):
    #one death is incorrect
    def test1(self):
        s = "The following have deaths before birth which is incorrect: ANGEL Florene "
        self.assertEquals(s, us03.user03("test8.ged"))

    #no deaths before births
    def test2(self):
        s = ""
        self.assertEquals(s, us03.user03("test7.ged"))
    #2 deaths before births
    def test3(self):
        s = "The following have deaths before birth which is incorrect: ANGEL Florene RAYMOND MIGUEL "
        self.assertEquals(s, us03.user03("test9.ged"))
    
    #no deaths before births
    def test4(self):
        s = ""
        self.assertEquals(s, us03.user03("test10.ged"))
    
    #no deaths before births
    def test5(self):
        s = ""
        self.assertEquals(s, us03.user03("test6.ged"))

if __name__ == '__main__':
    unittest.main()
