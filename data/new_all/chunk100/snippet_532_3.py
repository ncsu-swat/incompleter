# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(53763)

    gaps = _c_(53720, _n_(53718, "len", lambda: len), _n_(53719, "nums", lambda: nums))
    _l_(53721)
    swapped = True
    _l_(53722)
    i = 0
    _l_(53723)
    while _n_(53724, "gaps", lambda: gaps) > 1 or _n_(53725, "swapped", lambda: swapped):
        _l_(53760)

        gaps = _c_(53731, _n_(53726, "int", lambda: int), _c_(53729, _n_(53727, "float", lambda: float), _n_(53728, "gaps", lambda: gaps)) / _n_(53730, "shrink_fact", lambda: shrink_fact))
        _l_(53732)
        swapped = False
        _l_(53733)
        i = 0
        _l_(53734)
        while _n_(53735, "gaps", lambda: gaps) + _n_(53736, "i", lambda: i) < _c_(53739, _n_(53737, "len", lambda: len), _n_(53738, "nums", lambda: nums)):
            _l_(53759)

            if _n_(53740, "nums", lambda: nums)[_n_(53741, "i", lambda: i)] > _n_(53742, "nums", lambda: nums)[_n_(53743, "i", lambda: i) + _n_(53744, "gaps", lambda: gaps)]:
                _l_(53757)

                (_n_(53745, "nums", lambda: nums)[_n_(53746, "i", lambda: i)], _n_(53747, "nums", lambda: nums)[_n_(53748, "i", lambda: i) + _n_(53749, "gaps", lambda: gaps)]) = (_n_(53750, "nums", lambda: nums)[_n_(53751, "i", lambda: i) + _n_(53752, "gaps", lambda: gaps)], _n_(53753, "nums", lambda: nums)[_n_(53754, "i", lambda: i)])
                _l_(53755)
                swapped = True
                _l_(53756)
            i += 1
            _l_(53758)
    aux = _n_(53761, "nums", lambda: nums)
    _l_(53762)
    return aux
num1 = _c_(53767, _a_(53766, _c_(53765, _n_(53764, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(53768)
nums = [_c_(53771, _n_(53769, "int", lambda: int), _n_(53770, "item", lambda: item)) for item in _c_(53774, _a_(53773, _n_(53772, "num1", lambda: num1), "split"), ',')]
_l_(53775)
_c_(53780, _n_(53776, "print", lambda: print), _c_(53779, _n_(53777, "comb_sort", lambda: comb_sort), _n_(53778, "nums", lambda: nums)))
_l_(53781)