# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
y = 123
_l_(117257)
_c_(117260, _n_(117258, "print", lambda: print), '\nOriginal Number: ', _n_(117259, "x", lambda: x))
_l_(117261)
_c_(117266, _n_(117262, "print", lambda: print), 'Formatted Number(left padding, width 2): ' + _c_(117265, _a_(117263, '{:0>2d}', "format"), _n_(117264, "x", lambda: x)))
_l_(117267)
_c_(117270, _n_(117268, "print", lambda: print), 'Original Number: ', _n_(117269, "y", lambda: y))
_l_(117271)
_c_(117276, _n_(117272, "print", lambda: print), 'Formatted Number(left padding, width 6): ' + _c_(117275, _a_(117273, '{:0>6d}', "format"), _n_(117274, "y", lambda: y)))
_l_(117277)
_c_(117279, _n_(117278, "print", lambda: print))
_l_(117280)