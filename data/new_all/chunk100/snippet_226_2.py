# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_largest_words(str1):
    _l_(17807)

    word = ''
    _l_(17753)
    all_words = []
    _l_(17754)
    for i in _c_(17759, _n_(17755, "range", lambda: range), 0, _c_(17758, _n_(17756, "len", lambda: len), _n_(17757, "str1", lambda: str1))):
        _l_(17773)

        if _n_(17760, "str1", lambda: str1)[_n_(17761, "i", lambda: i)] != ' ':
            _l_(17772)

            word = _n_(17762, "word", lambda: word) + _n_(17763, "str1", lambda: str1)[_n_(17764, "i", lambda: i)]
            _l_(17765)
        else:
            _c_(17769, _a_(17767, _n_(17766, "all_words", lambda: all_words), "append"), _n_(17768, "word", lambda: word))
            _l_(17770)
            word = ''
            _l_(17771)
    small = large = _n_(17774, "all_words", lambda: all_words)[0]
    _l_(17775)
    for k in _c_(17780, _n_(17776, "range", lambda: range), 0, _c_(17779, _n_(17777, "len", lambda: len), _n_(17778, "all_words", lambda: all_words))):
        _l_(17803)

        if _c_(17783, _n_(17781, "len", lambda: len), _n_(17782, "small", lambda: small)) > _c_(17787, _n_(17784, "len", lambda: len), _n_(17785, "all_words", lambda: all_words)[_n_(17786, "k", lambda: k)]):
            _l_(17791)

            small = _n_(17788, "all_words", lambda: all_words)[_n_(17789, "k", lambda: k)]
            _l_(17790)
        if _c_(17794, _n_(17792, "len", lambda: len), _n_(17793, "large", lambda: large)) < _c_(17798, _n_(17795, "len", lambda: len), _n_(17796, "all_words", lambda: all_words)[_n_(17797, "k", lambda: k)]):
            _l_(17802)

            large = _n_(17799, "all_words", lambda: all_words)[_n_(17800, "k", lambda: k)]
            _l_(17801)
    aux = (_n_(17804, "small", lambda: small), _n_(17805, "large", lambda: large))
    _l_(17806)
    return aux
str1 = 'Write a Java program to sort an array of given integers using Quick sort Algorithm.'
_l_(17808)
_c_(17811, _n_(17809, "print", lambda: print), 'Original Strings:\n', _n_(17810, "str1", lambda: str1))
_l_(17812)
(small, large) = _c_(17815, _n_(17813, "smallest_largest_words", lambda: smallest_largest_words), _n_(17814, "str1", lambda: str1))
_l_(17816)
_c_(17819, _n_(17817, "print", lambda: print), 'Smallest word: ' + _n_(17818, "small", lambda: small))
_l_(17820)
_c_(17823, _n_(17821, "print", lambda: print), 'Largest word: ' + _n_(17822, "large", lambda: large))
_l_(17824)