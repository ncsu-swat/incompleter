# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def uncommon_chars_concat(s1, s2):
    _l_(95749)

    set1 = _c_(95730, _n_(95728, "set", lambda: set), _n_(95729, "s1", lambda: s1))
    _l_(95731)
    set2 = _c_(95734, _n_(95732, "set", lambda: set), _n_(95733, "s2", lambda: s2))
    _l_(95735)
    result = [_n_(95736, "ch", lambda: ch) for ch in _n_(95737, "s1", lambda: s1) if _n_(95738, "ch", lambda: ch) not in _n_(95739, "common_chars", lambda: common_chars)] + [_n_(95740, "ch", lambda: ch) for ch in _n_(95741, "s2", lambda: s2) if _n_(95742, "ch", lambda: ch) not in _n_(95743, "common_chars", lambda: common_chars)]
    _l_(95744)
    aux = _c_(95747, _a_(95745, '', "join"), _n_(95746, "result", lambda: result))
    _l_(95748)
    return aux
s1 = 'abcdpqr'
_l_(95750)
s2 = 'xyzabcd'
_l_(95751)
_c_(95755, _n_(95752, "print", lambda: print), 'Original Substrings:\n', _n_(95753, "s1", lambda: s1) + '\n', _n_(95754, "s2", lambda: s2))
_l_(95756)
_c_(95758, _n_(95757, "print", lambda: print), '\nAfter concatenating uncommon characters:')
_l_(95759)
_c_(95765, _n_(95760, "print", lambda: print), _c_(95764, _n_(95761, "uncommon_chars_concat", lambda: uncommon_chars_concat), _n_(95762, "s1", lambda: s1), _n_(95763, "s2", lambda: s2)))
_l_(95766)