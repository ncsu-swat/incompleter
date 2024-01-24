# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48802655/xml-etree-elementtree-parse-attributeerror-list-object-has-no-attribute-ge
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.etree.ElementTree as ET
    _l_(529733)

except ImportError:
    pass

tree = _c_(529736, _a_(529735, _n_(529734, "ET", lambda: ET), "parse"), 'sample.xml')   
_l_(529737)   
root = _c_(529740, _a_(529739, _n_(529738, "tree", lambda: tree), "getroot"))
_l_(529741)

for elem in _n_(529742, "root", lambda: root):
    _l_(529751)


    _c_(529749, _n_(529743, "print", lambda: print), _c_(529748, _a_(529747, _c_(529746, _a_(529745, _n_(529744, "elem", lambda: elem), "findall"), 'alarmTime'), "get"), 'id'))
    _l_(529750)