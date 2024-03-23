# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5278)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5305)

    d1 = _c_(5281, _n_(5279, "Counter", lambda: Counter), _n_(5280, "str1", lambda: str1))
    _l_(5282)
    common_dict = _n_(5283, "d1", lambda: d1) & _n_(5284, "d2", lambda: d2)
    _l_(5285)
    if _c_(5288, _n_(5286, "len", lambda: len), _n_(5287, "common_dict", lambda: common_dict)) == 0:
        _l_(5290)

        aux = 'No common characters.'
        _l_(5289)
        return aux
    common_chars = _c_(5295, _n_(5291, "list", lambda: list), _c_(5294, _a_(5293, _n_(5292, "common_dict", lambda: common_dict), "elements")))
    _l_(5296)
    common_chars = _c_(5299, _n_(5297, "sorted", lambda: sorted), _n_(5298, "common_chars", lambda: common_chars))
    _l_(5300)
    aux = _c_(5303, _a_(5301, '', "join"), _n_(5302, "common_chars", lambda: common_chars))
    _l_(5304)
    return aux
str1 = 'Python'
_l_(5306)
str2 = 'PHP'
_l_(5307)
_c_(5311, _n_(5308, "print", lambda: print), 'Two strings: ' + _n_(5309, "str1", lambda: str1) + ' : ' + _n_(5310, "str2", lambda: str2))
_l_(5312)
_c_(5318, _n_(5313, "print", lambda: print), _c_(5317, _n_(5314, "common_chars", lambda: common_chars), _n_(5315, "str1", lambda: str1), _n_(5316, "str2", lambda: str2)))
_l_(5319)
str1 = 'Java'
_l_(5320)
str2 = 'PHP'
_l_(5321)
_c_(5325, _n_(5322, "print", lambda: print), 'Two strings: ' + _n_(5323, "str1", lambda: str1) + ' : ' + _n_(5324, "str2", lambda: str2))
_l_(5326)
_c_(5332, _n_(5327, "print", lambda: print), _c_(5331, _n_(5328, "common_chars", lambda: common_chars), _n_(5329, "str1", lambda: str1), _n_(5330, "str2", lambda: str2)))
_l_(5333)