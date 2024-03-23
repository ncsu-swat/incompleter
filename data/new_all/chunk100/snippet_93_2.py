# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(94560)

except ImportError:
    pass
try:
    from heapq import merge
    _l_(94562)

except ImportError:
    pass

def nth_hamming_number(n):
    _l_(94598)


    def num_recur():
        _l_(94586)

        last = 1
        _l_(94563)
        yield _n_(94564, "last", lambda: last)
        _l_(94565)
        (x, y, z) = _c_(94570, _a_(94567, _n_(94566, "itertools", lambda: itertools), "tee"), _c_(94569, _n_(94568, "num_recur", lambda: num_recur)), 3)
        _l_(94571)
        for n in _c_(94579, _n_(94572, "merge", lambda: merge), (2 * _n_(94573, "i", lambda: i) for i in _n_(94574, "x", lambda: x)), (3 * _n_(94575, "i", lambda: i) for i in _n_(94576, "y", lambda: y)), (5 * _n_(94577, "i", lambda: i) for i in _n_(94578, "z", lambda: z))):
            _l_(94585)

            if _n_(94580, "n", lambda: n) != _n_(94581, "last", lambda: last):
                _l_(94584)

                yield _n_(94582, "n", lambda: n)
                _l_(94583)
    result = _c_(94592, _a_(94588, _n_(94587, "itertools", lambda: itertools), "islice"), _c_(94590, _n_(94589, "num_recur", lambda: num_recur)), _n_(94591, "n", lambda: n))
    _l_(94593)
    aux = _c_(94596, _n_(94594, "list", lambda: list), _n_(94595, "result", lambda: result))[-1]
    _l_(94597)
    return aux
_c_(94602, _n_(94599, "print", lambda: print), _c_(94601, _n_(94600, "nth_hamming_number", lambda: nth_hamming_number), 8))
_l_(94603)
_c_(94607, _n_(94604, "print", lambda: print), _c_(94606, _n_(94605, "nth_hamming_number", lambda: nth_hamming_number), 14))
_l_(94608)
_c_(94612, _n_(94609, "print", lambda: print), _c_(94611, _n_(94610, "nth_hamming_number", lambda: nth_hamming_number), 17))
_l_(94613)