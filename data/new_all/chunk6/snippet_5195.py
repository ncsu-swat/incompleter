# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62584911/opening-an-image-using-imagetk-in-pillow-causing-an-attributeerror-and-runtimeer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image, ImageTk
    _l_(359100)

except ImportError:
    pass

image = _c_(359103, _a_(359102, _n_(359101, "Image", lambda: Image), "open"), "0.gif")
_l_(359104)
photo = _c_(359108, _a_(359106, _n_(359105, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(359107, "image", lambda: image))
_l_(359109)