# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(60896)

except ImportError:
    pass

def char_shortest_distancer(str1, char1):
    _l_(60943)

    result = [_c_(60899, _n_(60897, "len", lambda: len), _n_(60898, "str1", lambda: str1))] * _c_(60902, _n_(60900, "len", lambda: len), _n_(60901, "str1", lambda: str1))
    _l_(60903)
    prev_char = -_c_(60906, _n_(60904, "len", lambda: len), _n_(60905, "str1", lambda: str1))
    _l_(60907)
    for i in _c_(60922, _a_(60909, _n_(60908, "it", lambda: it), "chain"), _c_(60914, _n_(60910, "range", lambda: range), _c_(60913, _n_(60911, "len", lambda: len), _n_(60912, "str1", lambda: str1))), _c_(60921, _n_(60915, "reversed", lambda: reversed), _c_(60920, _n_(60916, "range", lambda: range), _c_(60919, _n_(60917, "len", lambda: len), _n_(60918, "str1", lambda: str1))))):
        _l_(60940)

        if _n_(60923, "str1", lambda: str1)[_n_(60924, "i", lambda: i)] == _n_(60925, "char1", lambda: char1):
            _l_(60928)

            prev_char = _n_(60926, "i", lambda: i)
            _l_(60927)
        _n_(60929, "result", lambda: result)[_n_(60930, "i", lambda: i)] = _c_(60938, _n_(60931, "min", lambda: min), _n_(60932, "result", lambda: result)[_n_(60933, "i", lambda: i)], _c_(60937, _n_(60934, "abs", lambda: abs), _n_(60935, "i", lambda: i) - _n_(60936, "prev_char", lambda: prev_char)))
        _l_(60939)
    aux = _n_(60941, "result", lambda: result)
    _l_(60942)
    return aux
str1 = 'w3resource'
_l_(60944)
chr1 = 'r'
_l_(60945)
_c_(60949, _n_(60946, "print", lambda: print), 'Original string:', _n_(60947, "str1", lambda: str1), ': Specified character:', _n_(60948, "chr1", lambda: chr1))
_l_(60950)
_c_(60956, _n_(60951, "print", lambda: print), _c_(60955, _n_(60952, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60953, "str1", lambda: str1), _n_(60954, "chr1", lambda: chr1)))
_l_(60957)
str1 = 'python exercises'
_l_(60958)
chr1 = 'e'
_l_(60959)
_c_(60963, _n_(60960, "print", lambda: print), '\nOriginal string:', _n_(60961, "str1", lambda: str1), ': Specified character:', _n_(60962, "chr1", lambda: chr1))
_l_(60964)
_c_(60970, _n_(60965, "print", lambda: print), _c_(60969, _n_(60966, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60967, "str1", lambda: str1), _n_(60968, "chr1", lambda: chr1)))
_l_(60971)
chr1 = 'S'
_l_(60972)
_c_(60976, _n_(60973, "print", lambda: print), '\nOriginal string:', _n_(60974, "str1", lambda: str1), ': Specified character:', _n_(60975, "chr1", lambda: chr1))
_l_(60977)
_c_(60983, _n_(60978, "print", lambda: print), _c_(60982, _n_(60979, "char_shortest_distancer", lambda: char_shortest_distancer), _n_(60980, "str1", lambda: str1), _n_(60981, "chr1", lambda: chr1)))
_l_(60984)