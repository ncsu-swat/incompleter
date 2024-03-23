# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
i = _c_(66725, _n_(66722, "int", lambda: int), _c_(66724, _n_(66723, "input", lambda: input), 'Input an integer: '))
_l_(66726)
o = _c_(66731, _n_(66727, "str", lambda: str), _c_(66730, _n_(66728, "oct", lambda: oct), _n_(66729, "i", lambda: i)))[2:]
_l_(66732)
h = _c_(66735, _a_(66734, _n_(66733, "h", lambda: h), "upper"))
_l_(66736)
b = _c_(66741, _n_(66737, "str", lambda: str), _c_(66740, _n_(66738, "bin", lambda: bin), _n_(66739, "i", lambda: i)))[2:]
_l_(66742)
d = _c_(66745, _n_(66743, "str", lambda: str), _n_(66744, "i", lambda: i))
_l_(66746)
_c_(66748, _n_(66747, "print", lambda: print), 'Decimal Octal Hexadecimal (capitalized), Binary')
_l_(66749)
_c_(66755, _n_(66750, "print", lambda: print), _n_(66751, "d", lambda: d), '  ', _n_(66752, "o", lambda: o), ' ', _n_(66753, "h", lambda: h), '                   ', _n_(66754, "b", lambda: b))
_l_(66756)