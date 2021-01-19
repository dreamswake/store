'''
    测试集：
        能动态将测试集进行组合一起执行用例。
'''
# 通过unittest来创建测试集

import unittest
from Demo.uTest import TestCalc
from HTMLTestRunner import HTMLTestRunner
import os
suite = unittest.TestSuite()  #获取 一个测试集
# suite.addTest(TestCalc("testAdd"))   #添加一个测试用例
# 使用测试加载器: 使用默认加载器，去寻找（"用例所在路径","测试用例名称的规则"）   os.getcwd()获取当前文件的所在绝对路径
tests = unittest.defaultTestLoader.discover(os.getcwd(),"*test.py")
suite.addTest(tests)


#创建一个文本运行器：产生得结果会以文本方式展示
# runner = unittest.TextTestRunner()
#使用html运行期：生成以html报告结果
f = open("计算器得测试报告.html","w+",encoding="utf-8") #准备一个报告文件
runner = HTMLTestRunner.HTMLTestRunner(#使用html运行器写入到报告里
    stream = f,#将报告写到那个文件流
    verbosity = 1,#报告得详细程度
    title = "计算器得测试报告"
)
#使用运行器来运行测试集
runner.run(suite)











