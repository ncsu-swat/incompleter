# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
result = {}
_l_(119526)
for key, value in _c_(119529, _a_(119528, _n_(119527, "student_data", lambda: student_data), "items")):
    _l_(119539)

    if _n_(119530, "value", lambda: value) not in _c_(119533, _a_(119532, _n_(119531, "result", lambda: result), "values")):
        _l_(119538)

        _n_(119534, "result", lambda: result)[_n_(119535, "key", lambda: key)] = _n_(119536, "value", lambda: value)
        _l_(119537)
_c_(119542, _n_(119540, "print", lambda: print), _n_(119541, "result", lambda: result))
_l_(119543)