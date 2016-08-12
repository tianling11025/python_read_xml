#coding=utf-8
import os
import xml.etree.ElementTree as ET
import appium.webdriver.common.mobileby as By

filepath = os.path.abspath("")+"/pages/work_page.xml"

class BasePage(object):

    def __init__(self,driver):
        """构造函数"""
        self._driver = driver

    def read_element(self):
        tree = ET.parse(filepath)
        for element in tree.findall("page"):
            name = element.get("name")
            if name == u"工作":
                value = element.attrib
                print value['value']

    def find_element(self):
        pass


if __name__ == "__main__":
    BasePage.read_element()

