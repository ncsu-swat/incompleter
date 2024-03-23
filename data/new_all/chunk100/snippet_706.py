# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import hashlib
    _l_(61642)

except ImportError:
    pass
with _c_(61644, _n_(61643, "open", lambda: open), "your_filename.txt", "rb") as f:
    _l_(61658)

    file_hash = _c_(61647, _a_(61646, _n_(61645, "hashlib", lambda: hashlib), "md5"))
    _l_(61648)
    while chunk := _c_(61651, _a_(61650, _n_(61649, "f", lambda: f), "read"), 8192):
        _l_(61657)

        _c_(61655, _a_(61653, _n_(61652, "file_hash", lambda: file_hash), "update"), _n_(61654, "chunk", lambda: chunk))
        _l_(61656)

_c_(61663, _n_(61659, "print", lambda: print), _c_(61662, _a_(61661, _n_(61660, "file_hash", lambda: file_hash), "digest")))
_l_(61664)
_c_(61669, _n_(61665, "print", lambda: print), _c_(61668, _a_(61667, _n_(61666, "file_hash", lambda: file_hash), "hexdigest")))  # to get a printable str instead of bytes
_l_(61670)  # to get a printable str instead of bytes

