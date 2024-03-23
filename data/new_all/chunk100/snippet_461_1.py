# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = 3
_l_(48998)
_c_(49001, _n_(48999, "print", lambda: print), '\nOriginal Number: ', _n_(49000, "x", lambda: x))
_l_(49002)
_c_(49007, _n_(49003, "print", lambda: print), 'Formatted Number(left padding, width 2): ' + _c_(49006, _a_(49004, '{:0>2d}', "format"), _n_(49005, "x", lambda: x)))
_l_(49008)
_c_(49011, _n_(49009, "print", lambda: print), 'Original Number: ', _n_(49010, "y", lambda: y))
_l_(49012)
_c_(49017, _n_(49013, "print", lambda: print), 'Formatted Number(left padding, width 6): ' + _c_(49016, _a_(49014, '{:0>6d}', "format"), _n_(49015, "y", lambda: y)))
_l_(49018)
_c_(49020, _n_(49019, "print", lambda: print))
_l_(49021)