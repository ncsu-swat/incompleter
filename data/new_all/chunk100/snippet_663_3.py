# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_of_dicts(marks):
    _l_(68557)

    vals = _c_(68545, _n_(68541, "zip", lambda: zip), *[_n_(68542, "marks", lambda: marks)[_n_(68543, "k", lambda: k)] for k in _n_(68544, "keys", lambda: keys)])
    _l_(68546)
    result = [_c_(68552, _n_(68547, "dict", lambda: dict), _c_(68551, _n_(68548, "zip", lambda: zip), _n_(68549, "keys", lambda: keys), _n_(68550, "v", lambda: v))) for v in _n_(68553, "vals", lambda: vals)]
    _l_(68554)
    aux = _n_(68555, "result", lambda: result)
    _l_(68556)
    return aux
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
_l_(68558)
_c_(68560, _n_(68559, "print", lambda: print), 'Original dictionary of lists:')
_l_(68561)
_c_(68564, _n_(68562, "print", lambda: print), _n_(68563, "marks", lambda: marks))
_l_(68565)
_c_(68567, _n_(68566, "print", lambda: print), '\nSplit said dictionary of lists into list of dictionaries:')
_l_(68568)
_c_(68573, _n_(68569, "print", lambda: print), _c_(68572, _n_(68570, "list_of_dicts", lambda: list_of_dicts), _n_(68571, "marks", lambda: marks)))
_l_(68574)