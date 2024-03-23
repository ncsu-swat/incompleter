# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(69431)

except ImportError:
    pass

def max_time(nums):
    _l_(69467)

    for i in _c_(69436, _n_(69432, "range", lambda: range), _c_(69435, _n_(69433, "len", lambda: len), _n_(69434, "nums", lambda: nums))):
        _l_(69440)

        _n_(69437, "nums", lambda: nums)[_n_(69438, "i", lambda: i)] *= -1
        _l_(69439)
    _c_(69443, _a_(69442, _n_(69441, "nums", lambda: nums), "sort"))
    _l_(69444)
    for (hr1, hr2, m1, m2) in _c_(69448, _a_(69446, _n_(69445, "itertools", lambda: itertools), "permutations"), _n_(69447, "nums", lambda: nums)):
        _l_(69464)

        hrs = -(10 * _n_(69449, "hr1", lambda: hr1) + _n_(69450, "hr2", lambda: hr2))
        _l_(69451)
        mins = -(10 * _n_(69452, "m1", lambda: m1) + _n_(69453, "m2", lambda: m2))
        _l_(69454)
        if 60 > _n_(69455, "mins", lambda: mins) >= 0 and 24 > _n_(69456, "hrs", lambda: hrs) >= 0:
            _l_(69463)

            result = _c_(69460, _a_(69457, '{:02}:{:02}', "format"), _n_(69458, "hrs", lambda: hrs), _n_(69459, "mins", lambda: mins))
            _l_(69461)
            break
            _l_(69462)
    aux = _n_(69465, "result", lambda: result)
    _l_(69466)
    return aux
nums = [1, 2, 3, 4]
_l_(69468)
_c_(69471, _n_(69469, "print", lambda: print), 'Original array:', _n_(69470, "nums", lambda: nums))
_l_(69472)
_c_(69477, _n_(69473, "print", lambda: print), 'Latest time: ', _c_(69476, _n_(69474, "max_time", lambda: max_time), _n_(69475, "nums", lambda: nums)))
_l_(69478)
_c_(69481, _n_(69479, "print", lambda: print), '\nOriginal array:', _n_(69480, "nums", lambda: nums))
_l_(69482)
_c_(69487, _n_(69483, "print", lambda: print), 'Latest time: ', _c_(69486, _n_(69484, "max_time", lambda: max_time), _n_(69485, "nums", lambda: nums)))
_l_(69488)
nums = [2, 2, 4, 5]
_l_(69489)
_c_(69492, _n_(69490, "print", lambda: print), '\nOriginal array:', _n_(69491, "nums", lambda: nums))
_l_(69493)
_c_(69498, _n_(69494, "print", lambda: print), 'Latest time: ', _c_(69497, _n_(69495, "max_time", lambda: max_time), _n_(69496, "nums", lambda: nums)))
_l_(69499)
nums = [2, 2, 4, 3]
_l_(69500)
_c_(69503, _n_(69501, "print", lambda: print), '\nOriginal array:', _n_(69502, "nums", lambda: nums))
_l_(69504)
_c_(69509, _n_(69505, "print", lambda: print), 'Latest time: ', _c_(69508, _n_(69506, "max_time", lambda: max_time), _n_(69507, "nums", lambda: nums)))
_l_(69510)
nums = [0, 2, 4, 3]
_l_(69511)
_c_(69514, _n_(69512, "print", lambda: print), '\nOriginal array:', _n_(69513, "nums", lambda: nums))
_l_(69515)
_c_(69520, _n_(69516, "print", lambda: print), 'Latest time: ', _c_(69519, _n_(69517, "max_time", lambda: max_time), _n_(69518, "nums", lambda: nums)))
_l_(69521)