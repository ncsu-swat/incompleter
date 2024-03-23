# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
i = _c_(66867, _n_(66864, "int", lambda: int), _c_(66866, _n_(66865, "input", lambda: input), 'Input an integer: '))
_l_(66868)
o = _c_(66873, _n_(66869, "str", lambda: str), _c_(66872, _n_(66870, "oct", lambda: oct), _n_(66871, "i", lambda: i)))[2:]
_l_(66874)
h = _c_(66879, _n_(66875, "str", lambda: str), _c_(66878, _n_(66876, "hex", lambda: hex), _n_(66877, "i", lambda: i)))[2:]
_l_(66880)
h = _c_(66883, _a_(66882, _n_(66881, "h", lambda: h), "upper"))
_l_(66884)
b = _c_(66889, _n_(66885, "str", lambda: str), _c_(66888, _n_(66886, "bin", lambda: bin), _n_(66887, "i", lambda: i)))[2:]
_l_(66890)
_c_(66892, _n_(66891, "print", lambda: print), 'Decimal Octal Hexadecimal (capitalized), Binary')
_l_(66893)
_c_(66899, _n_(66894, "print", lambda: print), _n_(66895, "d", lambda: d), '  ', _n_(66896, "o", lambda: o), ' ', _n_(66897, "h", lambda: h), '                   ', _n_(66898, "b", lambda: b))
_l_(66900)