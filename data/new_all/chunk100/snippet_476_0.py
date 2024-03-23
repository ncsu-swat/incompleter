# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array as arr
    _l_(49779)

except ImportError:
    pass

def test(nums):
    _l_(49788)

    aux = _c_(49786, _n_(49780, "sorted", lambda: sorted), _c_(49783, _n_(49781, "set", lambda: set), _n_(49782, "nums", lambda: nums)), key=_a_(49785, _n_(49784, "nums", lambda: nums), "index"))
    _l_(49787)
    return aux
_c_(49790, _n_(49789, "print", lambda: print), 'Original array:')
_l_(49791)
for i in _c_(49796, _n_(49792, "range", lambda: range), _c_(49795, _n_(49793, "len", lambda: len), _n_(49794, "array_num", lambda: array_num))):
    _l_(49802)

    _c_(49800, _n_(49797, "print", lambda: print), _n_(49798, "array_num", lambda: array_num)[_n_(49799, "i", lambda: i)], end=' ')
    _l_(49801)
_c_(49804, _n_(49803, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(49805)
result = _c_(49811, _a_(49807, _n_(49806, "arr", lambda: arr), "array"), 'i', _c_(49810, _n_(49808, "test", lambda: test), _n_(49809, "array_num", lambda: array_num)))
_l_(49812)
for i in _c_(49817, _n_(49813, "range", lambda: range), _c_(49816, _n_(49814, "len", lambda: len), _n_(49815, "result", lambda: result))):
    _l_(49823)

    _c_(49821, _n_(49818, "print", lambda: print), _n_(49819, "result", lambda: result)[_n_(49820, "i", lambda: i)], end=' ')
    _l_(49822)
array_num = _c_(49826, _a_(49825, _n_(49824, "arr", lambda: arr), "array"), 'i', [2, 4, 2, 6, 4, 8])
_l_(49827)
_c_(49829, _n_(49828, "print", lambda: print), '\nOriginal array:')
_l_(49830)
for i in _c_(49835, _n_(49831, "range", lambda: range), _c_(49834, _n_(49832, "len", lambda: len), _n_(49833, "array_num", lambda: array_num))):
    _l_(49841)

    _c_(49839, _n_(49836, "print", lambda: print), _n_(49837, "array_num", lambda: array_num)[_n_(49838, "i", lambda: i)], end=' ')
    _l_(49840)
_c_(49843, _n_(49842, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(49844)
result = _c_(49850, _a_(49846, _n_(49845, "arr", lambda: arr), "array"), 'i', _c_(49849, _n_(49847, "test", lambda: test), _n_(49848, "array_num", lambda: array_num)))
_l_(49851)
for i in _c_(49856, _n_(49852, "range", lambda: range), _c_(49855, _n_(49853, "len", lambda: len), _n_(49854, "result", lambda: result))):
    _l_(49862)

    _c_(49860, _n_(49857, "print", lambda: print), _n_(49858, "result", lambda: result)[_n_(49859, "i", lambda: i)], end=' ')
    _l_(49861)