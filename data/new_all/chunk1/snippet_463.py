# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48224245/typeerror-string-argument-without-an-encoding-in-3-4-but-not-in-3-6
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from base64 import b64decode
    _l_(400629)

except ImportError:
    pass
try:
    from lzma import LZMADecompressor
    _l_(400631)

except ImportError:
    pass


class B64LZMA(_n_(400632, "str", lambda: str)):
    _l_(400651)

    """A string of base64 encoded, LZMA compressed data."""

    def __bytes__(self):
        _l_(400643)

        """Returns the decompressed data."""
        aux = _c_(400641, _a_(400635, _c_(400634, _n_(400633, "LZMADecompressor", lambda: LZMADecompressor)), "decompress"), _c_(400640, _n_(400636, "b64decode", lambda: b64decode), _c_(400639, _a_(400638, _n_(400637, "self", lambda: self), "encode"))))
        _l_(400642)
        return aux

    def __str__(self):
        _l_(400650)

        """Returns the string decoded from __bytes__."""
        aux = _c_(400648, _a_(400647, _c_(400646, _n_(400644, "bytes", lambda: bytes), _n_(400645, "self", lambda: self)), "decode"))
        _l_(400649)
        return aux


TEST_STR = _c_(400653, _n_(400652, "B64LZMA", lambda: B64LZMA), '/Td6WFoAAATm1rRGAgAhARYAAAB0L+WjAQALSGVsbG8gd29ybGQuAGt+oFiSvoAYAAEkDKYY2NgftvN9AQAAAAAEWVo=')
_l_(400654)

if _n_(400655, "__name__", lambda: __name__) == '__main__':
    _l_(400660)

    _c_(400658, _n_(400656, "print", lambda: print), _n_(400657, "TEST_STR", lambda: TEST_STR))
    _l_(400659)