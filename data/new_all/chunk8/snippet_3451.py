# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74029182/is-there-a-better-solution-for-matplotlib-attributeerror-module-backend-intera
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(640996)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(640998)

except ImportError:
    pass
img = _c_(641001, _a_(641000, _n_(640999, "cv2", lambda: cv2), "imread"), 'IMG_9249.PNG', 0)
_l_(641002)

_c_(641006, _a_(641004, _n_(641003, "plt", lambda: plt), "imshow"), _n_(641005, "img", lambda: img), cmap='gray')
_l_(641007)
_c_(641010, _a_(641009, _n_(641008, "plt", lambda: plt), "show"))
_l_(641011)