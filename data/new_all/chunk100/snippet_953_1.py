# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def uncommon_chars_concat(s1, s2):
    _l_(95592)

    set1 = _c_(95572, _n_(95570, "set", lambda: set), _n_(95571, "s1", lambda: s1))
    _l_(95573)
    common_chars = _c_(95577, _n_(95574, "list", lambda: list), _n_(95575, "set1", lambda: set1) & _n_(95576, "set2", lambda: set2))
    _l_(95578)
    result = [_n_(95579, "ch", lambda: ch) for ch in _n_(95580, "s1", lambda: s1) if _n_(95581, "ch", lambda: ch) not in _n_(95582, "common_chars", lambda: common_chars)] + [_n_(95583, "ch", lambda: ch) for ch in _n_(95584, "s2", lambda: s2) if _n_(95585, "ch", lambda: ch) not in _n_(95586, "common_chars", lambda: common_chars)]
    _l_(95587)
    aux = _c_(95590, _a_(95588, '', "join"), _n_(95589, "result", lambda: result))
    _l_(95591)
    return aux
s1 = 'abcdpqr'
_l_(95593)
s2 = 'xyzabcd'
_l_(95594)
_c_(95598, _n_(95595, "print", lambda: print), 'Original Substrings:\n', _n_(95596, "s1", lambda: s1) + '\n', _n_(95597, "s2", lambda: s2))
_l_(95599)
_c_(95601, _n_(95600, "print", lambda: print), '\nAfter concatenating uncommon characters:')
_l_(95602)
_c_(95608, _n_(95603, "print", lambda: print), _c_(95607, _n_(95604, "uncommon_chars_concat", lambda: uncommon_chars_concat), _n_(95605, "s1", lambda: s1), _n_(95606, "s2", lambda: s2)))
_l_(95609)