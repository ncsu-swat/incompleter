# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62190286/unable-to-understand-dtype-errors-in-opencv2-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(366026)

except ImportError:
    pass
try:
    import cv2
    _l_(366028)

except ImportError:
    pass


########################
# function#
########################

def draw_circle(event, x, y, flags, params):
    _l_(366052)

    if _n_(366029, "event", lambda: event) == _a_(366031, _n_(366030, "cv2", lambda: cv2), "EVENT_LBUTTONDOWN"):
        _l_(366051)

        _c_(366037, _a_(366033, _n_(366032, "cv2", lambda: cv2), "circle"), _n_(366034, "img", lambda: img), (_n_(366035, "x", lambda: x), _n_(366036, "y", lambda: y)), 100, (0, 0, 255), -1)
        _l_(366038)
    elif _n_(366039, "event", lambda: event) == _a_(366041, _n_(366040, "cv2", lambda: cv2), "EVENT_RBUTTONDOWN"):
        _l_(366050)

        _c_(366047, _a_(366043, _n_(366042, "cv2", lambda: cv2), "circle"), _n_(366044, "img", lambda: img), (_n_(366045, "x", lambda: x), _n_(366046, "y", lambda: y)), 100, (0, 255, 0), -1)
        _l_(366048)
    else:
        aux = ""
        _l_(366049)
        return aux


_c_(366055, _a_(366054, _n_(366053, "cv2", lambda: cv2), "namedWindow"), winname="output")
_l_(366056)
_c_(366060, _a_(366058, _n_(366057, "cv2", lambda: cv2), "setMouseCallback"), "output", _n_(366059, "draw_circle", lambda: draw_circle))
_l_(366061)


##########################
######showing images#####
##########################

img = _c_(366066, _a_(366063, _n_(366062, "np", lambda: np), "zeros"), (512, 512, 3), dtype=_a_(366065, _n_(366064, "np", lambda: np), "int8")) #----------- problem here
_l_(366067) #----------- problem here

while True:
    _l_(366078)

    _c_(366071, _a_(366069, _n_(366068, "cv2", lambda: cv2), "imshow"), "output", _n_(366070, "img", lambda: img))
    _l_(366072)

    if _c_(366075, _a_(366074, _n_(366073, "cv2", lambda: cv2), "waitKey"), 20) & 0xFF == 27:
        _l_(366077)

        break
        _l_(366076)

_c_(366081, _a_(366080, _n_(366079, "cv2", lambda: cv2), "destroyAllWindows"))
_l_(366082)