# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(69157)

except ImportError:
    pass

def max_time(nums):
    _l_(69193)

    for i in _c_(69162, _n_(69158, "range", lambda: range), _c_(69161, _n_(69159, "len", lambda: len), _n_(69160, "nums", lambda: nums))):
        _l_(69166)

        _n_(69163, "nums", lambda: nums)[_n_(69164, "i", lambda: i)] *= -1
        _l_(69165)
    _c_(69169, _a_(69168, _n_(69167, "nums", lambda: nums), "sort"))
    _l_(69170)
    for (hr1, hr2, m1, m2) in _c_(69174, _a_(69172, _n_(69171, "itertools", lambda: itertools), "permutations"), _n_(69173, "nums", lambda: nums)):
        _l_(69190)

        hrs = -(10 * _n_(69175, "hr1", lambda: hr1) + _n_(69176, "hr2", lambda: hr2))
        _l_(69177)
        mins = -(10 * _n_(69178, "m1", lambda: m1) + _n_(69179, "m2", lambda: m2))
        _l_(69180)
        if 60 > _n_(69181, "mins", lambda: mins) >= 0 and 24 > _n_(69182, "hrs", lambda: hrs) >= 0:
            _l_(69189)

            result = _c_(69186, _a_(69183, '{:02}:{:02}', "format"), _n_(69184, "hrs", lambda: hrs), _n_(69185, "mins", lambda: mins))
            _l_(69187)
            break
            _l_(69188)
    aux = _n_(69191, "result", lambda: result)
    _l_(69192)
    return aux
nums = [1, 2, 3, 4]
_l_(69194)
_c_(69197, _n_(69195, "print", lambda: print), 'Original array:', _n_(69196, "nums", lambda: nums))
_l_(69198)
_c_(69203, _n_(69199, "print", lambda: print), 'Latest time: ', _c_(69202, _n_(69200, "max_time", lambda: max_time), _n_(69201, "nums", lambda: nums)))
_l_(69204)
nums = [1, 2, 4, 5]
_l_(69205)
_c_(69208, _n_(69206, "print", lambda: print), '\nOriginal array:', _n_(69207, "nums", lambda: nums))
_l_(69209)
_c_(69214, _n_(69210, "print", lambda: print), 'Latest time: ', _c_(69213, _n_(69211, "max_time", lambda: max_time), _n_(69212, "nums", lambda: nums)))
_l_(69215)
nums = [2, 2, 4, 5]
_l_(69216)
_c_(69219, _n_(69217, "print", lambda: print), '\nOriginal array:', _n_(69218, "nums", lambda: nums))
_l_(69220)
_c_(69225, _n_(69221, "print", lambda: print), 'Latest time: ', _c_(69224, _n_(69222, "max_time", lambda: max_time), _n_(69223, "nums", lambda: nums)))
_l_(69226)
nums = [2, 2, 4, 3]
_l_(69227)
_c_(69230, _n_(69228, "print", lambda: print), '\nOriginal array:', _n_(69229, "nums", lambda: nums))
_l_(69231)
_c_(69236, _n_(69232, "print", lambda: print), 'Latest time: ', _c_(69235, _n_(69233, "max_time", lambda: max_time), _n_(69234, "nums", lambda: nums)))
_l_(69237)
_c_(69240, _n_(69238, "print", lambda: print), '\nOriginal array:', _n_(69239, "nums", lambda: nums))
_l_(69241)
_c_(69246, _n_(69242, "print", lambda: print), 'Latest time: ', _c_(69245, _n_(69243, "max_time", lambda: max_time), _n_(69244, "nums", lambda: nums)))
_l_(69247)