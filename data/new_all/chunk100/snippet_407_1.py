# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_words(list1, remove_words):
    _l_(39943)

    result = _c_(39939, _n_(39933, "list", lambda: list), _c_(39938, _n_(39934, "filter", lambda: filter), lambda word: _n_(39935, "word", lambda: word) not in _n_(39936, "remove_words", lambda: remove_words), _n_(39937, "list1", lambda: list1)))
    _l_(39940)
    aux = _n_(39941, "result", lambda: result)
    _l_(39942)
    return aux
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
_l_(39944)
_c_(39946, _n_(39945, "print", lambda: print), 'Original list:')
_l_(39947)
_c_(39950, _n_(39948, "print", lambda: print), _n_(39949, "colors", lambda: colors))
_l_(39951)
_c_(39953, _n_(39952, "print", lambda: print), '\nRemove words:')
_l_(39954)
_c_(39957, _n_(39955, "print", lambda: print), _n_(39956, "remove_colors", lambda: remove_colors))
_l_(39958)
_c_(39960, _n_(39959, "print", lambda: print), '\nAfter removing the specified words from the said list:')
_l_(39961)
_c_(39967, _n_(39962, "print", lambda: print), _c_(39966, _n_(39963, "remove_words", lambda: remove_words), _n_(39964, "colors", lambda: colors), _n_(39965, "remove_colors", lambda: remove_colors)))
_l_(39968)