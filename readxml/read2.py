#coding=utf-8
import os
import xml.etree.ElementTree as ET

fp = os.path.abspath("")+"/readxml"
fp1 = os.path.abspath("")+"/pages/work_page.xml"

tree = ET.parse(fp+"/test.xml")

tree1 = ET.parse(fp1)
#print tree1.getroot()



for element in tree.findall("object"):
    name = element.get("name")
    if name == u'机票模块⼊口':
        value = element.attrib
        print value['findby'],value['value']



for page in tree1.findall("page"):
    name = page.get("pagename")

    if name == u'工作':
        #value = element.attrib
        value = page.find("object").attrib
        print  value['findby'],value['value']
