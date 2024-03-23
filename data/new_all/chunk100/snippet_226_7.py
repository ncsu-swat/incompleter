# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_largest_words(str1):
    _l_(17953)

    all_words = []
    _l_(17898)
    str1 = _n_(17899, "str1", lambda: str1) + ' '
    _l_(17900)
    for i in _c_(17905, _n_(17901, "range", lambda: range), 0, _c_(17904, _n_(17902, "len", lambda: len), _n_(17903, "str1", lambda: str1))):
        _l_(17919)

        if _n_(17906, "str1", lambda: str1)[_n_(17907, "i", lambda: i)] != ' ':
            _l_(17918)

            word = _n_(17908, "word", lambda: word) + _n_(17909, "str1", lambda: str1)[_n_(17910, "i", lambda: i)]
            _l_(17911)
        else:
            _c_(17915, _a_(17913, _n_(17912, "all_words", lambda: all_words), "append"), _n_(17914, "word", lambda: word))
            _l_(17916)
            word = ''
            _l_(17917)
    small = large = _n_(17920, "all_words", lambda: all_words)[0]
    _l_(17921)
    for k in _c_(17926, _n_(17922, "range", lambda: range), 0, _c_(17925, _n_(17923, "len", lambda: len), _n_(17924, "all_words", lambda: all_words))):
        _l_(17949)

        if _c_(17929, _n_(17927, "len", lambda: len), _n_(17928, "small", lambda: small)) > _c_(17933, _n_(17930, "len", lambda: len), _n_(17931, "all_words", lambda: all_words)[_n_(17932, "k", lambda: k)]):
            _l_(17937)

            small = _n_(17934, "all_words", lambda: all_words)[_n_(17935, "k", lambda: k)]
            _l_(17936)
        if _c_(17940, _n_(17938, "len", lambda: len), _n_(17939, "large", lambda: large)) < _c_(17944, _n_(17941, "len", lambda: len), _n_(17942, "all_words", lambda: all_words)[_n_(17943, "k", lambda: k)]):
            _l_(17948)

            large = _n_(17945, "all_words", lambda: all_words)[_n_(17946, "k", lambda: k)]
            _l_(17947)
    aux = (_n_(17950, "small", lambda: small), _n_(17951, "large", lambda: large))
    _l_(17952)
    return aux
str1 = 'Write a Java program to sort an array of given integers using Quick sort Algorithm.'
_l_(17954)
_c_(17957, _n_(17955, "print", lambda: print), 'Original Strings:\n', _n_(17956, "str1", lambda: str1))
_l_(17958)
(small, large) = _c_(17961, _n_(17959, "smallest_largest_words", lambda: smallest_largest_words), _n_(17960, "str1", lambda: str1))
_l_(17962)
_c_(17965, _n_(17963, "print", lambda: print), 'Smallest word: ' + _n_(17964, "small", lambda: small))
_l_(17966)
_c_(17969, _n_(17967, "print", lambda: print), 'Largest word: ' + _n_(17968, "large", lambda: large))
_l_(17970)