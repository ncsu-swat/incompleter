# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(100683)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(100714)

    d1 = _c_(100686, _n_(100684, "Counter", lambda: Counter), _n_(100685, "str1", lambda: str1))
    _l_(100687)
    d2 = _c_(100690, _n_(100688, "Counter", lambda: Counter), _n_(100689, "str2", lambda: str2))
    _l_(100691)
    common_dict = _n_(100692, "d1", lambda: d1) & _n_(100693, "d2", lambda: d2)
    _l_(100694)
    if _c_(100697, _n_(100695, "len", lambda: len), _n_(100696, "common_dict", lambda: common_dict)) == 0:
        _l_(100699)

        aux = 'No common characters.'
        _l_(100698)
        return aux
    common_chars = _c_(100704, _n_(100700, "list", lambda: list), _c_(100703, _a_(100702, _n_(100701, "common_dict", lambda: common_dict), "elements")))
    _l_(100705)
    common_chars = _c_(100708, _n_(100706, "sorted", lambda: sorted), _n_(100707, "common_chars", lambda: common_chars))
    _l_(100709)
    aux = _c_(100712, _a_(100710, '', "join"), _n_(100711, "common_chars", lambda: common_chars))
    _l_(100713)
    return aux
str2 = 'PHP'
_l_(100715)
_c_(100719, _n_(100716, "print", lambda: print), 'Two strings: ' + _n_(100717, "str1", lambda: str1) + ' : ' + _n_(100718, "str2", lambda: str2))
_l_(100720)
_c_(100726, _n_(100721, "print", lambda: print), _c_(100725, _n_(100722, "common_chars", lambda: common_chars), _n_(100723, "str1", lambda: str1), _n_(100724, "str2", lambda: str2)))
_l_(100727)
str1 = 'Java'
_l_(100728)
str2 = 'PHP'
_l_(100729)
_c_(100733, _n_(100730, "print", lambda: print), 'Two strings: ' + _n_(100731, "str1", lambda: str1) + ' : ' + _n_(100732, "str2", lambda: str2))
_l_(100734)
_c_(100740, _n_(100735, "print", lambda: print), _c_(100739, _n_(100736, "common_chars", lambda: common_chars), _n_(100737, "str1", lambda: str1), _n_(100738, "str2", lambda: str2)))
_l_(100741)