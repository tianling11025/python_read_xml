#coding=utf-8
import os
import xml.etree.ElementTree as ET
from time import sleep
pagepath = os.path.abspath("..")+"/pages/work_page.xml"


class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def read_element(self,page_name,object_name):
        """从xml中得到页面及该页面下元素"""
        pages = ET.parse(pagepath)
        for page in pages.findall("page"):
            # 第一次遍历,获取所有page页
            pagename = page.get("pagename")
            if pagename == page_name:
                # 获取所需页面
                for object in page.findall("object"):
                    # 第二次遍历,获取该页面下所有object对象
                    name = object.get("name")
                    if name == object_name:
                        # 获取所需元素
                        value = object.attrib
                        #print value['findby'], value['value']  # 输出定位方式及值
                        return value['findby'], value['value']

    def get_element(self,*locator):
        return self.driver.find_element(*locator)

    def click_element(self,locator):
        self.get_element(*locator).click()


    def enter_element(self,locator,text):
        self.get_element(*locator).send_keys(text)

    def get_screenshot(self,path,name):
        sleep(2)
        self.driver.get_screenshot_as_file(path+name+".png")

    def back_home(self):
        """"返回主页操作"""
        try:
            back_btn = self.driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")
            back_btn1 = self.driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]")
        except:
            pass
        else:
            if back_btn.is_enabled():
                back_btn.click()
                sleep(3)
                self.back_home()
            elif back_btn1.is_enabled():
                back_btn1.click()
                sleep(3)
                self.back_home()
