# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60359)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60406)

    result = [_c_(60362, _n_(60360, "len", lambda: len), _n_(60361, "str1", lambda: str1))] * _c_(60365, _n_(60363, "len", lambda: len), _n_(60364, "str1", lambda: str1))
    _l_(60366)
    prev_char = -_c_(60369, _n_(60367, "len", lambda: len), _n_(60368, "str1", lambda: str1))
    _l_(60370)
    for i in _c_(60385, _a_(60372, _n_(60371, "it", lambda: it), "chain"), _c_(60377, _n_(60373, "range", lambda: range), _c_(60376, _n_(60374, "len", lambda: len), _n_(60375, "str1", lambda: str1))), _c_(60384, _n_(60378, "reversed", lambda: reversed), _c_(60383, _n_(60379, "range", lambda: range), _c_(60382, _n_(60380, "len", lambda: len), _n_(60381, "str1", lambda: str1))))):
        _l_(60403)

        if _n_(60386, "str1", lambda: str1)[_n_(60387, "i", lambda: i)] == _n_(60388, "char1", lambda: char1):
            _l_(60391)

            prev_char = _n_(60389, "i", lambda: i)
            _l_(60390)
        _n_(60392, "result", lambda: result)[_n_(60393, "i", lambda: i)] = _c_(60401, _n_(60394, "min", lambda: min), _n_(60395, "result", lambda: result)[_n_(60396, "i", lambda: i)], _c_(60400, _n_(60397, "abs", lambda: abs), _n_(60398, "i", lambda: i) - _n_(60399, "prev_char", lambda: prev_char)))
        _l_(60402)
    aux = _n_(60404, "result", lambda: result)
    _l_(60405)
    return aux
str1 = 'w3resource'
_l_(60407)
_c_(60411, _n_(60408, "print", lambda: print), 'Original string:', _n_(60409, "str1", lambda: str1), ': Specified character:', _n_(60410, "chr1", lambda: chr1))
_l_(60412)
_c_(60418, _n_(60413, "print", lambda: print), _c_(60417, _n_(60414, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60415, "str1", lambda: str1), _n_(60416, "chr1", lambda: chr1)))
_l_(60419)
str1 = 'python exercises'
_l_(60420)
chr1 = 'e'
_l_(60421)
_c_(60425, _n_(60422, "print", lambda: print), '\nOriginal string:', _n_(60423, "str1", lambda: str1), ': Specified character:', _n_(60424, "chr1", lambda: chr1))
_l_(60426)
_c_(60432, _n_(60427, "print", lambda: print), _c_(60431, _n_(60428, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60429, "str1", lambda: str1), _n_(60430, "chr1", lambda: chr1)))
_l_(60433)
str1 = 'JavaScript'
_l_(60434)
chr1 = 'S'
_l_(60435)
_c_(60439, _n_(60436, "print", lambda: print), '\nOriginal string:', _n_(60437, "str1", lambda: str1), ': Specified character:', _n_(60438, "chr1", lambda: chr1))
_l_(60440)
_c_(60446, _n_(60441, "print", lambda: print), _c_(60445, _n_(60442, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60443, "str1", lambda: str1), _n_(60444, "chr1", lambda: chr1)))
_l_(60447)