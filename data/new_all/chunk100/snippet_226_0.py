# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_largest_words(str1):
    _l_(17663)

    word = ''
    _l_(17608)
    str1 = _n_(17609, "str1", lambda: str1) + ' '
    _l_(17610)
    for i in _c_(17615, _n_(17611, "range", lambda: range), 0, _c_(17614, _n_(17612, "len", lambda: len), _n_(17613, "str1", lambda: str1))):
        _l_(17629)

        if _n_(17616, "str1", lambda: str1)[_n_(17617, "i", lambda: i)] != ' ':
            _l_(17628)

            word = _n_(17618, "word", lambda: word) + _n_(17619, "str1", lambda: str1)[_n_(17620, "i", lambda: i)]
            _l_(17621)
        else:
            _c_(17625, _a_(17623, _n_(17622, "all_words", lambda: all_words), "append"), _n_(17624, "word", lambda: word))
            _l_(17626)
            word = ''
            _l_(17627)
    small = large = _n_(17630, "all_words", lambda: all_words)[0]
    _l_(17631)
    for k in _c_(17636, _n_(17632, "range", lambda: range), 0, _c_(17635, _n_(17633, "len", lambda: len), _n_(17634, "all_words", lambda: all_words))):
        _l_(17659)

        if _c_(17639, _n_(17637, "len", lambda: len), _n_(17638, "small", lambda: small)) > _c_(17643, _n_(17640, "len", lambda: len), _n_(17641, "all_words", lambda: all_words)[_n_(17642, "k", lambda: k)]):
            _l_(17647)

            small = _n_(17644, "all_words", lambda: all_words)[_n_(17645, "k", lambda: k)]
            _l_(17646)
        if _c_(17650, _n_(17648, "len", lambda: len), _n_(17649, "large", lambda: large)) < _c_(17654, _n_(17651, "len", lambda: len), _n_(17652, "all_words", lambda: all_words)[_n_(17653, "k", lambda: k)]):
            _l_(17658)

            large = _n_(17655, "all_words", lambda: all_words)[_n_(17656, "k", lambda: k)]
            _l_(17657)
    aux = (_n_(17660, "small", lambda: small), _n_(17661, "large", lambda: large))
    _l_(17662)
    return aux
str1 = 'Write a Java program to sort an array of given integers using Quick sort Algorithm.'
_l_(17664)
_c_(17667, _n_(17665, "print", lambda: print), 'Original Strings:\n', _n_(17666, "str1", lambda: str1))
_l_(17668)
(small, large) = _c_(17671, _n_(17669, "smallest_largest_words", lambda: smallest_largest_words), _n_(17670, "str1", lambda: str1))
_l_(17672)
_c_(17675, _n_(17673, "print", lambda: print), 'Smallest word: ' + _n_(17674, "small", lambda: small))
_l_(17676)
_c_(17679, _n_(17677, "print", lambda: print), 'Largest word: ' + _n_(17678, "large", lambda: large))
_l_(17680)