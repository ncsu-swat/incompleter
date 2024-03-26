# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(100623)

except ImportError:
    pass

def common_chars(str1, str2):
    _l_(100654)

    d1 = _c_(100626, _n_(100624, "Counter", lambda: Counter), _n_(100625, "str1", lambda: str1))
    _l_(100627)
    d2 = _c_(100630, _n_(100628, "Counter", lambda: Counter), _n_(100629, "str2", lambda: str2))
    _l_(100631)
    common_dict = _n_(100632, "d1", lambda: d1) & _n_(100633, "d2", lambda: d2)
    _l_(100634)
    if _c_(100637, _n_(100635, "len", lambda: len), _n_(100636, "common_dict", lambda: common_dict)) == 0:
        _l_(100639)

        aux = 'No common characters.'
        _l_(100638)
        return aux
    common_chars = _c_(100644, _n_(100640, "list", lambda: list), _c_(100643, _a_(100642, _n_(100641, "common_dict", lambda: common_dict), "elements")))
    _l_(100645)
    common_chars = _c_(100648, _n_(100646, "sorted", lambda: sorted), _n_(100647, "common_chars", lambda: common_chars))
    _l_(100649)
    aux = _c_(100652, _a_(100650, '', "join"), _n_(100651, "common_chars", lambda: common_chars))
    _l_(100653)
    return aux
str1 = 'Python'
_l_(100655)
_c_(100659, _n_(100656, "print", lambda: print), 'Two strings: ' + _n_(100657, "str1", lambda: str1) + ' : ' + _n_(100658, "str2", lambda: str2))
_l_(100660)
_c_(100666, _n_(100661, "print", lambda: print), _c_(100665, _n_(100662, "common_chars", lambda: common_chars), _n_(100663, "str1", lambda: str1), _n_(100664, "str2", lambda: str2)))
_l_(100667)
str1 = 'Java'
_l_(100668)
str2 = 'PHP'
_l_(100669)
_c_(100673, _n_(100670, "print", lambda: print), 'Two strings: ' + _n_(100671, "str1", lambda: str1) + ' : ' + _n_(100672, "str2", lambda: str2))
_l_(100674)
_c_(100680, _n_(100675, "print", lambda: print), _c_(100679, _n_(100676, "common_chars", lambda: common_chars), _n_(100677, "str1", lambda: str1), _n_(100678, "str2", lambda: str2)))
_l_(100681)