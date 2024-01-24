# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41368728/typeerror-a-bytes-like-object-is-required-not-str-in-python-3-5-2-and-pytess
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(689626)

    import Image
    _l_(689621)
except _n_(689622, "ImportError", lambda: ImportError):
    _l_(689625)

    try:
        from PIL import Image
        _l_(689624)

    except ImportError:
        pass
try:
    import pytesseract
    _l_(689628)

except ImportError:
    pass


_c_(689636, _n_(689629, "print", lambda: print), _c_(689635, _a_(689631, _n_(689630, "pytesseract", lambda: pytesseract), "image_to_string"), _c_(689634, _a_(689633, _n_(689632, "Image", lambda: Image), "open"), 'd:/testimages/name.gif'), lang='chi_sim'))
_l_(689637)
_c_(689645, _n_(689638, "print", lambda: print), _c_(689644, _a_(689640, _n_(689639, "pytesseract", lambda: pytesseract), "image_to_string"), _c_(689643, _a_(689642, _n_(689641, "Image", lambda: Image), "open"), 'd:/testimages/mobile.gif')))
_l_(689646)