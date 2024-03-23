# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(53827)

    shrink_fact = 1.3
    _l_(53782)
    gaps = _c_(53785, _n_(53783, "len", lambda: len), _n_(53784, "nums", lambda: nums))
    _l_(53786)
    swapped = True
    _l_(53787)
    i = 0
    _l_(53788)
    while _n_(53789, "gaps", lambda: gaps) > 1 or _n_(53790, "swapped", lambda: swapped):
        _l_(53824)

        gaps = _c_(53796, _n_(53791, "int", lambda: int), _c_(53794, _n_(53792, "float", lambda: float), _n_(53793, "gaps", lambda: gaps)) / _n_(53795, "shrink_fact", lambda: shrink_fact))
        _l_(53797)
        swapped = False
        _l_(53798)
        while _n_(53799, "gaps", lambda: gaps) + _n_(53800, "i", lambda: i) < _c_(53803, _n_(53801, "len", lambda: len), _n_(53802, "nums", lambda: nums)):
            _l_(53823)

            if _n_(53804, "nums", lambda: nums)[_n_(53805, "i", lambda: i)] > _n_(53806, "nums", lambda: nums)[_n_(53807, "i", lambda: i) + _n_(53808, "gaps", lambda: gaps)]:
                _l_(53821)

                (_n_(53809, "nums", lambda: nums)[_n_(53810, "i", lambda: i)], _n_(53811, "nums", lambda: nums)[_n_(53812, "i", lambda: i) + _n_(53813, "gaps", lambda: gaps)]) = (_n_(53814, "nums", lambda: nums)[_n_(53815, "i", lambda: i) + _n_(53816, "gaps", lambda: gaps)], _n_(53817, "nums", lambda: nums)[_n_(53818, "i", lambda: i)])
                _l_(53819)
                swapped = True
                _l_(53820)
            i += 1
            _l_(53822)
    aux = _n_(53825, "nums", lambda: nums)
    _l_(53826)
    return aux
num1 = _c_(53831, _a_(53830, _c_(53829, _n_(53828, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(53832)
nums = [_c_(53835, _n_(53833, "int", lambda: int), _n_(53834, "item", lambda: item)) for item in _c_(53838, _a_(53837, _n_(53836, "num1", lambda: num1), "split"), ',')]
_l_(53839)
_c_(53844, _n_(53840, "print", lambda: print), _c_(53843, _n_(53841, "comb_sort", lambda: comb_sort), _n_(53842, "nums", lambda: nums)))
_l_(53845)