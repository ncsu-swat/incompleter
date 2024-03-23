# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def uncommon_chars_concat(s1, s2):
    _l_(95553)

    set1 = _c_(95529, _n_(95527, "set", lambda: set), _n_(95528, "s1", lambda: s1))
    _l_(95530)
    set2 = _c_(95533, _n_(95531, "set", lambda: set), _n_(95532, "s2", lambda: s2))
    _l_(95534)
    common_chars = _c_(95538, _n_(95535, "list", lambda: list), _n_(95536, "set1", lambda: set1) & _n_(95537, "set2", lambda: set2))
    _l_(95539)
    result = [_n_(95540, "ch", lambda: ch) for ch in _n_(95541, "s1", lambda: s1) if _n_(95542, "ch", lambda: ch) not in _n_(95543, "common_chars", lambda: common_chars)] + [_n_(95544, "ch", lambda: ch) for ch in _n_(95545, "s2", lambda: s2) if _n_(95546, "ch", lambda: ch) not in _n_(95547, "common_chars", lambda: common_chars)]
    _l_(95548)
    aux = _c_(95551, _a_(95549, '', "join"), _n_(95550, "result", lambda: result))
    _l_(95552)
    return aux
s2 = 'xyzabcd'
_l_(95554)
_c_(95558, _n_(95555, "print", lambda: print), 'Original Substrings:\n', _n_(95556, "s1", lambda: s1) + '\n', _n_(95557, "s2", lambda: s2))
_l_(95559)
_c_(95561, _n_(95560, "print", lambda: print), '\nAfter concatenating uncommon characters:')
_l_(95562)
_c_(95568, _n_(95563, "print", lambda: print), _c_(95567, _n_(95564, "uncommon_chars_concat", lambda: uncommon_chars_concat), _n_(95565, "s1", lambda: s1), _n_(95566, "s2", lambda: s2)))
_l_(95569)