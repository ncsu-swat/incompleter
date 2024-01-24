# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50906123/nameerror-name-image-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(376700)

except ImportError:
    pass
im = _c_(376703, _a_(376702, _n_(376701, "Image", lambda: Image), "open"), 'MobileNet-inference-images/American_Cam.jpg')
_l_(376704)
_c_(376707, _a_(376706, _n_(376705, "im", lambda: im), "show"))
_l_(376708)