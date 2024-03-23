# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(81564)

    nums = _c_(81519, _n_(81515, "list", lambda: list), _c_(81518, _n_(81516, "str", lambda: str), _n_(81517, "n", lambda: n)))
    _l_(81520)
    for i in _c_(81525, _n_(81521, "range", lambda: range), _c_(81524, _n_(81522, "len", lambda: len), _n_(81523, "nums", lambda: nums)) - 2, -1, -1):
        _l_(81562)

        if _n_(81526, "nums", lambda: nums)[_n_(81527, "i", lambda: i)] < _n_(81528, "nums", lambda: nums)[_n_(81529, "i", lambda: i) + 1]:
            _l_(81561)

            z = _n_(81530, "nums", lambda: nums)[_n_(81531, "i", lambda: i):]
            _l_(81532)
            y = _c_(81539, _n_(81533, "min", lambda: min), _c_(81538, _n_(81534, "filter", lambda: filter), lambda x: _n_(81535, "x", lambda: x) > _n_(81536, "z", lambda: z)[0], _n_(81537, "z", lambda: z)))
            _l_(81540)
            _c_(81544, _a_(81542, _n_(81541, "z", lambda: z), "remove"), _n_(81543, "y", lambda: y))
            _l_(81545)
            _c_(81548, _a_(81547, _n_(81546, "z", lambda: z), "sort"))
            _l_(81549)
            _n_(81550, "nums", lambda: nums)[_n_(81551, "i", lambda: i):] = [_n_(81552, "y", lambda: y)] + _n_(81553, "z", lambda: z)
            _l_(81554)
            aux = _c_(81559, _n_(81555, "int", lambda: int), _c_(81558, _a_(81556, '', "join"), _n_(81557, "nums", lambda: nums)))
            _l_(81560)
            return aux
    aux = False
    _l_(81563)
    return aux
n = 12
_l_(81565)
_c_(81568, _n_(81566, "print", lambda: print), 'Original number:', _n_(81567, "n", lambda: n))
_l_(81569)
_c_(81574, _n_(81570, "print", lambda: print), 'Next bigger number:', _c_(81573, _n_(81571, "rearrange_bigger", lambda: rearrange_bigger), _n_(81572, "n", lambda: n)))
_l_(81575)
n = 10
_l_(81576)
_c_(81579, _n_(81577, "print", lambda: print), '\nOriginal number:', _n_(81578, "n", lambda: n))
_l_(81580)
_c_(81585, _n_(81581, "print", lambda: print), 'Next bigger number:', _c_(81584, _n_(81582, "rearrange_bigger", lambda: rearrange_bigger), _n_(81583, "n", lambda: n)))
_l_(81586)
n = 201
_l_(81587)
_c_(81590, _n_(81588, "print", lambda: print), '\nOriginal number:', _n_(81589, "n", lambda: n))
_l_(81591)
_c_(81596, _n_(81592, "print", lambda: print), 'Next bigger number:', _c_(81595, _n_(81593, "rearrange_bigger", lambda: rearrange_bigger), _n_(81594, "n", lambda: n)))
_l_(81597)
n = 102
_l_(81598)
_c_(81601, _n_(81599, "print", lambda: print), '\nOriginal number:', _n_(81600, "n", lambda: n))
_l_(81602)
_c_(81607, _n_(81603, "print", lambda: print), 'Next bigger number:', _c_(81606, _n_(81604, "rearrange_bigger", lambda: rearrange_bigger), _n_(81605, "n", lambda: n)))
_l_(81608)
_c_(81611, _n_(81609, "print", lambda: print), '\nOriginal number:', _n_(81610, "n", lambda: n))
_l_(81612)
_c_(81617, _n_(81613, "print", lambda: print), 'Next bigger number:', _c_(81616, _n_(81614, "rearrange_bigger", lambda: rearrange_bigger), _n_(81615, "n", lambda: n)))
_l_(81618)