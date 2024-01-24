# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47868014/zip-does-not-work-for-imshow-typeerror-image-data-cannot-be-converted-to-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(390155)

except ImportError:
    pass
a=[[1,2,3],[4,5,6]]
_l_(390156)
img_data=_c_(390159, _n_(390157, "zip", lambda: zip), *_n_(390158, "a", lambda: a))
_l_(390160)
_c_(390164, _a_(390162, _n_(390161, "plt", lambda: plt), "imshow"), _n_(390163, "img_data", lambda: img_data))
_l_(390165)