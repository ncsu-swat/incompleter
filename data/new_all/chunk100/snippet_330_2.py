# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(33020)

except ImportError:
    pass

def generateStrings(input):
    _l_(33044)

    part1 = [_n_(33021, "key", lambda: key) for (key, count) in _c_(33024, _a_(33023, _n_(33022, "str_char_ctr", lambda: str_char_ctr), "items")) if _n_(33025, "count", lambda: count) == 1]
    _l_(33026)
    part2 = [_n_(33027, "key", lambda: key) for (key, count) in _c_(33030, _a_(33029, _n_(33028, "str_char_ctr", lambda: str_char_ctr), "items")) if _n_(33031, "count", lambda: count) > 1]
    _l_(33032)
    _c_(33035, _a_(33034, _n_(33033, "part1", lambda: part1), "sort"))
    _l_(33036)
    _c_(33039, _a_(33038, _n_(33037, "part2", lambda: part2), "sort"))
    _l_(33040)
    aux = (_n_(33041, "part1", lambda: part1), _n_(33042, "part2", lambda: part2))
    _l_(33043)
    return aux
input = 'aabbcceffgh'
_l_(33045)
(s1, s2) = _c_(33048, _n_(33046, "generateStrings", lambda: generateStrings), _n_(33047, "input", lambda: input))
_l_(33049)
_c_(33054, _n_(33050, "print", lambda: print), _c_(33053, _a_(33051, '', "join"), _n_(33052, "s1", lambda: s1)))
_l_(33055)
_c_(33060, _n_(33056, "print", lambda: print), _c_(33059, _a_(33057, '', "join"), _n_(33058, "s2", lambda: s2)))
_l_(33061)