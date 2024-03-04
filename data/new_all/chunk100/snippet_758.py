# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(61678)

except ImportError:
    pass

im = _c_(61681, _a_(61680, _n_(61679, "Image", lambda: Image), "open"), 'whatever.png')
_l_(61682)
width, height = _a_(61684, _n_(61683, "im", lambda: im), "size")
_l_(61685)

