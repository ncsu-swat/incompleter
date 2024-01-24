# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46170165/attributeerror-cv2-filestorage-object-has-no-attribute-getnode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(678870)

except ImportError:
    pass

if _n_(678871, "__name__", lambda: __name__) == "__main__":
    _l_(678886)

    savePath = "/home/s/Desktop/Imgcov/"
    _l_(678872)
    filename = _n_(678873, "savePath", lambda: savePath) + "depth.xml"
    _l_(678874)
    fs = _c_(678880, _a_(678876, _n_(678875, "cv2", lambda: cv2), "FileStorage"), _n_(678877, "filename", lambda: filename), _a_(678879, _n_(678878, "cv2", lambda: cv2), "FILE_STORAGE_READ"))
    _l_(678881)
    matrix = _c_(678884, _a_(678883, _n_(678882, "fs", lambda: fs), "getNode"), "data") 
    _l_(678885) 