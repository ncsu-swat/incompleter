# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import accumulate
    _l_(22106)

except ImportError:
    pass

def cumsum(lst):
    _l_(22113)

    aux = _c_(22111, _n_(22107, "list", lambda: list), _c_(22110, _n_(22108, "accumulate", lambda: accumulate), _n_(22109, "lst", lambda: lst)))
    _l_(22112)
    return aux
_c_(22115, _n_(22114, "print", lambda: print), 'Original list elements:')
_l_(22116)
_c_(22119, _n_(22117, "print", lambda: print), _n_(22118, "nums", lambda: nums))
_l_(22120)
_c_(22122, _n_(22121, "print", lambda: print), 'Cumulative sum of the elements of the said list:')
_l_(22123)
_c_(22128, _n_(22124, "print", lambda: print), _c_(22127, _n_(22125, "cumsum", lambda: cumsum), _n_(22126, "nums", lambda: nums)))
_l_(22129)
nums = [-1, -2, -3, 4]
_l_(22130)
_c_(22132, _n_(22131, "print", lambda: print), '\nOriginal list elements:')
_l_(22133)
_c_(22136, _n_(22134, "print", lambda: print), _n_(22135, "nums", lambda: nums))
_l_(22137)
_c_(22139, _n_(22138, "print", lambda: print), 'Cumulative sum of the elements of the said list:')
_l_(22140)
_c_(22145, _n_(22141, "print", lambda: print), _c_(22144, _n_(22142, "cumsum", lambda: cumsum), _n_(22143, "nums", lambda: nums)))
_l_(22146)