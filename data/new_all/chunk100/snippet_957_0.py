# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import islice
    _l_(95832)

except ImportError:
    pass

def split_list(lst, n):
    _l_(95841)

    lst = _c_(95835, _n_(95833, "iter", lambda: iter), _n_(95834, "lst", lambda: lst))
    _l_(95836)
    aux = _c_(95839, _n_(95837, "list", lambda: list), _n_(95838, "result", lambda: result))
    _l_(95840)
    return aux
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
_l_(95842)
_c_(95844, _n_(95843, "print", lambda: print), 'Original list:')
_l_(95845)
_c_(95848, _n_(95846, "print", lambda: print), _n_(95847, "nums", lambda: nums))
_l_(95849)
n = 3
_l_(95850)
_c_(95853, _n_(95851, "print", lambda: print), '\nSplit the said list into equal size', _n_(95852, "n", lambda: n))
_l_(95854)
_c_(95860, _n_(95855, "print", lambda: print), _c_(95859, _n_(95856, "split_list", lambda: split_list), _n_(95857, "nums", lambda: nums), _n_(95858, "n", lambda: n)))
_l_(95861)
n = 4
_l_(95862)
_c_(95865, _n_(95863, "print", lambda: print), '\nSplit the said list into equal size', _n_(95864, "n", lambda: n))
_l_(95866)
_c_(95872, _n_(95867, "print", lambda: print), _c_(95871, _n_(95868, "split_list", lambda: split_list), _n_(95869, "nums", lambda: nums), _n_(95870, "n", lambda: n)))
_l_(95873)
n = 5
_l_(95874)
_c_(95877, _n_(95875, "print", lambda: print), '\nSplit the said list into equal size', _n_(95876, "n", lambda: n))
_l_(95878)
_c_(95884, _n_(95879, "print", lambda: print), _c_(95883, _n_(95880, "split_list", lambda: split_list), _n_(95881, "nums", lambda: nums), _n_(95882, "n", lambda: n)))
_l_(95885)