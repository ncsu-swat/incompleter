# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(81459)

    nums = _c_(81422, _n_(81418, "list", lambda: list), _c_(81421, _n_(81419, "str", lambda: str), _n_(81420, "n", lambda: n)))
    _l_(81423)
    for i in _c_(81428, _n_(81424, "range", lambda: range), _c_(81427, _n_(81425, "len", lambda: len), _n_(81426, "nums", lambda: nums)) - 2, -1, -1):
        _l_(81457)

        if _n_(81429, "nums", lambda: nums)[_n_(81430, "i", lambda: i)] < _n_(81431, "nums", lambda: nums)[_n_(81432, "i", lambda: i) + 1]:
            _l_(81456)

            z = _n_(81433, "nums", lambda: nums)[_n_(81434, "i", lambda: i):]
            _l_(81435)
            _c_(81439, _a_(81437, _n_(81436, "z", lambda: z), "remove"), _n_(81438, "y", lambda: y))
            _l_(81440)
            _c_(81443, _a_(81442, _n_(81441, "z", lambda: z), "sort"))
            _l_(81444)
            _n_(81445, "nums", lambda: nums)[_n_(81446, "i", lambda: i):] = [_n_(81447, "y", lambda: y)] + _n_(81448, "z", lambda: z)
            _l_(81449)
            aux = _c_(81454, _n_(81450, "int", lambda: int), _c_(81453, _a_(81451, '', "join"), _n_(81452, "nums", lambda: nums)))
            _l_(81455)
            return aux
    aux = False
    _l_(81458)
    return aux
n = 12
_l_(81460)
_c_(81463, _n_(81461, "print", lambda: print), 'Original number:', _n_(81462, "n", lambda: n))
_l_(81464)
_c_(81469, _n_(81465, "print", lambda: print), 'Next bigger number:', _c_(81468, _n_(81466, "rearrange_bigger", lambda: rearrange_bigger), _n_(81467, "n", lambda: n)))
_l_(81470)
n = 10
_l_(81471)
_c_(81474, _n_(81472, "print", lambda: print), '\nOriginal number:', _n_(81473, "n", lambda: n))
_l_(81475)
_c_(81480, _n_(81476, "print", lambda: print), 'Next bigger number:', _c_(81479, _n_(81477, "rearrange_bigger", lambda: rearrange_bigger), _n_(81478, "n", lambda: n)))
_l_(81481)
n = 201
_l_(81482)
_c_(81485, _n_(81483, "print", lambda: print), '\nOriginal number:', _n_(81484, "n", lambda: n))
_l_(81486)
_c_(81491, _n_(81487, "print", lambda: print), 'Next bigger number:', _c_(81490, _n_(81488, "rearrange_bigger", lambda: rearrange_bigger), _n_(81489, "n", lambda: n)))
_l_(81492)
n = 102
_l_(81493)
_c_(81496, _n_(81494, "print", lambda: print), '\nOriginal number:', _n_(81495, "n", lambda: n))
_l_(81497)
_c_(81502, _n_(81498, "print", lambda: print), 'Next bigger number:', _c_(81501, _n_(81499, "rearrange_bigger", lambda: rearrange_bigger), _n_(81500, "n", lambda: n)))
_l_(81503)
n = 445
_l_(81504)
_c_(81507, _n_(81505, "print", lambda: print), '\nOriginal number:', _n_(81506, "n", lambda: n))
_l_(81508)
_c_(81513, _n_(81509, "print", lambda: print), 'Next bigger number:', _c_(81512, _n_(81510, "rearrange_bigger", lambda: rearrange_bigger), _n_(81511, "n", lambda: n)))
_l_(81514)