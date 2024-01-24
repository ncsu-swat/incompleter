# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/17092520/typeerror-list-does-not-support-the-buffer-interface-when-writing-bytes-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file = _c_(376858, _n_(376856, "open", lambda: open), _n_(376857, "filename", lambda: filename) + ".bmp", "rb")
_l_(376859)
data = _c_(376862, _a_(376861, _n_(376860, "file", lambda: file), "read"))
_l_(376863)
_c_(376866, _a_(376865, _n_(376864, "file", lambda: file), "close"))
_l_(376867)
new = []
_l_(376868)

for byte in _n_(376869, "data", lambda: data):
    _l_(376884)

    byte = _c_(376872, _n_(376870, "int", lambda: int), _n_(376871, "byte", lambda: byte))
    _l_(376873)
    if _n_(376874, "byte", lambda: byte)%2:
        _l_(376876)

        byte -= 1
        _l_(376875)
    _c_(376882, _a_(376878, _n_(376877, "new", lambda: new), "append"), _c_(376881, _n_(376879, "bin", lambda: bin), _n_(376880, "byte", lambda: byte)))
    _l_(376883)

file = _c_(376887, _n_(376885, "open", lambda: open), _n_(376886, "filename", lambda: filename) + ".bmp", "wb")
_l_(376888)
_c_(376892, _a_(376890, _n_(376889, "file", lambda: file), "write"), _n_(376891, "new", lambda: new))
_l_(376893)
_c_(376896, _a_(376895, _n_(376894, "file", lambda: file), "close"))
_l_(376897)