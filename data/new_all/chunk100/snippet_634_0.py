# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array as arr
    _l_(65769)

except ImportError:
    pass

def test(nums):
    _l_(65780)

    aux = _c_(65773, _n_(65770, "sum", lambda: sum), _c_(65772, _n_(65771, "range", lambda: range), 10, 21)) - _c_(65778, _n_(65774, "sum", lambda: sum), _c_(65777, _n_(65775, "list", lambda: list), _n_(65776, "nums", lambda: nums)))
    _l_(65779)
    return aux
_c_(65782, _n_(65781, "print", lambda: print), 'Original array:')
_l_(65783)
for i in _c_(65788, _n_(65784, "range", lambda: range), _c_(65787, _n_(65785, "len", lambda: len), _n_(65786, "array_num", lambda: array_num))):
    _l_(65794)

    _c_(65792, _n_(65789, "print", lambda: print), _n_(65790, "array_num", lambda: array_num)[_n_(65791, "i", lambda: i)], end=' ')
    _l_(65793)
_c_(65799, _n_(65795, "print", lambda: print), '\nMissing number in the said array (10-20): ', _c_(65798, _n_(65796, "test", lambda: test), _n_(65797, "array_num", lambda: array_num)))
_l_(65800)
array_num = _c_(65803, _a_(65802, _n_(65801, "arr", lambda: arr), "array"), 'i', [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
_l_(65804)
_c_(65806, _n_(65805, "print", lambda: print), '\nOriginal array:')
_l_(65807)
for i in _c_(65812, _n_(65808, "range", lambda: range), _c_(65811, _n_(65809, "len", lambda: len), _n_(65810, "array_num", lambda: array_num))):
    _l_(65818)

    _c_(65816, _n_(65813, "print", lambda: print), _n_(65814, "array_num", lambda: array_num)[_n_(65815, "i", lambda: i)], end=' ')
    _l_(65817)
_c_(65823, _n_(65819, "print", lambda: print), '\nMissing number in the said array (10-20): ', _c_(65822, _n_(65820, "test", lambda: test), _n_(65821, "array_num", lambda: array_num)))
_l_(65824)