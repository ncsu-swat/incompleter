# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
# WRONG! will result in TypeError: getPumps() missing 1 required positional argument: 'self'
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
p = _n_(65005, "Pump", lambda: Pump)
_l_(65006)
_c_(65009, _a_(65008, _n_(65007, "p", lambda: p), "getPumps"))
_l_(65010)

# CORRECT!
p = _c_(65012, _n_(65011, "Pump", lambda: Pump))
_l_(65013)
_c_(65016, _a_(65015, _n_(65014, "p", lambda: p), "getPumps"))
_l_(65017)

