# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
i = _c_(66797, _n_(66794, "int", lambda: int), _c_(66796, _n_(66795, "input", lambda: input), 'Input an integer: '))
_l_(66798)
h = _c_(66803, _n_(66799, "str", lambda: str), _c_(66802, _n_(66800, "hex", lambda: hex), _n_(66801, "i", lambda: i)))[2:]
_l_(66804)
h = _c_(66807, _a_(66806, _n_(66805, "h", lambda: h), "upper"))
_l_(66808)
b = _c_(66813, _n_(66809, "str", lambda: str), _c_(66812, _n_(66810, "bin", lambda: bin), _n_(66811, "i", lambda: i)))[2:]
_l_(66814)
d = _c_(66817, _n_(66815, "str", lambda: str), _n_(66816, "i", lambda: i))
_l_(66818)
_c_(66820, _n_(66819, "print", lambda: print), 'Decimal Octal Hexadecimal (capitalized), Binary')
_l_(66821)
_c_(66827, _n_(66822, "print", lambda: print), _n_(66823, "d", lambda: d), '  ', _n_(66824, "o", lambda: o), ' ', _n_(66825, "h", lambda: h), '                   ', _n_(66826, "b", lambda: b))
_l_(66828)