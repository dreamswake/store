import unittest
from Demo.calc import Calc
class TestCalc1(unittest.TestCase):
    def testIncre(self):
        c = Calc()
        a = 9
        b = 10
        s =-1
        sum = c.Incre(a,b)
        self.assertEqual(s,sum)

    def testIncre1(self):
        c = Calc()
        a = -9
        b = 10
        s =-19
        sum = c.Incre(a,b)
        self.assertEqual(s,sum)

    def testIncre2(self):
        c = Calc()
        a = -9
        b = -10
        s =1
        sum = c.Incre(a,b)
        self.assertEqual(s,sum)


    def testIncre3(self):
        c = Calc()
        a = 9
        b = -10
        s =19
        sum = c.Incre(a,b)
        self.assertEqual(s,sum)










