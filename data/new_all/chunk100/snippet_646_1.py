# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
i = _c_(66760, _n_(66757, "int", lambda: int), _c_(66759, _n_(66758, "input", lambda: input), 'Input an integer: '))
_l_(66761)
o = _c_(66766, _n_(66762, "str", lambda: str), _c_(66765, _n_(66763, "oct", lambda: oct), _n_(66764, "i", lambda: i)))[2:]
_l_(66767)
h = _c_(66772, _n_(66768, "str", lambda: str), _c_(66771, _n_(66769, "hex", lambda: hex), _n_(66770, "i", lambda: i)))[2:]
_l_(66773)
b = _c_(66778, _n_(66774, "str", lambda: str), _c_(66777, _n_(66775, "bin", lambda: bin), _n_(66776, "i", lambda: i)))[2:]
_l_(66779)
d = _c_(66782, _n_(66780, "str", lambda: str), _n_(66781, "i", lambda: i))
_l_(66783)
_c_(66785, _n_(66784, "print", lambda: print), 'Decimal Octal Hexadecimal (capitalized), Binary')
_l_(66786)
_c_(66792, _n_(66787, "print", lambda: print), _n_(66788, "d", lambda: d), '  ', _n_(66789, "o", lambda: o), ' ', _n_(66790, "h", lambda: h), '                   ', _n_(66791, "b", lambda: b))
_l_(66793)