import xml.dom.minidom as md
import os
fp = os.path.abspath("")

domtree = md.parse(fp+'/test.xml')
