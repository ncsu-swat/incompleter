# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(5104)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(5135)

    d1 = _c_(5107, _n_(5105, "Counter", lambda: Counter), _n_(5106, "str1", lambda: str1))
    _l_(5108)
    d2 = _c_(5111, _n_(5109, "Counter", lambda: Counter), _n_(5110, "str2", lambda: str2))
    _l_(5112)
    common_dict = _n_(5113, "d1", lambda: d1) & _n_(5114, "d2", lambda: d2)
    _l_(5115)
    if _c_(5118, _n_(5116, "len", lambda: len), _n_(5117, "common_dict", lambda: common_dict)) == 0:
        _l_(5120)

        aux = 'No common characters.'
        _l_(5119)
        return aux
    common_chars = _c_(5125, _n_(5121, "list", lambda: list), _c_(5124, _a_(5123, _n_(5122, "common_dict", lambda: common_dict), "elements")))
    _l_(5126)
    common_chars = _c_(5129, _n_(5127, "sorted", lambda: sorted), _n_(5128, "common_chars", lambda: common_chars))
    _l_(5130)
    aux = _c_(5133, _a_(5131, '', "join"), _n_(5132, "common_chars", lambda: common_chars))
    _l_(5134)
    return aux
str1 = 'Python'
_l_(5136)
str2 = 'PHP'
_l_(5137)
_c_(5141, _n_(5138, "print", lambda: print), 'Two strings: ' + _n_(5139, "str1", lambda: str1) + ' : ' + _n_(5140, "str2", lambda: str2))
_l_(5142)
_c_(5148, _n_(5143, "print", lambda: print), _c_(5147, _n_(5144, "common_chars", lambda: common_chars), _n_(5145, "str1", lambda: str1), _n_(5146, "str2", lambda: str2)))
_l_(5149)
str2 = 'PHP'
_l_(5150)
_c_(5154, _n_(5151, "print", lambda: print), 'Two strings: ' + _n_(5152, "str1", lambda: str1) + ' : ' + _n_(5153, "str2", lambda: str2))
_l_(5155)
_c_(5161, _n_(5156, "print", lambda: print), _c_(5160, _n_(5157, "common_chars", lambda: common_chars), _n_(5158, "str1", lambda: str1), _n_(5159, "str2", lambda: str2)))
_l_(5162)