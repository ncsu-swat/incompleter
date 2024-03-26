# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_largest_words(str1):
    _l_(105919)

    word = ''
    _l_(105863)
    all_words = []
    _l_(105864)
    str1 = _n_(105865, "str1", lambda: str1) + ' '
    _l_(105866)
    for i in _c_(105871, _n_(105867, "range", lambda: range), 0, _c_(105870, _n_(105868, "len", lambda: len), _n_(105869, "str1", lambda: str1))):
        _l_(105885)

        if _n_(105872, "str1", lambda: str1)[_n_(105873, "i", lambda: i)] != ' ':
            _l_(105884)

            word = _n_(105874, "word", lambda: word) + _n_(105875, "str1", lambda: str1)[_n_(105876, "i", lambda: i)]
            _l_(105877)
        else:
            _c_(105881, _a_(105879, _n_(105878, "all_words", lambda: all_words), "append"), _n_(105880, "word", lambda: word))
            _l_(105882)
            word = ''
            _l_(105883)
    small = large = _n_(105886, "all_words", lambda: all_words)[0]
    _l_(105887)
    for k in _c_(105892, _n_(105888, "range", lambda: range), 0, _c_(105891, _n_(105889, "len", lambda: len), _n_(105890, "all_words", lambda: all_words))):
        _l_(105915)

        if _c_(105895, _n_(105893, "len", lambda: len), _n_(105894, "small", lambda: small)) > _c_(105899, _n_(105896, "len", lambda: len), _n_(105897, "all_words", lambda: all_words)[_n_(105898, "k", lambda: k)]):
            _l_(105903)

            small = _n_(105900, "all_words", lambda: all_words)[_n_(105901, "k", lambda: k)]
            _l_(105902)
        if _c_(105906, _n_(105904, "len", lambda: len), _n_(105905, "large", lambda: large)) < _c_(105910, _n_(105907, "len", lambda: len), _n_(105908, "all_words", lambda: all_words)[_n_(105909, "k", lambda: k)]):
            _l_(105914)

            large = _n_(105911, "all_words", lambda: all_words)[_n_(105912, "k", lambda: k)]
            _l_(105913)
    aux = (_n_(105916, "small", lambda: small), _n_(105917, "large", lambda: large))
    _l_(105918)
    return aux
_c_(105922, _n_(105920, "print", lambda: print), 'Original Strings:\n', _n_(105921, "str1", lambda: str1))
_l_(105923)
small, large = _c_(105926, _n_(105924, "smallest_largest_words", lambda: smallest_largest_words), _n_(105925, "str1", lambda: str1))
_l_(105927)
_c_(105930, _n_(105928, "print", lambda: print), 'Smallest word: ' + _n_(105929, "small", lambda: small))
_l_(105931)
_c_(105934, _n_(105932, "print", lambda: print), 'Largest word: ' + _n_(105933, "large", lambda: large))
_l_(105935)