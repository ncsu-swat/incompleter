# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59286117/google-colab-attributeerror-numpy-ndarray-object-has-no-attribute-seek-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(653899)

except ImportError:
    pass
try:
    import numpy as np
    _l_(653901)

except ImportError:
    pass
try:
    import sys
    _l_(653903)

except ImportError:
    pass
try:
    import PIL
    _l_(653905)

except ImportError:
    pass
try:
    import cv2
    _l_(653907)

except ImportError:
    pass

rgb = _c_(653910, _a_(653909, _n_(653908, "cv2", lambda: cv2), "imread"), "/content/teste/LC08_L1TP_222063_20180702_20180716_01_T1_1_3.tif")
_l_(653911)
tir = _c_(653914, _a_(653913, _n_(653912, "cv2", lambda: cv2), "imread"), "/content/teste/LC08_L1TP_222063_20180702_20180716_01_T1_TIR_1_3.tif")
_l_(653915)
qb = _c_(653918, _a_(653917, _n_(653916, "cv2", lambda: cv2), "imread"), "/content/teste/LC08_L1TP_222063_20180702_20180716_01_T1_QB_1_3.tif")
_l_(653919)


list_im = [_n_(653920, "rgb", lambda: rgb), _n_(653921, "tir", lambda: tir), _n_(653922, "qb", lambda: qb)]
_l_(653923)
imgs    = [ _c_(653928, _a_(653926, _a_(653925, _n_(653924, "PIL", lambda: PIL), "Image"), "open"), _n_(653927, "i", lambda: i)) for i in _n_(653929, "list_im", lambda: list_im) ]
_l_(653930)
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = _c_(653940, _n_(653931, "sorted", lambda: sorted), [(_c_(653936, _a_(653933, _n_(653932, "np", lambda: np), "sum"), _a_(653935, _n_(653934, "i", lambda: i), "size")), _a_(653938, _n_(653937, "i", lambda: i), "size") ) for i in _n_(653939, "imgs", lambda: imgs)])[0][1]
_l_(653941)
imgs_comb = _c_(653952, _a_(653943, _n_(653942, "np", lambda: np), "hstack"), (_c_(653950, _a_(653945, _n_(653944, "np", lambda: np), "asarray"), _c_(653949, _a_(653947, _n_(653946, "i", lambda: i), "resize"), _n_(653948, "min_shape", lambda: min_shape)) ) for i in _n_(653951, "imgs", lambda: imgs) ) )
_l_(653953)

# save that beautiful picture
imgs_comb = _c_(653958, _a_(653956, _a_(653955, _n_(653954, "PIL", lambda: PIL), "Image"), "fromarray"), _n_(653957, "imgs_comb", lambda: imgs_comb))
_l_(653959)
_c_(653962, _a_(653961, _n_(653960, "imgs_comb", lambda: imgs_comb), "save"), 'Trifecta.jpg' )
_l_(653963)