# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array as arr
    _l_(49864)

except ImportError:
    pass

def test(nums):
    _l_(49873)

    aux = _c_(49871, _n_(49865, "sorted", lambda: sorted), _c_(49868, _n_(49866, "set", lambda: set), _n_(49867, "nums", lambda: nums)), key=_a_(49870, _n_(49869, "nums", lambda: nums), "index"))
    _l_(49872)
    return aux
array_num = _c_(49876, _a_(49875, _n_(49874, "arr", lambda: arr), "array"), 'i', [1, 3, 5, 1, 3, 7, 9])
_l_(49877)
_c_(49879, _n_(49878, "print", lambda: print), 'Original array:')
_l_(49880)
for i in _c_(49885, _n_(49881, "range", lambda: range), _c_(49884, _n_(49882, "len", lambda: len), _n_(49883, "array_num", lambda: array_num))):
    _l_(49891)

    _c_(49889, _n_(49886, "print", lambda: print), _n_(49887, "array_num", lambda: array_num)[_n_(49888, "i", lambda: i)], end=' ')
    _l_(49890)
_c_(49893, _n_(49892, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(49894)
result = _c_(49900, _a_(49896, _n_(49895, "arr", lambda: arr), "array"), 'i', _c_(49899, _n_(49897, "test", lambda: test), _n_(49898, "array_num", lambda: array_num)))
_l_(49901)
for i in _c_(49906, _n_(49902, "range", lambda: range), _c_(49905, _n_(49903, "len", lambda: len), _n_(49904, "result", lambda: result))):
    _l_(49912)

    _c_(49910, _n_(49907, "print", lambda: print), _n_(49908, "result", lambda: result)[_n_(49909, "i", lambda: i)], end=' ')
    _l_(49911)
array_num = _c_(49915, _a_(49914, _n_(49913, "arr", lambda: arr), "array"), 'i', [2, 4, 2, 6, 4, 8])
_l_(49916)
_c_(49918, _n_(49917, "print", lambda: print), '\nOriginal array:')
_l_(49919)
for i in _c_(49924, _n_(49920, "range", lambda: range), _c_(49923, _n_(49921, "len", lambda: len), _n_(49922, "array_num", lambda: array_num))):
    _l_(49930)

    _c_(49928, _n_(49925, "print", lambda: print), _n_(49926, "array_num", lambda: array_num)[_n_(49927, "i", lambda: i)], end=' ')
    _l_(49929)
_c_(49932, _n_(49931, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(49933)
for i in _c_(49938, _n_(49934, "range", lambda: range), _c_(49937, _n_(49935, "len", lambda: len), _n_(49936, "result", lambda: result))):
    _l_(49944)

    _c_(49942, _n_(49939, "print", lambda: print), _n_(49940, "result", lambda: result)[_n_(49941, "i", lambda: i)], end=' ')
    _l_(49943)