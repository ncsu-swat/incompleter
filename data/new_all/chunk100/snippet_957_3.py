# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import islice
    _l_(96010)

except ImportError:
    pass

def split_list(lst, n):
    _l_(96028)

    lst = _c_(96013, _n_(96011, "iter", lambda: iter), _n_(96012, "lst", lambda: lst))
    _l_(96014)
    result = _c_(96022, _n_(96015, "iter", lambda: iter), lambda : _c_(96021, _n_(96016, "tuple", lambda: tuple), _c_(96020, _n_(96017, "islice", lambda: islice), _n_(96018, "lst", lambda: lst), _n_(96019, "n", lambda: n))), ())
    _l_(96023)
    aux = _c_(96026, _n_(96024, "list", lambda: list), _n_(96025, "result", lambda: result))
    _l_(96027)
    return aux
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
_l_(96029)
_c_(96031, _n_(96030, "print", lambda: print), 'Original list:')
_l_(96032)
_c_(96035, _n_(96033, "print", lambda: print), _n_(96034, "nums", lambda: nums))
_l_(96036)
_c_(96039, _n_(96037, "print", lambda: print), '\nSplit the said list into equal size', _n_(96038, "n", lambda: n))
_l_(96040)
_c_(96046, _n_(96041, "print", lambda: print), _c_(96045, _n_(96042, "split_list", lambda: split_list), _n_(96043, "nums", lambda: nums), _n_(96044, "n", lambda: n)))
_l_(96047)
n = 4
_l_(96048)
_c_(96051, _n_(96049, "print", lambda: print), '\nSplit the said list into equal size', _n_(96050, "n", lambda: n))
_l_(96052)
_c_(96058, _n_(96053, "print", lambda: print), _c_(96057, _n_(96054, "split_list", lambda: split_list), _n_(96055, "nums", lambda: nums), _n_(96056, "n", lambda: n)))
_l_(96059)
n = 5
_l_(96060)
_c_(96063, _n_(96061, "print", lambda: print), '\nSplit the said list into equal size', _n_(96062, "n", lambda: n))
_l_(96064)
_c_(96070, _n_(96065, "print", lambda: print), _c_(96069, _n_(96066, "split_list", lambda: split_list), _n_(96067, "nums", lambda: nums), _n_(96068, "n", lambda: n)))
_l_(96071)