# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def word_count(str):
    _l_(9774)

    words = _c_(9759, _a_(9758, _n_(9757, "str", lambda: str), "split"))
    _l_(9760)
    for word in _n_(9761, "words", lambda: words):
        _l_(9771)

        if _n_(9762, "word", lambda: word) in _n_(9763, "counts", lambda: counts):
            _l_(9770)

            _n_(9764, "counts", lambda: counts)[_n_(9765, "word", lambda: word)] += 1
            _l_(9766)
        else:
            _n_(9767, "counts", lambda: counts)[_n_(9768, "word", lambda: word)] = 1
            _l_(9769)
    aux = _n_(9772, "counts", lambda: counts)
    _l_(9773)
    return aux
_c_(9778, _n_(9775, "print", lambda: print), _c_(9777, _n_(9776, "word_count", lambda: word_count), 'the quick brown fox jumps over the lazy dog.'))
_l_(9779)