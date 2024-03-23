# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_non_repeating_character(str1):
    _l_(83442)

    ctr = {}
    _l_(83417)
    for c in _n_(83418, "str1", lambda: str1):
        _l_(83433)

        if _n_(83419, "c", lambda: c) in _n_(83420, "ctr", lambda: ctr):
            _l_(83432)

            _n_(83421, "ctr", lambda: ctr)[_n_(83422, "c", lambda: c)] += 1
            _l_(83423)
        else:
            _n_(83424, "ctr", lambda: ctr)[_n_(83425, "c", lambda: c)] = 1
            _l_(83426)
            _c_(83430, _a_(83428, _n_(83427, "char_order", lambda: char_order), "append"), _n_(83429, "c", lambda: c))
            _l_(83431)
    for c in _n_(83434, "char_order", lambda: char_order):
        _l_(83440)

        if _n_(83435, "ctr", lambda: ctr)[_n_(83436, "c", lambda: c)] == 1:
            _l_(83439)

            aux = _n_(83437, "c", lambda: c)
            _l_(83438)
            return aux
    aux = None
    _l_(83441)
    return aux
_c_(83446, _n_(83443, "print", lambda: print), _c_(83445, _n_(83444, "first_non_repeating_character", lambda: first_non_repeating_character), 'abcdef'))
_l_(83447)
_c_(83451, _n_(83448, "print", lambda: print), _c_(83450, _n_(83449, "first_non_repeating_character", lambda: first_non_repeating_character), 'abcabcdef'))
_l_(83452)
_c_(83456, _n_(83453, "print", lambda: print), _c_(83455, _n_(83454, "first_non_repeating_character", lambda: first_non_repeating_character), 'aabbcc'))
_l_(83457)