# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_words(list1, remove_words):
    _l_(114749)

    result = _c_(114745, _n_(114739, "list", lambda: list), _c_(114744, _n_(114740, "filter", lambda: filter), lambda word: _n_(114741, "word", lambda: word) not in _n_(114742, "remove_words", lambda: remove_words), _n_(114743, "list1", lambda: list1)))
    _l_(114746)
    aux = _n_(114747, "result", lambda: result)
    _l_(114748)
    return aux
remove_colors = ['orange', 'black']
_l_(114750)
_c_(114752, _n_(114751, "print", lambda: print), 'Original list:')
_l_(114753)
_c_(114756, _n_(114754, "print", lambda: print), _n_(114755, "colors", lambda: colors))
_l_(114757)
_c_(114759, _n_(114758, "print", lambda: print), '\nRemove words:')
_l_(114760)
_c_(114763, _n_(114761, "print", lambda: print), _n_(114762, "remove_colors", lambda: remove_colors))
_l_(114764)
_c_(114766, _n_(114765, "print", lambda: print), '\nAfter removing the specified words from the said list:')
_l_(114767)
_c_(114773, _n_(114768, "print", lambda: print), _c_(114772, _n_(114769, "remove_words", lambda: remove_words), _n_(114770, "colors", lambda: colors), _n_(114771, "remove_colors", lambda: remove_colors)))
_l_(114774)