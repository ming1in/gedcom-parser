# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:24:41 2020

@author: ptrda
"""

import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from us53 import us53


class us53_test(unittest.TestCase):
    def test1(self):
        result = [{'Diane Brown', 'Kevin Brown'}]
        self.assertEqual(result, us53("seeds/us53/test53-1.ged"))

    def test2(self):
        result = [{'Paul Smith', 'John Smith'}, {'Diane Brown', 'Susan Jones', 'Kevin Brown'}]
        self.assertEqual(result, us53("seeds/us53/test53-2.ged"))

    def test3(self):
        result = []
        self.assertEqual(result, us53("seeds/us53/test53-3.ged"))


if __name__ == '__main__':
    unittest.main()