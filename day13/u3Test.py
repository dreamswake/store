import unittest
from Demo.calc import Calc
class TestCalc3(unittest.TestCase):
    def testDivide(self):
        c = Calc()
        a = 10
        b = 2
        s = 5
        sum = c.Divide(a,b)
        self.assertEqual(s,sum)

    def testDivide1(self):
        c = Calc()
        a = -10
        b = 2
        s = -5
        sum = c.Divide(a,b)
        self.assertEqual(s,sum)

    def testDivide2(self):
        c = Calc()
        a = 10
        b = -2
        s = -5
        sum = c.Divide(a,b)
        self.assertEqual(s,sum)

    def testDivide3(self):
        c = Calc()
        a = -10
        b = -2
        s = 5
        sum = c.Divide(a,b)
        self.assertEqual(s,sum)








