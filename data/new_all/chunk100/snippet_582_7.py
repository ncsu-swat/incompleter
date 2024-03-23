# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60806)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60853)

    result = [_c_(60809, _n_(60807, "len", lambda: len), _n_(60808, "str1", lambda: str1))] * _c_(60812, _n_(60810, "len", lambda: len), _n_(60811, "str1", lambda: str1))
    _l_(60813)
    prev_char = -_c_(60816, _n_(60814, "len", lambda: len), _n_(60815, "str1", lambda: str1))
    _l_(60817)
    for i in _c_(60832, _a_(60819, _n_(60818, "it", lambda: it), "chain"), _c_(60824, _n_(60820, "range", lambda: range), _c_(60823, _n_(60821, "len", lambda: len), _n_(60822, "str1", lambda: str1))), _c_(60831, _n_(60825, "reversed", lambda: reversed), _c_(60830, _n_(60826, "range", lambda: range), _c_(60829, _n_(60827, "len", lambda: len), _n_(60828, "str1", lambda: str1))))):
        _l_(60850)

        if _n_(60833, "str1", lambda: str1)[_n_(60834, "i", lambda: i)] == _n_(60835, "char1", lambda: char1):
            _l_(60838)

            prev_char = _n_(60836, "i", lambda: i)
            _l_(60837)
        _n_(60839, "result", lambda: result)[_n_(60840, "i", lambda: i)] = _c_(60848, _n_(60841, "min", lambda: min), _n_(60842, "result", lambda: result)[_n_(60843, "i", lambda: i)], _c_(60847, _n_(60844, "abs", lambda: abs), _n_(60845, "i", lambda: i) - _n_(60846, "prev_char", lambda: prev_char)))
        _l_(60849)
    aux = _n_(60851, "result", lambda: result)
    _l_(60852)
    return aux
chr1 = 'r'
_l_(60854)
_c_(60858, _n_(60855, "print", lambda: print), 'Original string:', _n_(60856, "str1", lambda: str1), ': Specified character:', _n_(60857, "chr1", lambda: chr1))
_l_(60859)
_c_(60865, _n_(60860, "print", lambda: print), _c_(60864, _n_(60861, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60862, "str1", lambda: str1), _n_(60863, "chr1", lambda: chr1)))
_l_(60866)
str1 = 'python exercises'
_l_(60867)
chr1 = 'e'
_l_(60868)
_c_(60872, _n_(60869, "print", lambda: print), '\nOriginal string:', _n_(60870, "str1", lambda: str1), ': Specified character:', _n_(60871, "chr1", lambda: chr1))
_l_(60873)
_c_(60879, _n_(60874, "print", lambda: print), _c_(60878, _n_(60875, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60876, "str1", lambda: str1), _n_(60877, "chr1", lambda: chr1)))
_l_(60880)
str1 = 'JavaScript'
_l_(60881)
chr1 = 'S'
_l_(60882)
_c_(60886, _n_(60883, "print", lambda: print), '\nOriginal string:', _n_(60884, "str1", lambda: str1), ': Specified character:', _n_(60885, "chr1", lambda: chr1))
_l_(60887)
_c_(60893, _n_(60888, "print", lambda: print), _c_(60892, _n_(60889, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60890, "str1", lambda: str1), _n_(60891, "chr1", lambda: chr1)))
_l_(60894)