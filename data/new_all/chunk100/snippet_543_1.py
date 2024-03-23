# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def long_words(n, str):
    _l_(54538)

    txt = _c_(54522, _a_(54521, _n_(54520, "str", lambda: str), "split"), ' ')
    _l_(54523)
    for x in _n_(54524, "txt", lambda: txt):
        _l_(54535)

        if _c_(54527, _n_(54525, "len", lambda: len), _n_(54526, "x", lambda: x)) > _n_(54528, "n", lambda: n):
            _l_(54534)

            _c_(54532, _a_(54530, _n_(54529, "word_len", lambda: word_len), "append"), _n_(54531, "x", lambda: x))
            _l_(54533)
    aux = _n_(54536, "word_len", lambda: word_len)
    _l_(54537)
    return aux
_c_(54542, _n_(54539, "print", lambda: print), _c_(54541, _n_(54540, "long_words", lambda: long_words), 3, 'The quick brown fox jumps over the lazy dog'))
_l_(54543)