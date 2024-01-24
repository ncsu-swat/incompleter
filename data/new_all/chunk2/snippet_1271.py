# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58878284/attribute-error-while-using-image-module-from-pil-library-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(457911)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(457913)

except ImportError:
    pass

root = _c_(457915, _n_(457914, "Tk", lambda: Tk))
_l_(457916)

image2 = _c_(457919, _a_(457918, _n_(457917, "Image", lambda: Image), "open"), 'hp png.png')
_l_(457920)

hp_image2 = _c_(457924, _n_(457921, "Label", lambda: Label), _n_(457922, "root", lambda: root) , image = _n_(457923, "image2", lambda: image2))
_l_(457925)

_c_(457929, _a_(457927, _n_(457926, "hp_image2", lambda: hp_image2), "pack"), fill = _n_(457928, "BOTH", lambda: BOTH))
_l_(457930)

_c_(457933, _a_(457932, _n_(457931, "root", lambda: root), "mainloop"))
_l_(457934)