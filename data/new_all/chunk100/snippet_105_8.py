# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5568)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5599)

    d1 = _c_(5571, _n_(5569, "Counter", lambda: Counter), _n_(5570, "str1", lambda: str1))
    _l_(5572)
    d2 = _c_(5575, _n_(5573, "Counter", lambda: Counter), _n_(5574, "str2", lambda: str2))
    _l_(5576)
    common_dict = _n_(5577, "d1", lambda: d1) & _n_(5578, "d2", lambda: d2)
    _l_(5579)
    if _c_(5582, _n_(5580, "len", lambda: len), _n_(5581, "common_dict", lambda: common_dict)) == 0:
        _l_(5584)

        aux = 'No common characters.'
        _l_(5583)
        return aux
    common_chars = _c_(5589, _n_(5585, "list", lambda: list), _c_(5588, _a_(5587, _n_(5586, "common_dict", lambda: common_dict), "elements")))
    _l_(5590)
    common_chars = _c_(5593, _n_(5591, "sorted", lambda: sorted), _n_(5592, "common_chars", lambda: common_chars))
    _l_(5594)
    aux = _c_(5597, _a_(5595, '', "join"), _n_(5596, "common_chars", lambda: common_chars))
    _l_(5598)
    return aux
str1 = 'Python'
_l_(5600)
str2 = 'PHP'
_l_(5601)
_c_(5605, _n_(5602, "print", lambda: print), 'Two strings: ' + _n_(5603, "str1", lambda: str1) + ' : ' + _n_(5604, "str2", lambda: str2))
_l_(5606)
_c_(5612, _n_(5607, "print", lambda: print), _c_(5611, _n_(5608, "common_chars", lambda: common_chars), _n_(5609, "str1", lambda: str1), _n_(5610, "str2", lambda: str2)))
_l_(5613)
str1 = 'Java'
_l_(5614)
_c_(5618, _n_(5615, "print", lambda: print), 'Two strings: ' + _n_(5616, "str1", lambda: str1) + ' : ' + _n_(5617, "str2", lambda: str2))
_l_(5619)
_c_(5625, _n_(5620, "print", lambda: print), _c_(5624, _n_(5621, "common_chars", lambda: common_chars), _n_(5622, "str1", lambda: str1), _n_(5623, "str2", lambda: str2)))
_l_(5626)