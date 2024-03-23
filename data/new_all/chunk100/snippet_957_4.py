# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import islice
    _l_(96073)

except ImportError:
    pass

def split_list(lst, n):
    _l_(96091)

    lst = _c_(96076, _n_(96074, "iter", lambda: iter), _n_(96075, "lst", lambda: lst))
    _l_(96077)
    result = _c_(96085, _n_(96078, "iter", lambda: iter), lambda : _c_(96084, _n_(96079, "tuple", lambda: tuple), _c_(96083, _n_(96080, "islice", lambda: islice), _n_(96081, "lst", lambda: lst), _n_(96082, "n", lambda: n))), ())
    _l_(96086)
    aux = _c_(96089, _n_(96087, "list", lambda: list), _n_(96088, "result", lambda: result))
    _l_(96090)
    return aux
_c_(96093, _n_(96092, "print", lambda: print), 'Original list:')
_l_(96094)
_c_(96097, _n_(96095, "print", lambda: print), _n_(96096, "nums", lambda: nums))
_l_(96098)
n = 3
_l_(96099)
_c_(96102, _n_(96100, "print", lambda: print), '\nSplit the said list into equal size', _n_(96101, "n", lambda: n))
_l_(96103)
_c_(96109, _n_(96104, "print", lambda: print), _c_(96108, _n_(96105, "split_list", lambda: split_list), _n_(96106, "nums", lambda: nums), _n_(96107, "n", lambda: n)))
_l_(96110)
n = 4
_l_(96111)
_c_(96114, _n_(96112, "print", lambda: print), '\nSplit the said list into equal size', _n_(96113, "n", lambda: n))
_l_(96115)
_c_(96121, _n_(96116, "print", lambda: print), _c_(96120, _n_(96117, "split_list", lambda: split_list), _n_(96118, "nums", lambda: nums), _n_(96119, "n", lambda: n)))
_l_(96122)
n = 5
_l_(96123)
_c_(96126, _n_(96124, "print", lambda: print), '\nSplit the said list into equal size', _n_(96125, "n", lambda: n))
_l_(96127)
_c_(96133, _n_(96128, "print", lambda: print), _c_(96132, _n_(96129, "split_list", lambda: split_list), _n_(96130, "nums", lambda: nums), _n_(96131, "n", lambda: n)))
_l_(96134)