# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(76571)

except ImportError:
    pass
try:
    import string
    _l_(76573)

except ImportError:
    pass
_c_(76575, _n_(76574, "print", lambda: print), 'Generate a random color hex:')
_l_(76576)
_c_(76583, _n_(76577, "print", lambda: print), _c_(76582, _a_(76578, '#{:06x}', "format"), _c_(76581, _a_(76580, _n_(76579, "random", lambda: random), "randint"), 0, 16777215)))
_l_(76584)
_c_(76586, _n_(76585, "print", lambda: print), '\nGenerate a random alphabetical string:')
_l_(76587)
s = ''
_l_(76588)
for i in _c_(76594, _n_(76589, "range", lambda: range), _c_(76593, _a_(76591, _n_(76590, "random", lambda: random), "randint"), 1, _n_(76592, "max_length", lambda: max_length))):
    _l_(76601)

    s += _c_(76599, _a_(76596, _n_(76595, "random", lambda: random), "choice"), _a_(76598, _n_(76597, "string", lambda: string), "ascii_letters"))
    _l_(76600)
_c_(76604, _n_(76602, "print", lambda: print), _n_(76603, "s", lambda: s))
_l_(76605)
_c_(76607, _n_(76606, "print", lambda: print), 'Generate a random value between two integers, inclusive:')
_l_(76608)
_c_(76613, _n_(76609, "print", lambda: print), _c_(76612, _a_(76611, _n_(76610, "random", lambda: random), "randint"), 0, 10))
_l_(76614)
_c_(76619, _n_(76615, "print", lambda: print), _c_(76618, _a_(76617, _n_(76616, "random", lambda: random), "randint"), -7, 7))
_l_(76620)
_c_(76625, _n_(76621, "print", lambda: print), _c_(76624, _a_(76623, _n_(76622, "random", lambda: random), "randint"), 1, 1))
_l_(76626)
_c_(76628, _n_(76627, "print", lambda: print), 'Generate a random multiple of 7 between 0 and 70:')
_l_(76629)
_c_(76634, _n_(76630, "print", lambda: print), _c_(76633, _a_(76632, _n_(76631, "random", lambda: random), "randint"), 0, 10) * 7)
_l_(76635)