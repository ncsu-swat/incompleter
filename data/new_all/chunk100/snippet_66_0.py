# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(68795)

except ImportError:
    pass

def max_time(nums):
    _l_(68826)

    for i in _c_(68800, _n_(68796, "range", lambda: range), _c_(68799, _n_(68797, "len", lambda: len), _n_(68798, "nums", lambda: nums))):
        _l_(68804)

        _n_(68801, "nums", lambda: nums)[_n_(68802, "i", lambda: i)] *= -1
        _l_(68803)
    _c_(68807, _a_(68806, _n_(68805, "nums", lambda: nums), "sort"))
    _l_(68808)
    for (hr1, hr2, m1, m2) in _c_(68812, _a_(68810, _n_(68809, "itertools", lambda: itertools), "permutations"), _n_(68811, "nums", lambda: nums)):
        _l_(68823)

        hrs = -(10 * _n_(68813, "hr1", lambda: hr1) + _n_(68814, "hr2", lambda: hr2))
        _l_(68815)
        mins = -(10 * _n_(68816, "m1", lambda: m1) + _n_(68817, "m2", lambda: m2))
        _l_(68818)
        if 60 > _n_(68819, "mins", lambda: mins) >= 0 and 24 > _n_(68820, "hrs", lambda: hrs) >= 0:
            _l_(68822)

            break
            _l_(68821)
    aux = _n_(68824, "result", lambda: result)
    _l_(68825)
    return aux
nums = [1, 2, 3, 4]
_l_(68827)
_c_(68830, _n_(68828, "print", lambda: print), 'Original array:', _n_(68829, "nums", lambda: nums))
_l_(68831)
_c_(68836, _n_(68832, "print", lambda: print), 'Latest time: ', _c_(68835, _n_(68833, "max_time", lambda: max_time), _n_(68834, "nums", lambda: nums)))
_l_(68837)
nums = [1, 2, 4, 5]
_l_(68838)
_c_(68841, _n_(68839, "print", lambda: print), '\nOriginal array:', _n_(68840, "nums", lambda: nums))
_l_(68842)
_c_(68847, _n_(68843, "print", lambda: print), 'Latest time: ', _c_(68846, _n_(68844, "max_time", lambda: max_time), _n_(68845, "nums", lambda: nums)))
_l_(68848)
nums = [2, 2, 4, 5]
_l_(68849)
_c_(68852, _n_(68850, "print", lambda: print), '\nOriginal array:', _n_(68851, "nums", lambda: nums))
_l_(68853)
_c_(68858, _n_(68854, "print", lambda: print), 'Latest time: ', _c_(68857, _n_(68855, "max_time", lambda: max_time), _n_(68856, "nums", lambda: nums)))
_l_(68859)
nums = [2, 2, 4, 3]
_l_(68860)
_c_(68863, _n_(68861, "print", lambda: print), '\nOriginal array:', _n_(68862, "nums", lambda: nums))
_l_(68864)
_c_(68869, _n_(68865, "print", lambda: print), 'Latest time: ', _c_(68868, _n_(68866, "max_time", lambda: max_time), _n_(68867, "nums", lambda: nums)))
_l_(68870)
nums = [0, 2, 4, 3]
_l_(68871)
_c_(68874, _n_(68872, "print", lambda: print), '\nOriginal array:', _n_(68873, "nums", lambda: nums))
_l_(68875)
_c_(68880, _n_(68876, "print", lambda: print), 'Latest time: ', _c_(68879, _n_(68877, "max_time", lambda: max_time), _n_(68878, "nums", lambda: nums)))
_l_(68881)