# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48702694/attributeerror-nonetype-object-has-no-attribute-items-pil-exif
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(573567)

except ImportError:
    pass
try:
    from PIL.ExifTags import TAGS
    _l_(573569)

except ImportError:
    pass

def get_exif(fn):
    _l_(573604)

    ret = {}
    _l_(573570)
    i = _c_(573574, _a_(573572, _n_(573571, "Image", lambda: Image), "open"), _n_(573573, "fn", lambda: fn))
    _l_(573575)
    _c_(573578, _a_(573577, _n_(573576, "i", lambda: i), "load"))
    _l_(573579)
    info = _c_(573582, _a_(573581, _n_(573580, "i", lambda: i), "_getexif"))
    _l_(573583)
    _c_(573586, _n_(573584, "print", lambda: print), _n_(573585, "info", lambda: info))
    _l_(573587)
    for tag, value in _c_(573590, _a_(573589, _n_(573588, "info", lambda: info), "items")):
        _l_(573601)

        decoded = _c_(573595, _a_(573592, _n_(573591, "TAGS", lambda: TAGS), "get"), _n_(573593, "tag", lambda: tag), _n_(573594, "tag", lambda: tag))
        _l_(573596)
        _n_(573597, "ret", lambda: ret)[_n_(573598, "decoded", lambda: decoded)] = _n_(573599, "value", lambda: value)
        _l_(573600)
    aux = _n_(573602, "ret", lambda: ret)
    _l_(573603)
    return aux

_c_(573607, _n_(573605, "get_exif", lambda: get_exif), _n_(573606, "img_path", lambda: img_path))
_l_(573608)