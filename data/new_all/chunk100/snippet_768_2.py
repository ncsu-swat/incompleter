# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def shift_first_last(lst):
    _l_(77986)

    x = _c_(77969, _a_(77968, _n_(77967, "lst", lambda: lst), "pop"), 0)
    _l_(77970)
    _c_(77974, _a_(77972, _n_(77971, "lst", lambda: lst), "insert"), 0, _n_(77973, "y", lambda: y))
    _l_(77975)
    _c_(77982, _a_(77977, _n_(77976, "lst", lambda: lst), "insert"), _c_(77980, _n_(77978, "len", lambda: len), _n_(77979, "lst", lambda: lst)), _n_(77981, "x", lambda: x))
    _l_(77983)
    aux = _n_(77984, "lst", lambda: lst)
    _l_(77985)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(77987)
_c_(77989, _n_(77988, "print", lambda: print), 'Original list:')
_l_(77990)
_c_(77993, _n_(77991, "print", lambda: print), _n_(77992, "nums", lambda: nums))
_l_(77994)
_c_(77996, _n_(77995, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(77997)
_c_(78002, _n_(77998, "print", lambda: print), _c_(78001, _n_(77999, "shift_first_last", lambda: shift_first_last), _n_(78000, "nums", lambda: nums)))
_l_(78003)
chars = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
_l_(78004)
_c_(78006, _n_(78005, "print", lambda: print), '\nOriginal list:')
_l_(78007)
_c_(78010, _n_(78008, "print", lambda: print), _n_(78009, "chars", lambda: chars))
_l_(78011)
_c_(78013, _n_(78012, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(78014)
_c_(78019, _n_(78015, "print", lambda: print), _c_(78018, _n_(78016, "shift_first_last", lambda: shift_first_last), _n_(78017, "chars", lambda: chars)))
_l_(78020)