# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(94504)

except ImportError:
    pass
try:
    from heapq import merge
    _l_(94506)

except ImportError:
    pass

def nth_hamming_number(n):
    _l_(94543)


    def num_recur():
        _l_(94531)

        yield _n_(94507, "last", lambda: last)
        _l_(94508)
        (x, y, z) = _c_(94513, _a_(94510, _n_(94509, "itertools", lambda: itertools), "tee"), _c_(94512, _n_(94511, "num_recur", lambda: num_recur)), 3)
        _l_(94514)
        for n in _c_(94522, _n_(94515, "merge", lambda: merge), (2 * _n_(94516, "i", lambda: i) for i in _n_(94517, "x", lambda: x)), (3 * _n_(94518, "i", lambda: i) for i in _n_(94519, "y", lambda: y)), (5 * _n_(94520, "i", lambda: i) for i in _n_(94521, "z", lambda: z))):
            _l_(94530)

            if _n_(94523, "n", lambda: n) != _n_(94524, "last", lambda: last):
                _l_(94529)

                yield _n_(94525, "n", lambda: n)
                _l_(94526)
                last = _n_(94527, "n", lambda: n)
                _l_(94528)
    result = _c_(94537, _a_(94533, _n_(94532, "itertools", lambda: itertools), "islice"), _c_(94535, _n_(94534, "num_recur", lambda: num_recur)), _n_(94536, "n", lambda: n))
    _l_(94538)
    aux = _c_(94541, _n_(94539, "list", lambda: list), _n_(94540, "result", lambda: result))[-1]
    _l_(94542)
    return aux
_c_(94547, _n_(94544, "print", lambda: print), _c_(94546, _n_(94545, "nth_hamming_number", lambda: nth_hamming_number), 8))
_l_(94548)
_c_(94552, _n_(94549, "print", lambda: print), _c_(94551, _n_(94550, "nth_hamming_number", lambda: nth_hamming_number), 14))
_l_(94553)
_c_(94557, _n_(94554, "print", lambda: print), _c_(94556, _n_(94555, "nth_hamming_number", lambda: nth_hamming_number), 17))
_l_(94558)