# coding=utf-8
import os
from test_cases import base_test_case
from utils import base_page

shotpath = os.path.abspath("..")+"/screenshots/"

class LoginSystem(base_test_case.BaseTestCase,base_page.BasePage):

    def test_1_login(self):
        """登录OA"""
        username = self.read_element(u'登录页',u'用户名')
        password = self.read_element(u'登录页',u'密码')
        login_btn = self.read_element(u'登录页', u'登录')

        self.enter_element(username,'liuhl')
        self.enter_element(password,'1qaz2wsx!')
        self.click_element(login_btn)
        self.get_screenshot(shotpath,"登录结果")

    def test_2_getPage(self):
        """打开考勤"""
        attendance = self.read_element(u'工作页',u'考勤')
        self.click_element(attendance)
        self.get_screenshot(shotpath,"考勤页")
