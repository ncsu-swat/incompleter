# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53344078/getting-a-typeerror-with-python-quandl-get-raise-on-status
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import quandl
    _l_(423864)

except ImportError:
    pass

data = _c_(423867, _a_(423866, _n_(423865, "quandl", lambda: quandl), "get"), "EIA/PET_RWTC_D")
_l_(423868)
_c_(423873, _n_(423869, "print", lambda: print), _c_(423872, _a_(423871, _n_(423870, "data", lambda: data), "head")))
_l_(423874)