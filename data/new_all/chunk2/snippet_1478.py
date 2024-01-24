# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53915690/typeerror-layout-of-the-output-array-img-is-incompatible-with-cvmat-stepndi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(438668)

except ImportError:
    pass
try:
    import cv2
    _l_(438670)

except ImportError:
    pass
try:
    import numpy as np
    _l_(438672)

except ImportError:
    pass

black = _c_(438677, _a_(438674, _n_(438673, "np", lambda: np), "zeros"), shape = (512, 512, 3), dtype = _a_(438676, _n_(438675, "np", lambda: np), "int64"))
_l_(438678)
_c_(438682, _a_(438680, _n_(438679, "cv2", lambda: cv2), "circle"), _n_(438681, "black", lambda: black), center = (100, 100), radius = 50, color = (0, 255, 0), thickness = 10)
_l_(438683)

_c_(438687, _a_(438685, _n_(438684, "plt", lambda: plt), "imshow"), _n_(438686, "black", lambda: black))
_l_(438688)