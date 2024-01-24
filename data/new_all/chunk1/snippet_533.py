# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37163806/python-multiprocessing-attributeerror-str-object-has-no-attribute-has
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing
    _l_(399838)

except ImportError:
    pass
p = _c_(399842, _a_(399840, _n_(399839, "multiprocessing", lambda: multiprocessing), "Pool"), _n_(399841, "max_processes", lambda: max_processes))
_l_(399843)
_c_(399848, _a_(399845, _n_(399844, "p", lambda: p), "map"), _n_(399846, "worker_function", lambda: worker_function), _n_(399847, "input_data", lambda: input_data)) # trigger the error
_l_(399849) # trigger the error