# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_integer(list1):
    _l_(50549)

    result = _c_(50545, _n_(50541, "len", lambda: len), [_n_(50542, "e", lambda: e) for e in _n_(50543, "ert", lambda: ert) if _n_(50544, "e", lambda: e)])
    _l_(50546)
    aux = _n_(50547, "result", lambda: result)
    _l_(50548)
    return aux
list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
_l_(50550)
_c_(50552, _n_(50551, "print", lambda: print), 'Original list:')
_l_(50553)
_c_(50556, _n_(50554, "print", lambda: print), _n_(50555, "list1", lambda: list1))
_l_(50557)
_c_(50559, _n_(50558, "print", lambda: print), '\nNumber of floats in the said mixed list:')
_l_(50560)
_c_(50565, _n_(50561, "print", lambda: print), _c_(50564, _n_(50562, "count_integer", lambda: count_integer), _n_(50563, "list1", lambda: list1)))
_l_(50566)