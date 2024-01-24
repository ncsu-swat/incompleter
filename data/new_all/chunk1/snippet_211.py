# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48847515/typeerror-image-data-cannot-be-converted-to-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(383128)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(383130)

except ImportError:
    pass

img1 = _c_(383133, _a_(383132, _n_(383131, "cv2", lambda: cv2), "imread"), 'images\colombia_city.jpg')
_l_(383134)
img2 = _c_(383137, _a_(383136, _n_(383135, "cv2", lambda: cv2), "imread"), 'images\colombia_city_2.jpg')
_l_(383138)

#img = img1 + img2
#img = cv2.add(img1,img2)
abc = _c_(383143, _a_(383140, _n_(383139, "cv2", lambda: cv2), "addWeighted"), _n_(383141, "img1", lambda: img1),0.7,_n_(383142, "img2", lambda: img2),0.3,55)
_l_(383144)

_c_(383148, _a_(383146, _n_(383145, "plt", lambda: plt), "imshow"), _n_(383147, "abc", lambda: abc))
_l_(383149)
_c_(383152, _a_(383151, _n_(383150, "plt", lambda: plt), "show"))
_l_(383153)
_c_(383156, _a_(383155, _n_(383154, "plt", lambda: plt), "title"), "Weighted"); _c_(383159, _a_(383158, _n_(383157, "plt", lambda: plt), "axes"))
_l_(383160)
_c_(383163, _a_(383162, _n_(383161, "plt", lambda: plt), "waitforbuttonpress"))
_l_(383164)