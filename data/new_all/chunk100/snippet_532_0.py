# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(53577)

    shrink_fact = 1.3
    _l_(53532)
    gaps = _c_(53535, _n_(53533, "len", lambda: len), _n_(53534, "nums", lambda: nums))
    _l_(53536)
    swapped = True
    _l_(53537)
    while _n_(53538, "gaps", lambda: gaps) > 1 or _n_(53539, "swapped", lambda: swapped):
        _l_(53574)

        gaps = _c_(53545, _n_(53540, "int", lambda: int), _c_(53543, _n_(53541, "float", lambda: float), _n_(53542, "gaps", lambda: gaps)) / _n_(53544, "shrink_fact", lambda: shrink_fact))
        _l_(53546)
        swapped = False
        _l_(53547)
        i = 0
        _l_(53548)
        while _n_(53549, "gaps", lambda: gaps) + _n_(53550, "i", lambda: i) < _c_(53553, _n_(53551, "len", lambda: len), _n_(53552, "nums", lambda: nums)):
            _l_(53573)

            if _n_(53554, "nums", lambda: nums)[_n_(53555, "i", lambda: i)] > _n_(53556, "nums", lambda: nums)[_n_(53557, "i", lambda: i) + _n_(53558, "gaps", lambda: gaps)]:
                _l_(53571)

                (_n_(53559, "nums", lambda: nums)[_n_(53560, "i", lambda: i)], _n_(53561, "nums", lambda: nums)[_n_(53562, "i", lambda: i) + _n_(53563, "gaps", lambda: gaps)]) = (_n_(53564, "nums", lambda: nums)[_n_(53565, "i", lambda: i) + _n_(53566, "gaps", lambda: gaps)], _n_(53567, "nums", lambda: nums)[_n_(53568, "i", lambda: i)])
                _l_(53569)
                swapped = True
                _l_(53570)
            i += 1
            _l_(53572)
    aux = _n_(53575, "nums", lambda: nums)
    _l_(53576)
    return aux
num1 = _c_(53581, _a_(53580, _c_(53579, _n_(53578, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(53582)
nums = [_c_(53585, _n_(53583, "int", lambda: int), _n_(53584, "item", lambda: item)) for item in _c_(53588, _a_(53587, _n_(53586, "num1", lambda: num1), "split"), ',')]
_l_(53589)
_c_(53594, _n_(53590, "print", lambda: print), _c_(53593, _n_(53591, "comb_sort", lambda: comb_sort), _n_(53592, "nums", lambda: nums)))
_l_(53595)