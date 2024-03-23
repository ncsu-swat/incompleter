# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def uncommon_chars_concat(s1, s2):
    _l_(95711)

    set1 = _c_(95687, _n_(95685, "set", lambda: set), _n_(95686, "s1", lambda: s1))
    _l_(95688)
    set2 = _c_(95691, _n_(95689, "set", lambda: set), _n_(95690, "s2", lambda: s2))
    _l_(95692)
    common_chars = _c_(95696, _n_(95693, "list", lambda: list), _n_(95694, "set1", lambda: set1) & _n_(95695, "set2", lambda: set2))
    _l_(95697)
    result = [_n_(95698, "ch", lambda: ch) for ch in _n_(95699, "s1", lambda: s1) if _n_(95700, "ch", lambda: ch) not in _n_(95701, "common_chars", lambda: common_chars)] + [_n_(95702, "ch", lambda: ch) for ch in _n_(95703, "s2", lambda: s2) if _n_(95704, "ch", lambda: ch) not in _n_(95705, "common_chars", lambda: common_chars)]
    _l_(95706)
    aux = _c_(95709, _a_(95707, '', "join"), _n_(95708, "result", lambda: result))
    _l_(95710)
    return aux
s1 = 'abcdpqr'
_l_(95712)
_c_(95716, _n_(95713, "print", lambda: print), 'Original Substrings:\n', _n_(95714, "s1", lambda: s1) + '\n', _n_(95715, "s2", lambda: s2))
_l_(95717)
_c_(95719, _n_(95718, "print", lambda: print), '\nAfter concatenating uncommon characters:')
_l_(95720)
_c_(95726, _n_(95721, "print", lambda: print), _c_(95725, _n_(95722, "uncommon_chars_concat", lambda: uncommon_chars_concat), _n_(95723, "s1", lambda: s1), _n_(95724, "s2", lambda: s2)))
_l_(95727)