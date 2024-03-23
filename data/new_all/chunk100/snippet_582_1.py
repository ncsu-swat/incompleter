# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60275)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60315)

    prev_char = -_c_(60278, _n_(60276, "len", lambda: len), _n_(60277, "str1", lambda: str1))
    _l_(60279)
    for i in _c_(60294, _a_(60281, _n_(60280, "it", lambda: it), "chain"), _c_(60286, _n_(60282, "range", lambda: range), _c_(60285, _n_(60283, "len", lambda: len), _n_(60284, "str1", lambda: str1))), _c_(60293, _n_(60287, "reversed", lambda: reversed), _c_(60292, _n_(60288, "range", lambda: range), _c_(60291, _n_(60289, "len", lambda: len), _n_(60290, "str1", lambda: str1))))):
        _l_(60312)

        if _n_(60295, "str1", lambda: str1)[_n_(60296, "i", lambda: i)] == _n_(60297, "char1", lambda: char1):
            _l_(60300)

            prev_char = _n_(60298, "i", lambda: i)
            _l_(60299)
        _n_(60301, "result", lambda: result)[_n_(60302, "i", lambda: i)] = _c_(60310, _n_(60303, "min", lambda: min), _n_(60304, "result", lambda: result)[_n_(60305, "i", lambda: i)], _c_(60309, _n_(60306, "abs", lambda: abs), _n_(60307, "i", lambda: i) - _n_(60308, "prev_char", lambda: prev_char)))
        _l_(60311)
    aux = _n_(60313, "result", lambda: result)
    _l_(60314)
    return aux
str1 = 'w3resource'
_l_(60316)
chr1 = 'r'
_l_(60317)
_c_(60321, _n_(60318, "print", lambda: print), 'Original string:', _n_(60319, "str1", lambda: str1), ': Specified character:', _n_(60320, "chr1", lambda: chr1))
_l_(60322)
_c_(60328, _n_(60323, "print", lambda: print), _c_(60327, _n_(60324, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60325, "str1", lambda: str1), _n_(60326, "chr1", lambda: chr1)))
_l_(60329)
str1 = 'python exercises'
_l_(60330)
chr1 = 'e'
_l_(60331)
_c_(60335, _n_(60332, "print", lambda: print), '\nOriginal string:', _n_(60333, "str1", lambda: str1), ': Specified character:', _n_(60334, "chr1", lambda: chr1))
_l_(60336)
_c_(60342, _n_(60337, "print", lambda: print), _c_(60341, _n_(60338, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60339, "str1", lambda: str1), _n_(60340, "chr1", lambda: chr1)))
_l_(60343)
str1 = 'JavaScript'
_l_(60344)
chr1 = 'S'
_l_(60345)
_c_(60349, _n_(60346, "print", lambda: print), '\nOriginal string:', _n_(60347, "str1", lambda: str1), ': Specified character:', _n_(60348, "chr1", lambda: chr1))
_l_(60350)
_c_(60356, _n_(60351, "print", lambda: print), _c_(60355, _n_(60352, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60353, "str1", lambda: str1), _n_(60354, "chr1", lambda: chr1)))
_l_(60357)