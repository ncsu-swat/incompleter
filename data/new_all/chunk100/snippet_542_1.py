# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(54458)

except ImportError:
    pass

def max_sub_string(str1):
    _l_(54471)

    aux = _c_(54469, _n_(54459, "max", lambda: max), (_c_(54464, _n_(54460, "len", lambda: len), _c_(54463, _n_(54461, "list", lambda: list), _n_(54462, "x", lambda: x))) for (_, x) in _c_(54468, _a_(54466, _n_(54465, "itertools", lambda: itertools), "groupby"), _n_(54467, "str1", lambda: str1))))
    _l_(54470)
    return aux
_c_(54474, _n_(54472, "print", lambda: print), 'Original string:', _n_(54473, "str1", lambda: str1))
_l_(54475)
_c_(54477, _n_(54476, "print", lambda: print), 'Maximum length of a substring with unique characters of the said string:')
_l_(54478)
_c_(54483, _n_(54479, "print", lambda: print), _c_(54482, _n_(54480, "max_sub_string", lambda: max_sub_string), _n_(54481, "str1", lambda: str1)))
_l_(54484)
str1 = 'c++ exercises'
_l_(54485)
_c_(54488, _n_(54486, "print", lambda: print), '\nOriginal string:', _n_(54487, "str1", lambda: str1))
_l_(54489)
_c_(54491, _n_(54490, "print", lambda: print), 'Maximum length of a substring with unique characters of the said string:')
_l_(54492)
_c_(54497, _n_(54493, "print", lambda: print), _c_(54496, _n_(54494, "max_sub_string", lambda: max_sub_string), _n_(54495, "str1", lambda: str1)))
_l_(54498)