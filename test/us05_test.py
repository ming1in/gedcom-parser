import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
os.chdir(os.path.abspath('../test/seeds'))

class us05_test(unittest.testCase):
    def test1(self): 
        s = ""
        self.assertEquals(s, us05.user05('test7.ged'))
    def test2(self): #3 couples have false marriage dates
        s = "The following people have marriage dates after death date: ['ANGEL Florene', 'EDITH JIMENEZ', 'ANGEL Florene', 'MERCEDES FUENTES', 'RAYMOND MIGUEL', 'JULIA HERMINEZ']"
        self.assertEquals(s, us05.user05('test16.ged'))
    def test3(self):  #2 couples have false marriage dates
        s = "The following people have marriage dates after death date: ['ANGEL Florene', 'EDITH JIMENEZ', 'RAYMOND MIGUEL', 'JULIA HERMINEZ']"
        self.assertEquals(s, us05.user05('test15.ged'))
    def test4(self):
        s = ""
        self.assertEquals(s, us05.user05('test13.ged'))
    def test5(self):
        s = 


