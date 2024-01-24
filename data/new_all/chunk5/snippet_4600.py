# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54619517/receiving-error-attributeerror-module-cv2-cv2-has-no-attribute-comparehist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(664131)

except ImportError:
    pass
try:
    import cv2 as cv
    _l_(664133)

except ImportError:
    pass

img = _c_(664136, _a_(664135, _n_(664134, "cv", lambda: cv), "imread"), '../data/im3.jpg')
_l_(664137)
img2 = _c_(664140, _a_(664139, _n_(664138, "cv", lambda: cv), "imread"), '../data/im4.jpg')
_l_(664141)
gray = _c_(664147, _a_(664143, _n_(664142, "cv", lambda: cv), "cvtColor"), _n_(664144, "img", lambda: img), _a_(664146, _n_(664145, "cv", lambda: cv), "COLOR_BGR2GRAY"))
_l_(664148)
gray2 = _c_(664154, _a_(664150, _n_(664149, "cv", lambda: cv), "cvtColor"), _n_(664151, "img2", lambda: img2), _a_(664153, _n_(664152, "cv", lambda: cv), "COLOR_BGR2GRAY"))
_l_(664155)

sift = _c_(664159, _a_(664158, _a_(664157, _n_(664156, "cv", lambda: cv), "xfeatures2d"), "SIFT_create"))
_l_(664160)
kp, des1 = _c_(664164, _a_(664162, _n_(664161, "sift", lambda: sift), "detectAndCompute"), _n_(664163, "gray", lambda: gray),None)
_l_(664165)
kp2, des2 = _c_(664169, _a_(664167, _n_(664166, "sift", lambda: sift), "detectAndCompute"), _n_(664168, "gray2", lambda: gray2),None)
_l_(664170)


_c_(664178, _n_(664171, "print", lambda: print), _c_(664177, _a_(664173, _n_(664172, "cv", lambda: cv), "CompareHist"), _n_(664174, "des1", lambda: des1)[0], _n_(664175, "des2", lambda: des2)[0], _n_(664176, "CV_COMP_CORREL", lambda: CV_COMP_CORREL)))
_l_(664179)