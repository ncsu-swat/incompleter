# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21909435/how-do-i-resolve-this-error-typeerror-argument-1-must-be-pygame-surface-not-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(395223)

except ImportError:
    pass
sprites = _c_(395226, _a_(395225, _n_(395224, "Image", lambda: Image), "open"), 'sprites.png')
_l_(395227)
_c_(395232, _a_(395229, _n_(395228, "background", lambda: background), "blit"), _n_(395230, "sprites", lambda: sprites), (0, 0), _n_(395231, "rect", lambda: rect))
_l_(395233)