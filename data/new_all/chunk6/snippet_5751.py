# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55459743/typeerror-cannot-parse-from-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(345350)

except ImportError:
    pass
try:
    from lxml import etree
    _l_(345352)

except ImportError:
    pass
path = 'C:/Users/xxx/Desktop/python/python-parsing/data'
_l_(345353)
filename = _c_(345357, _a_(345355, _n_(345354, "os", lambda: os), "listdir"), _n_(345356, "path", lambda: path))
_l_(345358)
tree = _c_(345362, _a_(345360, _n_(345359, "etree", lambda: etree), "parse"), _n_(345361, "filename", lambda: filename))
_l_(345363)
test = _c_(345366, _a_(345365, _n_(345364, "tree", lambda: tree), "xpath"), '///p[@name="bName"]')
_l_(345367)
_c_(345372, _n_(345368, "print", lambda: print), _c_(345371, _a_(345369, "", "join"), _n_(345370, "test", lambda: test)))
_l_(345373)