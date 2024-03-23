# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5390)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5418)

    d1 = _c_(5393, _n_(5391, "Counter", lambda: Counter), _n_(5392, "str1", lambda: str1))
    _l_(5394)
    d2 = _c_(5397, _n_(5395, "Counter", lambda: Counter), _n_(5396, "str2", lambda: str2))
    _l_(5398)
    if _c_(5401, _n_(5399, "len", lambda: len), _n_(5400, "common_dict", lambda: common_dict)) == 0:
        _l_(5403)

        aux = 'No common characters.'
        _l_(5402)
        return aux
    common_chars = _c_(5408, _n_(5404, "list", lambda: list), _c_(5407, _a_(5406, _n_(5405, "common_dict", lambda: common_dict), "elements")))
    _l_(5409)
    common_chars = _c_(5412, _n_(5410, "sorted", lambda: sorted), _n_(5411, "common_chars", lambda: common_chars))
    _l_(5413)
    aux = _c_(5416, _a_(5414, '', "join"), _n_(5415, "common_chars", lambda: common_chars))
    _l_(5417)
    return aux
str1 = 'Python'
_l_(5419)
str2 = 'PHP'
_l_(5420)
_c_(5424, _n_(5421, "print", lambda: print), 'Two strings: ' + _n_(5422, "str1", lambda: str1) + ' : ' + _n_(5423, "str2", lambda: str2))
_l_(5425)
_c_(5431, _n_(5426, "print", lambda: print), _c_(5430, _n_(5427, "common_chars", lambda: common_chars), _n_(5428, "str1", lambda: str1), _n_(5429, "str2", lambda: str2)))
_l_(5432)
str1 = 'Java'
_l_(5433)
str2 = 'PHP'
_l_(5434)
_c_(5438, _n_(5435, "print", lambda: print), 'Two strings: ' + _n_(5436, "str1", lambda: str1) + ' : ' + _n_(5437, "str2", lambda: str2))
_l_(5439)
_c_(5445, _n_(5440, "print", lambda: print), _c_(5444, _n_(5441, "common_chars", lambda: common_chars), _n_(5442, "str1", lambda: str1), _n_(5443, "str2", lambda: str2)))
_l_(5446)