# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(34323)

except ImportError:
    pass
try:
    import string
    _l_(34325)

except ImportError:
    pass
_c_(34327, _n_(34326, "print", lambda: print), 'Generate a random alphabetical character:')
_l_(34328)
_c_(34335, _n_(34329, "print", lambda: print), _c_(34334, _a_(34331, _n_(34330, "random", lambda: random), "choice"), _a_(34333, _n_(34332, "string", lambda: string), "ascii_letters")))
_l_(34336)
_c_(34338, _n_(34337, "print", lambda: print), '\nGenerate a random alphabetical string:')
_l_(34339)
str1 = ''
_l_(34340)
for i in _c_(34346, _n_(34341, "range", lambda: range), _c_(34345, _a_(34343, _n_(34342, "random", lambda: random), "randint"), 1, _n_(34344, "max_length", lambda: max_length))):
    _l_(34353)

    str1 += _c_(34351, _a_(34348, _n_(34347, "random", lambda: random), "choice"), _a_(34350, _n_(34349, "string", lambda: string), "ascii_letters"))
    _l_(34352)
_c_(34356, _n_(34354, "print", lambda: print), _n_(34355, "str1", lambda: str1))
_l_(34357)
_c_(34359, _n_(34358, "print", lambda: print), '\nGenerate a random alphabetical string of a fixed length:')
_l_(34360)
str1 = ''
_l_(34361)
for i in _c_(34363, _n_(34362, "range", lambda: range), 10):
    _l_(34370)

    str1 += _c_(34368, _a_(34365, _n_(34364, "random", lambda: random), "choice"), _a_(34367, _n_(34366, "string", lambda: string), "ascii_letters"))
    _l_(34369)
_c_(34373, _n_(34371, "print", lambda: print), _n_(34372, "str1", lambda: str1))
_l_(34374)