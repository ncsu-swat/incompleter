# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(68973)

except ImportError:
    pass

def max_time(nums):
    _l_(69009)

    for i in _c_(68978, _n_(68974, "range", lambda: range), _c_(68977, _n_(68975, "len", lambda: len), _n_(68976, "nums", lambda: nums))):
        _l_(68982)

        _n_(68979, "nums", lambda: nums)[_n_(68980, "i", lambda: i)] *= -1
        _l_(68981)
    _c_(68985, _a_(68984, _n_(68983, "nums", lambda: nums), "sort"))
    _l_(68986)
    for (hr1, hr2, m1, m2) in _c_(68990, _a_(68988, _n_(68987, "itertools", lambda: itertools), "permutations"), _n_(68989, "nums", lambda: nums)):
        _l_(69006)

        hrs = -(10 * _n_(68991, "hr1", lambda: hr1) + _n_(68992, "hr2", lambda: hr2))
        _l_(68993)
        mins = -(10 * _n_(68994, "m1", lambda: m1) + _n_(68995, "m2", lambda: m2))
        _l_(68996)
        if 60 > _n_(68997, "mins", lambda: mins) >= 0 and 24 > _n_(68998, "hrs", lambda: hrs) >= 0:
            _l_(69005)

            result = _c_(69002, _a_(68999, '{:02}:{:02}', "format"), _n_(69000, "hrs", lambda: hrs), _n_(69001, "mins", lambda: mins))
            _l_(69003)
            break
            _l_(69004)
    aux = _n_(69007, "result", lambda: result)
    _l_(69008)
    return aux
nums = [1, 2, 3, 4]
_l_(69010)
_c_(69013, _n_(69011, "print", lambda: print), 'Original array:', _n_(69012, "nums", lambda: nums))
_l_(69014)
_c_(69019, _n_(69015, "print", lambda: print), 'Latest time: ', _c_(69018, _n_(69016, "max_time", lambda: max_time), _n_(69017, "nums", lambda: nums)))
_l_(69020)
nums = [1, 2, 4, 5]
_l_(69021)
_c_(69024, _n_(69022, "print", lambda: print), '\nOriginal array:', _n_(69023, "nums", lambda: nums))
_l_(69025)
_c_(69030, _n_(69026, "print", lambda: print), 'Latest time: ', _c_(69029, _n_(69027, "max_time", lambda: max_time), _n_(69028, "nums", lambda: nums)))
_l_(69031)
_c_(69034, _n_(69032, "print", lambda: print), '\nOriginal array:', _n_(69033, "nums", lambda: nums))
_l_(69035)
_c_(69040, _n_(69036, "print", lambda: print), 'Latest time: ', _c_(69039, _n_(69037, "max_time", lambda: max_time), _n_(69038, "nums", lambda: nums)))
_l_(69041)
nums = [2, 2, 4, 3]
_l_(69042)
_c_(69045, _n_(69043, "print", lambda: print), '\nOriginal array:', _n_(69044, "nums", lambda: nums))
_l_(69046)
_c_(69051, _n_(69047, "print", lambda: print), 'Latest time: ', _c_(69050, _n_(69048, "max_time", lambda: max_time), _n_(69049, "nums", lambda: nums)))
_l_(69052)
nums = [0, 2, 4, 3]
_l_(69053)
_c_(69056, _n_(69054, "print", lambda: print), '\nOriginal array:', _n_(69055, "nums", lambda: nums))
_l_(69057)
_c_(69062, _n_(69058, "print", lambda: print), 'Latest time: ', _c_(69061, _n_(69059, "max_time", lambda: max_time), _n_(69060, "nums", lambda: nums)))
_l_(69063)