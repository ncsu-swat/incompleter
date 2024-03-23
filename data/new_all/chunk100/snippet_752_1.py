# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(76637)

except ImportError:
    pass
try:
    import string
    _l_(76639)

except ImportError:
    pass
_c_(76641, _n_(76640, "print", lambda: print), 'Generate a random color hex:')
_l_(76642)
_c_(76649, _n_(76643, "print", lambda: print), _c_(76648, _a_(76644, '#{:06x}', "format"), _c_(76647, _a_(76646, _n_(76645, "random", lambda: random), "randint"), 0, 16777215)))
_l_(76650)
_c_(76652, _n_(76651, "print", lambda: print), '\nGenerate a random alphabetical string:')
_l_(76653)
max_length = 255
_l_(76654)
for i in _c_(76660, _n_(76655, "range", lambda: range), _c_(76659, _a_(76657, _n_(76656, "random", lambda: random), "randint"), 1, _n_(76658, "max_length", lambda: max_length))):
    _l_(76667)

    s += _c_(76665, _a_(76662, _n_(76661, "random", lambda: random), "choice"), _a_(76664, _n_(76663, "string", lambda: string), "ascii_letters"))
    _l_(76666)
_c_(76670, _n_(76668, "print", lambda: print), _n_(76669, "s", lambda: s))
_l_(76671)
_c_(76673, _n_(76672, "print", lambda: print), 'Generate a random value between two integers, inclusive:')
_l_(76674)
_c_(76679, _n_(76675, "print", lambda: print), _c_(76678, _a_(76677, _n_(76676, "random", lambda: random), "randint"), 0, 10))
_l_(76680)
_c_(76685, _n_(76681, "print", lambda: print), _c_(76684, _a_(76683, _n_(76682, "random", lambda: random), "randint"), -7, 7))
_l_(76686)
_c_(76691, _n_(76687, "print", lambda: print), _c_(76690, _a_(76689, _n_(76688, "random", lambda: random), "randint"), 1, 1))
_l_(76692)
_c_(76694, _n_(76693, "print", lambda: print), 'Generate a random multiple of 7 between 0 and 70:')
_l_(76695)
_c_(76700, _n_(76696, "print", lambda: print), _c_(76699, _a_(76698, _n_(76697, "random", lambda: random), "randint"), 0, 10) * 7)
_l_(76701)