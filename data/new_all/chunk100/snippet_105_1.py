# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5164)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5191)

    d1 = _c_(5167, _n_(5165, "Counter", lambda: Counter), _n_(5166, "str1", lambda: str1))
    _l_(5168)
    d2 = _c_(5171, _n_(5169, "Counter", lambda: Counter), _n_(5170, "str2", lambda: str2))
    _l_(5172)
    common_dict = _n_(5173, "d1", lambda: d1) & _n_(5174, "d2", lambda: d2)
    _l_(5175)
    if _c_(5178, _n_(5176, "len", lambda: len), _n_(5177, "common_dict", lambda: common_dict)) == 0:
        _l_(5180)

        aux = 'No common characters.'
        _l_(5179)
        return aux
    common_chars = _c_(5185, _n_(5181, "list", lambda: list), _c_(5184, _a_(5183, _n_(5182, "common_dict", lambda: common_dict), "elements")))
    _l_(5186)
    aux = _c_(5189, _a_(5187, '', "join"), _n_(5188, "common_chars", lambda: common_chars))
    _l_(5190)
    return aux
str1 = 'Python'
_l_(5192)
str2 = 'PHP'
_l_(5193)
_c_(5197, _n_(5194, "print", lambda: print), 'Two strings: ' + _n_(5195, "str1", lambda: str1) + ' : ' + _n_(5196, "str2", lambda: str2))
_l_(5198)
_c_(5204, _n_(5199, "print", lambda: print), _c_(5203, _n_(5200, "common_chars", lambda: common_chars), _n_(5201, "str1", lambda: str1), _n_(5202, "str2", lambda: str2)))
_l_(5205)
str1 = 'Java'
_l_(5206)
str2 = 'PHP'
_l_(5207)
_c_(5211, _n_(5208, "print", lambda: print), 'Two strings: ' + _n_(5209, "str1", lambda: str1) + ' : ' + _n_(5210, "str2", lambda: str2))
_l_(5212)
_c_(5218, _n_(5213, "print", lambda: print), _c_(5217, _n_(5214, "common_chars", lambda: common_chars), _n_(5215, "str1", lambda: str1), _n_(5216, "str2", lambda: str2)))
_l_(5219)