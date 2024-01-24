#Source: https://stackoverflow.com/questions/55459743/typeerror-cannot-parse-from-list
import os 
from lxml import etree
path = 'C:/Users/xxx/Desktop/python/python-parsing/data'
filename = os.listdir(path)
tree = etree.parse(filename)
test = tree.xpath('///p[@name="bName"]')
print ("".join(test))