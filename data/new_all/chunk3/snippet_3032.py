# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52841747/create-dictionary-from-mysql-attributeerror-tuple-object-has-no-attribute-na
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cursor = _c_(566507, _a_(566506, _n_(566505, "conn", lambda: conn), "cursor"))
_l_(566508)

_c_(566511, _a_(566510, _n_(566509, "cursor", lambda: cursor), "execute"), "select server_id, name from servers")
_l_(566512)

dict = {}
_l_(566513)
for row in _n_(566514, "cursor", lambda: cursor):
    _l_(566525)

    _n_(566515, "dict", lambda: dict)[_a_(566517, _n_(566516, "row", lambda: row), "server_id")] = _a_(566519, _n_(566518, "row", lambda: row), "name")
    _l_(566520)

    _c_(566523, _n_(566521, "print", lambda: print), _n_(566522, "dict", lambda: dict))
    _l_(566524)