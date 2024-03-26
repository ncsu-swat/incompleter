# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array as arr
    _l_(117856)

except ImportError:
    pass

def test(nums):
    _l_(117865)

    aux = _c_(117863, _n_(117857, "sorted", lambda: sorted), _c_(117860, _n_(117858, "set", lambda: set), _n_(117859, "nums", lambda: nums)), key=_a_(117862, _n_(117861, "nums", lambda: nums), "index"))
    _l_(117864)
    return aux
array_num = _c_(117868, _a_(117867, _n_(117866, "arr", lambda: arr), "array"), 'i', [1, 3, 5, 1, 3, 7, 9])
_l_(117869)
_c_(117871, _n_(117870, "print", lambda: print), 'Original array:')
_l_(117872)
for i in _c_(117877, _n_(117873, "range", lambda: range), _c_(117876, _n_(117874, "len", lambda: len), _n_(117875, "array_num", lambda: array_num))):
    _l_(117883)

    _c_(117881, _n_(117878, "print", lambda: print), _n_(117879, "array_num", lambda: array_num)[_n_(117880, "i", lambda: i)], end=' ')
    _l_(117882)
_c_(117885, _n_(117884, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(117886)
for i in _c_(117891, _n_(117887, "range", lambda: range), _c_(117890, _n_(117888, "len", lambda: len), _n_(117889, "result", lambda: result))):
    _l_(117897)

    _c_(117895, _n_(117892, "print", lambda: print), _n_(117893, "result", lambda: result)[_n_(117894, "i", lambda: i)], end=' ')
    _l_(117896)
array_num = _c_(117900, _a_(117899, _n_(117898, "arr", lambda: arr), "array"), 'i', [2, 4, 2, 6, 4, 8])
_l_(117901)
_c_(117903, _n_(117902, "print", lambda: print), '\nOriginal array:')
_l_(117904)
for i in _c_(117909, _n_(117905, "range", lambda: range), _c_(117908, _n_(117906, "len", lambda: len), _n_(117907, "array_num", lambda: array_num))):
    _l_(117915)

    _c_(117913, _n_(117910, "print", lambda: print), _n_(117911, "array_num", lambda: array_num)[_n_(117912, "i", lambda: i)], end=' ')
    _l_(117914)
_c_(117917, _n_(117916, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(117918)
result = _c_(117924, _a_(117920, _n_(117919, "arr", lambda: arr), "array"), 'i', _c_(117923, _n_(117921, "test", lambda: test), _n_(117922, "array_num", lambda: array_num)))
_l_(117925)
for i in _c_(117930, _n_(117926, "range", lambda: range), _c_(117929, _n_(117927, "len", lambda: len), _n_(117928, "result", lambda: result))):
    _l_(117936)

    _c_(117934, _n_(117931, "print", lambda: print), _n_(117932, "result", lambda: result)[_n_(117933, "i", lambda: i)], end=' ')
    _l_(117935)