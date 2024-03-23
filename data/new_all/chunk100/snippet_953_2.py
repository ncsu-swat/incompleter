# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def uncommon_chars_concat(s1, s2):
    _l_(95632)

    set2 = _c_(95612, _n_(95610, "set", lambda: set), _n_(95611, "s2", lambda: s2))
    _l_(95613)
    common_chars = _c_(95617, _n_(95614, "list", lambda: list), _n_(95615, "set1", lambda: set1) & _n_(95616, "set2", lambda: set2))
    _l_(95618)
    result = [_n_(95619, "ch", lambda: ch) for ch in _n_(95620, "s1", lambda: s1) if _n_(95621, "ch", lambda: ch) not in _n_(95622, "common_chars", lambda: common_chars)] + [_n_(95623, "ch", lambda: ch) for ch in _n_(95624, "s2", lambda: s2) if _n_(95625, "ch", lambda: ch) not in _n_(95626, "common_chars", lambda: common_chars)]
    _l_(95627)
    aux = _c_(95630, _a_(95628, '', "join"), _n_(95629, "result", lambda: result))
    _l_(95631)
    return aux
s1 = 'abcdpqr'
_l_(95633)
s2 = 'xyzabcd'
_l_(95634)
_c_(95638, _n_(95635, "print", lambda: print), 'Original Substrings:\n', _n_(95636, "s1", lambda: s1) + '\n', _n_(95637, "s2", lambda: s2))
_l_(95639)
_c_(95641, _n_(95640, "print", lambda: print), '\nAfter concatenating uncommon characters:')
_l_(95642)
_c_(95648, _n_(95643, "print", lambda: print), _c_(95647, _n_(95644, "uncommon_chars_concat", lambda: uncommon_chars_concat), _n_(95645, "s1", lambda: s1), _n_(95646, "s2", lambda: s2)))
_l_(95649)