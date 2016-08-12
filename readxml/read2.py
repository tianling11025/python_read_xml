#coding=utf-8
import os
import xml.etree.ElementTree as ET

fp = os.path.abspath("")+"/readxml"
fp1 = os.path.abspath("")+"/pages/work_page.xml"

tree = ET.parse(fp+"/test.xml")

pages = ET.parse(fp1)
#print tree1.getroot()



for element in tree.findall("object"):
    name = element.get("name")
    if name == u'机票模块⼊口':
        value = element.attrib
        print value['findby'],value['value']


"""""
for page in pages.findall("page"):
    name = page.get("pagename")
    if name == u'工作':
        #value = element.attrib
        #value = page.find("object").attrib
        # print  value['findby'],value['value']
        for object in page.findall("object"):
            name2 = object.get("name")
            if name2 == u'考勤':
                print name2
                value = object.attrib
                #value = page.find("object").attrib
                print value['findby'],value['value']
"""""




for page in pages.findall("page"):
    #第一次遍历,获取所有page页
    pagename = page.get("pagename")
    if pagename == u'工作':
        #获取所需页面
        for object in page.findall("object"):
            #第二次遍历,获取该页面下所有object对象
            name = object.get("name")
            if name == u'考勤':
                #获取所需元素
                value = object.attrib
                print value['findby'],value['value']#输出定位方式及值