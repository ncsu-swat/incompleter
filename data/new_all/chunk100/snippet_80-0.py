# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(120650)

    nums = _c_(120605, _n_(120601, "list", lambda: list), _c_(120604, _n_(120602, "str", lambda: str), _n_(120603, "n", lambda: n)))
    _l_(120606)
    for i in _c_(120611, _n_(120607, "range", lambda: range), _c_(120610, _n_(120608, "len", lambda: len), _n_(120609, "nums", lambda: nums)) - 2, -1, -1):
        _l_(120648)

        if _n_(120612, "nums", lambda: nums)[_n_(120613, "i", lambda: i)] < _n_(120614, "nums", lambda: nums)[_n_(120615, "i", lambda: i) + 1]:
            _l_(120647)

            z = _n_(120616, "nums", lambda: nums)[_n_(120617, "i", lambda: i):]
            _l_(120618)
            y = _c_(120625, _n_(120619, "min", lambda: min), _c_(120624, _n_(120620, "filter", lambda: filter), lambda x: _n_(120621, "x", lambda: x) > _n_(120622, "z", lambda: z)[0], _n_(120623, "z", lambda: z)))
            _l_(120626)
            _c_(120630, _a_(120628, _n_(120627, "z", lambda: z), "remove"), _n_(120629, "y", lambda: y))
            _l_(120631)
            _c_(120634, _a_(120633, _n_(120632, "z", lambda: z), "sort"))
            _l_(120635)
            _n_(120636, "nums", lambda: nums)[_n_(120637, "i", lambda: i):] = [_n_(120638, "y", lambda: y)] + _n_(120639, "z", lambda: z)
            _l_(120640)
            aux = _c_(120645, _n_(120641, "int", lambda: int), _c_(120644, _a_(120642, '', "join"), _n_(120643, "nums", lambda: nums)))
            _l_(120646)
            return aux
    aux = False
    _l_(120649)
    return aux
_c_(120653, _n_(120651, "print", lambda: print), 'Original number:', _n_(120652, "n", lambda: n))
_l_(120654)
_c_(120659, _n_(120655, "print", lambda: print), 'Next bigger number:', _c_(120658, _n_(120656, "rearrange_bigger", lambda: rearrange_bigger), _n_(120657, "n", lambda: n)))
_l_(120660)
n = 10
_l_(120661)
_c_(120664, _n_(120662, "print", lambda: print), '\nOriginal number:', _n_(120663, "n", lambda: n))
_l_(120665)
_c_(120670, _n_(120666, "print", lambda: print), 'Next bigger number:', _c_(120669, _n_(120667, "rearrange_bigger", lambda: rearrange_bigger), _n_(120668, "n", lambda: n)))
_l_(120671)
n = 201
_l_(120672)
_c_(120675, _n_(120673, "print", lambda: print), '\nOriginal number:', _n_(120674, "n", lambda: n))
_l_(120676)
_c_(120681, _n_(120677, "print", lambda: print), 'Next bigger number:', _c_(120680, _n_(120678, "rearrange_bigger", lambda: rearrange_bigger), _n_(120679, "n", lambda: n)))
_l_(120682)
n = 102
_l_(120683)
_c_(120686, _n_(120684, "print", lambda: print), '\nOriginal number:', _n_(120685, "n", lambda: n))
_l_(120687)
_c_(120692, _n_(120688, "print", lambda: print), 'Next bigger number:', _c_(120691, _n_(120689, "rearrange_bigger", lambda: rearrange_bigger), _n_(120690, "n", lambda: n)))
_l_(120693)
n = 445
_l_(120694)
_c_(120697, _n_(120695, "print", lambda: print), '\nOriginal number:', _n_(120696, "n", lambda: n))
_l_(120698)
_c_(120703, _n_(120699, "print", lambda: print), 'Next bigger number:', _c_(120702, _n_(120700, "rearrange_bigger", lambda: rearrange_bigger), _n_(120701, "n", lambda: n)))
_l_(120704)