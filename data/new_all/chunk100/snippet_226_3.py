# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_largest_words(str1):
    _l_(17881)

    word = ''
    _l_(17825)
    all_words = []
    _l_(17826)
    str1 = _n_(17827, "str1", lambda: str1) + ' '
    _l_(17828)
    for i in _c_(17833, _n_(17829, "range", lambda: range), 0, _c_(17832, _n_(17830, "len", lambda: len), _n_(17831, "str1", lambda: str1))):
        _l_(17847)

        if _n_(17834, "str1", lambda: str1)[_n_(17835, "i", lambda: i)] != ' ':
            _l_(17846)

            word = _n_(17836, "word", lambda: word) + _n_(17837, "str1", lambda: str1)[_n_(17838, "i", lambda: i)]
            _l_(17839)
        else:
            _c_(17843, _a_(17841, _n_(17840, "all_words", lambda: all_words), "append"), _n_(17842, "word", lambda: word))
            _l_(17844)
            word = ''
            _l_(17845)
    small = large = _n_(17848, "all_words", lambda: all_words)[0]
    _l_(17849)
    for k in _c_(17854, _n_(17850, "range", lambda: range), 0, _c_(17853, _n_(17851, "len", lambda: len), _n_(17852, "all_words", lambda: all_words))):
        _l_(17877)

        if _c_(17857, _n_(17855, "len", lambda: len), _n_(17856, "small", lambda: small)) > _c_(17861, _n_(17858, "len", lambda: len), _n_(17859, "all_words", lambda: all_words)[_n_(17860, "k", lambda: k)]):
            _l_(17865)

            small = _n_(17862, "all_words", lambda: all_words)[_n_(17863, "k", lambda: k)]
            _l_(17864)
        if _c_(17868, _n_(17866, "len", lambda: len), _n_(17867, "large", lambda: large)) < _c_(17872, _n_(17869, "len", lambda: len), _n_(17870, "all_words", lambda: all_words)[_n_(17871, "k", lambda: k)]):
            _l_(17876)

            large = _n_(17873, "all_words", lambda: all_words)[_n_(17874, "k", lambda: k)]
            _l_(17875)
    aux = (_n_(17878, "small", lambda: small), _n_(17879, "large", lambda: large))
    _l_(17880)
    return aux
_c_(17884, _n_(17882, "print", lambda: print), 'Original Strings:\n', _n_(17883, "str1", lambda: str1))
_l_(17885)
(small, large) = _c_(17888, _n_(17886, "smallest_largest_words", lambda: smallest_largest_words), _n_(17887, "str1", lambda: str1))
_l_(17889)
_c_(17892, _n_(17890, "print", lambda: print), 'Smallest word: ' + _n_(17891, "small", lambda: small))
_l_(17893)
_c_(17896, _n_(17894, "print", lambda: print), 'Largest word: ' + _n_(17895, "large", lambda: large))
_l_(17897)