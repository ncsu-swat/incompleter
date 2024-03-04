# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s_str: _n_(61820, "str", lambda: str) = "\x00\x01\x00\xc0\x01\x00\x00\x00\x04"
_l_(61821)

s_bytes: _n_(61822, "bytes", lambda: bytes) = b'\x00\x01\x00\xc0\x01\x00\x00\x00\x04'
_l_(61823)

s_new: _n_(61824, "bytes", lambda: bytes) = _c_(61827, _n_(61825, "bytes", lambda: bytes), _n_(61826, "s", lambda: s), encoding="raw_unicode_escape")
_l_(61828)

