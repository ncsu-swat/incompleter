# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58418821/xml-parsing-error-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.etree.ElementTree as ET
    _l_(406571)

except ImportError:
    pass

root = _c_(406575, _a_(406573, _n_(406572, "ET", lambda: ET), "fromstring"), _n_(406574, "my_xml_file", lambda: my_xml_file))
_l_(406576)

u = _c_(406582, _a_(406581, _a_(406580, _c_(406579, _a_(406578, _n_(406577, "root", lambda: root), "find"), ".//name"), "text"), "rstrip"))
_l_(406583)
_c_(406586, _n_(406584, "print", lambda: print), "Name: %s\n" % _n_(406585, "u", lambda: u))
_l_(406587)