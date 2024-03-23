# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import decimal
    _l_(49715)

except ImportError:
    pass
_c_(49717, _n_(49716, "print", lambda: print), 'Construct a Decimal from a float:')
_l_(49718)
_c_(49721, _n_(49719, "print", lambda: print), _n_(49720, "pi_val", lambda: pi_val))
_l_(49722)
_c_(49727, _n_(49723, "print", lambda: print), _c_(49726, _a_(49725, _n_(49724, "pi_val", lambda: pi_val), "as_tuple")))
_l_(49728)
_c_(49730, _n_(49729, "print", lambda: print), '\nConstruct a Decimal from a string:')
_l_(49731)
num_str = _c_(49734, _a_(49733, _n_(49732, "decimal", lambda: decimal), "Decimal"), '123.25')
_l_(49735)
_c_(49738, _n_(49736, "print", lambda: print), _n_(49737, "num_str", lambda: num_str))
_l_(49739)
_c_(49744, _n_(49740, "print", lambda: print), _c_(49743, _a_(49742, _n_(49741, "num_str", lambda: num_str), "as_tuple")))
_l_(49745)