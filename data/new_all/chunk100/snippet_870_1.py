# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_even_odd(nums):
    _l_(85930)

    first_odd = _c_(85925, _n_(85921, "next", lambda: next), (_n_(85922, "el", lambda: el) for el in _n_(85923, "nums", lambda: nums) if _n_(85924, "el", lambda: el) % 2 != 0), -1)
    _l_(85926)
    aux = (_n_(85927, "first_even", lambda: first_even), _n_(85928, "first_odd", lambda: first_odd))
    _l_(85929)
    return aux
nums = [1, 3, 5, 7, 4, 1, 6, 8]
_l_(85931)
_c_(85933, _n_(85932, "print", lambda: print), 'Original list:')
_l_(85934)
_c_(85937, _n_(85935, "print", lambda: print), _n_(85936, "nums", lambda: nums))
_l_(85938)
_c_(85940, _n_(85939, "print", lambda: print), '\nFirst even and odd number of the said list of numbers:')
_l_(85941)
_c_(85946, _n_(85942, "print", lambda: print), _c_(85945, _n_(85943, "first_even_odd", lambda: first_even_odd), _n_(85944, "nums", lambda: nums)))
_l_(85947)