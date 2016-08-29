# coding=utf-8
import os
from test_cases import base_test_case
from utils import base_page
from time import sleep
shotpath = os.path.abspath("..")+"/screenshots/"

class NewRequest(base_test_case.BaseTestCase,base_page.BasePage):

    def setUp(self):
        pass

    def newRequest(self,type):
        """请假流程"""
        request = self.read_element(u'工作页',u'申请')
        leave = self.read_element(u'申请页',u'请假申请')
        leavetype = self.read_element(u'请假申请页',u'请假类型')
        #sick = self.read_element(u'请假申请页',u'病假')
        paper = self.read_element(u'请假申请页',u'单据')
        time_widget1 = self.read_element(u'请假申请页',u'时间控件1')
        time_widget2 = self.read_element(u'请假申请页',u'时间控件2')
        submit_btn = self.read_element(u'请假申请页',u'提交')
        confirm1 = self.read_element(u'请假申请页',u'确定')
        confirm2 = self.read_element(u'请假申请页',u'确定1')

        self.click_element(request)
        self.get_screenshot(shotpath,"申请页")
        self.click_element(leave)
        self.get_screenshot(shotpath,"请假申请")
        self.click_element(leavetype)
        self.get_screenshot(shotpath,"展开请假类型")
        self.click_element(type)
        self.click_element(paper)
        self.get_screenshot(shotpath,"勾选单据")
        self.click_element(time_widget1)
        #self.click_element(confirm1)
        self.handle_timewidget()
        self.click_element(time_widget2)
        #self.click_element(confirm2)
        self.handle_timewidget()
        self.click_element(submit_btn)
        sleep(2)
        self.get_screenshot(shotpath,"提交完成")
        self.cancel_request()
        self.get_screenshot(shotpath,"撤销申请")
        self.back_home()
    def handle_timewidget(self):
        """针对时间控件的处理方式"""
        #获取所有id为确定的按钮,遍历按钮,找出显示在最上层的,点击;
        button = self.driver.find_elements_by_accessibility_id("确定")
        for clickable_btn in button:
            if clickable_btn.is_displayed():
                clickable_btn.click()

    def cancel_request(self):
        """取消请假申请"""
        detail = self.get_element(u'请假申请页',u'详情')
        cancel = self.get_element(u'请假申请页',u'撤销')
        self.click_element(detail)
        self.click_element(cancel)

    def test_1_login(self):
        """登录OA"""
        username = self.read_element(u'登录页',u'用户名')
        password = self.read_element(u'登录页',u'密码')
        login_btn = self.read_element(u'登录页', u'登录')

        self.enter_element(username,'liuhl')
        self.enter_element(password,'1qaz2wsx@')
        self.click_element(login_btn)
        self.get_screenshot(shotpath,"登录结果")
        self.handle_alert()

    def test_2(self):
        """病假"""
        reqtype = self.read_element(u'请假申请页', u'病假')
        self.newRequest(reqtype)

    def test_3(self):
        """婚假"""
        reqtype = self.read_element(u'请假申请页', u'婚假')
        self.newRequest(reqtype)





