# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rearrange_bigger(n):
    _l_(81362)

    for i in _c_(81323, _n_(81319, "range", lambda: range), _c_(81322, _n_(81320, "len", lambda: len), _n_(81321, "nums", lambda: nums)) - 2, -1, -1):
        _l_(81360)

        if _n_(81324, "nums", lambda: nums)[_n_(81325, "i", lambda: i)] < _n_(81326, "nums", lambda: nums)[_n_(81327, "i", lambda: i) + 1]:
            _l_(81359)

            z = _n_(81328, "nums", lambda: nums)[_n_(81329, "i", lambda: i):]
            _l_(81330)
            y = _c_(81337, _n_(81331, "min", lambda: min), _c_(81336, _n_(81332, "filter", lambda: filter), lambda x: _n_(81333, "x", lambda: x) > _n_(81334, "z", lambda: z)[0], _n_(81335, "z", lambda: z)))
            _l_(81338)
            _c_(81342, _a_(81340, _n_(81339, "z", lambda: z), "remove"), _n_(81341, "y", lambda: y))
            _l_(81343)
            _c_(81346, _a_(81345, _n_(81344, "z", lambda: z), "sort"))
            _l_(81347)
            _n_(81348, "nums", lambda: nums)[_n_(81349, "i", lambda: i):] = [_n_(81350, "y", lambda: y)] + _n_(81351, "z", lambda: z)
            _l_(81352)
            aux = _c_(81357, _n_(81353, "int", lambda: int), _c_(81356, _a_(81354, '', "join"), _n_(81355, "nums", lambda: nums)))
            _l_(81358)
            return aux
    aux = False
    _l_(81361)
    return aux
n = 12
_l_(81363)
_c_(81366, _n_(81364, "print", lambda: print), 'Original number:', _n_(81365, "n", lambda: n))
_l_(81367)
_c_(81372, _n_(81368, "print", lambda: print), 'Next bigger number:', _c_(81371, _n_(81369, "rearrange_bigger", lambda: rearrange_bigger), _n_(81370, "n", lambda: n)))
_l_(81373)
n = 10
_l_(81374)
_c_(81377, _n_(81375, "print", lambda: print), '\nOriginal number:', _n_(81376, "n", lambda: n))
_l_(81378)
_c_(81383, _n_(81379, "print", lambda: print), 'Next bigger number:', _c_(81382, _n_(81380, "rearrange_bigger", lambda: rearrange_bigger), _n_(81381, "n", lambda: n)))
_l_(81384)
n = 201
_l_(81385)
_c_(81388, _n_(81386, "print", lambda: print), '\nOriginal number:', _n_(81387, "n", lambda: n))
_l_(81389)
_c_(81394, _n_(81390, "print", lambda: print), 'Next bigger number:', _c_(81393, _n_(81391, "rearrange_bigger", lambda: rearrange_bigger), _n_(81392, "n", lambda: n)))
_l_(81395)
n = 102
_l_(81396)
_c_(81399, _n_(81397, "print", lambda: print), '\nOriginal number:', _n_(81398, "n", lambda: n))
_l_(81400)
_c_(81405, _n_(81401, "print", lambda: print), 'Next bigger number:', _c_(81404, _n_(81402, "rearrange_bigger", lambda: rearrange_bigger), _n_(81403, "n", lambda: n)))
_l_(81406)
n = 445
_l_(81407)
_c_(81410, _n_(81408, "print", lambda: print), '\nOriginal number:', _n_(81409, "n", lambda: n))
_l_(81411)
_c_(81416, _n_(81412, "print", lambda: print), 'Next bigger number:', _c_(81415, _n_(81413, "rearrange_bigger", lambda: rearrange_bigger), _n_(81414, "n", lambda: n)))
_l_(81417)