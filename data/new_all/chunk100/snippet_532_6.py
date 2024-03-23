# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def comb_sort(nums):
    _l_(53956)

    shrink_fact = 1.3
    _l_(53910)
    gaps = _c_(53913, _n_(53911, "len", lambda: len), _n_(53912, "nums", lambda: nums))
    _l_(53914)
    swapped = True
    _l_(53915)
    i = 0
    _l_(53916)
    while _n_(53917, "gaps", lambda: gaps) > 1 or _n_(53918, "swapped", lambda: swapped):
        _l_(53953)

        gaps = _c_(53924, _n_(53919, "int", lambda: int), _c_(53922, _n_(53920, "float", lambda: float), _n_(53921, "gaps", lambda: gaps)) / _n_(53923, "shrink_fact", lambda: shrink_fact))
        _l_(53925)
        swapped = False
        _l_(53926)
        i = 0
        _l_(53927)
        while _n_(53928, "gaps", lambda: gaps) + _n_(53929, "i", lambda: i) < _c_(53932, _n_(53930, "len", lambda: len), _n_(53931, "nums", lambda: nums)):
            _l_(53952)

            if _n_(53933, "nums", lambda: nums)[_n_(53934, "i", lambda: i)] > _n_(53935, "nums", lambda: nums)[_n_(53936, "i", lambda: i) + _n_(53937, "gaps", lambda: gaps)]:
                _l_(53950)

                (_n_(53938, "nums", lambda: nums)[_n_(53939, "i", lambda: i)], _n_(53940, "nums", lambda: nums)[_n_(53941, "i", lambda: i) + _n_(53942, "gaps", lambda: gaps)]) = (_n_(53943, "nums", lambda: nums)[_n_(53944, "i", lambda: i) + _n_(53945, "gaps", lambda: gaps)], _n_(53946, "nums", lambda: nums)[_n_(53947, "i", lambda: i)])
                _l_(53948)
                swapped = True
                _l_(53949)
            i += 1
            _l_(53951)
    aux = _n_(53954, "nums", lambda: nums)
    _l_(53955)
    return aux
nums = [_c_(53959, _n_(53957, "int", lambda: int), _n_(53958, "item", lambda: item)) for item in _c_(53962, _a_(53961, _n_(53960, "num1", lambda: num1), "split"), ',')]
_l_(53963)
_c_(53968, _n_(53964, "print", lambda: print), _c_(53967, _n_(53965, "comb_sort", lambda: comb_sort), _n_(53966, "nums", lambda: nums)))
_l_(53969)