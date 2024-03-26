# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(111436)

except ImportError:
    pass
try:
    import string
    _l_(111438)

except ImportError:
    pass
_c_(111440, _n_(111439, "print", lambda: print), 'Generate a random alphabetical character:')
_l_(111441)
_c_(111448, _n_(111442, "print", lambda: print), _c_(111447, _a_(111444, _n_(111443, "random", lambda: random), "choice"), _a_(111446, _n_(111445, "string", lambda: string), "ascii_letters")))
_l_(111449)
_c_(111451, _n_(111450, "print", lambda: print), '\nGenerate a random alphabetical string:')
_l_(111452)
str1 = ''
_l_(111453)
for i in _c_(111459, _n_(111454, "range", lambda: range), _c_(111458, _a_(111456, _n_(111455, "random", lambda: random), "randint"), 1, _n_(111457, "max_length", lambda: max_length))):
    _l_(111466)

    str1 += _c_(111464, _a_(111461, _n_(111460, "random", lambda: random), "choice"), _a_(111463, _n_(111462, "string", lambda: string), "ascii_letters"))
    _l_(111465)
_c_(111469, _n_(111467, "print", lambda: print), _n_(111468, "str1", lambda: str1))
_l_(111470)
_c_(111472, _n_(111471, "print", lambda: print), '\nGenerate a random alphabetical string of a fixed length:')
_l_(111473)
str1 = ''
_l_(111474)
for i in _c_(111476, _n_(111475, "range", lambda: range), 10):
    _l_(111483)

    str1 += _c_(111481, _a_(111478, _n_(111477, "random", lambda: random), "choice"), _a_(111480, _n_(111479, "string", lambda: string), "ascii_letters"))
    _l_(111482)
_c_(111486, _n_(111484, "print", lambda: print), _n_(111485, "str1", lambda: str1))
_l_(111487)