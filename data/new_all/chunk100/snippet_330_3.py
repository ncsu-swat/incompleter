# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(33063)

except ImportError:
    pass

def generateStrings(input):
    _l_(33085)

    str_char_ctr = _c_(33066, _n_(33064, "Counter", lambda: Counter), _n_(33065, "input", lambda: input))
    _l_(33067)
    part2 = [_n_(33068, "key", lambda: key) for (key, count) in _c_(33071, _a_(33070, _n_(33069, "str_char_ctr", lambda: str_char_ctr), "items")) if _n_(33072, "count", lambda: count) > 1]
    _l_(33073)
    _c_(33076, _a_(33075, _n_(33074, "part1", lambda: part1), "sort"))
    _l_(33077)
    _c_(33080, _a_(33079, _n_(33078, "part2", lambda: part2), "sort"))
    _l_(33081)
    aux = (_n_(33082, "part1", lambda: part1), _n_(33083, "part2", lambda: part2))
    _l_(33084)
    return aux
input = 'aabbcceffgh'
_l_(33086)
(s1, s2) = _c_(33089, _n_(33087, "generateStrings", lambda: generateStrings), _n_(33088, "input", lambda: input))
_l_(33090)
_c_(33095, _n_(33091, "print", lambda: print), _c_(33094, _a_(33092, '', "join"), _n_(33093, "s1", lambda: s1)))
_l_(33096)
_c_(33101, _n_(33097, "print", lambda: print), _c_(33100, _a_(33098, '', "join"), _n_(33099, "s2", lambda: s2)))
_l_(33102)