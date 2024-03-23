# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(81668)

    nums = _c_(81623, _n_(81619, "list", lambda: list), _c_(81622, _n_(81620, "str", lambda: str), _n_(81621, "n", lambda: n)))
    _l_(81624)
    for i in _c_(81629, _n_(81625, "range", lambda: range), _c_(81628, _n_(81626, "len", lambda: len), _n_(81627, "nums", lambda: nums)) - 2, -1, -1):
        _l_(81666)

        if _n_(81630, "nums", lambda: nums)[_n_(81631, "i", lambda: i)] < _n_(81632, "nums", lambda: nums)[_n_(81633, "i", lambda: i) + 1]:
            _l_(81665)

            z = _n_(81634, "nums", lambda: nums)[_n_(81635, "i", lambda: i):]
            _l_(81636)
            y = _c_(81643, _n_(81637, "min", lambda: min), _c_(81642, _n_(81638, "filter", lambda: filter), lambda x: _n_(81639, "x", lambda: x) > _n_(81640, "z", lambda: z)[0], _n_(81641, "z", lambda: z)))
            _l_(81644)
            _c_(81648, _a_(81646, _n_(81645, "z", lambda: z), "remove"), _n_(81647, "y", lambda: y))
            _l_(81649)
            _c_(81652, _a_(81651, _n_(81650, "z", lambda: z), "sort"))
            _l_(81653)
            _n_(81654, "nums", lambda: nums)[_n_(81655, "i", lambda: i):] = [_n_(81656, "y", lambda: y)] + _n_(81657, "z", lambda: z)
            _l_(81658)
            aux = _c_(81663, _n_(81659, "int", lambda: int), _c_(81662, _a_(81660, '', "join"), _n_(81661, "nums", lambda: nums)))
            _l_(81664)
            return aux
    aux = False
    _l_(81667)
    return aux
n = 12
_l_(81669)
_c_(81672, _n_(81670, "print", lambda: print), 'Original number:', _n_(81671, "n", lambda: n))
_l_(81673)
_c_(81678, _n_(81674, "print", lambda: print), 'Next bigger number:', _c_(81677, _n_(81675, "rearrange_bigger", lambda: rearrange_bigger), _n_(81676, "n", lambda: n)))
_l_(81679)
n = 10
_l_(81680)
_c_(81683, _n_(81681, "print", lambda: print), '\nOriginal number:', _n_(81682, "n", lambda: n))
_l_(81684)
_c_(81689, _n_(81685, "print", lambda: print), 'Next bigger number:', _c_(81688, _n_(81686, "rearrange_bigger", lambda: rearrange_bigger), _n_(81687, "n", lambda: n)))
_l_(81690)
_c_(81693, _n_(81691, "print", lambda: print), '\nOriginal number:', _n_(81692, "n", lambda: n))
_l_(81694)
_c_(81699, _n_(81695, "print", lambda: print), 'Next bigger number:', _c_(81698, _n_(81696, "rearrange_bigger", lambda: rearrange_bigger), _n_(81697, "n", lambda: n)))
_l_(81700)
n = 102
_l_(81701)
_c_(81704, _n_(81702, "print", lambda: print), '\nOriginal number:', _n_(81703, "n", lambda: n))
_l_(81705)
_c_(81710, _n_(81706, "print", lambda: print), 'Next bigger number:', _c_(81709, _n_(81707, "rearrange_bigger", lambda: rearrange_bigger), _n_(81708, "n", lambda: n)))
_l_(81711)
n = 445
_l_(81712)
_c_(81715, _n_(81713, "print", lambda: print), '\nOriginal number:', _n_(81714, "n", lambda: n))
_l_(81716)
_c_(81721, _n_(81717, "print", lambda: print), 'Next bigger number:', _c_(81720, _n_(81718, "rearrange_bigger", lambda: rearrange_bigger), _n_(81719, "n", lambda: n)))
_l_(81722)