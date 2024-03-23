# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60539)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60582)

    result = [_c_(60542, _n_(60540, "len", lambda: len), _n_(60541, "str1", lambda: str1))] * _c_(60545, _n_(60543, "len", lambda: len), _n_(60544, "str1", lambda: str1))
    _l_(60546)
    for i in _c_(60561, _a_(60548, _n_(60547, "it", lambda: it), "chain"), _c_(60553, _n_(60549, "range", lambda: range), _c_(60552, _n_(60550, "len", lambda: len), _n_(60551, "str1", lambda: str1))), _c_(60560, _n_(60554, "reversed", lambda: reversed), _c_(60559, _n_(60555, "range", lambda: range), _c_(60558, _n_(60556, "len", lambda: len), _n_(60557, "str1", lambda: str1))))):
        _l_(60579)

        if _n_(60562, "str1", lambda: str1)[_n_(60563, "i", lambda: i)] == _n_(60564, "char1", lambda: char1):
            _l_(60567)

            prev_char = _n_(60565, "i", lambda: i)
            _l_(60566)
        _n_(60568, "result", lambda: result)[_n_(60569, "i", lambda: i)] = _c_(60577, _n_(60570, "min", lambda: min), _n_(60571, "result", lambda: result)[_n_(60572, "i", lambda: i)], _c_(60576, _n_(60573, "abs", lambda: abs), _n_(60574, "i", lambda: i) - _n_(60575, "prev_char", lambda: prev_char)))
        _l_(60578)
    aux = _n_(60580, "result", lambda: result)
    _l_(60581)
    return aux
str1 = 'w3resource'
_l_(60583)
chr1 = 'r'
_l_(60584)
_c_(60588, _n_(60585, "print", lambda: print), 'Original string:', _n_(60586, "str1", lambda: str1), ': Specified character:', _n_(60587, "chr1", lambda: chr1))
_l_(60589)
_c_(60595, _n_(60590, "print", lambda: print), _c_(60594, _n_(60591, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60592, "str1", lambda: str1), _n_(60593, "chr1", lambda: chr1)))
_l_(60596)
str1 = 'python exercises'
_l_(60597)
chr1 = 'e'
_l_(60598)
_c_(60602, _n_(60599, "print", lambda: print), '\nOriginal string:', _n_(60600, "str1", lambda: str1), ': Specified character:', _n_(60601, "chr1", lambda: chr1))
_l_(60603)
_c_(60609, _n_(60604, "print", lambda: print), _c_(60608, _n_(60605, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60606, "str1", lambda: str1), _n_(60607, "chr1", lambda: chr1)))
_l_(60610)
str1 = 'JavaScript'
_l_(60611)
chr1 = 'S'
_l_(60612)
_c_(60616, _n_(60613, "print", lambda: print), '\nOriginal string:', _n_(60614, "str1", lambda: str1), ': Specified character:', _n_(60615, "chr1", lambda: chr1))
_l_(60617)
_c_(60623, _n_(60618, "print", lambda: print), _c_(60622, _n_(60619, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60620, "str1", lambda: str1), _n_(60621, "chr1", lambda: chr1)))
_l_(60624)