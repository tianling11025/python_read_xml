# coding=utf-8
import os
import sys
import time
import unittest

from libs import HTMLTestRunner
from test_cases import login_system
from test_cases import newrequest

reload(sys)
sys.setdefaultencoding("utf-8")

result_path= os.path.abspath("..")+"/test_result/"

# 获取当前时间
def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(login_system.LoginSystem))
    suite.addTest(unittest.makeSuite(newrequest.NewRequest))


    filename = result_path +' '+ ' '+ getNowTime()+ ' '+'MyReport.html'

    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title=u'移动OA测试报告',
    description=u'OA申请及考勤部分测试')

    runner.run(suite)




if __name__=='__main__':
    suite()