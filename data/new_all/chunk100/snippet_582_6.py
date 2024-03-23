# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60716)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60763)

    result = [_c_(60719, _n_(60717, "len", lambda: len), _n_(60718, "str1", lambda: str1))] * _c_(60722, _n_(60720, "len", lambda: len), _n_(60721, "str1", lambda: str1))
    _l_(60723)
    prev_char = -_c_(60726, _n_(60724, "len", lambda: len), _n_(60725, "str1", lambda: str1))
    _l_(60727)
    for i in _c_(60742, _a_(60729, _n_(60728, "it", lambda: it), "chain"), _c_(60734, _n_(60730, "range", lambda: range), _c_(60733, _n_(60731, "len", lambda: len), _n_(60732, "str1", lambda: str1))), _c_(60741, _n_(60735, "reversed", lambda: reversed), _c_(60740, _n_(60736, "range", lambda: range), _c_(60739, _n_(60737, "len", lambda: len), _n_(60738, "str1", lambda: str1))))):
        _l_(60760)

        if _n_(60743, "str1", lambda: str1)[_n_(60744, "i", lambda: i)] == _n_(60745, "char1", lambda: char1):
            _l_(60748)

            prev_char = _n_(60746, "i", lambda: i)
            _l_(60747)
        _n_(60749, "result", lambda: result)[_n_(60750, "i", lambda: i)] = _c_(60758, _n_(60751, "min", lambda: min), _n_(60752, "result", lambda: result)[_n_(60753, "i", lambda: i)], _c_(60757, _n_(60754, "abs", lambda: abs), _n_(60755, "i", lambda: i) - _n_(60756, "prev_char", lambda: prev_char)))
        _l_(60759)
    aux = _n_(60761, "result", lambda: result)
    _l_(60762)
    return aux
str1 = 'w3resource'
_l_(60764)
chr1 = 'r'
_l_(60765)
_c_(60769, _n_(60766, "print", lambda: print), 'Original string:', _n_(60767, "str1", lambda: str1), ': Specified character:', _n_(60768, "chr1", lambda: chr1))
_l_(60770)
_c_(60776, _n_(60771, "print", lambda: print), _c_(60775, _n_(60772, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60773, "str1", lambda: str1), _n_(60774, "chr1", lambda: chr1)))
_l_(60777)
chr1 = 'e'
_l_(60778)
_c_(60782, _n_(60779, "print", lambda: print), '\nOriginal string:', _n_(60780, "str1", lambda: str1), ': Specified character:', _n_(60781, "chr1", lambda: chr1))
_l_(60783)
_c_(60789, _n_(60784, "print", lambda: print), _c_(60788, _n_(60785, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60786, "str1", lambda: str1), _n_(60787, "chr1", lambda: chr1)))
_l_(60790)
str1 = 'JavaScript'
_l_(60791)
chr1 = 'S'
_l_(60792)
_c_(60796, _n_(60793, "print", lambda: print), '\nOriginal string:', _n_(60794, "str1", lambda: str1), ': Specified character:', _n_(60795, "chr1", lambda: chr1))
_l_(60797)
_c_(60803, _n_(60798, "print", lambda: print), _c_(60802, _n_(60799, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60800, "str1", lambda: str1), _n_(60801, "chr1", lambda: chr1)))
_l_(60804)