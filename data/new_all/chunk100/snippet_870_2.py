# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_even_odd(nums):
    _l_(85957)

    first_even = _c_(85952, _n_(85948, "next", lambda: next), (_n_(85949, "el", lambda: el) for el in _n_(85950, "nums", lambda: nums) if _n_(85951, "el", lambda: el) % 2 == 0), -1)
    _l_(85953)
    aux = (_n_(85954, "first_even", lambda: first_even), _n_(85955, "first_odd", lambda: first_odd))
    _l_(85956)
    return aux
nums = [1, 3, 5, 7, 4, 1, 6, 8]
_l_(85958)
_c_(85960, _n_(85959, "print", lambda: print), 'Original list:')
_l_(85961)
_c_(85964, _n_(85962, "print", lambda: print), _n_(85963, "nums", lambda: nums))
_l_(85965)
_c_(85967, _n_(85966, "print", lambda: print), '\nFirst even and odd number of the said list of numbers:')
_l_(85968)
_c_(85973, _n_(85969, "print", lambda: print), _c_(85972, _n_(85970, "first_even_odd", lambda: first_even_odd), _n_(85971, "nums", lambda: nums)))
_l_(85974)