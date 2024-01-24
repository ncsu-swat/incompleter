# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64962517/typeerror-expected-str-bytes-or-os-pathlike-object-not-numpy-ndarray
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(595049)

except ImportError:
    pass
try:
    import numpy as np
    _l_(595051)

except ImportError:
    pass
try:
    from lsd import *
    _l_(595053)

except ImportError:
    pass
try:
    import cv2
    _l_(595055)

except ImportError:
    pass

im = _c_(595058, _a_(595057, _n_(595056, "cv2", lambda: cv2), "imread"), '/home/lenovo/Downloads/python-lsd-master/test_data/chairs.pgm')
_l_(595059)

#fullName = '1.jpg'

folder, imgName = _c_(595064, _a_(595062, _a_(595061, _n_(595060, "os", lambda: os), "path"), "split"), _n_(595063, "im", lambda: im))
_l_(595065)

src = _c_(595071, _a_(595067, _n_(595066, "cv2", lambda: cv2), "imread"), _n_(595068, "im", lambda: im), _a_(595070, _n_(595069, "cv2", lambda: cv2), "IMREAD_COLOR"))
_l_(595072)

gray = _c_(595078, _a_(595074, _n_(595073, "cv2", lambda: cv2), "cvtColor"), _n_(595075, "src", lambda: src), _a_(595077, _n_(595076, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
_l_(595079)

lines =_a_(595081, _n_(595080, "lsd", lambda: lsd), "__module__")
_l_(595082)

#path1=os.path.normpath('/home/lenovo/pylsd/example/751626ntl.txt')

for i in _c_(595086, _n_(595083, "range", lambda: range), _a_(595085, _n_(595084, "lines", lambda: lines), "shape")[0]):
    _l_(595121)


    pt1 = (_c_(595090, _n_(595087, "int", lambda: int), _n_(595088, "lines", lambda: lines)[_n_(595089, "i", lambda: i), 0]), _c_(595094, _n_(595091, "int", lambda: int), _n_(595092, "lines", lambda: lines)[_n_(595093, "i", lambda: i), 1]))
    _l_(595095)

    pt2 = (_c_(595099, _n_(595096, "int", lambda: int), _n_(595097, "lines", lambda: lines)[_n_(595098, "i", lambda: i), 2]), _c_(595103, _n_(595100, "int", lambda: int), _n_(595101, "lines", lambda: lines)[_n_(595102, "i", lambda: i), 3]))
    _l_(595104)

    width = _n_(595105, "lines", lambda: lines)[_n_(595106, "i", lambda: i), 4]
    _l_(595107)

    _c_(595119, _a_(595109, _n_(595108, "cv2", lambda: cv2), "line"), _n_(595110, "src", lambda: src), _n_(595111, "pt1", lambda: pt1), _n_(595112, "pt2", lambda: pt2), (0, 0, 255), _c_(595118, _n_(595113, "int", lambda: int), _c_(595117, _a_(595115, _n_(595114, "np", lambda: np), "ceil"), _n_(595116, "width", lambda: width) / 2)))
    _l_(595120)

_c_(595133, _a_(595123, _n_(595122, "cv2", lambda: cv2), "imwrite"), _c_(595131, _a_(595126, _a_(595125, _n_(595124, "os", lambda: os), "path"), "join"), _n_(595127, "folder", lambda: folder), 'cv2_' + _c_(595130, _a_(595129, _n_(595128, "imgName", lambda: imgName), "split"), '.')[0] + '.jpg'), _n_(595132, "src", lambda: src))
_l_(595134)