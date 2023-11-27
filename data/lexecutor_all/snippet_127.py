# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(1548335)

except ImportError:
    pass

_c_(1548338, _a_(1548337, _n_(1548336, "plt", lambda: plt), "plot"), [0, 1], [0, 1], label="Label 1")
_l_(1548339)
_c_(1548342, _a_(1548341, _n_(1548340, "plt", lambda: plt), "plot"), [0, 1], [0, 2], label='Label 2')
_l_(1548343)

_c_(1548346, _a_(1548345, _n_(1548344, "plt", lambda: plt), "legend"), loc=(1.05, 0.5))
_l_(1548347)
_c_(1548350, _a_(1548349, _n_(1548348, "plt", lambda: plt), "tight_layout"))
_l_(1548351)

