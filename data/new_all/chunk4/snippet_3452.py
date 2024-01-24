# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74029182/is-there-a-better-solution-for-matplotlib-attributeerror-module-backend-intera
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(582980)

except ImportError:
    pass
try:
    import matplotlib
    _l_(582982)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(582984)

except ImportError:
    pass

_c_(582989, _n_(582985, "print", lambda: print), _c_(582988, _a_(582987, _n_(582986, "matplotlib", lambda: matplotlib), "get_backend")))  # here prints "module://backend_interagg" on pycharm with "Show plots in tool window" ticked
_l_(582990)  # here prints "module://backend_interagg" on pycharm with "Show plots in tool window" ticked
_c_(582993, _a_(582992, _n_(582991, "matplotlib", lambda: matplotlib), "use"), 'TkAgg')
_l_(582994)
_c_(582999, _n_(582995, "print", lambda: print), _c_(582998, _a_(582997, _n_(582996, "matplotlib", lambda: matplotlib), "get_backend")))  # here prints "TkAgg"
_l_(583000)  # here prints "TkAgg"

img = _c_(583003, _a_(583002, _n_(583001, "cv2", lambda: cv2), "imread"), 'IMG_9249.PNG', 0)
_l_(583004)

_c_(583008, _a_(583006, _n_(583005, "plt", lambda: plt), "imshow"), _n_(583007, "img", lambda: img), cmap='gray')
_l_(583009)
_c_(583012, _a_(583011, _n_(583010, "plt", lambda: plt), "show"))
_l_(583013)