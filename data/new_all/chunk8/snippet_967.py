# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63647817/attributeerror-module-cv2-cv2-has-no-attribute-createmat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(402624)

except ImportError:
    pass

def warpImage(image, corners, target):
    _l_(402657)

    mat = _c_(402629, _a_(402626, _n_(402625, "cv2", lambda: cv2), "CreateMat"), 3, 3, _a_(402628, _n_(402627, "cv2", lambda: cv2), "CV_32F"))
    _l_(402630)
    _c_(402636, _a_(402632, _n_(402631, "cv2", lambda: cv2), "GetPerspectiveTransform"), _n_(402633, "corners", lambda: corners), _n_(402634, "target", lambda: target), _n_(402635, "mat", lambda: mat))
    _l_(402637)
    out = _c_(402644, _a_(402639, _n_(402638, "cv2", lambda: cv2), "CreateMat"), _n_(402640, "height", lambda: height), _n_(402641, "width", lambda: width), _a_(402643, _n_(402642, "cv2", lambda: cv2), "CV_8UC3"))
    _l_(402645)
    _c_(402653, _a_(402647, _n_(402646, "cv2", lambda: cv2), "WarpPerspective"), _n_(402648, "image", lambda: image), _n_(402649, "out", lambda: out), _n_(402650, "mat", lambda: mat), _a_(402652, _n_(402651, "cv2", lambda: cv2), "CV_INTER_CUBIC"))
    _l_(402654)
    aux = _n_(402655, "out", lambda: out)
    _l_(402656)
    return aux


if _n_(402658, "__name__", lambda: __name__) == '__main__':
    _l_(402681)

    width, height = 400, 250
    _l_(402659)
    corners = [(171,72),(331,93),(333,188),(177,210)]
    _l_(402660)
    target = [(0,0),(_n_(402661, "width", lambda: width),0),(_n_(402662, "width", lambda: width),_n_(402663, "height", lambda: height)),(0,_n_(402664, "height", lambda: height))]
    _l_(402665)
    image = _c_(402668, _a_(402667, _n_(402666, "cv2", lambda: cv2), "imread"), 'fries_warped.jpg')
    _l_(402669)
    out = _c_(402674, _n_(402670, "warpImage", lambda: warpImage), _n_(402671, "image", lambda: image), _n_(402672, "corners", lambda: corners), _n_(402673, "target", lambda: target))
    _l_(402675)
    _c_(402679, _a_(402677, _n_(402676, "cv2", lambda: cv2), "imwrite"), 'fries_rect.jpg', _n_(402678, "out", lambda: out))
    _l_(402680)