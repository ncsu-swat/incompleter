# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_longest_word(words_list):
    _l_(35013)

    for n in _n_(34996, "words_list", lambda: words_list):
        _l_(35005)

        _c_(35003, _a_(34998, _n_(34997, "word_len", lambda: word_len), "append"), (_c_(35001, _n_(34999, "len", lambda: len), _n_(35000, "n", lambda: n)), _n_(35002, "n", lambda: n)))
        _l_(35004)
    _c_(35008, _a_(35007, _n_(35006, "word_len", lambda: word_len), "sort"))
    _l_(35009)
    aux = (_n_(35010, "word_len", lambda: word_len)[-1][0], _n_(35011, "word_len", lambda: word_len)[-1][1])
    _l_(35012)
    return aux
result = _c_(35015, _n_(35014, "find_longest_word", lambda: find_longest_word), ['PHP', 'Exercises', 'Backend'])
_l_(35016)
_c_(35019, _n_(35017, "print", lambda: print), '\nLongest word: ', _n_(35018, "result", lambda: result)[1])
_l_(35020)
_c_(35023, _n_(35021, "print", lambda: print), 'Length of the longest word: ', _n_(35022, "result", lambda: result)[0])
_l_(35024)