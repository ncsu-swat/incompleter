# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/13186772/attributeerror-while-parsing-xml
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.etree.ElementTree as etree
    _l_(435988)

except ImportError:
    pass

infile = r'C:\temp\test.xml'
_l_(435989)

authors = []
_l_(435990)
tree = _c_(435994, _a_(435992, _n_(435991, "etree", lambda: etree), "parse"), _n_(435993, "infile", lambda: infile))
_l_(435995)
root = _c_(435998, _a_(435997, _n_(435996, "tree", lambda: tree), "getroot"))
_l_(435999)
for elem in _c_(436002, _a_(436001, _n_(436000, "tree", lambda: tree), "iter"), tag='Author'):
    _l_(436019)

    sn = _a_(436006, _c_(436005, _a_(436004, _n_(436003, "elem", lambda: elem), "find"), 'LastName'), "text")
    _l_(436007)
    fn = _a_(436011, _c_(436010, _a_(436009, _n_(436008, "elem", lambda: elem), "find"), 'Initials'), "text")
    _l_(436012)
    _c_(436017, _a_(436014, _n_(436013, "authors", lambda: authors), "append"), _n_(436015, "fn", lambda: fn) + ' ' + _n_(436016, "sn", lambda: sn))
    _l_(436018)
for x in _n_(436020, "authors", lambda: authors):
    _l_(436025)

    _c_(436023, _n_(436021, "print", lambda: print), _n_(436022, "x", lambda: x))
    _l_(436024)