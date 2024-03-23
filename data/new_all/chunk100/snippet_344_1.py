# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(34376)

except ImportError:
    pass
try:
    import string
    _l_(34378)

except ImportError:
    pass
_c_(34380, _n_(34379, "print", lambda: print), 'Generate a random alphabetical character:')
_l_(34381)
_c_(34388, _n_(34382, "print", lambda: print), _c_(34387, _a_(34384, _n_(34383, "random", lambda: random), "choice"), _a_(34386, _n_(34385, "string", lambda: string), "ascii_letters")))
_l_(34389)
_c_(34391, _n_(34390, "print", lambda: print), '\nGenerate a random alphabetical string:')
_l_(34392)
max_length = 255
_l_(34393)
for i in _c_(34399, _n_(34394, "range", lambda: range), _c_(34398, _a_(34396, _n_(34395, "random", lambda: random), "randint"), 1, _n_(34397, "max_length", lambda: max_length))):
    _l_(34406)

    str1 += _c_(34404, _a_(34401, _n_(34400, "random", lambda: random), "choice"), _a_(34403, _n_(34402, "string", lambda: string), "ascii_letters"))
    _l_(34405)
_c_(34409, _n_(34407, "print", lambda: print), _n_(34408, "str1", lambda: str1))
_l_(34410)
_c_(34412, _n_(34411, "print", lambda: print), '\nGenerate a random alphabetical string of a fixed length:')
_l_(34413)
str1 = ''
_l_(34414)
for i in _c_(34416, _n_(34415, "range", lambda: range), 10):
    _l_(34423)

    str1 += _c_(34421, _a_(34418, _n_(34417, "random", lambda: random), "choice"), _a_(34420, _n_(34419, "string", lambda: string), "ascii_letters"))
    _l_(34422)
_c_(34426, _n_(34424, "print", lambda: print), _n_(34425, "str1", lambda: str1))
_l_(34427)