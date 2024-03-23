# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(81978)

    nums = _c_(81933, _n_(81929, "list", lambda: list), _c_(81932, _n_(81930, "str", lambda: str), _n_(81931, "n", lambda: n)))
    _l_(81934)
    for i in _c_(81939, _n_(81935, "range", lambda: range), _c_(81938, _n_(81936, "len", lambda: len), _n_(81937, "nums", lambda: nums)) - 2, -1, -1):
        _l_(81976)

        if _n_(81940, "nums", lambda: nums)[_n_(81941, "i", lambda: i)] < _n_(81942, "nums", lambda: nums)[_n_(81943, "i", lambda: i) + 1]:
            _l_(81975)

            z = _n_(81944, "nums", lambda: nums)[_n_(81945, "i", lambda: i):]
            _l_(81946)
            y = _c_(81953, _n_(81947, "min", lambda: min), _c_(81952, _n_(81948, "filter", lambda: filter), lambda x: _n_(81949, "x", lambda: x) > _n_(81950, "z", lambda: z)[0], _n_(81951, "z", lambda: z)))
            _l_(81954)
            _c_(81958, _a_(81956, _n_(81955, "z", lambda: z), "remove"), _n_(81957, "y", lambda: y))
            _l_(81959)
            _c_(81962, _a_(81961, _n_(81960, "z", lambda: z), "sort"))
            _l_(81963)
            _n_(81964, "nums", lambda: nums)[_n_(81965, "i", lambda: i):] = [_n_(81966, "y", lambda: y)] + _n_(81967, "z", lambda: z)
            _l_(81968)
            aux = _c_(81973, _n_(81969, "int", lambda: int), _c_(81972, _a_(81970, '', "join"), _n_(81971, "nums", lambda: nums)))
            _l_(81974)
            return aux
    aux = False
    _l_(81977)
    return aux
n = 12
_l_(81979)
_c_(81982, _n_(81980, "print", lambda: print), 'Original number:', _n_(81981, "n", lambda: n))
_l_(81983)
_c_(81988, _n_(81984, "print", lambda: print), 'Next bigger number:', _c_(81987, _n_(81985, "rearrange_bigger", lambda: rearrange_bigger), _n_(81986, "n", lambda: n)))
_l_(81989)
_c_(81992, _n_(81990, "print", lambda: print), '\nOriginal number:', _n_(81991, "n", lambda: n))
_l_(81993)
_c_(81998, _n_(81994, "print", lambda: print), 'Next bigger number:', _c_(81997, _n_(81995, "rearrange_bigger", lambda: rearrange_bigger), _n_(81996, "n", lambda: n)))
_l_(81999)
n = 201
_l_(82000)
_c_(82003, _n_(82001, "print", lambda: print), '\nOriginal number:', _n_(82002, "n", lambda: n))
_l_(82004)
_c_(82009, _n_(82005, "print", lambda: print), 'Next bigger number:', _c_(82008, _n_(82006, "rearrange_bigger", lambda: rearrange_bigger), _n_(82007, "n", lambda: n)))
_l_(82010)
n = 102
_l_(82011)
_c_(82014, _n_(82012, "print", lambda: print), '\nOriginal number:', _n_(82013, "n", lambda: n))
_l_(82015)
_c_(82020, _n_(82016, "print", lambda: print), 'Next bigger number:', _c_(82019, _n_(82017, "rearrange_bigger", lambda: rearrange_bigger), _n_(82018, "n", lambda: n)))
_l_(82021)
n = 445
_l_(82022)
_c_(82025, _n_(82023, "print", lambda: print), '\nOriginal number:', _n_(82024, "n", lambda: n))
_l_(82026)
_c_(82031, _n_(82027, "print", lambda: print), 'Next bigger number:', _c_(82030, _n_(82028, "rearrange_bigger", lambda: rearrange_bigger), _n_(82029, "n", lambda: n)))
_l_(82032)