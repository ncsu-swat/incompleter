# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_largest_words(str1):
    _l_(17735)

    word = ''
    _l_(17681)
    all_words = []
    _l_(17682)
    str1 = _n_(17683, "str1", lambda: str1) + ' '
    _l_(17684)
    for i in _c_(17689, _n_(17685, "range", lambda: range), 0, _c_(17688, _n_(17686, "len", lambda: len), _n_(17687, "str1", lambda: str1))):
        _l_(17703)

        if _n_(17690, "str1", lambda: str1)[_n_(17691, "i", lambda: i)] != ' ':
            _l_(17702)

            word = _n_(17692, "word", lambda: word) + _n_(17693, "str1", lambda: str1)[_n_(17694, "i", lambda: i)]
            _l_(17695)
        else:
            _c_(17699, _a_(17697, _n_(17696, "all_words", lambda: all_words), "append"), _n_(17698, "word", lambda: word))
            _l_(17700)
            word = ''
            _l_(17701)
    for k in _c_(17708, _n_(17704, "range", lambda: range), 0, _c_(17707, _n_(17705, "len", lambda: len), _n_(17706, "all_words", lambda: all_words))):
        _l_(17731)

        if _c_(17711, _n_(17709, "len", lambda: len), _n_(17710, "small", lambda: small)) > _c_(17715, _n_(17712, "len", lambda: len), _n_(17713, "all_words", lambda: all_words)[_n_(17714, "k", lambda: k)]):
            _l_(17719)

            small = _n_(17716, "all_words", lambda: all_words)[_n_(17717, "k", lambda: k)]
            _l_(17718)
        if _c_(17722, _n_(17720, "len", lambda: len), _n_(17721, "large", lambda: large)) < _c_(17726, _n_(17723, "len", lambda: len), _n_(17724, "all_words", lambda: all_words)[_n_(17725, "k", lambda: k)]):
            _l_(17730)

            large = _n_(17727, "all_words", lambda: all_words)[_n_(17728, "k", lambda: k)]
            _l_(17729)
    aux = (_n_(17732, "small", lambda: small), _n_(17733, "large", lambda: large))
    _l_(17734)
    return aux
str1 = 'Write a Java program to sort an array of given integers using Quick sort Algorithm.'
_l_(17736)
_c_(17739, _n_(17737, "print", lambda: print), 'Original Strings:\n', _n_(17738, "str1", lambda: str1))
_l_(17740)
(small, large) = _c_(17743, _n_(17741, "smallest_largest_words", lambda: smallest_largest_words), _n_(17742, "str1", lambda: str1))
_l_(17744)
_c_(17747, _n_(17745, "print", lambda: print), 'Smallest word: ' + _n_(17746, "small", lambda: small))
_l_(17748)
_c_(17751, _n_(17749, "print", lambda: print), 'Largest word: ' + _n_(17750, "large", lambda: large))
_l_(17752)