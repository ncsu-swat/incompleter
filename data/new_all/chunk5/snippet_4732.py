# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51049124/importing-from-file-vs-internet-in-genfromtxt-numpy-date-typeerror-must-be-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(691726)

except ImportError:
    pass
try:
    from matplotlib.dates import bytespdate2num
    _l_(691728)

except ImportError:
    pass

names = ["A", "B", "C", "D", "E", "F", "G"]
_l_(691729)
my_array1 = _c_(691735, _a_(691731, _n_(691730, "np", lambda: np), "genfromtxt"), "goog.csv",                     
                          delimiter=',',
                          skip_header=1,
                          names=_n_(691732, "names", lambda: names),
                          dtype=None,
                          converters={0: _c_(691734, _n_(691733, "bytespdate2num", lambda: bytespdate2num), '%Y-%m-%d')})
_l_(691736)
_c_(691739, _n_(691737, "print", lambda: print), _n_(691738, "my_array1", lambda: my_array1)["A"])
_l_(691740)