# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_even_odd(nums):
    _l_(85904)

    first_even = _c_(85893, _n_(85889, "next", lambda: next), (_n_(85890, "el", lambda: el) for el in _n_(85891, "nums", lambda: nums) if _n_(85892, "el", lambda: el) % 2 == 0), -1)
    _l_(85894)
    first_odd = _c_(85899, _n_(85895, "next", lambda: next), (_n_(85896, "el", lambda: el) for el in _n_(85897, "nums", lambda: nums) if _n_(85898, "el", lambda: el) % 2 != 0), -1)
    _l_(85900)
    aux = (_n_(85901, "first_even", lambda: first_even), _n_(85902, "first_odd", lambda: first_odd))
    _l_(85903)
    return aux
_c_(85906, _n_(85905, "print", lambda: print), 'Original list:')
_l_(85907)
_c_(85910, _n_(85908, "print", lambda: print), _n_(85909, "nums", lambda: nums))
_l_(85911)
_c_(85913, _n_(85912, "print", lambda: print), '\nFirst even and odd number of the said list of numbers:')
_l_(85914)
_c_(85919, _n_(85915, "print", lambda: print), _c_(85918, _n_(85916, "first_even_odd", lambda: first_even_odd), _n_(85917, "nums", lambda: nums)))
_l_(85920)