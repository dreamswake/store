'''
1.提供工具：unittest
1.1 继承unittest.TestCase
1.2 写测试方法：必须是testXxxx
1.3 unittest 自带断言
'''



import unittest
from Demo.calc import Calc
class TestCalc(unittest.TestCase):
    def testAdd(self):
        c = Calc()
        #测试数据
        a = 9
        b = 10
        s = 19   #期望结果
        sum = c.Add(9,10)   #实际结果
        self.assertEqual(s,sum)

    def testAdd1(self):
        c = Calc()
        a = 9
        b = -10
        s = -1
        sum = c.Add(a,b)
        self.assertEqual(s,sum)

    def testAdd2(self):
        c = Calc()
        a = -9
        b = 10
        s = 1
        sum = c.Add(a,b)
        self.assertEqual(s,sum)

    def testAdd3(self):
        c = Calc()
        a = -9
        b = -10
        s = -19
        sum = c.Add(a,b)
        self.assertEqual(s,sum)





















