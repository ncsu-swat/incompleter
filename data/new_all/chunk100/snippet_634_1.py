# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array as arr
    _l_(65826)

except ImportError:
    pass

def test(nums):
    _l_(65837)

    aux = _c_(65830, _n_(65827, "sum", lambda: sum), _c_(65829, _n_(65828, "range", lambda: range), 10, 21)) - _c_(65835, _n_(65831, "sum", lambda: sum), _c_(65834, _n_(65832, "list", lambda: list), _n_(65833, "nums", lambda: nums)))
    _l_(65836)
    return aux
array_num = _c_(65840, _a_(65839, _n_(65838, "arr", lambda: arr), "array"), 'i', [10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
_l_(65841)
_c_(65843, _n_(65842, "print", lambda: print), 'Original array:')
_l_(65844)
for i in _c_(65849, _n_(65845, "range", lambda: range), _c_(65848, _n_(65846, "len", lambda: len), _n_(65847, "array_num", lambda: array_num))):
    _l_(65855)

    _c_(65853, _n_(65850, "print", lambda: print), _n_(65851, "array_num", lambda: array_num)[_n_(65852, "i", lambda: i)], end=' ')
    _l_(65854)
_c_(65860, _n_(65856, "print", lambda: print), '\nMissing number in the said array (10-20): ', _c_(65859, _n_(65857, "test", lambda: test), _n_(65858, "array_num", lambda: array_num)))
_l_(65861)
_c_(65863, _n_(65862, "print", lambda: print), '\nOriginal array:')
_l_(65864)
for i in _c_(65869, _n_(65865, "range", lambda: range), _c_(65868, _n_(65866, "len", lambda: len), _n_(65867, "array_num", lambda: array_num))):
    _l_(65875)

    _c_(65873, _n_(65870, "print", lambda: print), _n_(65871, "array_num", lambda: array_num)[_n_(65872, "i", lambda: i)], end=' ')
    _l_(65874)
_c_(65880, _n_(65876, "print", lambda: print), '\nMissing number in the said array (10-20): ', _c_(65879, _n_(65877, "test", lambda: test), _n_(65878, "array_num", lambda: array_num)))
_l_(65881)