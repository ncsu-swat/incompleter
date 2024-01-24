# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62489015/getting-attributeerror-nonetype-object-has-no-attribute-strip-while-reading
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from lxml import etree
    _l_(533964)

except ImportError:
    pass
try:
    from collections import defaultdict
    _l_(533966)

except ImportError:
    pass

root_1 = _c_(533971, _a_(533970, _c_(533969, _a_(533968, _n_(533967, "etree", lambda: etree), "parse"), 'a.xml'), "getroot"))
_l_(533972)

d1 = []
_l_(533973)
for node in _c_(533976, _a_(533975, _n_(533974, "root_1", lambda: root_1), "findall"), './/human '):
    _l_(534022)

    item = _c_(533979, _n_(533977, "defaultdict", lambda: defaultdict), _n_(533978, "list", lambda: list))
    _l_(533980)
    for x in _c_(533983, _a_(533982, _n_(533981, "node", lambda: node), "iter")):
        _l_(534014)

        if _a_(533985, _n_(533984, "x", lambda: x), "attrib"):
            _l_(533998)

            _c_(533996, _a_(533991, _n_(533986, "item", lambda: item)[_c_(533990, _a_(533989, _a_(533988, _n_(533987, "x", lambda: x), "attrib"), "keys"))[0]], "append"), _c_(533995, _a_(533994, _a_(533993, _n_(533992, "x", lambda: x), "attrib"), "values"))[0])
            _l_(533997)
        if _c_(534002, _a_(534001, _a_(534000, _n_(533999, "x", lambda: x), "text"), "strip")):
            _l_(534013)

            _c_(534011, _a_(534006, _n_(534003, "item", lambda: item)[_a_(534005, _n_(534004, "x", lambda: x), "tag")], "append"), _c_(534010, _a_(534009, _a_(534008, _n_(534007, "x", lambda: x), "text"), "strip")))
            _l_(534012)
    _c_(534020, _a_(534016, _n_(534015, "d1", lambda: d1), "append"), _c_(534019, _n_(534017, "dict", lambda: dict), _n_(534018, "item", lambda: item)))
    _l_(534021)



d1 = _c_(534026, _n_(534023, "sorted", lambda: sorted), _n_(534024, "d1", lambda: d1), key = lambda x: _n_(534025, "x", lambda: x)['gender'])
_l_(534027)
_c_(534030, _n_(534028, "print", lambda: print), _n_(534029, "d1", lambda: d1))
_l_(534031)