# coding=utf-8
import os
import time
import unittest

from test_cases import login_system
from test_suites import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

result_path= os.path.abspath("..")+"/test_result/"

# 获取当前时间
def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(login_system.LoginSystem))

    filename = result_path +' '+ ' '+ getNowTime()+ ' '+'MyReport.html'

    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title='testresult')

    runner.run(suite)




if __name__=='__main__':
    suite()