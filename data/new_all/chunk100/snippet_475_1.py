# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import decimal
    _l_(49747)

except ImportError:
    pass
_c_(49749, _n_(49748, "print", lambda: print), 'Construct a Decimal from a float:')
_l_(49750)
pi_val = _c_(49753, _a_(49752, _n_(49751, "decimal", lambda: decimal), "Decimal"), 3.14159)
_l_(49754)
_c_(49757, _n_(49755, "print", lambda: print), _n_(49756, "pi_val", lambda: pi_val))
_l_(49758)
_c_(49763, _n_(49759, "print", lambda: print), _c_(49762, _a_(49761, _n_(49760, "pi_val", lambda: pi_val), "as_tuple")))
_l_(49764)
_c_(49766, _n_(49765, "print", lambda: print), '\nConstruct a Decimal from a string:')
_l_(49767)
_c_(49770, _n_(49768, "print", lambda: print), _n_(49769, "num_str", lambda: num_str))
_l_(49771)
_c_(49776, _n_(49772, "print", lambda: print), _c_(49775, _a_(49774, _n_(49773, "num_str", lambda: num_str), "as_tuple")))
_l_(49777)