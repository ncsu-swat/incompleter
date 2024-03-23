# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import islice
    _l_(95947)

except ImportError:
    pass

def split_list(lst, n):
    _l_(95965)

    lst = _c_(95950, _n_(95948, "iter", lambda: iter), _n_(95949, "lst", lambda: lst))
    _l_(95951)
    result = _c_(95959, _n_(95952, "iter", lambda: iter), lambda : _c_(95958, _n_(95953, "tuple", lambda: tuple), _c_(95957, _n_(95954, "islice", lambda: islice), _n_(95955, "lst", lambda: lst), _n_(95956, "n", lambda: n))), ())
    _l_(95960)
    aux = _c_(95963, _n_(95961, "list", lambda: list), _n_(95962, "result", lambda: result))
    _l_(95964)
    return aux
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
_l_(95966)
_c_(95968, _n_(95967, "print", lambda: print), 'Original list:')
_l_(95969)
_c_(95972, _n_(95970, "print", lambda: print), _n_(95971, "nums", lambda: nums))
_l_(95973)
n = 3
_l_(95974)
_c_(95977, _n_(95975, "print", lambda: print), '\nSplit the said list into equal size', _n_(95976, "n", lambda: n))
_l_(95978)
_c_(95984, _n_(95979, "print", lambda: print), _c_(95983, _n_(95980, "split_list", lambda: split_list), _n_(95981, "nums", lambda: nums), _n_(95982, "n", lambda: n)))
_l_(95985)
n = 4
_l_(95986)
_c_(95989, _n_(95987, "print", lambda: print), '\nSplit the said list into equal size', _n_(95988, "n", lambda: n))
_l_(95990)
_c_(95996, _n_(95991, "print", lambda: print), _c_(95995, _n_(95992, "split_list", lambda: split_list), _n_(95993, "nums", lambda: nums), _n_(95994, "n", lambda: n)))
_l_(95997)
_c_(96000, _n_(95998, "print", lambda: print), '\nSplit the said list into equal size', _n_(95999, "n", lambda: n))
_l_(96001)
_c_(96007, _n_(96002, "print", lambda: print), _c_(96006, _n_(96003, "split_list", lambda: split_list), _n_(96004, "nums", lambda: nums), _n_(96005, "n", lambda: n)))
_l_(96008)