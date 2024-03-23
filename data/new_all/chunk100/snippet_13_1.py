# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def word_count(str):
    _l_(9796)

    counts = _c_(9781, _n_(9780, "dict", lambda: dict))
    _l_(9782)
    for word in _n_(9783, "words", lambda: words):
        _l_(9793)

        if _n_(9784, "word", lambda: word) in _n_(9785, "counts", lambda: counts):
            _l_(9792)

            _n_(9786, "counts", lambda: counts)[_n_(9787, "word", lambda: word)] += 1
            _l_(9788)
        else:
            _n_(9789, "counts", lambda: counts)[_n_(9790, "word", lambda: word)] = 1
            _l_(9791)
    aux = _n_(9794, "counts", lambda: counts)
    _l_(9795)
    return aux
_c_(9800, _n_(9797, "print", lambda: print), _c_(9799, _n_(9798, "word_count", lambda: word_count), 'the quick brown fox jumps over the lazy dog.'))
_l_(9801)