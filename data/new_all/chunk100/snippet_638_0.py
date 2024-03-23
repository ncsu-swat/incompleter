# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(dictt):
    _l_(66032)

    min_value = 1
    _l_(66020)
    result = [_n_(66021, "k", lambda: k) for (k, v) in _c_(66024, _a_(66023, _n_(66022, "dictt", lambda: dictt), "items")) if _c_(66027, _n_(66025, "len", lambda: len), _n_(66026, "v", lambda: v)) == _n_(66028, "min_value", lambda: min_value)]
    _l_(66029)
    aux = _n_(66030, "result", lambda: result)
    _l_(66031)
    return aux
_c_(66034, _n_(66033, "print", lambda: print), '\nOriginal Dictionary:')
_l_(66035)
_c_(66038, _n_(66036, "print", lambda: print), _n_(66037, "dictt", lambda: dictt))
_l_(66039)
_c_(66041, _n_(66040, "print", lambda: print), '\nShortest list of values with the keys of the said dictionary:')
_l_(66042)
_c_(66047, _n_(66043, "print", lambda: print), _c_(66046, _n_(66044, "test", lambda: test), _n_(66045, "dictt", lambda: dictt)))
_l_(66048)