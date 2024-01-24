# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46482460/matplotlib-type-error-when-trying-to-plot-simple-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(694898)

except ImportError:
    pass
_c_(694901, _a_(694900, _n_(694899, "plt", lambda: plt), "plot"), [1,2,3,4])
_l_(694902)
_c_(694905, _a_(694904, _n_(694903, "plt", lambda: plt), "ylabel"), 'some numbers')
_l_(694906)
_c_(694909, _a_(694908, _n_(694907, "plt", lambda: plt), "show"))
_l_(694910)