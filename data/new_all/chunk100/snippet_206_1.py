# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = 3000000
_l_(16012)
_c_(16015, _n_(16013, "print", lambda: print), '\nOriginal Number: ', _n_(16014, "x", lambda: x))
_l_(16016)
_c_(16021, _n_(16017, "print", lambda: print), 'Formatted Number with comma separator: ' + _c_(16020, _a_(16018, '{:,}', "format"), _n_(16019, "x", lambda: x)))
_l_(16022)
_c_(16025, _n_(16023, "print", lambda: print), 'Original Number: ', _n_(16024, "y", lambda: y))
_l_(16026)
_c_(16031, _n_(16027, "print", lambda: print), 'Formatted Number with comma separator: ' + _c_(16030, _a_(16028, '{:,}', "format"), _n_(16029, "y", lambda: y)))
_l_(16032)
_c_(16034, _n_(16033, "print", lambda: print))
_l_(16035)