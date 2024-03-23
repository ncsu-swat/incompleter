# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
y = 123
_l_(48974)
_c_(48977, _n_(48975, "print", lambda: print), '\nOriginal Number: ', _n_(48976, "x", lambda: x))
_l_(48978)
_c_(48983, _n_(48979, "print", lambda: print), 'Formatted Number(left padding, width 2): ' + _c_(48982, _a_(48980, '{:0>2d}', "format"), _n_(48981, "x", lambda: x)))
_l_(48984)
_c_(48987, _n_(48985, "print", lambda: print), 'Original Number: ', _n_(48986, "y", lambda: y))
_l_(48988)
_c_(48993, _n_(48989, "print", lambda: print), 'Formatted Number(left padding, width 6): ' + _c_(48992, _a_(48990, '{:0>6d}', "format"), _n_(48991, "y", lambda: y)))
_l_(48994)
_c_(48996, _n_(48995, "print", lambda: print))
_l_(48997)