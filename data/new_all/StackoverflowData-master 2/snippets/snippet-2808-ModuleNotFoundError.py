#Source: https://stackoverflow.com/questions/62489015/getting-attributeerror-nonetype-object-has-no-attribute-strip-while-reading
from lxml import etree
from collections import defaultdict

root_1 = etree.parse('a.xml').getroot()

d1 = []
for node in root_1.findall('.//human '):
    item = defaultdict(list)
    for x in node.iter():
        if x.attrib:
            item[x.attrib.keys()[0]].append(x.attrib.values()[0])
        if x.text.strip():
            item[x.tag].append(x.text.strip())
    d1.append(dict(item))



d1 = sorted(d1, key = lambda x: x['gender'])
print(d1)