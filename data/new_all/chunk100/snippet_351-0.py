# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_longest_word(words_list):
    _l_(111743)

    word_len = []
    _l_(111725)
    for n in _n_(111726, "words_list", lambda: words_list):
        _l_(111735)

        _c_(111733, _a_(111728, _n_(111727, "word_len", lambda: word_len), "append"), (_c_(111731, _n_(111729, "len", lambda: len), _n_(111730, "n", lambda: n)), _n_(111732, "n", lambda: n)))
        _l_(111734)
    _c_(111738, _a_(111737, _n_(111736, "word_len", lambda: word_len), "sort"))
    _l_(111739)
    aux = (_n_(111740, "word_len", lambda: word_len)[-1][0], _n_(111741, "word_len", lambda: word_len)[-1][1])
    _l_(111742)
    return aux
_c_(111746, _n_(111744, "print", lambda: print), '\nLongest word: ', _n_(111745, "result", lambda: result)[1])
_l_(111747)
_c_(111750, _n_(111748, "print", lambda: print), 'Length of the longest word: ', _n_(111749, "result", lambda: result)[0])
_l_(111751)