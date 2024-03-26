# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import accumulate
    _l_(108054)

except ImportError:
    pass

def cumsum(lst):
    _l_(108061)

    aux = _c_(108059, _n_(108055, "list", lambda: list), _c_(108058, _n_(108056, "accumulate", lambda: accumulate), _n_(108057, "lst", lambda: lst)))
    _l_(108060)
    return aux
_c_(108063, _n_(108062, "print", lambda: print), 'Original list elements:')
_l_(108064)
_c_(108067, _n_(108065, "print", lambda: print), _n_(108066, "nums", lambda: nums))
_l_(108068)
_c_(108070, _n_(108069, "print", lambda: print), 'Cumulative sum of the elements of the said list:')
_l_(108071)
_c_(108076, _n_(108072, "print", lambda: print), _c_(108075, _n_(108073, "cumsum", lambda: cumsum), _n_(108074, "nums", lambda: nums)))
_l_(108077)
nums = [-1, -2, -3, 4]
_l_(108078)
_c_(108080, _n_(108079, "print", lambda: print), '\nOriginal list elements:')
_l_(108081)
_c_(108084, _n_(108082, "print", lambda: print), _n_(108083, "nums", lambda: nums))
_l_(108085)
_c_(108087, _n_(108086, "print", lambda: print), 'Cumulative sum of the elements of the said list:')
_l_(108088)
_c_(108093, _n_(108089, "print", lambda: print), _c_(108092, _n_(108090, "cumsum", lambda: cumsum), _n_(108091, "nums", lambda: nums)))
_l_(108094)