# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_words(list1, remove_words):
    _l_(114713)

    result = _c_(114709, _n_(114703, "list", lambda: list), _c_(114708, _n_(114704, "filter", lambda: filter), lambda word: _n_(114705, "word", lambda: word) not in _n_(114706, "remove_words", lambda: remove_words), _n_(114707, "list1", lambda: list1)))
    _l_(114710)
    aux = _n_(114711, "result", lambda: result)
    _l_(114712)
    return aux
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
_l_(114714)
_c_(114716, _n_(114715, "print", lambda: print), 'Original list:')
_l_(114717)
_c_(114720, _n_(114718, "print", lambda: print), _n_(114719, "colors", lambda: colors))
_l_(114721)
_c_(114723, _n_(114722, "print", lambda: print), '\nRemove words:')
_l_(114724)
_c_(114727, _n_(114725, "print", lambda: print), _n_(114726, "remove_colors", lambda: remove_colors))
_l_(114728)
_c_(114730, _n_(114729, "print", lambda: print), '\nAfter removing the specified words from the said list:')
_l_(114731)
_c_(114737, _n_(114732, "print", lambda: print), _c_(114736, _n_(114733, "remove_words", lambda: remove_words), _n_(114734, "colors", lambda: colors), _n_(114735, "remove_colors", lambda: remove_colors)))
_l_(114738)