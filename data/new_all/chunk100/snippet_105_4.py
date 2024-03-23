# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5335)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5360)

    d1 = _c_(5338, _n_(5336, "Counter", lambda: Counter), _n_(5337, "str1", lambda: str1))
    _l_(5339)
    d2 = _c_(5342, _n_(5340, "Counter", lambda: Counter), _n_(5341, "str2", lambda: str2))
    _l_(5343)
    common_dict = _n_(5344, "d1", lambda: d1) & _n_(5345, "d2", lambda: d2)
    _l_(5346)
    if _c_(5349, _n_(5347, "len", lambda: len), _n_(5348, "common_dict", lambda: common_dict)) == 0:
        _l_(5351)

        aux = 'No common characters.'
        _l_(5350)
        return aux
    common_chars = _c_(5354, _n_(5352, "sorted", lambda: sorted), _n_(5353, "common_chars", lambda: common_chars))
    _l_(5355)
    aux = _c_(5358, _a_(5356, '', "join"), _n_(5357, "common_chars", lambda: common_chars))
    _l_(5359)
    return aux
str1 = 'Python'
_l_(5361)
str2 = 'PHP'
_l_(5362)
_c_(5366, _n_(5363, "print", lambda: print), 'Two strings: ' + _n_(5364, "str1", lambda: str1) + ' : ' + _n_(5365, "str2", lambda: str2))
_l_(5367)
_c_(5373, _n_(5368, "print", lambda: print), _c_(5372, _n_(5369, "common_chars", lambda: common_chars), _n_(5370, "str1", lambda: str1), _n_(5371, "str2", lambda: str2)))
_l_(5374)
str1 = 'Java'
_l_(5375)
str2 = 'PHP'
_l_(5376)
_c_(5380, _n_(5377, "print", lambda: print), 'Two strings: ' + _n_(5378, "str1", lambda: str1) + ' : ' + _n_(5379, "str2", lambda: str2))
_l_(5381)
_c_(5387, _n_(5382, "print", lambda: print), _c_(5386, _n_(5383, "common_chars", lambda: common_chars), _n_(5384, "str1", lambda: str1), _n_(5385, "str2", lambda: str2)))
_l_(5388)