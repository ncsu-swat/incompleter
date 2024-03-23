# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
i = _c_(66832, _n_(66829, "int", lambda: int), _c_(66831, _n_(66830, "input", lambda: input), 'Input an integer: '))
_l_(66833)
o = _c_(66838, _n_(66834, "str", lambda: str), _c_(66837, _n_(66835, "oct", lambda: oct), _n_(66836, "i", lambda: i)))[2:]
_l_(66839)
h = _c_(66844, _n_(66840, "str", lambda: str), _c_(66843, _n_(66841, "hex", lambda: hex), _n_(66842, "i", lambda: i)))[2:]
_l_(66845)
h = _c_(66848, _a_(66847, _n_(66846, "h", lambda: h), "upper"))
_l_(66849)
d = _c_(66852, _n_(66850, "str", lambda: str), _n_(66851, "i", lambda: i))
_l_(66853)
_c_(66855, _n_(66854, "print", lambda: print), 'Decimal Octal Hexadecimal (capitalized), Binary')
_l_(66856)
_c_(66862, _n_(66857, "print", lambda: print), _n_(66858, "d", lambda: d), '  ', _n_(66859, "o", lambda: o), ' ', _n_(66860, "h", lambda: h), '                   ', _n_(66861, "b", lambda: b))
_l_(66863)