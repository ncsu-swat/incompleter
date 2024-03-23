# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array as arr
    _l_(50031)

except ImportError:
    pass

def test(nums):
    _l_(50040)

    aux = _c_(50038, _n_(50032, "sorted", lambda: sorted), _c_(50035, _n_(50033, "set", lambda: set), _n_(50034, "nums", lambda: nums)), key=_a_(50037, _n_(50036, "nums", lambda: nums), "index"))
    _l_(50039)
    return aux
array_num = _c_(50043, _a_(50042, _n_(50041, "arr", lambda: arr), "array"), 'i', [1, 3, 5, 1, 3, 7, 9])
_l_(50044)
_c_(50046, _n_(50045, "print", lambda: print), 'Original array:')
_l_(50047)
for i in _c_(50052, _n_(50048, "range", lambda: range), _c_(50051, _n_(50049, "len", lambda: len), _n_(50050, "array_num", lambda: array_num))):
    _l_(50058)

    _c_(50056, _n_(50053, "print", lambda: print), _n_(50054, "array_num", lambda: array_num)[_n_(50055, "i", lambda: i)], end=' ')
    _l_(50057)
_c_(50060, _n_(50059, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(50061)
for i in _c_(50066, _n_(50062, "range", lambda: range), _c_(50065, _n_(50063, "len", lambda: len), _n_(50064, "result", lambda: result))):
    _l_(50072)

    _c_(50070, _n_(50067, "print", lambda: print), _n_(50068, "result", lambda: result)[_n_(50069, "i", lambda: i)], end=' ')
    _l_(50071)
array_num = _c_(50075, _a_(50074, _n_(50073, "arr", lambda: arr), "array"), 'i', [2, 4, 2, 6, 4, 8])
_l_(50076)
_c_(50078, _n_(50077, "print", lambda: print), '\nOriginal array:')
_l_(50079)
for i in _c_(50084, _n_(50080, "range", lambda: range), _c_(50083, _n_(50081, "len", lambda: len), _n_(50082, "array_num", lambda: array_num))):
    _l_(50090)

    _c_(50088, _n_(50085, "print", lambda: print), _n_(50086, "array_num", lambda: array_num)[_n_(50087, "i", lambda: i)], end=' ')
    _l_(50089)
_c_(50092, _n_(50091, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(50093)
result = _c_(50099, _a_(50095, _n_(50094, "arr", lambda: arr), "array"), 'i', _c_(50098, _n_(50096, "test", lambda: test), _n_(50097, "array_num", lambda: array_num)))
_l_(50100)
for i in _c_(50105, _n_(50101, "range", lambda: range), _c_(50104, _n_(50102, "len", lambda: len), _n_(50103, "result", lambda: result))):
    _l_(50111)

    _c_(50109, _n_(50106, "print", lambda: print), _n_(50107, "result", lambda: result)[_n_(50108, "i", lambda: i)], end=' ')
    _l_(50110)