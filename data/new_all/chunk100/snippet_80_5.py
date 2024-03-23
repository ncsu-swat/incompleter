# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(81873)

    nums = _c_(81831, _n_(81827, "list", lambda: list), _c_(81830, _n_(81828, "str", lambda: str), _n_(81829, "n", lambda: n)))
    _l_(81832)
    for i in _c_(81837, _n_(81833, "range", lambda: range), _c_(81836, _n_(81834, "len", lambda: len), _n_(81835, "nums", lambda: nums)) - 2, -1, -1):
        _l_(81871)

        if _n_(81838, "nums", lambda: nums)[_n_(81839, "i", lambda: i)] < _n_(81840, "nums", lambda: nums)[_n_(81841, "i", lambda: i) + 1]:
            _l_(81870)

            y = _c_(81848, _n_(81842, "min", lambda: min), _c_(81847, _n_(81843, "filter", lambda: filter), lambda x: _n_(81844, "x", lambda: x) > _n_(81845, "z", lambda: z)[0], _n_(81846, "z", lambda: z)))
            _l_(81849)
            _c_(81853, _a_(81851, _n_(81850, "z", lambda: z), "remove"), _n_(81852, "y", lambda: y))
            _l_(81854)
            _c_(81857, _a_(81856, _n_(81855, "z", lambda: z), "sort"))
            _l_(81858)
            _n_(81859, "nums", lambda: nums)[_n_(81860, "i", lambda: i):] = [_n_(81861, "y", lambda: y)] + _n_(81862, "z", lambda: z)
            _l_(81863)
            aux = _c_(81868, _n_(81864, "int", lambda: int), _c_(81867, _a_(81865, '', "join"), _n_(81866, "nums", lambda: nums)))
            _l_(81869)
            return aux
    aux = False
    _l_(81872)
    return aux
n = 12
_l_(81874)
_c_(81877, _n_(81875, "print", lambda: print), 'Original number:', _n_(81876, "n", lambda: n))
_l_(81878)
_c_(81883, _n_(81879, "print", lambda: print), 'Next bigger number:', _c_(81882, _n_(81880, "rearrange_bigger", lambda: rearrange_bigger), _n_(81881, "n", lambda: n)))
_l_(81884)
n = 10
_l_(81885)
_c_(81888, _n_(81886, "print", lambda: print), '\nOriginal number:', _n_(81887, "n", lambda: n))
_l_(81889)
_c_(81894, _n_(81890, "print", lambda: print), 'Next bigger number:', _c_(81893, _n_(81891, "rearrange_bigger", lambda: rearrange_bigger), _n_(81892, "n", lambda: n)))
_l_(81895)
n = 201
_l_(81896)
_c_(81899, _n_(81897, "print", lambda: print), '\nOriginal number:', _n_(81898, "n", lambda: n))
_l_(81900)
_c_(81905, _n_(81901, "print", lambda: print), 'Next bigger number:', _c_(81904, _n_(81902, "rearrange_bigger", lambda: rearrange_bigger), _n_(81903, "n", lambda: n)))
_l_(81906)
n = 102
_l_(81907)
_c_(81910, _n_(81908, "print", lambda: print), '\nOriginal number:', _n_(81909, "n", lambda: n))
_l_(81911)
_c_(81916, _n_(81912, "print", lambda: print), 'Next bigger number:', _c_(81915, _n_(81913, "rearrange_bigger", lambda: rearrange_bigger), _n_(81914, "n", lambda: n)))
_l_(81917)
n = 445
_l_(81918)
_c_(81921, _n_(81919, "print", lambda: print), '\nOriginal number:', _n_(81920, "n", lambda: n))
_l_(81922)
_c_(81927, _n_(81923, "print", lambda: print), 'Next bigger number:', _c_(81926, _n_(81924, "rearrange_bigger", lambda: rearrange_bigger), _n_(81925, "n", lambda: n)))
_l_(81928)