# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def relative_order(lst):
    _l_(114047)

    result = [_n_(114036, "i", lambda: i) for i in _c_(114041, _n_(114037, "range", lambda: range), _c_(114040, _n_(114038, "len", lambda: len), _n_(114039, "lst", lambda: lst))) if _n_(114042, "lst", lambda: lst)[_n_(114043, "i", lambda: i)] == None]
    _l_(114044)
    aux = _n_(114045, "result", lambda: result)
    _l_(114046)
    return aux
_c_(114049, _n_(114048, "print", lambda: print), 'Original list:')
_l_(114050)
_c_(114053, _n_(114051, "print", lambda: print), _n_(114052, "nums", lambda: nums))
_l_(114054)
_c_(114056, _n_(114055, "print", lambda: print), '\nIndexes of all None items of the list:')
_l_(114057)
_c_(114062, _n_(114058, "print", lambda: print), _c_(114061, _n_(114059, "relative_order", lambda: relative_order), _n_(114060, "nums", lambda: nums)))
_l_(114063)