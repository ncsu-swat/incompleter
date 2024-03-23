# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(69065)

except ImportError:
    pass

def max_time(nums):
    _l_(69101)

    for i in _c_(69070, _n_(69066, "range", lambda: range), _c_(69069, _n_(69067, "len", lambda: len), _n_(69068, "nums", lambda: nums))):
        _l_(69074)

        _n_(69071, "nums", lambda: nums)[_n_(69072, "i", lambda: i)] *= -1
        _l_(69073)
    _c_(69077, _a_(69076, _n_(69075, "nums", lambda: nums), "sort"))
    _l_(69078)
    for (hr1, hr2, m1, m2) in _c_(69082, _a_(69080, _n_(69079, "itertools", lambda: itertools), "permutations"), _n_(69081, "nums", lambda: nums)):
        _l_(69098)

        hrs = -(10 * _n_(69083, "hr1", lambda: hr1) + _n_(69084, "hr2", lambda: hr2))
        _l_(69085)
        mins = -(10 * _n_(69086, "m1", lambda: m1) + _n_(69087, "m2", lambda: m2))
        _l_(69088)
        if 60 > _n_(69089, "mins", lambda: mins) >= 0 and 24 > _n_(69090, "hrs", lambda: hrs) >= 0:
            _l_(69097)

            result = _c_(69094, _a_(69091, '{:02}:{:02}', "format"), _n_(69092, "hrs", lambda: hrs), _n_(69093, "mins", lambda: mins))
            _l_(69095)
            break
            _l_(69096)
    aux = _n_(69099, "result", lambda: result)
    _l_(69100)
    return aux
nums = [1, 2, 3, 4]
_l_(69102)
_c_(69105, _n_(69103, "print", lambda: print), 'Original array:', _n_(69104, "nums", lambda: nums))
_l_(69106)
_c_(69111, _n_(69107, "print", lambda: print), 'Latest time: ', _c_(69110, _n_(69108, "max_time", lambda: max_time), _n_(69109, "nums", lambda: nums)))
_l_(69112)
nums = [1, 2, 4, 5]
_l_(69113)
_c_(69116, _n_(69114, "print", lambda: print), '\nOriginal array:', _n_(69115, "nums", lambda: nums))
_l_(69117)
_c_(69122, _n_(69118, "print", lambda: print), 'Latest time: ', _c_(69121, _n_(69119, "max_time", lambda: max_time), _n_(69120, "nums", lambda: nums)))
_l_(69123)
nums = [2, 2, 4, 5]
_l_(69124)
_c_(69127, _n_(69125, "print", lambda: print), '\nOriginal array:', _n_(69126, "nums", lambda: nums))
_l_(69128)
_c_(69133, _n_(69129, "print", lambda: print), 'Latest time: ', _c_(69132, _n_(69130, "max_time", lambda: max_time), _n_(69131, "nums", lambda: nums)))
_l_(69134)
_c_(69137, _n_(69135, "print", lambda: print), '\nOriginal array:', _n_(69136, "nums", lambda: nums))
_l_(69138)
_c_(69143, _n_(69139, "print", lambda: print), 'Latest time: ', _c_(69142, _n_(69140, "max_time", lambda: max_time), _n_(69141, "nums", lambda: nums)))
_l_(69144)
nums = [0, 2, 4, 3]
_l_(69145)
_c_(69148, _n_(69146, "print", lambda: print), '\nOriginal array:', _n_(69147, "nums", lambda: nums))
_l_(69149)
_c_(69154, _n_(69150, "print", lambda: print), 'Latest time: ', _c_(69153, _n_(69151, "max_time", lambda: max_time), _n_(69152, "nums", lambda: nums)))
_l_(69155)