# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_val(list_val):
    _l_(80345)

    max_val = _c_(80341, _n_(80334, "max", lambda: max), _n_(80335, "list_val", lambda: list_val), key=lambda i: (_c_(80339, _n_(80336, "isinstance", lambda: isinstance), _n_(80337, "i", lambda: i), _n_(80338, "int", lambda: int)), _n_(80340, "i", lambda: i)))
    _l_(80342)
    aux = _n_(80343, "max_val", lambda: max_val)
    _l_(80344)
    return aux
_c_(80347, _n_(80346, "print", lambda: print), 'Original list:')
_l_(80348)
_c_(80351, _n_(80349, "print", lambda: print), _n_(80350, "list_val", lambda: list_val))
_l_(80352)
_c_(80354, _n_(80353, "print", lambda: print), '\nMaximum values in the said list using lambda:')
_l_(80355)
_c_(80360, _n_(80356, "print", lambda: print), _c_(80359, _n_(80357, "max_val", lambda: max_val), _n_(80358, "list_val", lambda: list_val)))
_l_(80361)