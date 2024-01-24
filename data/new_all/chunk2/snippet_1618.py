# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70428685/why-do-i-get-a-attributeerror-in-this-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def total_filesize(images: _n_(453296, "List", lambda: List)[_n_(453297, "ImageMetadata", lambda: ImageMetadata)]):
    _l_(453314)

    total = 0
    _l_(453298)
    try:
        _l_(453311)

        for i in _n_(453299, "images", lambda: images):
            _l_(453304)

            total = _n_(453300, "total", lambda: total) + _a_(453302, _n_(453301, "i", lambda: i), "filesize")
            _l_(453303)
    except _n_(453305, "BaseException", lambda: BaseException) as ex:
        _l_(453310)

        _c_(453308, _a_(453307, _n_(453306, "logger", lambda: logger), "error"), "Caught exception trying to compute total filesize for images", exc_info=True)
        _l_(453309)
    aux = _n_(453312, "total", lambda: total)
    _l_(453313)
    return aux