# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(82082)

    nums = _c_(82037, _n_(82033, "list", lambda: list), _c_(82036, _n_(82034, "str", lambda: str), _n_(82035, "n", lambda: n)))
    _l_(82038)
    for i in _c_(82043, _n_(82039, "range", lambda: range), _c_(82042, _n_(82040, "len", lambda: len), _n_(82041, "nums", lambda: nums)) - 2, -1, -1):
        _l_(82080)

        if _n_(82044, "nums", lambda: nums)[_n_(82045, "i", lambda: i)] < _n_(82046, "nums", lambda: nums)[_n_(82047, "i", lambda: i) + 1]:
            _l_(82079)

            z = _n_(82048, "nums", lambda: nums)[_n_(82049, "i", lambda: i):]
            _l_(82050)
            y = _c_(82057, _n_(82051, "min", lambda: min), _c_(82056, _n_(82052, "filter", lambda: filter), lambda x: _n_(82053, "x", lambda: x) > _n_(82054, "z", lambda: z)[0], _n_(82055, "z", lambda: z)))
            _l_(82058)
            _c_(82062, _a_(82060, _n_(82059, "z", lambda: z), "remove"), _n_(82061, "y", lambda: y))
            _l_(82063)
            _c_(82066, _a_(82065, _n_(82064, "z", lambda: z), "sort"))
            _l_(82067)
            _n_(82068, "nums", lambda: nums)[_n_(82069, "i", lambda: i):] = [_n_(82070, "y", lambda: y)] + _n_(82071, "z", lambda: z)
            _l_(82072)
            aux = _c_(82077, _n_(82073, "int", lambda: int), _c_(82076, _a_(82074, '', "join"), _n_(82075, "nums", lambda: nums)))
            _l_(82078)
            return aux
    aux = False
    _l_(82081)
    return aux
_c_(82085, _n_(82083, "print", lambda: print), 'Original number:', _n_(82084, "n", lambda: n))
_l_(82086)
_c_(82091, _n_(82087, "print", lambda: print), 'Next bigger number:', _c_(82090, _n_(82088, "rearrange_bigger", lambda: rearrange_bigger), _n_(82089, "n", lambda: n)))
_l_(82092)
n = 10
_l_(82093)
_c_(82096, _n_(82094, "print", lambda: print), '\nOriginal number:', _n_(82095, "n", lambda: n))
_l_(82097)
_c_(82102, _n_(82098, "print", lambda: print), 'Next bigger number:', _c_(82101, _n_(82099, "rearrange_bigger", lambda: rearrange_bigger), _n_(82100, "n", lambda: n)))
_l_(82103)
n = 201
_l_(82104)
_c_(82107, _n_(82105, "print", lambda: print), '\nOriginal number:', _n_(82106, "n", lambda: n))
_l_(82108)
_c_(82113, _n_(82109, "print", lambda: print), 'Next bigger number:', _c_(82112, _n_(82110, "rearrange_bigger", lambda: rearrange_bigger), _n_(82111, "n", lambda: n)))
_l_(82114)
n = 102
_l_(82115)
_c_(82118, _n_(82116, "print", lambda: print), '\nOriginal number:', _n_(82117, "n", lambda: n))
_l_(82119)
_c_(82124, _n_(82120, "print", lambda: print), 'Next bigger number:', _c_(82123, _n_(82121, "rearrange_bigger", lambda: rearrange_bigger), _n_(82122, "n", lambda: n)))
_l_(82125)
n = 445
_l_(82126)
_c_(82129, _n_(82127, "print", lambda: print), '\nOriginal number:', _n_(82128, "n", lambda: n))
_l_(82130)
_c_(82135, _n_(82131, "print", lambda: print), 'Next bigger number:', _c_(82134, _n_(82132, "rearrange_bigger", lambda: rearrange_bigger), _n_(82133, "n", lambda: n)))
_l_(82136)