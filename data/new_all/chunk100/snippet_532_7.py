# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(54009)

    shrink_fact = 1.3
    _l_(53970)
    gaps = _c_(53973, _n_(53971, "len", lambda: len), _n_(53972, "nums", lambda: nums))
    _l_(53974)
    swapped = True
    _l_(53975)
    i = 0
    _l_(53976)
    while _n_(53977, "gaps", lambda: gaps) > 1 or _n_(53978, "swapped", lambda: swapped):
        _l_(54006)

        swapped = False
        _l_(53979)
        i = 0
        _l_(53980)
        while _n_(53981, "gaps", lambda: gaps) + _n_(53982, "i", lambda: i) < _c_(53985, _n_(53983, "len", lambda: len), _n_(53984, "nums", lambda: nums)):
            _l_(54005)

            if _n_(53986, "nums", lambda: nums)[_n_(53987, "i", lambda: i)] > _n_(53988, "nums", lambda: nums)[_n_(53989, "i", lambda: i) + _n_(53990, "gaps", lambda: gaps)]:
                _l_(54003)

                (_n_(53991, "nums", lambda: nums)[_n_(53992, "i", lambda: i)], _n_(53993, "nums", lambda: nums)[_n_(53994, "i", lambda: i) + _n_(53995, "gaps", lambda: gaps)]) = (_n_(53996, "nums", lambda: nums)[_n_(53997, "i", lambda: i) + _n_(53998, "gaps", lambda: gaps)], _n_(53999, "nums", lambda: nums)[_n_(54000, "i", lambda: i)])
                _l_(54001)
                swapped = True
                _l_(54002)
            i += 1
            _l_(54004)
    aux = _n_(54007, "nums", lambda: nums)
    _l_(54008)
    return aux
num1 = _c_(54013, _a_(54012, _c_(54011, _n_(54010, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(54014)
nums = [_c_(54017, _n_(54015, "int", lambda: int), _n_(54016, "item", lambda: item)) for item in _c_(54020, _a_(54019, _n_(54018, "num1", lambda: num1), "split"), ',')]
_l_(54021)
_c_(54026, _n_(54022, "print", lambda: print), _c_(54025, _n_(54023, "comb_sort", lambda: comb_sort), _n_(54024, "nums", lambda: nums)))
_l_(54027)