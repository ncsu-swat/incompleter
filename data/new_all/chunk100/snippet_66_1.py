# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(68883)

except ImportError:
    pass

def max_time(nums):
    _l_(68916)

    for i in _c_(68888, _n_(68884, "range", lambda: range), _c_(68887, _n_(68885, "len", lambda: len), _n_(68886, "nums", lambda: nums))):
        _l_(68892)

        _n_(68889, "nums", lambda: nums)[_n_(68890, "i", lambda: i)] *= -1
        _l_(68891)
    _c_(68895, _a_(68894, _n_(68893, "nums", lambda: nums), "sort"))
    _l_(68896)
    for (hr1, hr2, m1, m2) in _c_(68900, _a_(68898, _n_(68897, "itertools", lambda: itertools), "permutations"), _n_(68899, "nums", lambda: nums)):
        _l_(68913)

        mins = -(10 * _n_(68901, "m1", lambda: m1) + _n_(68902, "m2", lambda: m2))
        _l_(68903)
        if 60 > _n_(68904, "mins", lambda: mins) >= 0 and 24 > _n_(68905, "hrs", lambda: hrs) >= 0:
            _l_(68912)

            result = _c_(68909, _a_(68906, '{:02}:{:02}', "format"), _n_(68907, "hrs", lambda: hrs), _n_(68908, "mins", lambda: mins))
            _l_(68910)
            break
            _l_(68911)
    aux = _n_(68914, "result", lambda: result)
    _l_(68915)
    return aux
nums = [1, 2, 3, 4]
_l_(68917)
_c_(68920, _n_(68918, "print", lambda: print), 'Original array:', _n_(68919, "nums", lambda: nums))
_l_(68921)
_c_(68926, _n_(68922, "print", lambda: print), 'Latest time: ', _c_(68925, _n_(68923, "max_time", lambda: max_time), _n_(68924, "nums", lambda: nums)))
_l_(68927)
nums = [1, 2, 4, 5]
_l_(68928)
_c_(68931, _n_(68929, "print", lambda: print), '\nOriginal array:', _n_(68930, "nums", lambda: nums))
_l_(68932)
_c_(68937, _n_(68933, "print", lambda: print), 'Latest time: ', _c_(68936, _n_(68934, "max_time", lambda: max_time), _n_(68935, "nums", lambda: nums)))
_l_(68938)
nums = [2, 2, 4, 5]
_l_(68939)
_c_(68942, _n_(68940, "print", lambda: print), '\nOriginal array:', _n_(68941, "nums", lambda: nums))
_l_(68943)
_c_(68948, _n_(68944, "print", lambda: print), 'Latest time: ', _c_(68947, _n_(68945, "max_time", lambda: max_time), _n_(68946, "nums", lambda: nums)))
_l_(68949)
nums = [2, 2, 4, 3]
_l_(68950)
_c_(68953, _n_(68951, "print", lambda: print), '\nOriginal array:', _n_(68952, "nums", lambda: nums))
_l_(68954)
_c_(68959, _n_(68955, "print", lambda: print), 'Latest time: ', _c_(68958, _n_(68956, "max_time", lambda: max_time), _n_(68957, "nums", lambda: nums)))
_l_(68960)
nums = [0, 2, 4, 3]
_l_(68961)
_c_(68964, _n_(68962, "print", lambda: print), '\nOriginal array:', _n_(68963, "nums", lambda: nums))
_l_(68965)
_c_(68970, _n_(68966, "print", lambda: print), 'Latest time: ', _c_(68969, _n_(68967, "max_time", lambda: max_time), _n_(68968, "nums", lambda: nums)))
_l_(68971)