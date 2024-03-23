# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(34429)

except ImportError:
    pass
try:
    import string
    _l_(34431)

except ImportError:
    pass
_c_(34433, _n_(34432, "print", lambda: print), 'Generate a random alphabetical character:')
_l_(34434)
_c_(34441, _n_(34435, "print", lambda: print), _c_(34440, _a_(34437, _n_(34436, "random", lambda: random), "choice"), _a_(34439, _n_(34438, "string", lambda: string), "ascii_letters")))
_l_(34442)
_c_(34444, _n_(34443, "print", lambda: print), '\nGenerate a random alphabetical string:')
_l_(34445)
max_length = 255
_l_(34446)
str1 = ''
_l_(34447)
for i in _c_(34453, _n_(34448, "range", lambda: range), _c_(34452, _a_(34450, _n_(34449, "random", lambda: random), "randint"), 1, _n_(34451, "max_length", lambda: max_length))):
    _l_(34460)

    str1 += _c_(34458, _a_(34455, _n_(34454, "random", lambda: random), "choice"), _a_(34457, _n_(34456, "string", lambda: string), "ascii_letters"))
    _l_(34459)
_c_(34463, _n_(34461, "print", lambda: print), _n_(34462, "str1", lambda: str1))
_l_(34464)
_c_(34466, _n_(34465, "print", lambda: print), '\nGenerate a random alphabetical string of a fixed length:')
_l_(34467)
for i in _c_(34469, _n_(34468, "range", lambda: range), 10):
    _l_(34476)

    str1 += _c_(34474, _a_(34471, _n_(34470, "random", lambda: random), "choice"), _a_(34473, _n_(34472, "string", lambda: string), "ascii_letters"))
    _l_(34475)
_c_(34479, _n_(34477, "print", lambda: print), _n_(34478, "str1", lambda: str1))
_l_(34480)