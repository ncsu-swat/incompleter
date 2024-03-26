# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import decimal
    _l_(117824)

except ImportError:
    pass
_c_(117826, _n_(117825, "print", lambda: print), 'Construct a Decimal from a float:')
_l_(117827)
_c_(117830, _n_(117828, "print", lambda: print), _n_(117829, "pi_val", lambda: pi_val))
_l_(117831)
_c_(117836, _n_(117832, "print", lambda: print), _c_(117835, _a_(117834, _n_(117833, "pi_val", lambda: pi_val), "as_tuple")))
_l_(117837)
_c_(117839, _n_(117838, "print", lambda: print), '\nConstruct a Decimal from a string:')
_l_(117840)
num_str = _c_(117843, _a_(117842, _n_(117841, "decimal", lambda: decimal), "Decimal"), '123.25')
_l_(117844)
_c_(117847, _n_(117845, "print", lambda: print), _n_(117846, "num_str", lambda: num_str))
_l_(117848)
_c_(117853, _n_(117849, "print", lambda: print), _c_(117852, _a_(117851, _n_(117850, "num_str", lambda: num_str), "as_tuple")))
_l_(117854)