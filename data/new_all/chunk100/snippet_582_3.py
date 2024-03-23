# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60449)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60496)

    result = [_c_(60452, _n_(60450, "len", lambda: len), _n_(60451, "str1", lambda: str1))] * _c_(60455, _n_(60453, "len", lambda: len), _n_(60454, "str1", lambda: str1))
    _l_(60456)
    prev_char = -_c_(60459, _n_(60457, "len", lambda: len), _n_(60458, "str1", lambda: str1))
    _l_(60460)
    for i in _c_(60475, _a_(60462, _n_(60461, "it", lambda: it), "chain"), _c_(60467, _n_(60463, "range", lambda: range), _c_(60466, _n_(60464, "len", lambda: len), _n_(60465, "str1", lambda: str1))), _c_(60474, _n_(60468, "reversed", lambda: reversed), _c_(60473, _n_(60469, "range", lambda: range), _c_(60472, _n_(60470, "len", lambda: len), _n_(60471, "str1", lambda: str1))))):
        _l_(60493)

        if _n_(60476, "str1", lambda: str1)[_n_(60477, "i", lambda: i)] == _n_(60478, "char1", lambda: char1):
            _l_(60481)

            prev_char = _n_(60479, "i", lambda: i)
            _l_(60480)
        _n_(60482, "result", lambda: result)[_n_(60483, "i", lambda: i)] = _c_(60491, _n_(60484, "min", lambda: min), _n_(60485, "result", lambda: result)[_n_(60486, "i", lambda: i)], _c_(60490, _n_(60487, "abs", lambda: abs), _n_(60488, "i", lambda: i) - _n_(60489, "prev_char", lambda: prev_char)))
        _l_(60492)
    aux = _n_(60494, "result", lambda: result)
    _l_(60495)
    return aux
str1 = 'w3resource'
_l_(60497)
chr1 = 'r'
_l_(60498)
_c_(60502, _n_(60499, "print", lambda: print), 'Original string:', _n_(60500, "str1", lambda: str1), ': Specified character:', _n_(60501, "chr1", lambda: chr1))
_l_(60503)
_c_(60509, _n_(60504, "print", lambda: print), _c_(60508, _n_(60505, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60506, "str1", lambda: str1), _n_(60507, "chr1", lambda: chr1)))
_l_(60510)
str1 = 'python exercises'
_l_(60511)
_c_(60515, _n_(60512, "print", lambda: print), '\nOriginal string:', _n_(60513, "str1", lambda: str1), ': Specified character:', _n_(60514, "chr1", lambda: chr1))
_l_(60516)
_c_(60522, _n_(60517, "print", lambda: print), _c_(60521, _n_(60518, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60519, "str1", lambda: str1), _n_(60520, "chr1", lambda: chr1)))
_l_(60523)
str1 = 'JavaScript'
_l_(60524)
chr1 = 'S'
_l_(60525)
_c_(60529, _n_(60526, "print", lambda: print), '\nOriginal string:', _n_(60527, "str1", lambda: str1), ': Specified character:', _n_(60528, "chr1", lambda: chr1))
_l_(60530)
_c_(60536, _n_(60531, "print", lambda: print), _c_(60535, _n_(60532, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60533, "str1", lambda: str1), _n_(60534, "chr1", lambda: chr1)))
_l_(60537)