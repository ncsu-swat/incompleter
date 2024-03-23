# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(69339)

except ImportError:
    pass

def max_time(nums):
    _l_(69375)

    for i in _c_(69344, _n_(69340, "range", lambda: range), _c_(69343, _n_(69341, "len", lambda: len), _n_(69342, "nums", lambda: nums))):
        _l_(69348)

        _n_(69345, "nums", lambda: nums)[_n_(69346, "i", lambda: i)] *= -1
        _l_(69347)
    _c_(69351, _a_(69350, _n_(69349, "nums", lambda: nums), "sort"))
    _l_(69352)
    for (hr1, hr2, m1, m2) in _c_(69356, _a_(69354, _n_(69353, "itertools", lambda: itertools), "permutations"), _n_(69355, "nums", lambda: nums)):
        _l_(69372)

        hrs = -(10 * _n_(69357, "hr1", lambda: hr1) + _n_(69358, "hr2", lambda: hr2))
        _l_(69359)
        mins = -(10 * _n_(69360, "m1", lambda: m1) + _n_(69361, "m2", lambda: m2))
        _l_(69362)
        if 60 > _n_(69363, "mins", lambda: mins) >= 0 and 24 > _n_(69364, "hrs", lambda: hrs) >= 0:
            _l_(69371)

            result = _c_(69368, _a_(69365, '{:02}:{:02}', "format"), _n_(69366, "hrs", lambda: hrs), _n_(69367, "mins", lambda: mins))
            _l_(69369)
            break
            _l_(69370)
    aux = _n_(69373, "result", lambda: result)
    _l_(69374)
    return aux
_c_(69378, _n_(69376, "print", lambda: print), 'Original array:', _n_(69377, "nums", lambda: nums))
_l_(69379)
_c_(69384, _n_(69380, "print", lambda: print), 'Latest time: ', _c_(69383, _n_(69381, "max_time", lambda: max_time), _n_(69382, "nums", lambda: nums)))
_l_(69385)
nums = [1, 2, 4, 5]
_l_(69386)
_c_(69389, _n_(69387, "print", lambda: print), '\nOriginal array:', _n_(69388, "nums", lambda: nums))
_l_(69390)
_c_(69395, _n_(69391, "print", lambda: print), 'Latest time: ', _c_(69394, _n_(69392, "max_time", lambda: max_time), _n_(69393, "nums", lambda: nums)))
_l_(69396)
nums = [2, 2, 4, 5]
_l_(69397)
_c_(69400, _n_(69398, "print", lambda: print), '\nOriginal array:', _n_(69399, "nums", lambda: nums))
_l_(69401)
_c_(69406, _n_(69402, "print", lambda: print), 'Latest time: ', _c_(69405, _n_(69403, "max_time", lambda: max_time), _n_(69404, "nums", lambda: nums)))
_l_(69407)
nums = [2, 2, 4, 3]
_l_(69408)
_c_(69411, _n_(69409, "print", lambda: print), '\nOriginal array:', _n_(69410, "nums", lambda: nums))
_l_(69412)
_c_(69417, _n_(69413, "print", lambda: print), 'Latest time: ', _c_(69416, _n_(69414, "max_time", lambda: max_time), _n_(69415, "nums", lambda: nums)))
_l_(69418)
nums = [0, 2, 4, 3]
_l_(69419)
_c_(69422, _n_(69420, "print", lambda: print), '\nOriginal array:', _n_(69421, "nums", lambda: nums))
_l_(69423)
_c_(69428, _n_(69424, "print", lambda: print), 'Latest time: ', _c_(69427, _n_(69425, "max_time", lambda: max_time), _n_(69426, "nums", lambda: nums)))
_l_(69429)