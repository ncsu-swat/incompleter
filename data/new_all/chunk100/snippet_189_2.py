# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(15146)

    result = [_n_(15137, "x", lambda: x) + _n_(15138, "y", lambda: y) for (x, y) in _c_(15142, _n_(15139, "zip", lambda: zip), _n_(15140, "lst", lambda: lst)[::2], _n_(15141, "lst", lambda: lst)[1::2])]
    _l_(15143)
    aux = _n_(15144, "result", lambda: result)
    _l_(15145)
    return aux
nums = ['1', '2', '3', '4', '5', '6', '7', '8']
_l_(15147)
_c_(15149, _n_(15148, "print", lambda: print), 'Original list:')
_l_(15150)
_c_(15153, _n_(15151, "print", lambda: print), _n_(15152, "nums", lambda: nums))
_l_(15154)
_c_(15156, _n_(15155, "print", lambda: print), '\nJoin adjacent members of a given list:')
_l_(15157)
_c_(15162, _n_(15158, "print", lambda: print), _c_(15161, _n_(15159, "test", lambda: test), _n_(15160, "nums", lambda: nums)))
_l_(15163)
_c_(15165, _n_(15164, "print", lambda: print), '\nOriginal list:')
_l_(15166)
_c_(15169, _n_(15167, "print", lambda: print), _n_(15168, "nums", lambda: nums))
_l_(15170)
_c_(15172, _n_(15171, "print", lambda: print), '\nJoin adjacent members of a given list:')
_l_(15173)
_c_(15178, _n_(15174, "print", lambda: print), _c_(15177, _n_(15175, "test", lambda: test), _n_(15176, "nums", lambda: nums)))
_l_(15179)