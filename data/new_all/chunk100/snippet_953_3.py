# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def uncommon_chars_concat(s1, s2):
    _l_(95667)

    set1 = _c_(95652, _n_(95650, "set", lambda: set), _n_(95651, "s1", lambda: s1))
    _l_(95653)
    set2 = _c_(95656, _n_(95654, "set", lambda: set), _n_(95655, "s2", lambda: s2))
    _l_(95657)
    common_chars = _c_(95661, _n_(95658, "list", lambda: list), _n_(95659, "set1", lambda: set1) & _n_(95660, "set2", lambda: set2))
    _l_(95662)
    aux = _c_(95665, _a_(95663, '', "join"), _n_(95664, "result", lambda: result))
    _l_(95666)
    return aux
s1 = 'abcdpqr'
_l_(95668)
s2 = 'xyzabcd'
_l_(95669)
_c_(95673, _n_(95670, "print", lambda: print), 'Original Substrings:\n', _n_(95671, "s1", lambda: s1) + '\n', _n_(95672, "s2", lambda: s2))
_l_(95674)
_c_(95676, _n_(95675, "print", lambda: print), '\nAfter concatenating uncommon characters:')
_l_(95677)
_c_(95683, _n_(95678, "print", lambda: print), _c_(95682, _n_(95679, "uncommon_chars_concat", lambda: uncommon_chars_concat), _n_(95680, "s1", lambda: s1), _n_(95681, "s2", lambda: s2)))
_l_(95684)