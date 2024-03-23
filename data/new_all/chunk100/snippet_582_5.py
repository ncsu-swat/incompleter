# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60626)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60673)

    result = [_c_(60629, _n_(60627, "len", lambda: len), _n_(60628, "str1", lambda: str1))] * _c_(60632, _n_(60630, "len", lambda: len), _n_(60631, "str1", lambda: str1))
    _l_(60633)
    prev_char = -_c_(60636, _n_(60634, "len", lambda: len), _n_(60635, "str1", lambda: str1))
    _l_(60637)
    for i in _c_(60652, _a_(60639, _n_(60638, "it", lambda: it), "chain"), _c_(60644, _n_(60640, "range", lambda: range), _c_(60643, _n_(60641, "len", lambda: len), _n_(60642, "str1", lambda: str1))), _c_(60651, _n_(60645, "reversed", lambda: reversed), _c_(60650, _n_(60646, "range", lambda: range), _c_(60649, _n_(60647, "len", lambda: len), _n_(60648, "str1", lambda: str1))))):
        _l_(60670)

        if _n_(60653, "str1", lambda: str1)[_n_(60654, "i", lambda: i)] == _n_(60655, "char1", lambda: char1):
            _l_(60658)

            prev_char = _n_(60656, "i", lambda: i)
            _l_(60657)
        _n_(60659, "result", lambda: result)[_n_(60660, "i", lambda: i)] = _c_(60668, _n_(60661, "min", lambda: min), _n_(60662, "result", lambda: result)[_n_(60663, "i", lambda: i)], _c_(60667, _n_(60664, "abs", lambda: abs), _n_(60665, "i", lambda: i) - _n_(60666, "prev_char", lambda: prev_char)))
        _l_(60669)
    aux = _n_(60671, "result", lambda: result)
    _l_(60672)
    return aux
str1 = 'w3resource'
_l_(60674)
chr1 = 'r'
_l_(60675)
_c_(60679, _n_(60676, "print", lambda: print), 'Original string:', _n_(60677, "str1", lambda: str1), ': Specified character:', _n_(60678, "chr1", lambda: chr1))
_l_(60680)
_c_(60686, _n_(60681, "print", lambda: print), _c_(60685, _n_(60682, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60683, "str1", lambda: str1), _n_(60684, "chr1", lambda: chr1)))
_l_(60687)
str1 = 'python exercises'
_l_(60688)
chr1 = 'e'
_l_(60689)
_c_(60693, _n_(60690, "print", lambda: print), '\nOriginal string:', _n_(60691, "str1", lambda: str1), ': Specified character:', _n_(60692, "chr1", lambda: chr1))
_l_(60694)
_c_(60700, _n_(60695, "print", lambda: print), _c_(60699, _n_(60696, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60697, "str1", lambda: str1), _n_(60698, "chr1", lambda: chr1)))
_l_(60701)
str1 = 'JavaScript'
_l_(60702)
_c_(60706, _n_(60703, "print", lambda: print), '\nOriginal string:', _n_(60704, "str1", lambda: str1), ': Specified character:', _n_(60705, "chr1", lambda: chr1))
_l_(60707)
_c_(60713, _n_(60708, "print", lambda: print), _c_(60712, _n_(60709, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60710, "str1", lambda: str1), _n_(60711, "chr1", lambda: chr1)))
_l_(60714)