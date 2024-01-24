# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33762610/pytesseract-error-on-python3-filenotfounderror-winerror-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pytesseract
    _l_(421041)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(421043)

except ImportError:
    pass

img = _c_(421046, _a_(421045, _n_(421044, "Image", lambda: Image), "open"), 'test.png')
_l_(421047)
_c_(421053, _n_(421048, "print", lambda: print), _c_(421052, _a_(421050, _n_(421049, "pytesseract", lambda: pytesseract), "image_to_string"), _n_(421051, "img", lambda: img)))
_l_(421054)