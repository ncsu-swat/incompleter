# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46482460/matplotlib-type-error-when-trying-to-plot-simple-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(658081)

except ImportError:
    pass
_c_(658084, _a_(658083, _n_(658082, "plt", lambda: plt), "plot"), [1,2,3,4])
_l_(658085)
_c_(658088, _a_(658087, _n_(658086, "plt", lambda: plt), "ylabel"), 'some numbers')
_l_(658089)
_c_(658092, _a_(658091, _n_(658090, "plt", lambda: plt), "show"))
_l_(658093)