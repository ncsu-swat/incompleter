# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_non_repeating_character(str1):
    _l_(83483)

    char_order = []
    _l_(83458)
    for c in _n_(83459, "str1", lambda: str1):
        _l_(83474)

        if _n_(83460, "c", lambda: c) in _n_(83461, "ctr", lambda: ctr):
            _l_(83473)

            _n_(83462, "ctr", lambda: ctr)[_n_(83463, "c", lambda: c)] += 1
            _l_(83464)
        else:
            _n_(83465, "ctr", lambda: ctr)[_n_(83466, "c", lambda: c)] = 1
            _l_(83467)
            _c_(83471, _a_(83469, _n_(83468, "char_order", lambda: char_order), "append"), _n_(83470, "c", lambda: c))
            _l_(83472)
    for c in _n_(83475, "char_order", lambda: char_order):
        _l_(83481)

        if _n_(83476, "ctr", lambda: ctr)[_n_(83477, "c", lambda: c)] == 1:
            _l_(83480)

            aux = _n_(83478, "c", lambda: c)
            _l_(83479)
            return aux
    aux = None
    _l_(83482)
    return aux
_c_(83487, _n_(83484, "print", lambda: print), _c_(83486, _n_(83485, "first_non_repeating_character", lambda: first_non_repeating_character), 'abcdef'))
_l_(83488)
_c_(83492, _n_(83489, "print", lambda: print), _c_(83491, _n_(83490, "first_non_repeating_character", lambda: first_non_repeating_character), 'abcabcdef'))
_l_(83493)
_c_(83497, _n_(83494, "print", lambda: print), _c_(83496, _n_(83495, "first_non_repeating_character", lambda: first_non_repeating_character), 'aabbcc'))
_l_(83498)