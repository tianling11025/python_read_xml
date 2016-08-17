#coding = utf-8
from appium import webdriver
import unittest,os
from time import sleep
class BaseTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone 6s'
        desired_caps['app'] = os.path.abspath('/Users/yixin/Desktop/YXOA.app')
        desired_caps['autoAcceptAlerts'] = 'true'
        desired_caps['language'] = 'zh-Hans'
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(20)
        #cls.driver.execute_script()


    @classmethod
    def tearDownClass(cls):
        sleep(10)
    	cls.driver.quit()