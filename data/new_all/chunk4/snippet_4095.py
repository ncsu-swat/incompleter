# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62957721/typeerror-str-object-is-not-callable-when-printing-an-integer-and-words
#stage 2 dice rolling
#P1D1 means player ones dice one value and so on with P1D2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(639345)

except ImportError:
    pass
_c_(639347, _n_(639346, "print", lambda: print), "player ones turn")
_l_(639348)
P1D1 = _c_(639351, _a_(639350, _n_(639349, "random", lambda: random), "randint"), 1,6)
_l_(639352)
_c_(639356, _n_(639353, "print", lambda: print), _c_(639355, "your number is ", _n_(639354, "P1D1", lambda: P1D1)))
_l_(639357)