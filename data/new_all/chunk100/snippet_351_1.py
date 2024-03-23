# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_longest_word(words_list):
    _l_(35043)

    word_len = []
    _l_(35025)
    for n in _n_(35026, "words_list", lambda: words_list):
        _l_(35035)

        _c_(35033, _a_(35028, _n_(35027, "word_len", lambda: word_len), "append"), (_c_(35031, _n_(35029, "len", lambda: len), _n_(35030, "n", lambda: n)), _n_(35032, "n", lambda: n)))
        _l_(35034)
    _c_(35038, _a_(35037, _n_(35036, "word_len", lambda: word_len), "sort"))
    _l_(35039)
    aux = (_n_(35040, "word_len", lambda: word_len)[-1][0], _n_(35041, "word_len", lambda: word_len)[-1][1])
    _l_(35042)
    return aux
_c_(35046, _n_(35044, "print", lambda: print), '\nLongest word: ', _n_(35045, "result", lambda: result)[1])
_l_(35047)
_c_(35050, _n_(35048, "print", lambda: print), 'Length of the longest word: ', _n_(35049, "result", lambda: result)[0])
_l_(35051)