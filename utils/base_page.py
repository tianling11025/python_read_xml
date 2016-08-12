#coding=utf-8
import os
import xml.etree.ElementTree as ET
import appium.webdriver.common.mobileby as By

filepath = os.path.abspath("..")+"/pages/work_page.xml"

class BasePage(object):

    def read_element(self,page_name,object_name):

        pages = ET.parse(filepath)
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
                        print value['findby'], value['value']  # 输出定位方式及值


    def find_element(self,findby,value):


        pass


if __name__ == "__main__":
    test = BasePage()
    test.read_element(u'工作',u'考勤')
