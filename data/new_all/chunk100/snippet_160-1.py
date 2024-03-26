# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_chars(str1, unwanted_chars):
    _l_(102886)

    for i in _n_(102877, "unwanted_chars", lambda: unwanted_chars):
        _l_(102883)

        str1 = _c_(102881, _a_(102879, _n_(102878, "str1", lambda: str1), "replace"), _n_(102880, "i", lambda: i), '')
        _l_(102882)
    aux = _n_(102884, "str1", lambda: str1)
    _l_(102885)
    return aux
str2 = 'A%^!B#*CD'
_l_(102887)
unwanted_chars = ['#', '*', '!', '^', '%']
_l_(102888)
_c_(102891, _n_(102889, "print", lambda: print), 'Original String : ' + _n_(102890, "str1", lambda: str1))
_l_(102892)
_c_(102894, _n_(102893, "print", lambda: print), 'After removing unwanted characters:')
_l_(102895)
_c_(102901, _n_(102896, "print", lambda: print), _c_(102900, _n_(102897, "remove_chars", lambda: remove_chars), _n_(102898, "str1", lambda: str1), _n_(102899, "unwanted_chars", lambda: unwanted_chars)))
_l_(102902)
_c_(102905, _n_(102903, "print", lambda: print), '\nOriginal String : ' + _n_(102904, "str2", lambda: str2))
_l_(102906)
_c_(102908, _n_(102907, "print", lambda: print), 'After removing unwanted characters:')
_l_(102909)
_c_(102915, _n_(102910, "print", lambda: print), _c_(102914, _n_(102911, "remove_chars", lambda: remove_chars), _n_(102912, "str2", lambda: str2), _n_(102913, "unwanted_chars", lambda: unwanted_chars)))
_l_(102916)