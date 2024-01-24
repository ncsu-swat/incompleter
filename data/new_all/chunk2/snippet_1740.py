# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59266158/python-opencv-probabilistic-hough-line-transform-typeerror-object-of-type-no
#-*- coding:utf-8-*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(434898)

except ImportError:
    pass
try:
    import cv2
    _l_(434900)

except ImportError:
    pass
try:
    from skimage import io
    _l_(434902)

except ImportError:
    pass
try:
    import numpy as np
    _l_(434904)

except ImportError:
    pass

# Load image file
fpath = 'D:/Users/'
_l_(434905)
image = _c_(434909, _a_(434907, _n_(434906, "io", lambda: io), "imread"), _n_(434908, "fpath", lambda: fpath) + 'checkerboard.JPG')
_l_(434910)
image_original = _c_(434913, _a_(434912, _n_(434911, "image", lambda: image), "copy"))
_l_(434914)

edges = _c_(434918, _a_(434916, _n_(434915, "cv2", lambda: cv2), "Canny"), _n_(434917, "image", lambda: image), 50, 200, apertureSize=3)
_l_(434919)
gray = _c_(434925, _a_(434921, _n_(434920, "cv2", lambda: cv2), "cvtColor"), _n_(434922, "edges", lambda: edges), _a_(434924, _n_(434923, "cv2", lambda: cv2), "COLOR_GRAY2BGR"))
_l_(434926)

minLineLength = 100
_l_(434927)
maxLineGap = 0
_l_(434928)
# Perform the probabilistic Hough transform
lines = _c_(434936, _a_(434930, _n_(434929, "cv2", lambda: cv2), "HoughLinesP"), image=_n_(434931, "edges", lambda: edges), rho=1, theta=_a_(434933, _n_(434932, "np", lambda: np), "pi")/180, threshold=100, minLineLength=_n_(434934, "minLineLength", lambda: minLineLength), maxLineGap=_n_(434935, "maxLineGap", lambda: maxLineGap))
_l_(434937)

for i in _c_(434942, _n_(434938, "range", lambda: range), _c_(434941, _n_(434939, "len", lambda: len), _n_(434940, "lines", lambda: lines))):
    _l_(434955)

    for x1, y1, x2, y2 in _n_(434943, "lines", lambda: lines)[_n_(434944, "i", lambda: i)]:
        _l_(434954)

        _c_(434952, _a_(434946, _n_(434945, "cv2", lambda: cv2), "line"), _n_(434947, "image", lambda: image), (_n_(434948, "x1", lambda: x1), _n_(434949, "y1", lambda: y1)), (_n_(434950, "x2", lambda: x2), _n_(434951, "y2", lambda: y2)), (0, 0, 255), 3)
        _l_(434953)

_c_(434958, _a_(434957, _n_(434956, "plt", lambda: plt), "figure"), figsize=(10, 5), dpi=150)
_l_(434959)
_c_(434962, _a_(434961, _n_(434960, "plt", lambda: plt), "subplot"), 1, 2, 1)
_l_(434963)
_c_(434967, _a_(434965, _n_(434964, "plt", lambda: plt), "imshow"), _n_(434966, "image_original", lambda: image_original), cmap='gray', vmin=0, vmax=255)
_l_(434968)

_c_(434971, _a_(434970, _n_(434969, "plt", lambda: plt), "subplot"), 1, 2, 2)
_l_(434972)
_c_(434976, _a_(434974, _n_(434973, "plt", lambda: plt), "imshow"), _n_(434975, "image", lambda: image), cmap='gray', vmin=0, vmax=255)
_l_(434977)

_c_(434980, _a_(434979, _n_(434978, "plt", lambda: plt), "show"))
_l_(434981)