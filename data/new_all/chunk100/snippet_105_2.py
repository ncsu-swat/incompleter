# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5221)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5248)

    d2 = _c_(5224, _n_(5222, "Counter", lambda: Counter), _n_(5223, "str2", lambda: str2))
    _l_(5225)
    common_dict = _n_(5226, "d1", lambda: d1) & _n_(5227, "d2", lambda: d2)
    _l_(5228)
    if _c_(5231, _n_(5229, "len", lambda: len), _n_(5230, "common_dict", lambda: common_dict)) == 0:
        _l_(5233)

        aux = 'No common characters.'
        _l_(5232)
        return aux
    common_chars = _c_(5238, _n_(5234, "list", lambda: list), _c_(5237, _a_(5236, _n_(5235, "common_dict", lambda: common_dict), "elements")))
    _l_(5239)
    common_chars = _c_(5242, _n_(5240, "sorted", lambda: sorted), _n_(5241, "common_chars", lambda: common_chars))
    _l_(5243)
    aux = _c_(5246, _a_(5244, '', "join"), _n_(5245, "common_chars", lambda: common_chars))
    _l_(5247)
    return aux
str1 = 'Python'
_l_(5249)
str2 = 'PHP'
_l_(5250)
_c_(5254, _n_(5251, "print", lambda: print), 'Two strings: ' + _n_(5252, "str1", lambda: str1) + ' : ' + _n_(5253, "str2", lambda: str2))
_l_(5255)
_c_(5261, _n_(5256, "print", lambda: print), _c_(5260, _n_(5257, "common_chars", lambda: common_chars), _n_(5258, "str1", lambda: str1), _n_(5259, "str2", lambda: str2)))
_l_(5262)
str1 = 'Java'
_l_(5263)
str2 = 'PHP'
_l_(5264)
_c_(5268, _n_(5265, "print", lambda: print), 'Two strings: ' + _n_(5266, "str1", lambda: str1) + ' : ' + _n_(5267, "str2", lambda: str2))
_l_(5269)
_c_(5275, _n_(5270, "print", lambda: print), _c_(5274, _n_(5271, "common_chars", lambda: common_chars), _n_(5272, "str1", lambda: str1), _n_(5273, "str2", lambda: str2)))
_l_(5276)