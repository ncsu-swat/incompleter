# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50736654/python-multiprocessing-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from multiprocessing import Pool
    _l_(398112)

except ImportError:
    pass
pool = _c_(398114, _n_(398113, "Pool", lambda: Pool), processes=4)
_l_(398115)
results = _c_(398120, _a_(398117, _n_(398116, "pool", lambda: pool), "map"), _n_(398118, "func_run", lambda: func_run), _n_(398119, "par", lambda: par))
_l_(398121)