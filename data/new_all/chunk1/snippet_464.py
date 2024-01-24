# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48224245/typeerror-string-argument-without-an-encoding-in-3-4-but-not-in-3-6
#! /usr/bin/env python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from base64 import b64decode
    _l_(393104)

except ImportError:
    pass
try:
    from lzma import LZMADecompressor
    _l_(393106)

except ImportError:
    pass
try:
    from sys import version
    _l_(393108)

except ImportError:
    pass


class B64LZMA(_n_(393109, "str", lambda: str)):
    _l_(393128)

    """A string of base64 encoded, LZMA compressed data."""

    def __bytes__(self):
        _l_(393120)

        """Returns the decompressed data."""
        aux = _c_(393118, _a_(393112, _c_(393111, _n_(393110, "LZMADecompressor", lambda: LZMADecompressor)), "decompress"), _c_(393117, _n_(393113, "b64decode", lambda: b64decode), _c_(393116, _a_(393115, _n_(393114, "self", lambda: self), "encode"))))
        _l_(393119)
        return aux

    def __str__(self):
        _l_(393127)

        """Returns the string decoded from __bytes__."""
        aux = _c_(393125, _a_(393124, _c_(393123, _n_(393121, "bytes", lambda: bytes), _n_(393122, "self", lambda: self)), "decode"))
        _l_(393126)
        return aux


TEST_STR = _c_(393130, _n_(393129, "B64LZMA", lambda: B64LZMA), '/Td6WFoAAATm1rRGAgAhARYAAAB0L+WjAQALSGVsbG8gd29ybGQuAGt+oFiSvoAYAAEkDKYY2NgftvN9AQAAAAAEWVo=')
_l_(393131)

if _n_(393132, "__name__", lambda: __name__) == '__main__':
    _l_(393141)

    _c_(393135, _n_(393133, "print", lambda: print), _n_(393134, "version", lambda: version))
    _l_(393136)
    _c_(393139, _n_(393137, "print", lambda: print), _n_(393138, "TEST_STR", lambda: TEST_STR))
    _l_(393140)