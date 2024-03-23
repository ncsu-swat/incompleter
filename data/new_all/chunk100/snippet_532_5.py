# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(53891)

    shrink_fact = 1.3
    _l_(53846)
    gaps = _c_(53849, _n_(53847, "len", lambda: len), _n_(53848, "nums", lambda: nums))
    _l_(53850)
    i = 0
    _l_(53851)
    while _n_(53852, "gaps", lambda: gaps) > 1 or _n_(53853, "swapped", lambda: swapped):
        _l_(53888)

        gaps = _c_(53859, _n_(53854, "int", lambda: int), _c_(53857, _n_(53855, "float", lambda: float), _n_(53856, "gaps", lambda: gaps)) / _n_(53858, "shrink_fact", lambda: shrink_fact))
        _l_(53860)
        swapped = False
        _l_(53861)
        i = 0
        _l_(53862)
        while _n_(53863, "gaps", lambda: gaps) + _n_(53864, "i", lambda: i) < _c_(53867, _n_(53865, "len", lambda: len), _n_(53866, "nums", lambda: nums)):
            _l_(53887)

            if _n_(53868, "nums", lambda: nums)[_n_(53869, "i", lambda: i)] > _n_(53870, "nums", lambda: nums)[_n_(53871, "i", lambda: i) + _n_(53872, "gaps", lambda: gaps)]:
                _l_(53885)

                (_n_(53873, "nums", lambda: nums)[_n_(53874, "i", lambda: i)], _n_(53875, "nums", lambda: nums)[_n_(53876, "i", lambda: i) + _n_(53877, "gaps", lambda: gaps)]) = (_n_(53878, "nums", lambda: nums)[_n_(53879, "i", lambda: i) + _n_(53880, "gaps", lambda: gaps)], _n_(53881, "nums", lambda: nums)[_n_(53882, "i", lambda: i)])
                _l_(53883)
                swapped = True
                _l_(53884)
            i += 1
            _l_(53886)
    aux = _n_(53889, "nums", lambda: nums)
    _l_(53890)
    return aux
num1 = _c_(53895, _a_(53894, _c_(53893, _n_(53892, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(53896)
nums = [_c_(53899, _n_(53897, "int", lambda: int), _n_(53898, "item", lambda: item)) for item in _c_(53902, _a_(53901, _n_(53900, "num1", lambda: num1), "split"), ',')]
_l_(53903)
_c_(53908, _n_(53904, "print", lambda: print), _c_(53907, _n_(53905, "comb_sort", lambda: comb_sort), _n_(53906, "nums", lambda: nums)))
_l_(53909)