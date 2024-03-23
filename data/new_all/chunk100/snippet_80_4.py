# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(81772)

    nums = _c_(81727, _n_(81723, "list", lambda: list), _c_(81726, _n_(81724, "str", lambda: str), _n_(81725, "n", lambda: n)))
    _l_(81728)
    for i in _c_(81733, _n_(81729, "range", lambda: range), _c_(81732, _n_(81730, "len", lambda: len), _n_(81731, "nums", lambda: nums)) - 2, -1, -1):
        _l_(81770)

        if _n_(81734, "nums", lambda: nums)[_n_(81735, "i", lambda: i)] < _n_(81736, "nums", lambda: nums)[_n_(81737, "i", lambda: i) + 1]:
            _l_(81769)

            z = _n_(81738, "nums", lambda: nums)[_n_(81739, "i", lambda: i):]
            _l_(81740)
            y = _c_(81747, _n_(81741, "min", lambda: min), _c_(81746, _n_(81742, "filter", lambda: filter), lambda x: _n_(81743, "x", lambda: x) > _n_(81744, "z", lambda: z)[0], _n_(81745, "z", lambda: z)))
            _l_(81748)
            _c_(81752, _a_(81750, _n_(81749, "z", lambda: z), "remove"), _n_(81751, "y", lambda: y))
            _l_(81753)
            _c_(81756, _a_(81755, _n_(81754, "z", lambda: z), "sort"))
            _l_(81757)
            _n_(81758, "nums", lambda: nums)[_n_(81759, "i", lambda: i):] = [_n_(81760, "y", lambda: y)] + _n_(81761, "z", lambda: z)
            _l_(81762)
            aux = _c_(81767, _n_(81763, "int", lambda: int), _c_(81766, _a_(81764, '', "join"), _n_(81765, "nums", lambda: nums)))
            _l_(81768)
            return aux
    aux = False
    _l_(81771)
    return aux
n = 12
_l_(81773)
_c_(81776, _n_(81774, "print", lambda: print), 'Original number:', _n_(81775, "n", lambda: n))
_l_(81777)
_c_(81782, _n_(81778, "print", lambda: print), 'Next bigger number:', _c_(81781, _n_(81779, "rearrange_bigger", lambda: rearrange_bigger), _n_(81780, "n", lambda: n)))
_l_(81783)
n = 10
_l_(81784)
_c_(81787, _n_(81785, "print", lambda: print), '\nOriginal number:', _n_(81786, "n", lambda: n))
_l_(81788)
_c_(81793, _n_(81789, "print", lambda: print), 'Next bigger number:', _c_(81792, _n_(81790, "rearrange_bigger", lambda: rearrange_bigger), _n_(81791, "n", lambda: n)))
_l_(81794)
n = 201
_l_(81795)
_c_(81798, _n_(81796, "print", lambda: print), '\nOriginal number:', _n_(81797, "n", lambda: n))
_l_(81799)
_c_(81804, _n_(81800, "print", lambda: print), 'Next bigger number:', _c_(81803, _n_(81801, "rearrange_bigger", lambda: rearrange_bigger), _n_(81802, "n", lambda: n)))
_l_(81805)
_c_(81808, _n_(81806, "print", lambda: print), '\nOriginal number:', _n_(81807, "n", lambda: n))
_l_(81809)
_c_(81814, _n_(81810, "print", lambda: print), 'Next bigger number:', _c_(81813, _n_(81811, "rearrange_bigger", lambda: rearrange_bigger), _n_(81812, "n", lambda: n)))
_l_(81815)
n = 445
_l_(81816)
_c_(81819, _n_(81817, "print", lambda: print), '\nOriginal number:', _n_(81818, "n", lambda: n))
_l_(81820)
_c_(81825, _n_(81821, "print", lambda: print), 'Next bigger number:', _c_(81824, _n_(81822, "rearrange_bigger", lambda: rearrange_bigger), _n_(81823, "n", lambda: n)))
_l_(81826)