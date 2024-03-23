# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import array as arr
    _l_(49946)

except ImportError:
    pass

def test(nums):
    _l_(49955)

    aux = _c_(49953, _n_(49947, "sorted", lambda: sorted), _c_(49950, _n_(49948, "set", lambda: set), _n_(49949, "nums", lambda: nums)), key=_a_(49952, _n_(49951, "nums", lambda: nums), "index"))
    _l_(49954)
    return aux
array_num = _c_(49958, _a_(49957, _n_(49956, "arr", lambda: arr), "array"), 'i', [1, 3, 5, 1, 3, 7, 9])
_l_(49959)
_c_(49961, _n_(49960, "print", lambda: print), 'Original array:')
_l_(49962)
for i in _c_(49967, _n_(49963, "range", lambda: range), _c_(49966, _n_(49964, "len", lambda: len), _n_(49965, "array_num", lambda: array_num))):
    _l_(49973)

    _c_(49971, _n_(49968, "print", lambda: print), _n_(49969, "array_num", lambda: array_num)[_n_(49970, "i", lambda: i)], end=' ')
    _l_(49972)
_c_(49975, _n_(49974, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(49976)
result = _c_(49982, _a_(49978, _n_(49977, "arr", lambda: arr), "array"), 'i', _c_(49981, _n_(49979, "test", lambda: test), _n_(49980, "array_num", lambda: array_num)))
_l_(49983)
for i in _c_(49988, _n_(49984, "range", lambda: range), _c_(49987, _n_(49985, "len", lambda: len), _n_(49986, "result", lambda: result))):
    _l_(49994)

    _c_(49992, _n_(49989, "print", lambda: print), _n_(49990, "result", lambda: result)[_n_(49991, "i", lambda: i)], end=' ')
    _l_(49993)
_c_(49996, _n_(49995, "print", lambda: print), '\nOriginal array:')
_l_(49997)
for i in _c_(50002, _n_(49998, "range", lambda: range), _c_(50001, _n_(49999, "len", lambda: len), _n_(50000, "array_num", lambda: array_num))):
    _l_(50008)

    _c_(50006, _n_(50003, "print", lambda: print), _n_(50004, "array_num", lambda: array_num)[_n_(50005, "i", lambda: i)], end=' ')
    _l_(50007)
_c_(50010, _n_(50009, "print", lambda: print), '\nAfter removing duplicate elements from the said array:')
_l_(50011)
result = _c_(50017, _a_(50013, _n_(50012, "arr", lambda: arr), "array"), 'i', _c_(50016, _n_(50014, "test", lambda: test), _n_(50015, "array_num", lambda: array_num)))
_l_(50018)
for i in _c_(50023, _n_(50019, "range", lambda: range), _c_(50022, _n_(50020, "len", lambda: len), _n_(50021, "result", lambda: result))):
    _l_(50029)

    _c_(50027, _n_(50024, "print", lambda: print), _n_(50025, "result", lambda: result)[_n_(50026, "i", lambda: i)], end=' ')
    _l_(50028)