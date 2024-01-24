# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59822759/python-import-random-issue-attributeerror-builtin-function-or-method-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(656916)

except ImportError:
    pass
try:
    from random import uniform, random, choice, sample, randint
    _l_(656918)

except ImportError:
    pass
somelist = ["temp1"]
_l_(656919)
randomList = _c_(656923, _a_(656921, _n_(656920, "random", lambda: random), "choice"), _n_(656922, "somelist", lambda: somelist))
_l_(656924)