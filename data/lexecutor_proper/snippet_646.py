# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(63992, _a_(63991, _a_(63990, _n_(63989, "np", lambda: np), "random"), "seed"), 2)
_l_(63993)
_c_(63997, _a_(63996, _a_(63995, _n_(63994, "np", lambda: np), "random"), "randn"), 2) # array([-0.41675785, -0.05626683])
_l_(63998) # array([-0.41675785, -0.05626683])
_c_(64002, _a_(64001, _a_(64000, _n_(63999, "np", lambda: np), "random"), "randn"), 1) # array([-1.24528809])
_l_(64003) # array([-1.24528809])

_c_(64007, _a_(64006, _a_(64005, _n_(64004, "np", lambda: np), "random"), "seed"), 2)
_l_(64008)
_c_(64012, _a_(64011, _a_(64010, _n_(64009, "np", lambda: np), "random"), "randn"), 1) # array([-0.41675785])
_l_(64013) # array([-0.41675785])
_c_(64017, _a_(64016, _a_(64015, _n_(64014, "np", lambda: np), "random"), "randn"), 2) # array([-0.05626683, -1.24528809])
_l_(64018) # array([-0.05626683, -1.24528809])

