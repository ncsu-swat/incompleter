# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(54070)

    shrink_fact = 1.3
    _l_(54028)
    swapped = True
    _l_(54029)
    i = 0
    _l_(54030)
    while _n_(54031, "gaps", lambda: gaps) > 1 or _n_(54032, "swapped", lambda: swapped):
        _l_(54067)

        gaps = _c_(54038, _n_(54033, "int", lambda: int), _c_(54036, _n_(54034, "float", lambda: float), _n_(54035, "gaps", lambda: gaps)) / _n_(54037, "shrink_fact", lambda: shrink_fact))
        _l_(54039)
        swapped = False
        _l_(54040)
        i = 0
        _l_(54041)
        while _n_(54042, "gaps", lambda: gaps) + _n_(54043, "i", lambda: i) < _c_(54046, _n_(54044, "len", lambda: len), _n_(54045, "nums", lambda: nums)):
            _l_(54066)

            if _n_(54047, "nums", lambda: nums)[_n_(54048, "i", lambda: i)] > _n_(54049, "nums", lambda: nums)[_n_(54050, "i", lambda: i) + _n_(54051, "gaps", lambda: gaps)]:
                _l_(54064)

                (_n_(54052, "nums", lambda: nums)[_n_(54053, "i", lambda: i)], _n_(54054, "nums", lambda: nums)[_n_(54055, "i", lambda: i) + _n_(54056, "gaps", lambda: gaps)]) = (_n_(54057, "nums", lambda: nums)[_n_(54058, "i", lambda: i) + _n_(54059, "gaps", lambda: gaps)], _n_(54060, "nums", lambda: nums)[_n_(54061, "i", lambda: i)])
                _l_(54062)
                swapped = True
                _l_(54063)
            i += 1
            _l_(54065)
    aux = _n_(54068, "nums", lambda: nums)
    _l_(54069)
    return aux
num1 = _c_(54074, _a_(54073, _c_(54072, _n_(54071, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(54075)
nums = [_c_(54078, _n_(54076, "int", lambda: int), _n_(54077, "item", lambda: item)) for item in _c_(54081, _a_(54080, _n_(54079, "num1", lambda: num1), "split"), ',')]
_l_(54082)
_c_(54087, _n_(54083, "print", lambda: print), _c_(54086, _n_(54084, "comb_sort", lambda: comb_sort), _n_(54085, "nums", lambda: nums)))
_l_(54088)