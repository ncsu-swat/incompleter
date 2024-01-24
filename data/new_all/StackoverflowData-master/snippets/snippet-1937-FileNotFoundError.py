#Source: https://stackoverflow.com/questions/13186772/attributeerror-while-parsing-xml
import xml.etree.ElementTree as etree

infile = r'C:\temp\test.xml'

authors = []
tree = etree.parse(infile)
root = tree.getroot()
for elem in tree.iter(tag='Author'):
    sn = elem.find('LastName').text
    fn = elem.find('Initials').text
    authors.append(fn + ' ' + sn)
for x in authors:
    print (x)