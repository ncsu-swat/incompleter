# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72963138/attributeerror-psutil-has-no-attribute-dirty
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import psutil
    _l_(432965)

except ImportError:
    pass
mem = _c_(432968, _a_(432967, _n_(432966, "psutil", lambda: psutil), "virtual_memory"))
_l_(432969)
_c_(432976, _a_(432971, _n_(432970, "x", lambda: x), "add_metric"), _a_(432973, _n_(432972, "schema", lambda: schema), "yy_MEMORY_DIRTY"), _a_(432975, _n_(432974, "mem", lambda: mem), "dirty"))
_l_(432977)