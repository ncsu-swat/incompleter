# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_chars(str1, unwanted_chars):
    _l_(10893)

    for i in _n_(10884, "unwanted_chars", lambda: unwanted_chars):
        _l_(10890)

        str1 = _c_(10888, _a_(10886, _n_(10885, "str1", lambda: str1), "replace"), _n_(10887, "i", lambda: i), '')
        _l_(10889)
    aux = _n_(10891, "str1", lambda: str1)
    _l_(10892)
    return aux
str1 = 'Pyth*^on Exercis^es'
_l_(10894)
str2 = 'A%^!B#*CD'
_l_(10895)
_c_(10898, _n_(10896, "print", lambda: print), 'Original String : ' + _n_(10897, "str1", lambda: str1))
_l_(10899)
_c_(10901, _n_(10900, "print", lambda: print), 'After removing unwanted characters:')
_l_(10902)
_c_(10908, _n_(10903, "print", lambda: print), _c_(10907, _n_(10904, "remove_chars", lambda: remove_chars), _n_(10905, "str1", lambda: str1), _n_(10906, "unwanted_chars", lambda: unwanted_chars)))
_l_(10909)
_c_(10912, _n_(10910, "print", lambda: print), '\nOriginal String : ' + _n_(10911, "str2", lambda: str2))
_l_(10913)
_c_(10915, _n_(10914, "print", lambda: print), 'After removing unwanted characters:')
_l_(10916)
_c_(10922, _n_(10917, "print", lambda: print), _c_(10921, _n_(10918, "remove_chars", lambda: remove_chars), _n_(10919, "str2", lambda: str2), _n_(10920, "unwanted_chars", lambda: unwanted_chars)))
_l_(10923)