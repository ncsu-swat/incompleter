# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(68660)

except ImportError:
    pass

def test(students):
    _l_(68675)

    for (key, value) in _c_(68663, _a_(68662, _n_(68661, "students", lambda: students), "items")):
        _l_(68670)

        _c_(68668, _a_(68666, _n_(68664, "obj", lambda: obj)[_n_(68665, "value", lambda: value)], "append"), _n_(68667, "key", lambda: key))
        _l_(68669)
    aux = _c_(68673, _n_(68671, "dict", lambda: dict), _n_(68672, "obj", lambda: obj))
    _l_(68674)
    return aux
students = {'Ora Mckinney': 8, 'Theodore Hollandl': 7, 'Mae Fleming': 7, 'Mathew Gilbert': 8, 'Ivan Little': 7}
_l_(68676)
_c_(68681, _n_(68677, "print", lambda: print), _c_(68680, _n_(68678, "test", lambda: test), _n_(68679, "students", lambda: students)))
_l_(68682)