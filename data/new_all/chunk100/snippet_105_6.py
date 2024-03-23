# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5448)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5479)

    d1 = _c_(5451, _n_(5449, "Counter", lambda: Counter), _n_(5450, "str1", lambda: str1))
    _l_(5452)
    d2 = _c_(5455, _n_(5453, "Counter", lambda: Counter), _n_(5454, "str2", lambda: str2))
    _l_(5456)
    common_dict = _n_(5457, "d1", lambda: d1) & _n_(5458, "d2", lambda: d2)
    _l_(5459)
    if _c_(5462, _n_(5460, "len", lambda: len), _n_(5461, "common_dict", lambda: common_dict)) == 0:
        _l_(5464)

        aux = 'No common characters.'
        _l_(5463)
        return aux
    common_chars = _c_(5469, _n_(5465, "list", lambda: list), _c_(5468, _a_(5467, _n_(5466, "common_dict", lambda: common_dict), "elements")))
    _l_(5470)
    common_chars = _c_(5473, _n_(5471, "sorted", lambda: sorted), _n_(5472, "common_chars", lambda: common_chars))
    _l_(5474)
    aux = _c_(5477, _a_(5475, '', "join"), _n_(5476, "common_chars", lambda: common_chars))
    _l_(5478)
    return aux
str2 = 'PHP'
_l_(5480)
_c_(5484, _n_(5481, "print", lambda: print), 'Two strings: ' + _n_(5482, "str1", lambda: str1) + ' : ' + _n_(5483, "str2", lambda: str2))
_l_(5485)
_c_(5491, _n_(5486, "print", lambda: print), _c_(5490, _n_(5487, "common_chars", lambda: common_chars), _n_(5488, "str1", lambda: str1), _n_(5489, "str2", lambda: str2)))
_l_(5492)
str1 = 'Java'
_l_(5493)
str2 = 'PHP'
_l_(5494)
_c_(5498, _n_(5495, "print", lambda: print), 'Two strings: ' + _n_(5496, "str1", lambda: str1) + ' : ' + _n_(5497, "str2", lambda: str2))
_l_(5499)
_c_(5505, _n_(5500, "print", lambda: print), _c_(5504, _n_(5501, "common_chars", lambda: common_chars), _n_(5502, "str1", lambda: str1), _n_(5503, "str2", lambda: str2)))
_l_(5506)