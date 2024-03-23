# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(32933)

except ImportError:
    pass

def generateStrings(input):
    _l_(32955)

    str_char_ctr = _c_(32936, _n_(32934, "Counter", lambda: Counter), _n_(32935, "input", lambda: input))
    _l_(32937)
    part1 = [_n_(32938, "key", lambda: key) for (key, count) in _c_(32941, _a_(32940, _n_(32939, "str_char_ctr", lambda: str_char_ctr), "items")) if _n_(32942, "count", lambda: count) == 1]
    _l_(32943)
    _c_(32946, _a_(32945, _n_(32944, "part1", lambda: part1), "sort"))
    _l_(32947)
    _c_(32950, _a_(32949, _n_(32948, "part2", lambda: part2), "sort"))
    _l_(32951)
    aux = (_n_(32952, "part1", lambda: part1), _n_(32953, "part2", lambda: part2))
    _l_(32954)
    return aux
input = 'aabbcceffgh'
_l_(32956)
(s1, s2) = _c_(32959, _n_(32957, "generateStrings", lambda: generateStrings), _n_(32958, "input", lambda: input))
_l_(32960)
_c_(32965, _n_(32961, "print", lambda: print), _c_(32964, _a_(32962, '', "join"), _n_(32963, "s1", lambda: s1)))
_l_(32966)
_c_(32971, _n_(32967, "print", lambda: print), _c_(32970, _a_(32968, '', "join"), _n_(32969, "s2", lambda: s2)))
_l_(32972)