# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74454579/python-typeerror-nonetype-object-is-not-subscriptable-in-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(534586)

except ImportError:
    pass
try:
    import cv2
    _l_(534588)

except ImportError:
    pass

def show_img(path):
    _l_(534692)


    img = _c_(534592, _a_(534590, _n_(534589, "cv2", lambda: cv2), "imread"), _n_(534591, "path", lambda: path))
    _l_(534593)
    b, g, r = _n_(534594, "img", lambda: img)[:,:,0], _n_(534595, "img", lambda: img)[:,:,1], _n_(534596, "img", lambda: img)[:,:,2]
    _l_(534597)
    hist_b = _c_(534601, _a_(534599, _n_(534598, "cv2", lambda: cv2), "calcHist"), [_n_(534600, "b", lambda: b)],[0],None,[256],[0,256])
    _l_(534602)
    hist_g = _c_(534606, _a_(534604, _n_(534603, "cv2", lambda: cv2), "calcHist"), [_n_(534605, "g", lambda: g)],[0],None,[256],[0,256])
    _l_(534607)
    hist_r = _c_(534611, _a_(534609, _n_(534608, "cv2", lambda: cv2), "calcHist"), [_n_(534610, "r", lambda: r)],[0],None,[256],[0,256])
    _l_(534612)
    _c_(534616, _a_(534614, _n_(534613, "plt", lambda: plt), "plot"), _n_(534615, "hist_r", lambda: hist_r), color='r', label="r")
    _l_(534617)
    _c_(534621, _a_(534619, _n_(534618, "plt", lambda: plt), "plot"), _n_(534620, "hist_g", lambda: hist_g), color='g', label="g")
    _l_(534622)
    _c_(534626, _a_(534624, _n_(534623, "plt", lambda: plt), "plot"), _n_(534625, "hist_b", lambda: hist_b), color='b', label="b")
    _l_(534627)
    _c_(534630, _a_(534629, _n_(534628, "plt", lambda: plt), "legend"))
    _l_(534631)
    _c_(534634, _a_(534633, _n_(534632, "plt", lambda: plt), "show")) 
    _l_(534635) 
    img2 = _c_(534641, _a_(534637, _n_(534636, "cv2", lambda: cv2), "cvtColor"), _n_(534638, "img", lambda: img), _a_(534640, _n_(534639, "cv2", lambda: cv2), "COLOR_BGR2HSV"))
    _l_(534642)
    h, s, v = _n_(534643, "img2", lambda: img2)[:,:,0], _n_(534644, "img2", lambda: img2)[:,:,1], _n_(534645, "img2", lambda: img2)[:,:,2]
    _l_(534646)
    hist_h = _c_(534650, _a_(534648, _n_(534647, "cv2", lambda: cv2), "calcHist"), [_n_(534649, "h", lambda: h)],[0],None,[256],[0,256])
    _l_(534651)
    hist_s = _c_(534655, _a_(534653, _n_(534652, "cv2", lambda: cv2), "calcHist"), [_n_(534654, "s", lambda: s)],[0],None,[256],[0,256])
    _l_(534656)
    hist_v = _c_(534660, _a_(534658, _n_(534657, "cv2", lambda: cv2), "calcHist"), [_n_(534659, "v", lambda: v)],[0],None,[256],[0,256])
    _l_(534661)
    _c_(534665, _a_(534663, _n_(534662, "plt", lambda: plt), "plot"), _n_(534664, "hist_h", lambda: hist_h), color='r', label="h")
    _l_(534666)
    _c_(534670, _a_(534668, _n_(534667, "plt", lambda: plt), "plot"), _n_(534669, "hist_s", lambda: hist_s), color='g', label="s")
    _l_(534671)
    _c_(534675, _a_(534673, _n_(534672, "plt", lambda: plt), "plot"), _n_(534674, "hist_v", lambda: hist_v), color='b', label="v")
    _l_(534676)
    _c_(534679, _a_(534678, _n_(534677, "plt", lambda: plt), "legend"))
    _l_(534680)
    _c_(534683, _a_(534682, _n_(534681, "plt", lambda: plt), "show"))
    _l_(534684)
    aux = _n_(534685, "hist_r", lambda: hist_r),_n_(534686, "hist_g", lambda: hist_g), _n_(534687, "hist_b", lambda: hist_b), _n_(534688, "hist_h", lambda: hist_h), _n_(534689, "hist_s", lambda: hist_s), _n_(534690, "hist_v", lambda: hist_v)
    _l_(534691)
    
    return aux


aaa = "/home/student_DC/desktop/optimization_11_10/original_duplicate.png "
_l_(534693)
r,g,b,h,s,v = _c_(534696, _n_(534694, "show_img", lambda: show_img), _n_(534695, "aaa", lambda: aaa))
_l_(534697)