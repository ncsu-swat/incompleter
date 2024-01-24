# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77595065/attributeerror-module-cv2-face-has-no-attribute-lbphfacerecognizer-create
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(589003)

except ImportError:
    pass

recognizer = _c_(589007, _a_(589006, _a_(589005, _n_(589004, "cv2", lambda: cv2), "face"), "LBPHFaceRecognizer_create"))
_l_(589008)