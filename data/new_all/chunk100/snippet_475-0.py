# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import decimal
    _l_(117792)

except ImportError:
    pass
_c_(117794, _n_(117793, "print", lambda: print), 'Construct a Decimal from a float:')
_l_(117795)
pi_val = _c_(117798, _a_(117797, _n_(117796, "decimal", lambda: decimal), "Decimal"), 3.14159)
_l_(117799)
_c_(117802, _n_(117800, "print", lambda: print), _n_(117801, "pi_val", lambda: pi_val))
_l_(117803)
_c_(117808, _n_(117804, "print", lambda: print), _c_(117807, _a_(117806, _n_(117805, "pi_val", lambda: pi_val), "as_tuple")))
_l_(117809)
_c_(117811, _n_(117810, "print", lambda: print), '\nConstruct a Decimal from a string:')
_l_(117812)
_c_(117815, _n_(117813, "print", lambda: print), _n_(117814, "num_str", lambda: num_str))
_l_(117816)
_c_(117821, _n_(117817, "print", lambda: print), _c_(117820, _a_(117819, _n_(117818, "num_str", lambda: num_str), "as_tuple")))
_l_(117822)