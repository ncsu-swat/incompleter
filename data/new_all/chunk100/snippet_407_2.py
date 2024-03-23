# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_words(list1, remove_words):
    _l_(39979)

    result = _c_(39975, _n_(39969, "list", lambda: list), _c_(39974, _n_(39970, "filter", lambda: filter), lambda word: _n_(39971, "word", lambda: word) not in _n_(39972, "remove_words", lambda: remove_words), _n_(39973, "list1", lambda: list1)))
    _l_(39976)
    aux = _n_(39977, "result", lambda: result)
    _l_(39978)
    return aux
remove_colors = ['orange', 'black']
_l_(39980)
_c_(39982, _n_(39981, "print", lambda: print), 'Original list:')
_l_(39983)
_c_(39986, _n_(39984, "print", lambda: print), _n_(39985, "colors", lambda: colors))
_l_(39987)
_c_(39989, _n_(39988, "print", lambda: print), '\nRemove words:')
_l_(39990)
_c_(39993, _n_(39991, "print", lambda: print), _n_(39992, "remove_colors", lambda: remove_colors))
_l_(39994)
_c_(39996, _n_(39995, "print", lambda: print), '\nAfter removing the specified words from the said list:')
_l_(39997)
_c_(40003, _n_(39998, "print", lambda: print), _c_(40002, _n_(39999, "remove_words", lambda: remove_words), _n_(40000, "colors", lambda: colors), _n_(40001, "remove_colors", lambda: remove_colors)))
_l_(40004)