# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(54416)

except ImportError:
    pass

def max_sub_string(str1):
    _l_(54429)

    aux = _c_(54427, _n_(54417, "max", lambda: max), (_c_(54422, _n_(54418, "len", lambda: len), _c_(54421, _n_(54419, "list", lambda: list), _n_(54420, "x", lambda: x))) for (_, x) in _c_(54426, _a_(54424, _n_(54423, "itertools", lambda: itertools), "groupby"), _n_(54425, "str1", lambda: str1))))
    _l_(54428)
    return aux
str1 = 'aaabbccddeeeee'
_l_(54430)
_c_(54433, _n_(54431, "print", lambda: print), 'Original string:', _n_(54432, "str1", lambda: str1))
_l_(54434)
_c_(54436, _n_(54435, "print", lambda: print), 'Maximum length of a substring with unique characters of the said string:')
_l_(54437)
_c_(54442, _n_(54438, "print", lambda: print), _c_(54441, _n_(54439, "max_sub_string", lambda: max_sub_string), _n_(54440, "str1", lambda: str1)))
_l_(54443)
_c_(54446, _n_(54444, "print", lambda: print), '\nOriginal string:', _n_(54445, "str1", lambda: str1))
_l_(54447)
_c_(54449, _n_(54448, "print", lambda: print), 'Maximum length of a substring with unique characters of the said string:')
_l_(54450)
_c_(54455, _n_(54451, "print", lambda: print), _c_(54454, _n_(54452, "max_sub_string", lambda: max_sub_string), _n_(54453, "str1", lambda: str1)))
_l_(54456)