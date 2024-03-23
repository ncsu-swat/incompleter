# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
o = _c_(66905, _n_(66901, "str", lambda: str), _c_(66904, _n_(66902, "oct", lambda: oct), _n_(66903, "i", lambda: i)))[2:]
_l_(66906)
h = _c_(66911, _n_(66907, "str", lambda: str), _c_(66910, _n_(66908, "hex", lambda: hex), _n_(66909, "i", lambda: i)))[2:]
_l_(66912)
h = _c_(66915, _a_(66914, _n_(66913, "h", lambda: h), "upper"))
_l_(66916)
b = _c_(66921, _n_(66917, "str", lambda: str), _c_(66920, _n_(66918, "bin", lambda: bin), _n_(66919, "i", lambda: i)))[2:]
_l_(66922)
d = _c_(66925, _n_(66923, "str", lambda: str), _n_(66924, "i", lambda: i))
_l_(66926)
_c_(66928, _n_(66927, "print", lambda: print), 'Decimal Octal Hexadecimal (capitalized), Binary')
_l_(66929)
_c_(66935, _n_(66930, "print", lambda: print), _n_(66931, "d", lambda: d), '  ', _n_(66932, "o", lambda: o), ' ', _n_(66933, "h", lambda: h), '                   ', _n_(66934, "b", lambda: b))
_l_(66936)