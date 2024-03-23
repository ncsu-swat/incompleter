# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5508)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5539)

    d1 = _c_(5511, _n_(5509, "Counter", lambda: Counter), _n_(5510, "str1", lambda: str1))
    _l_(5512)
    d2 = _c_(5515, _n_(5513, "Counter", lambda: Counter), _n_(5514, "str2", lambda: str2))
    _l_(5516)
    common_dict = _n_(5517, "d1", lambda: d1) & _n_(5518, "d2", lambda: d2)
    _l_(5519)
    if _c_(5522, _n_(5520, "len", lambda: len), _n_(5521, "common_dict", lambda: common_dict)) == 0:
        _l_(5524)

        aux = 'No common characters.'
        _l_(5523)
        return aux
    common_chars = _c_(5529, _n_(5525, "list", lambda: list), _c_(5528, _a_(5527, _n_(5526, "common_dict", lambda: common_dict), "elements")))
    _l_(5530)
    common_chars = _c_(5533, _n_(5531, "sorted", lambda: sorted), _n_(5532, "common_chars", lambda: common_chars))
    _l_(5534)
    aux = _c_(5537, _a_(5535, '', "join"), _n_(5536, "common_chars", lambda: common_chars))
    _l_(5538)
    return aux
str1 = 'Python'
_l_(5540)
_c_(5544, _n_(5541, "print", lambda: print), 'Two strings: ' + _n_(5542, "str1", lambda: str1) + ' : ' + _n_(5543, "str2", lambda: str2))
_l_(5545)
_c_(5551, _n_(5546, "print", lambda: print), _c_(5550, _n_(5547, "common_chars", lambda: common_chars), _n_(5548, "str1", lambda: str1), _n_(5549, "str2", lambda: str2)))
_l_(5552)
str1 = 'Java'
_l_(5553)
str2 = 'PHP'
_l_(5554)
_c_(5558, _n_(5555, "print", lambda: print), 'Two strings: ' + _n_(5556, "str1", lambda: str1) + ' : ' + _n_(5557, "str2", lambda: str2))
_l_(5559)
_c_(5565, _n_(5560, "print", lambda: print), _c_(5564, _n_(5561, "common_chars", lambda: common_chars), _n_(5562, "str1", lambda: str1), _n_(5563, "str2", lambda: str2)))
_l_(5566)