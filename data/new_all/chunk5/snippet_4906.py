# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41368728/typeerror-a-bytes-like-object-is-required-not-str-in-python-3-5-2-and-pytess
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(674626)

    import Image
    _l_(674621)
except _n_(674622, "ImportError", lambda: ImportError):
    _l_(674625)

    try:
        from PIL import Image
        _l_(674624)

    except ImportError:
        pass
try:
    import pytesseract
    _l_(674628)

except ImportError:
    pass


_c_(674636, _n_(674629, "print", lambda: print), _c_(674635, _a_(674631, _n_(674630, "pytesseract", lambda: pytesseract), "image_to_string"), _c_(674634, _a_(674633, _n_(674632, "Image", lambda: Image), "open"), 'd:/testimages/name.gif'), lang='chi_sim'))
_l_(674637)
_c_(674645, _n_(674638, "print", lambda: print), _c_(674644, _a_(674640, _n_(674639, "pytesseract", lambda: pytesseract), "image_to_string"), _c_(674643, _a_(674642, _n_(674641, "Image", lambda: Image), "open"), 'd:/testimages/mobile.gif')))
_l_(674646)