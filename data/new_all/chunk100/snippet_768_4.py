# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def shift_first_last(lst):
    _l_(78101)

    x = _c_(78080, _a_(78079, _n_(78078, "lst", lambda: lst), "pop"), 0)
    _l_(78081)
    y = _c_(78084, _a_(78083, _n_(78082, "lst", lambda: lst), "pop"))
    _l_(78085)
    _c_(78089, _a_(78087, _n_(78086, "lst", lambda: lst), "insert"), 0, _n_(78088, "y", lambda: y))
    _l_(78090)
    _c_(78097, _a_(78092, _n_(78091, "lst", lambda: lst), "insert"), _c_(78095, _n_(78093, "len", lambda: len), _n_(78094, "lst", lambda: lst)), _n_(78096, "x", lambda: x))
    _l_(78098)
    aux = _n_(78099, "lst", lambda: lst)
    _l_(78100)
    return aux
_c_(78103, _n_(78102, "print", lambda: print), 'Original list:')
_l_(78104)
_c_(78107, _n_(78105, "print", lambda: print), _n_(78106, "nums", lambda: nums))
_l_(78108)
_c_(78110, _n_(78109, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(78111)
_c_(78116, _n_(78112, "print", lambda: print), _c_(78115, _n_(78113, "shift_first_last", lambda: shift_first_last), _n_(78114, "nums", lambda: nums)))
_l_(78117)
chars = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
_l_(78118)
_c_(78120, _n_(78119, "print", lambda: print), '\nOriginal list:')
_l_(78121)
_c_(78124, _n_(78122, "print", lambda: print), _n_(78123, "chars", lambda: chars))
_l_(78125)
_c_(78127, _n_(78126, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(78128)
_c_(78133, _n_(78129, "print", lambda: print), _c_(78132, _n_(78130, "shift_first_last", lambda: shift_first_last), _n_(78131, "chars", lambda: chars)))
_l_(78134)