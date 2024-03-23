# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(53706)

    shrink_fact = 1.3
    _l_(53660)
    gaps = _c_(53663, _n_(53661, "len", lambda: len), _n_(53662, "nums", lambda: nums))
    _l_(53664)
    swapped = True
    _l_(53665)
    i = 0
    _l_(53666)
    while _n_(53667, "gaps", lambda: gaps) > 1 or _n_(53668, "swapped", lambda: swapped):
        _l_(53703)

        gaps = _c_(53674, _n_(53669, "int", lambda: int), _c_(53672, _n_(53670, "float", lambda: float), _n_(53671, "gaps", lambda: gaps)) / _n_(53673, "shrink_fact", lambda: shrink_fact))
        _l_(53675)
        swapped = False
        _l_(53676)
        i = 0
        _l_(53677)
        while _n_(53678, "gaps", lambda: gaps) + _n_(53679, "i", lambda: i) < _c_(53682, _n_(53680, "len", lambda: len), _n_(53681, "nums", lambda: nums)):
            _l_(53702)

            if _n_(53683, "nums", lambda: nums)[_n_(53684, "i", lambda: i)] > _n_(53685, "nums", lambda: nums)[_n_(53686, "i", lambda: i) + _n_(53687, "gaps", lambda: gaps)]:
                _l_(53700)

                (_n_(53688, "nums", lambda: nums)[_n_(53689, "i", lambda: i)], _n_(53690, "nums", lambda: nums)[_n_(53691, "i", lambda: i) + _n_(53692, "gaps", lambda: gaps)]) = (_n_(53693, "nums", lambda: nums)[_n_(53694, "i", lambda: i) + _n_(53695, "gaps", lambda: gaps)], _n_(53696, "nums", lambda: nums)[_n_(53697, "i", lambda: i)])
                _l_(53698)
                swapped = True
                _l_(53699)
            i += 1
            _l_(53701)
    aux = _n_(53704, "nums", lambda: nums)
    _l_(53705)
    return aux
num1 = _c_(53710, _a_(53709, _c_(53708, _n_(53707, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(53711)
_c_(53716, _n_(53712, "print", lambda: print), _c_(53715, _n_(53713, "comb_sort", lambda: comb_sort), _n_(53714, "nums", lambda: nums)))
_l_(53717)