#coding=utf-8
import xml.etree.ElementTree as ET
import os

def readxml():

    fp = os.path.abspath("")
    print fp

    tree = ET.parse(fp+"/students.xml")

    root = tree.getroot()
    print root[1][3].tag
    print root[1][3].attrib
    print root[1][3].text


    for student in root:
        print student.tag,student.attrib

    for student in root.findall("student"):
        no = student.get("no")
        name = student.find("name").text
        print no,name



if __name__ =="__main__":
    readxml()