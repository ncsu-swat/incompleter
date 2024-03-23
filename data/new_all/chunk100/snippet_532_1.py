# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(53641)

    shrink_fact = 1.3
    _l_(53596)
    gaps = _c_(53599, _n_(53597, "len", lambda: len), _n_(53598, "nums", lambda: nums))
    _l_(53600)
    swapped = True
    _l_(53601)
    i = 0
    _l_(53602)
    while _n_(53603, "gaps", lambda: gaps) > 1 or _n_(53604, "swapped", lambda: swapped):
        _l_(53638)

        gaps = _c_(53610, _n_(53605, "int", lambda: int), _c_(53608, _n_(53606, "float", lambda: float), _n_(53607, "gaps", lambda: gaps)) / _n_(53609, "shrink_fact", lambda: shrink_fact))
        _l_(53611)
        i = 0
        _l_(53612)
        while _n_(53613, "gaps", lambda: gaps) + _n_(53614, "i", lambda: i) < _c_(53617, _n_(53615, "len", lambda: len), _n_(53616, "nums", lambda: nums)):
            _l_(53637)

            if _n_(53618, "nums", lambda: nums)[_n_(53619, "i", lambda: i)] > _n_(53620, "nums", lambda: nums)[_n_(53621, "i", lambda: i) + _n_(53622, "gaps", lambda: gaps)]:
                _l_(53635)

                (_n_(53623, "nums", lambda: nums)[_n_(53624, "i", lambda: i)], _n_(53625, "nums", lambda: nums)[_n_(53626, "i", lambda: i) + _n_(53627, "gaps", lambda: gaps)]) = (_n_(53628, "nums", lambda: nums)[_n_(53629, "i", lambda: i) + _n_(53630, "gaps", lambda: gaps)], _n_(53631, "nums", lambda: nums)[_n_(53632, "i", lambda: i)])
                _l_(53633)
                swapped = True
                _l_(53634)
            i += 1
            _l_(53636)
    aux = _n_(53639, "nums", lambda: nums)
    _l_(53640)
    return aux
num1 = _c_(53645, _a_(53644, _c_(53643, _n_(53642, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(53646)
nums = [_c_(53649, _n_(53647, "int", lambda: int), _n_(53648, "item", lambda: item)) for item in _c_(53652, _a_(53651, _n_(53650, "num1", lambda: num1), "split"), ',')]
_l_(53653)
_c_(53658, _n_(53654, "print", lambda: print), _c_(53657, _n_(53655, "comb_sort", lambda: comb_sort), _n_(53656, "nums", lambda: nums)))
_l_(53659)