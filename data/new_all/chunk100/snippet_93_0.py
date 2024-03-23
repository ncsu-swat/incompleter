# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(94454)

except ImportError:
    pass
try:
    from heapq import merge
    _l_(94456)

except ImportError:
    pass

def nth_hamming_number(n):
    _l_(94487)


    def num_recur():
        _l_(94482)

        last = 1
        _l_(94457)
        yield _n_(94458, "last", lambda: last)
        _l_(94459)
        (x, y, z) = _c_(94464, _a_(94461, _n_(94460, "itertools", lambda: itertools), "tee"), _c_(94463, _n_(94462, "num_recur", lambda: num_recur)), 3)
        _l_(94465)
        for n in _c_(94473, _n_(94466, "merge", lambda: merge), (2 * _n_(94467, "i", lambda: i) for i in _n_(94468, "x", lambda: x)), (3 * _n_(94469, "i", lambda: i) for i in _n_(94470, "y", lambda: y)), (5 * _n_(94471, "i", lambda: i) for i in _n_(94472, "z", lambda: z))):
            _l_(94481)

            if _n_(94474, "n", lambda: n) != _n_(94475, "last", lambda: last):
                _l_(94480)

                yield _n_(94476, "n", lambda: n)
                _l_(94477)
                last = _n_(94478, "n", lambda: n)
                _l_(94479)
    aux = _c_(94485, _n_(94483, "list", lambda: list), _n_(94484, "result", lambda: result))[-1]
    _l_(94486)
    return aux
_c_(94491, _n_(94488, "print", lambda: print), _c_(94490, _n_(94489, "nth_hamming_number", lambda: nth_hamming_number), 8))
_l_(94492)
_c_(94496, _n_(94493, "print", lambda: print), _c_(94495, _n_(94494, "nth_hamming_number", lambda: nth_hamming_number), 14))
_l_(94497)
_c_(94501, _n_(94498, "print", lambda: print), _c_(94500, _n_(94499, "nth_hamming_number", lambda: nth_hamming_number), 17))
_l_(94502)