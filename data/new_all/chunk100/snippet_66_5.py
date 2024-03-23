# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(69249)

except ImportError:
    pass

def max_time(nums):
    _l_(69282)

    for i in _c_(69254, _n_(69250, "range", lambda: range), _c_(69253, _n_(69251, "len", lambda: len), _n_(69252, "nums", lambda: nums))):
        _l_(69258)

        _n_(69255, "nums", lambda: nums)[_n_(69256, "i", lambda: i)] *= -1
        _l_(69257)
    _c_(69261, _a_(69260, _n_(69259, "nums", lambda: nums), "sort"))
    _l_(69262)
    for (hr1, hr2, m1, m2) in _c_(69266, _a_(69264, _n_(69263, "itertools", lambda: itertools), "permutations"), _n_(69265, "nums", lambda: nums)):
        _l_(69279)

        hrs = -(10 * _n_(69267, "hr1", lambda: hr1) + _n_(69268, "hr2", lambda: hr2))
        _l_(69269)
        if 60 > _n_(69270, "mins", lambda: mins) >= 0 and 24 > _n_(69271, "hrs", lambda: hrs) >= 0:
            _l_(69278)

            result = _c_(69275, _a_(69272, '{:02}:{:02}', "format"), _n_(69273, "hrs", lambda: hrs), _n_(69274, "mins", lambda: mins))
            _l_(69276)
            break
            _l_(69277)
    aux = _n_(69280, "result", lambda: result)
    _l_(69281)
    return aux
nums = [1, 2, 3, 4]
_l_(69283)
_c_(69286, _n_(69284, "print", lambda: print), 'Original array:', _n_(69285, "nums", lambda: nums))
_l_(69287)
_c_(69292, _n_(69288, "print", lambda: print), 'Latest time: ', _c_(69291, _n_(69289, "max_time", lambda: max_time), _n_(69290, "nums", lambda: nums)))
_l_(69293)
nums = [1, 2, 4, 5]
_l_(69294)
_c_(69297, _n_(69295, "print", lambda: print), '\nOriginal array:', _n_(69296, "nums", lambda: nums))
_l_(69298)
_c_(69303, _n_(69299, "print", lambda: print), 'Latest time: ', _c_(69302, _n_(69300, "max_time", lambda: max_time), _n_(69301, "nums", lambda: nums)))
_l_(69304)
nums = [2, 2, 4, 5]
_l_(69305)
_c_(69308, _n_(69306, "print", lambda: print), '\nOriginal array:', _n_(69307, "nums", lambda: nums))
_l_(69309)
_c_(69314, _n_(69310, "print", lambda: print), 'Latest time: ', _c_(69313, _n_(69311, "max_time", lambda: max_time), _n_(69312, "nums", lambda: nums)))
_l_(69315)
nums = [2, 2, 4, 3]
_l_(69316)
_c_(69319, _n_(69317, "print", lambda: print), '\nOriginal array:', _n_(69318, "nums", lambda: nums))
_l_(69320)
_c_(69325, _n_(69321, "print", lambda: print), 'Latest time: ', _c_(69324, _n_(69322, "max_time", lambda: max_time), _n_(69323, "nums", lambda: nums)))
_l_(69326)
nums = [0, 2, 4, 3]
_l_(69327)
_c_(69330, _n_(69328, "print", lambda: print), '\nOriginal array:', _n_(69329, "nums", lambda: nums))
_l_(69331)
_c_(69336, _n_(69332, "print", lambda: print), 'Latest time: ', _c_(69335, _n_(69333, "max_time", lambda: max_time), _n_(69334, "nums", lambda: nums)))
_l_(69337)