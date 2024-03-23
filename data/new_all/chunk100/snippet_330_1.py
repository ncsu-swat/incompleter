# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(32974)

except ImportError:
    pass

def generateStrings(input):
    _l_(33002)

    str_char_ctr = _c_(32977, _n_(32975, "Counter", lambda: Counter), _n_(32976, "input", lambda: input))
    _l_(32978)
    part1 = [_n_(32979, "key", lambda: key) for (key, count) in _c_(32982, _a_(32981, _n_(32980, "str_char_ctr", lambda: str_char_ctr), "items")) if _n_(32983, "count", lambda: count) == 1]
    _l_(32984)
    part2 = [_n_(32985, "key", lambda: key) for (key, count) in _c_(32988, _a_(32987, _n_(32986, "str_char_ctr", lambda: str_char_ctr), "items")) if _n_(32989, "count", lambda: count) > 1]
    _l_(32990)
    _c_(32993, _a_(32992, _n_(32991, "part1", lambda: part1), "sort"))
    _l_(32994)
    _c_(32997, _a_(32996, _n_(32995, "part2", lambda: part2), "sort"))
    _l_(32998)
    aux = (_n_(32999, "part1", lambda: part1), _n_(33000, "part2", lambda: part2))
    _l_(33001)
    return aux
(s1, s2) = _c_(33005, _n_(33003, "generateStrings", lambda: generateStrings), _n_(33004, "input", lambda: input))
_l_(33006)
_c_(33011, _n_(33007, "print", lambda: print), _c_(33010, _a_(33008, '', "join"), _n_(33009, "s1", lambda: s1)))
_l_(33012)
_c_(33017, _n_(33013, "print", lambda: print), _c_(33016, _a_(33014, '', "join"), _n_(33015, "s2", lambda: s2)))
_l_(33018)