# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(str1):
    _l_(118190)

    result = [_c_(118180, _n_(118178, "int", lambda: int), _n_(118179, "str1", lambda: str1)) for str1 in _c_(118183, _a_(118182, _n_(118181, "str1", lambda: str1), "split")) if _c_(118186, _a_(118185, _n_(118184, "str1", lambda: str1), "isdigit"))]
    _l_(118187)
    aux = _n_(118188, "result", lambda: result)
    _l_(118189)
    return aux
_c_(118193, _n_(118191, "print", lambda: print), 'Original string:', _n_(118192, "str1", lambda: str1))
_l_(118194)
_c_(118196, _n_(118195, "print", lambda: print), 'Extract numbers from the said string:')
_l_(118197)
_c_(118202, _n_(118198, "print", lambda: print), _c_(118201, _n_(118199, "test", lambda: test), _n_(118200, "str1", lambda: str1)))
_l_(118203)